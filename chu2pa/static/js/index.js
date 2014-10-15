$(document).ready(function(){

    $('#student_check').on('click', function(){
        status = $('input[name=group1]:checked').val();
        $.ajax({
            url: '/student_check/',
            type: 'POST',
            dataType: "json",
            data: JSON.stringify(status),
            success:function(data){
                $('#checkin_show').append(
                    "<tr align='center'>" +
                    "<td>" + data.person + "</td>" +
                    "<td>" + data.date + "</td>" +
                    "<td>" + data.hour + "</td>" +
                    "<td>" + data.status + "</td>" +
                    "</tr>"
                )
            }
        })
    });



});