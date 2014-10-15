var dateAsString;

$(document).ready(function() {

    $("#datepicker").datepicker({
        onSelect: function (dateText, inst) {
            dateAsString = dateText.toString();
            $('#teacher_view').html("");
            $.ajax ({
                url: '/teacher_overview/',
                type: 'POST',
                dataType: "json",
                data: JSON.stringify(dateAsString),
                success: function(data){
                    for (i=0; i<data.length; i++) {
                        person = data[i].person;
                        date = data[i].date;
                        status = data[i].status;
                        $('#teacher_view').append(
                            "<tr align='center'>" +
                            "<td>" + person + "</td>" +
                            "<td>" + date + "</td>" +
                            "<td>" + status + "</td>" +
                            "</tr>"
                        )

                    }
                }
            })
        }
    });

});