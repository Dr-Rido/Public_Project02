# coding=gbk
import requests
from parsel import Selector
from fake_useragent import UserAgent
import json
from jsonpath import jsonpath
import execjs
import re
import os
"""今日头条根据指定url获取文章视频，图片，文本"""


def send_request(url_s: str, content=False):
    headers = {
        'User-Agent': UserAgent().chrome,
        'cookie': 'tt_webid=7132112568059790885; ttcid=a733c97f108a4c418503459236b2e98132; s_v_web_id=verify_l6uv3qnz_Au6bz3lh_VGYO_4WBM_9cby_YNPE9R16ESU9;  csrftoken=bf46fa7315e4f328710a9e3c2c8baf52; _tea_utm_cache_24=undefined; ttwid=1|BGzY_Ly7ZeQCeIcJNDtekuxNCyOscbGOZhvbv6NJ-8g|1660614742|3982d0cc41cde2e30116bf5a95c1f4fbb1dd6fa47ea11cf2fdecfff5fc96e6a9; MONITOR_WEB_ID=0e72496b-2897-41a2-a70b-c3a5c278f6ad; tt_scid=a-erYJcSOo.IxNTlsNPocr-i5Hkbv-McLEeqD68WtJ5gqQbQH7HJc-6pVoAvhMYy2676; msToken=mGhVE_zvFzS70C45gfyDUiZa-y5MD-zr9sOAS9nj4n0Cm1UKRAn4sFFDR3yZDPLyLG4bhDNdbDth0gJDJ5SMDFs8GNJFgsyQ22H6dIw4aBm2',
    }
    resp = requests.get(url=url_s, headers=headers)
    code = resp.status_code
    if content:
        return resp.content
    else:
        return resp.text


def parsel_videoid(html_p: str):
    selector = Selector(html_p)
    videoid = selector.css('div.article-content>article>div::attr(tt-videoid)').get()
    title = selector.css('div.main h1::text').get()
    article = selector.css('div.main article>p>strong>span::text').getall()
    # 文章类型二
    article2 = selector.css('article p span::text').getall()
    gif_url = selector.css('article img::attr(src)').getall()
    if not article:
        article = article2
        return videoid, title, article, gif_url


def get_main_url(videoid):
    hash_url = f'https://i.snssdk.com/video/urls/1/toutiao/mp4/{videoid}'
    json_data = requests.get(hash_url).text
    format_data = json_data.replace('tt__video__cb1e3t(', '').replace(')', '')
    json_data = json.loads(format_data)
    main_url = jsonpath(json_data, '$..main_url')
    return main_url


def get_url(hash_value):
    with open('video_url_js.js', 'r', encoding='utf-8')as f:
        js_read = f.read()
    js_compile = execjs.compile(js_read)
    url_ = js_compile.call('e', hash_value)
    return url_


def save_video(article_title, video_content):
    save_path = f'./数据/{article_title}/视频'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    with open(f'{save_path}/video.mp4', 'wb')as f:
        f.write(video_content)


def save_text(article_title, text_content: list):
    save_path = f'./数据/{article_title}/文本'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    with open(f'{save_path}/{article_title}.txt', 'w', encoding='utf-8')as t:
        for line in text_content:
            t.write(line+'\n')


def save_jpg(article_title, jpg_content:list):
    save_path = f'./数据/{article_title}/图片'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for i in range(len(jpg_content)):
        with open(f'{save_path}/{i}.jpg', 'wb')as j:
            j.write(jpg_content[i])


if __name__ == '__main__':
    url4 = 'https://www.toutiao.com/article/7137282522425541153/?log_from=d221be81afaa8_1661833855509'
    html = send_request(url4)
    # 获取视频id,标题,文章内容
    video_id, title, article, img_url = parsel_videoid(html)
    if video_id:
        # 视频hash数据
        hash_value = get_main_url(video_id)
        # 视频url
        video_url = get_url(hash_value[0])
        # 格式化视频url
        video_url_ = re.sub('\?a.*', '', video_url)
        # 获取视频内容
        contents = send_request(video_url_, content=True)
        # 下载视频的内容
        save_video(title, contents)
        print('视频内容下载完成')
    # 下载图片
    if img_url:
        img_b = []
        for url in img_url:
            content = send_request(url, content=True)
            img_b.append(content)
        img_b = set(img_b)
        img_b = list(img_b)
        save_jpg(title, img_b)
        print('图片内容下载完成')
    # 下载文本
    save_text(title, article)
    print('文本下载完成')

    # 获取主页面文章的url
    # h = send_request('https://www.toutiao.com/api/pc/list/feed?channel_id=3189398996&min_behot_time=0&refresh_count=1&category=pc_profile_channel&client_extra_params={"short_video_item":"filter"}&aid=24&app_name=toutiao_web&_signature=_02B4Z6wo00901nT6M6QAAIDC9PjJ5nGzHsZ03jcAAP5CW1VsKY0Gzu6EuFHQpiG0.Y01fOqKRzucm7szFYQuCYGeNUW1vynYCTF0K2ZHsjfb8SCjZTgKc7VBxPo.0A6.KMRDbPH1GITNfQWce6')
    # url_json = json.loads(h)
    # url_list = jsonpath(url_json, '$..display_url')
