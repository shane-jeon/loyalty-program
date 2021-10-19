'use strict';

// i have no idea what this does
const addTransaction = (serviceAdded) => {
    $('#add-to-points').append(`
        <tr>
            <td>${serviceAdded}</td>)
        </tr>
    `);
};

// I don't think i have to reset right now
// const resetCount = () => {
//     $('#reward-total-counter').html('0');
//     $('#total-rewards').empty();
// };

const redeemPoints = (cost) => {
    const rewardTotal = $('#reward-total-counter');

    let total = Number(rewardTotal.html());
    total -= cost;

    rewardTotal.html(total.toFixed());
}

const undoRedeem = (cost) => {
    const rewardTotal = $('#reward-total-counter');

    let total = Number(rewardTotal.html());
    total += cost;

    rewardTotal.html(total.toFixed());
}

const incrementRewardTotal = (point) => {
    const rewardTotal = $('#reward-total-counter');
    
    let total = Number(rewardTotal.html());
    total += point;

    rewardTotal.html(total.toFixed());
};

const decrementRewardTotal = (point) => {
    const rewardTotal = $('#reward-total-counter');
    
    let total = Number(rewardTotal.html());
    total -= point;

    rewardTotal.html(total.toFixed());
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

$('.sub-from-points').on('click', () => {
    addTransaction('facial');
    decrementRewardTotal(1);
});

// EDGECASE (sorta), redeem num f-string way
$('.redeem-points').on('click', () => {
    addTransaction('facial');
    redeemPoints(10);
});

$('.undo-redeem').on('click', () => {
    addTransaction('facial');
    undoRedeem(10);
});