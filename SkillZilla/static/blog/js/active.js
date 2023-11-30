$(document).ready(function () {
    let currentUrl = window.location.href;

    $('.navbar-nav .nav-link').each(function(){
        let link = this.href;
        if (currentUrl === link){
            $(this).parent().addClass('active');
            return false;
        }
    });
});
