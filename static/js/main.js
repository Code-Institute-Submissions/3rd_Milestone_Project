 $(document).ready(function(){
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $("a[href='#top']").click(function () {
        $("html, body").animate({ scrollTop: 0 }, 700, 'swing',);
        return false;
    });
 })