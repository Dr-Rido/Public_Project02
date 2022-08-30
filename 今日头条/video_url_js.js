function e(t) {
    var c = new Array(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,62,-1,-1,-1,63,52,53,54,55,56,57,58,59,60,61,-1,-1,-1,-1,-1,-1,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,-1,-1,-1,-1,-1,-1,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,-1,-1,-1,-1,-1);

    var e, o, i, r, n, a, s;
    for (a = t.length,
             n = 0,
             s = ""; a > n;) {
        do
            e = c[255 & t.charCodeAt(n++)];
        while (a > n && -1 == e);
        if (-1 == e)
            break;
        do
            o = c[255 & t.charCodeAt(n++)];
        while (a > n && -1 == o);
        if (-1 == o)
            break;
        s += String.fromCharCode(e << 2 | (48 & o) >> 4);
        do {
            if (i = 255 & t.charCodeAt(n++),
            61 == i)
                return s;
            i = c[i]
        } while (a > n && -1 == i);
        if (-1 == i)
            break;
        s += String.fromCharCode((15 & o) << 4 | (60 & i) >> 2);
        do {
            if (r = 255 & t.charCodeAt(n++),
            61 == r)
                return s;
            r = c[r]
        } while (a > n && -1 == r);
        if (-1 == r)
            break;
        s += String.fromCharCode((3 & i) << 6 | r)
    }
    return s
};

var get_s = function (){
    var a;
    a = '' + Math.floor(2147483648 * Math.random()).toString(36);
    return a
}

// var hash = 'aHR0cDovL3YyNi1kZWZhdWx0LjM2NXlnLmNvbS9jNjAyOGJkNTAyMDA2YTdkNTMxZDNjNTI1MGFiMzcyYi82MmZiMGE5ZC92aWRlby90b3MvY24vdG9zLWNuLXZlLTRjMDAxLWFsaW5jMi81OTYwMzQwZGM5ZGE0ZmRmOWI3NDljMzQzMzBlOWEwMS8/YT0yMDExJmNoPTAmY3I9MCZkcj0wJm5ldD01JmNkPTAlN0MwJTdDMCU3QzAmYnI9MjkzJmJ0PTI5MyZjcz0wJmRzPTEmZnQ9RklKLUlOTjZWazN3YjhNMnE4ZHpKTGVPWVpsY35+ZkJGMmJMQVlIV1dEWm0mbWltZV90eXBlPXZpZGVvX21wNCZxcz0wJnJjPWFUcGthRHBuTzJnMk56czNQR1E2TTBCcE16dDNiVFU2Wm5SMVpUTXpORGN6TTBCZ01DMWVZR0ZpTm1JeE5DNHRNakJqWVNOeE1XSnpjalJmY1hCZ0xTMWtMVEJ6Y3clM0QlM0QmbD0yMDIyMDgxNjEwMDkyMTAxMDIwODEwMDEzMjBEMjJGQzND';

// console.log(e(hash));
