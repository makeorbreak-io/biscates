$(document).ready(function() {
    $("#search i").on('click', function() {
        window.location.href = "/search?search=" + $("#search input").val();
    });

    $("#search input").keypress(function(e) {
        if(e.which == 13) {
          window.location.href = "/search?search=" + $("#search input").val();
        }
    });
});
