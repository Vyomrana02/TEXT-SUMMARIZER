$(document).ready(function () {
    $(".poster1").css({ "right": "32%" });
    $(".poster1").animate({ right: '49%' }, 500);

    $(".poster2").css({ "left": "65%" });
    $(".poster2").animate({ left: '77.5%' }, 500);
    AOS.init({
        offset: 300, // offset (in px) from the original trigger point
        duration: 700,
    });
    // document.addEventListener('DOMContentLoaded', function () { window.setTimeout(document.querySelector('svg').classList.add('animated'), 1000); })
});


