function showImage(id) {
    document.getElementById('m-img').src = id.getAttribute("src");
}

$(".card").hover(
    function () {
        $(this).addClass('shadow').css('cursor', 'pointer');
    }, function () {
        $(this).removeClass('shadow');
    }
);