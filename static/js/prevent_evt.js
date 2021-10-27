'use strict';

$('#submit-form').on('submit', evt => {
    evt.preventDefault();

    const pointInput = {
        point: $('#num_point').val(),
        bu_id: $('#bu_id').val(),
        client_id : $('#client_id').val()
    };

    $.post('/adjusting_points', pointInput, res => {
        // $('#reward-total-counter').html('new_points');
        console.log(res, "thIS IS THE RESULT")
        // JSON.stringify(res)
        // JSON.parse
        $('#reward-total-counter').html(res.new_points);
    });
});


// $('#submit-form').on('click', evt => {
//     evt.preventDefault();

//     const pointInput = {
//         point: $('#plus_one').val(),
//         bu_id: $('#bu_id').val(),
//         client_id : $('#client_id').val()
//     };

//     $.post('/adjusting_points', pointInput, res => {
//         // $('#reward-total-counter').html('new_points');
//         console.log(res, "thIS IS THE RESULT")
//         // JSON.stringify(res)
//         // JSON.parse
//         $('#reward-total-counter').html(res.new_points);
//     });
// });