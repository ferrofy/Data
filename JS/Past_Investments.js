document.addEventListener('DOMContentLoaded', () => {
    const openPopupBtns = document.querySelectorAll('.Company_Box');
    const popups = document.querySelectorAll('.Open_Box');
    const closeBtns = document.querySelectorAll('.Close_Btn');

    const investmentPool = { VPX: 510, Tanav: 610, KMX: 20, AKX: 20, Angel: 0, UCI: 0, SSX: 0, PPX: 0 };
    const investmentFarm = { VPX: 0, Tanav: 0, KMX: 0, AKX: 0, Angel: 0, UCI: 0, SSX: 0, PPX: 0 };

    const shareRatesPool = { VPX: 46, Tanav: 53, KMX: 1.5, AKX: 0, Angel: 1, UCI: 0, SSX: 0, PPX: 0 };
    const shareRatesFarm = { VPX: 0, Tanav: 0, KMX: 0, AKX: 0, Angel: 0, UCI: 0, SSX: 0, PPX: 0 };

    const startDate = new Date('December 7, 2024');
    const endDate = new Date('March 7, 2025');

    const calculateDateProgress = (start, end) => {
        const now = new Date();
        const totalDuration = end - start;
        const elapsedDuration = now - start;
        const elapsedDays = elapsedDuration / (1000 * 60 * 60 * 24);
        const totalDays = totalDuration / (1000 * 60 * 60 * 24);
        return Math.min((elapsedDays / totalDays) * 100, 100);
    };

    const updateInvestmentDetails = () => {
        const poolInvestmentsText = Object.entries(investmentPool).map(([investor, amount]) => `${investor} = ₹${amount}`).join('<br>');
        const farmInvestmentsText = Object.entries(investmentFarm).map(([investor, amount]) => `${investor} = ₹${amount}`).join('<br>');

        document.querySelector('#Pool_Popup .Investments_Details').innerHTML = `<b style="color:red; font-size:2em;">Investments</b><br>${poolInvestmentsText}<br>`;
        document.querySelector('#Farm_Popup .Investments_Details').innerHTML = `<b style="color:red; font-size:2em;">Investments</b><br>${farmInvestmentsText}<br>`;
    };

    const updateShareDetails = () => {
        const poolSharesText = Object.entries(shareRatesPool).map(([investor, rate]) => `${investor} = ${rate}%`).join('<br>');
        const farmSharesText = Object.entries(shareRatesFarm).map(([investor, rate]) => `${investor} = ${rate}%`).join('<br>');

        document.querySelector('#Pool_Popup .Shares_Details').innerHTML = `<b style="color:red; font-size:2em;">Shares</b><br>${poolSharesText}<br>`;
        document.querySelector('#Farm_Popup .Shares_Details').innerHTML = `<b style="color:red; font-size:2em;">Shares</b><br>${farmSharesText}<br>`;
    };

    const updateDateProgressBar = () => {
        const dateProgress = calculateDateProgress(startDate, endDate);
        document.getElementById('Pool_Date_Progress_Bar').style.width = `${dateProgress.toFixed(2)}%`;
        document.getElementById('Pool_Date_Progress_Bar').innerText = `${dateProgress.toFixed(2)} %`;
    };

    openPopupBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const popupId = btn.getAttribute('data-popup');
            document.getElementById(`${popupId}_Popup`).style.display = 'flex';
        });
    });

    closeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            btn.closest('.Open_Box').style.display = 'none';
        });
    });

    window.addEventListener('click', (e) => {
        popups.forEach(popup => {
            if (e.target === popup) {
                popup.style.display = 'none';
            }
        });
    });

    updateInvestmentDetails();
    updateShareDetails();


    updateDateProgressBar();
    setInterval(updateDateProgressBar, 60000);
});
