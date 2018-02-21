$(function(){

    $('#search-btn').on('click', function() {

        $.ajax({
            type: "GET",
            url: "/search/",
            data: {
                'search_text': $('#search').val()
            },
            success: getAppointments,
            dataType: 'html'
        });
        $('.messages').remove()
    });
});

function getAppointments(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}
