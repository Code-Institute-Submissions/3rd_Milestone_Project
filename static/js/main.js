/**
 * Properties:
 * sidenav 
 * image can be parallax 
 * chevron arrow can scroll up the page
 */
$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('a[href="#top"]').click(function(){
        $('html, body').animate({ scrollTop: 0 }, 700, 'swing',);
        return false;
        });
    $('.modal').modal();
});
