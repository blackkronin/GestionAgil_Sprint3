$(function (){
    var loadForm = function (){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $("#modal-calificar").modal("show");
            },
            success:function(data){
                $("#modal-calificar .modal-content").html(data.html_form);
            }
        })
    }
});