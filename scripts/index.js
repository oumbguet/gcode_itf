$(document).ready(function () {
    $(".plus").click(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "http://localhost:8080/move",
            data: {
                func: "move_Z",
                Z: 3
            },
            dataType: "text"
        });
    });

    $(".minus").click(function (e) {
        e.preventDefault();
        console.log("-1");
    });
});