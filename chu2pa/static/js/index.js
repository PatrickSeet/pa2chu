$(document).ready(function(){
<<<<<<< HEAD
    $('#student_check').on('click', function(){
=======

    $('#student_check').on('click', function(){
        status = $('input[name=group1]:checked').val();
>>>>>>> 7d5ca9f58d7e301285c97cb0f360632a4f0e1c68
        $.ajax({
            url: '/student_check/',
            type: 'POST',
            dataType: "json",
<<<<<<< HEAD
            success:function(data){
                var currentDate = new Date();
                var day = currentDate.getDate();
                var month = currentDate.getMonth() + 1;
                var year = currentDate.getFullYear();
                date = day + '/' + month + '/' + year;
                $('#student_status').append(
                    "<p>Person:" + data.person + "</p>" +
                    "<p>Person:" + date + "</p>" +
                    "<p>Person:" + data.status + "</p>"
=======
            data: JSON.stringify(status),
            success:function(data){
                $('#checkin_show').append(
                    "<tr align='center'>" +
                    "<td>" + data.person + "</td>" +
                    "<td>" + data.date + "</td>" +
                    "<td>" + data.hour + "</td>" +
                    "<td>" + data.status + "</td>" +
                    "</tr>"
>>>>>>> 7d5ca9f58d7e301285c97cb0f360632a4f0e1c68
                )
            }
        })
    });

<<<<<<< HEAD
=======


>>>>>>> 7d5ca9f58d7e301285c97cb0f360632a4f0e1c68
});