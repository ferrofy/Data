document.addEventListener('DOMContentLoaded', () => {
    const openPopupBtns = document.querySelectorAll('.Company_Box');
    const popups = document.querySelectorAll('.Open_Box');
    const closeBtns = document.querySelectorAll('.Close_Btn');

    
    const colors = {
        user: 'yellow', 
        percentage: 'red',
    };

    const planPool0xt = { VPX: 510, Tanav: 610, KMX: 20, AKX: 20, Angel: 0, UCI: 0, SSX: 0, PPX: 0 };
    const planFarm0xt = { VPX: 0, Tanav: 0, KMX: 0, AKX: 0, Angel: 0, UCI: 0, SSX: 0, PPX: 0 };


    const Total_Pool_Investments = Object.values(planPool0xt).reduce((sum, value) => sum + value, 0);
    const Total_Farm_Investments = Object.values(planFarm0xt).reduce((sum, value) => sum + value, 0);
    const Total_FerroFy_Investments = Total_Pool_Investments + Total_Farm_Investments;


    const calculateShares = (userInvestments, totalInvestments) => {
        return ((userInvestments * 100) / totalInvestments).toFixed(8).replace(/\.?0+$/, '');
    };


    const formatOutput = (user, poolShare, farmShare, ferroFyShare, popupId) => {
        let percentage;
        if (popupId === 'Pool') {
            percentage = poolShare;
        } else if (popupId === 'Farm') {
            percentage = farmShare;
        } else if (popupId === 'FerroFy') {
            percentage = ferroFyShare;
        }

        return `<span style="color: ${colors.user};">${user}</span> - <span style="color: ${colors.percentage};">${percentage}</span>%<br>`;
    };

    // Generate shares details based on popup type
    const generateSharesDetails = (popupId) => {
        let sharesDetails = '';
        for (const user in planPool0xt) {
            const User_Total_Pool_Investments = planPool0xt[user];
            const User_Total_Farm_Investments = planFarm0xt[user];
            const User_Total_FerroFy_Investments = User_Total_Pool_Investments + User_Total_Farm_Investments;

            const User_Shares_Pool = calculateShares(User_Total_Pool_Investments, Total_Pool_Investments);
            const User_Shares_Farm = calculateShares(User_Total_Farm_Investments, Total_Farm_Investments);
            const User_FerroFy_Pool = calculateShares(User_Total_FerroFy_Investments, Total_FerroFy_Investments);

            sharesDetails += formatOutput(user, User_Shares_Pool, User_Shares_Farm, User_FerroFy_Pool, popupId);
        }
        return sharesDetails;
    };

    // Attach event listeners
    openPopupBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const popupId = btn.getAttribute('data-popup');
            const popup = document.getElementById(popupId);
            popup.style.display = 'flex';
            popup.querySelector('.Shares_Details').innerHTML = generateSharesDetails(popupId);
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
});
