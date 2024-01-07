$(document).ready(function () {
    $('.navbar-nav ml-auto a').each(function(){
    let location = window.location.protocol + '//' + window.location.host +
    window.location.pathname;
    let link = this.href;
    if (location == link){
    $(this).parent().addClass('active');
    }

    });
});