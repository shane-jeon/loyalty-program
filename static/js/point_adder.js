'use strict';


const addTransaction = (serviceAdded) => {
    $('#add-to-points').append(`
        <tr>
            <td>${serviceAdded}</td>)
        </tr>
    `);
};

const resetCount = () => {
    $('#reward-total-counter').html('0');
    $('#total-rewards').empty();
};

const incrementRewardTotal = (cost) => {
    const rewardTotal = $('#reward-total-counter');
    
    let total = Number(rewardTotal.html());
    total += cost;

    rewardTotal.html(total.toFixed(2));
};

// const incrementRewardsGained = (amountGained) => {
//     let rewardGained = Number($('#reward-total-counter').html());
//     rewardGained += amountGained;

//     $('#reward-total-counter').html(rewardGained);
// };

$('.add-to-points').on('click', () => {
    addTransaction('facial');
    incrementRewardTotal(1);
});

$('#place-order').on('click', () => {
    
    resetCount();

    setProgressAndStatus(0, 'Reward has been cashed in!');
});