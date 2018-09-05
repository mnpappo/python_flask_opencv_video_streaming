$(document).ready(function () {
    $("#video_info").click(function(){
        $.ajax({
            type: "GET",
            url: "/getinfo",
            // url: "http://192.168.1.108/cgi-bin/configManager.cgi?action=getConfig&name=Encode",
            // data: ,
            cache: false,
            success: function (data) {
                $(".info_body").append(data);
                console.log(data);
            },
            error: function(e) {
                console.log(e);
            }
        });

        console.log("Hello");
    })
});