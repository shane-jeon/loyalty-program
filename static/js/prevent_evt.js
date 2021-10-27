'use strict';

$('#submit-form').on('submit', evt => {
    evt.preventDefault();

    const pointInput = {
        point: $('#num_point').val(),
        bu_id: $('#bu_id').val(),
        client_id : $('#client_id').val()
    };

    $.post('/adjusting_points', pointInput, res => {
        $('#reward-total-counter').html('new_points');
    });
});
