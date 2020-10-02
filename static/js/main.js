/**
 * JQuery functions
 * navbar can slide right
 * image can be parallax 
 * chevron arrow can scroll up the page
 */
$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $("a[href='#top']").click(function(){
        $("html, body").animate({ scrollTop: 0 }, 700, 'swing',);
        return false;
        });
    $('.modal').modal();
    $('#commentForm').validate();

    $('.submit-button').attr('disabled', true);
    $('.form-control').on('keyup', function () {
        var textarea_value = $(this).val();
        if (textarea_value != '') {
            $('input[type="submit"]').attr('disabled', false);
        } else {
            $('input[type="submit"]').attr('disabled', true);
        }
    })
})
