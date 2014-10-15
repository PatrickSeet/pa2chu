$(document).ready(function(){
    $('#student_check').on('click', function(){
        $.ajax({
            url: '/student_check/',
            type: 'POST',
            dataType: "json",
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
                )
            }
        })
    });

    $( "#datepicker" ).datepicker();

    $(document).on('click', '.find', function(){
        console.log("hell ya");
        teacher_choose = $("#datepicker").val();
        console.log(teacher_choose);
    });



});