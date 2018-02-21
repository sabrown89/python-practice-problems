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

    $('#new-btn').on('click', function() {
        $.ajax({
            type: "GET",
            url: "/create_form/",
            data: {'': ''},
            success: getNewForm,
            dataType: 'html'
        });
        document.getElementById('new-btn').remove();
        $('.messages').remove()
    });
});

function getAppointments(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}

function getNewForm(data, textStatus, jqXHR)
{
    $('#create-form').html(data);
}
