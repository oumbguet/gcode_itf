$(document).ready(function () {
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

    $(".send-abs").click(function (e) {
        e.preventDefault();
        var x = $("#abs_X").val();
        var y = $("#abs_Y").val();
        var z = $("#abs_Z").val();

        $.ajax({
            type: "POST",
            url: "http://localhost:8080/move",
            data: {
                func: "move_to",
                X: x,
                Y: y,
                Z: z
            },
            dataType: "text"
        }).done(function(response) {
            console.log(response);
        });
    });

    $(".send-rel").click(function (e) {
        e.preventDefault();
        var x = $("#rel_X").val();
        var y = $("#rel_Y").val();
        var z = $("#rel_Z").val();

        $.ajax({
            type: "POST",
            url: "http://localhost:8080/move",
            data: {
                func: "move",
                X: x,
                Y: y,
                Z: z
            },
            dataType: "text"
        }).done(function(response) {
            console.log(response);
        });
    });
});