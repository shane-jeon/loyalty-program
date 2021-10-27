'use strict';

const redeemPoints = (cost) => {
    const rewardTotal = $('.reward-total-counter');

    let total = Number(rewardTotal.html());
    total -= cost;

    rewardTotal.html(total.toFixed());
};


const undoRedeem = (cost) => {
    const rewardTotal = $('.reward-total-counter');

    let total = Number(rewardTotal.html());
    total += cost;

    rewardTotal.html(total.toFixed());
}

const incrementRewardTotal = (point) => {
    const rewardTotal = $('.reward-total-counter');
    
    let total = Number(rewardTotal.html());
    total += point;

    rewardTotal.html(total.toFixed());
};

$('#myFunction').on('click', (point) => {
    const myTotal = $('.my-total');
    const finalPoint = point + 1
    myTotal.html(finalPoint.toFixed());
});

const decrementRewardTotal = (point) => {
    const rewardTotal = $('.reward-total-counter');
    
    let total = Number(rewardTotal.html());
    total -= point;

    rewardTotal.html(total.toFixed());
};


$('#add-to-points').on('click', () => {
    incrementRewardTotal(1);
});


$('#sub-from-points').on('click', () => {
    decrementRewardTotal(1);
});

// EDGECASE (sorta), redeem num f-string way

document.querySelector('#redeem-points').addEventListener('click', () => {
    redeemPoints(10);
})

document.querySelector('#undo-redeem').addEventListener('click', () => {
    undoRedeem(10);
});

// create a function to put in as id, my function, function takes in client.reward_points and adds by one
// 2nd iteration w/point action
