$(document).ready(function () {

    $.ajax({
        type: "GET",
        url: "http://localhost:8080/move",
        contentType: "text"
    }).done(function(response) {
        console.log(response);
    }).fail(function(response, txt) {
        console.log(response);
        console.log(txt)
    });

    $(".offset-btn").click(function (e) {
        e.preventDefault();
        var direction = $(this).attr("direction");
        var axis = $(this).attr("axis");
        var offset = $("#offset-" + axis + "-" + direction).val();

        $.ajax({
            type: "POST",
            url: "http://localhost:8080/move",
            data: {
                func: "move_" + axis,
                Z: (direction == "left" ? -1 : 1) * offset
            },
            dataType: "text"
        }).done(function(response) {
            console.log(response);
        });
    });
});