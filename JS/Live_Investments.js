import { Pool_0x0_Plan_1, Farm_0xt, Share_Rate_Pool, Total_Need_Pool, Total_Need_Farm } from './Investment_Data.js';

document.addEventListener('DOMContentLoaded', () => {
    const openPopupBtns = document.querySelectorAll('.Company_Box');
    const popups = document.querySelectorAll('.Open_Box');
    const closeBtns = document.querySelectorAll('.Close_Btn');
    
    const calculateFillPercentage = (currentInvestments, totalNeeded) => {
        let totalCurrent = Object.values(currentInvestments).reduce((a, b) => a + b, 0);
        return (totalCurrent / totalNeeded) * 100;
    };

    const calculateShares = (investments, shareRate) => {
        const shares = {};
        for (let investor in investments) {
            shares[investor] = investments[investor] * shareRate / 10;
        }
        return shares;
    };

    const calculateFarmShares = (investments) => {
        const totalInvested = Object.values(investments).reduce((a, b) => a + b, 0);
        const shares = {};
        for (let investor in investments) {
            shares[investor] = (investments[investor] * 100 / totalInvested).toFixed(2);
        }
        return shares;
    };

    const formatSharePercentage = (percentage) => {
        return percentage % 1 === 0 ? `${percentage.toFixed(0)}%` : `${percentage.toFixed(2)}%`;
    };

    const updateLoadingBars = () => {
        const poolFillPercentage = calculateFillPercentage(Pool_0x0_Plan_1, Total_Need_Pool);
        const farmFillPercentage = calculateFillPercentage(Farm_0xt, Total_Need_Farm);

        document.getElementById('Loading_Bar_Pool').style.width = `${poolFillPercentage}%`;
        document.getElementById('Loading_Bar_Farm').style.width = `${farmFillPercentage}%`;

        document.getElementById('Loading_Bar_Pool_Btn').style.width = `${poolFillPercentage}%`;
        document.getElementById('Loading_Bar_Farm_Btn').style.width = `${farmFillPercentage}%`;

        document.getElementById('Loading_Bar_Pool').innerText = `${Math.round(poolFillPercentage)}%`;
        document.getElementById('Loading_Bar_Farm').innerText = `${Math.round(farmFillPercentage)}%`;
    };

    const updateSharesInfo = () => {
        const poolShares = calculateShares(Pool_0x0_Plan_1, Share_Rate_Pool);
        const farmShares = calculateFarmShares(Farm_0xt);

        const poolSharesText = Object.entries(poolShares).map(([investor, shares]) => `${investor} = ${formatSharePercentage(shares)}`).join('<br>');
        const farmSharesText = Object.entries(farmShares).map(([investor, shares]) => `${investor} = ${formatSharePercentage(shares)}`).join('<br>');

        document.querySelector('#Pool .Shares_Details').innerHTML = `<b style="color:red; font-size:2em;">Shares</b><br>${poolSharesText}<br>FerroFy = 5%<br>`;
        document.querySelector('#Farm .Shares_Details').innerHTML = `<b style="color:red; font-size:2em;">Shares</b><br>${farmSharesText}<br>FerroFy = 5.5%<br>`;

        document.querySelector('#Pool .Investments_Details').innerHTML = `<b style="color:red; font-size:2em;">Investments</b><br>${Object.entries(Pool_0x0_Plan_1).map(([investor, amount]) => `${investor} = ₹${amount}`).join('<br>')}<br>`;
        document.querySelector('#Farm .Investments_Details').innerHTML = `<b style="color:red; font-size:2em;">Investments</b><br>${Object.entries(Farm_0xt).map(([investor, amount]) => `${investor} = ₹${amount}`).join('<br>')}<br>`;
    };

    openPopupBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const popupId = btn.getAttribute('data-popup');
            document.getElementById(popupId).style.display = 'flex';
            const details = document.querySelector(`#${popupId} .Investments_Details`);
            details.style.display = 'block';
            const shareDetails = document.querySelector(`#${popupId} .Shares_Details`);
            shareDetails.style.display = 'block';
        });
    });

    closeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            btn.closest('.Open_Box').style.display = 'none';
            const details = btn.closest('.Open_Box').querySelector('.Investments_Details');
            details.style.display = 'none';
            const shareDetails = btn.closest('.Open_Box').querySelector('.Shares_Details');
            shareDetails.style.display = 'none';
        });
    });

    window.addEventListener('click', (e) => {
        popups.forEach(popup => {
            if (e.target === popup) {
                popup.style.display = 'none';
                const details = popup.querySelector('.Investments_Details');
                details.style.display = 'none';
                const shareDetails = popup.querySelector('.Shares_Details');
                shareDetails.style.display = 'none';
            }
        });
    });

    updateLoadingBars();
    updateSharesInfo();
});
