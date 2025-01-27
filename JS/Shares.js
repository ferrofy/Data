document.addEventListener('DOMContentLoaded', () => {
    const openPopupBtns = document.querySelectorAll('.Company_Box');
    const popups = document.querySelectorAll('.Open_Box');
    const closeBtns = document.querySelectorAll('.Close_Btn');

    const planPool0xt = { VPX: 510, Tanav: 610, KMX: 20, AKX: 20, Angel: 0, UCI: 0, SSX: 0, PPX: 0 };
    const planFarm0xt = { VPX: 600, Tanav: 600, KMX: 0, AKX: 80, Angel: 70, UCI: 0, SSX: 0, PPX: 500 };

    openPopupBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const popupId = btn.getAttribute('data-popup');
            document.getElementById(popupId).style.display = 'flex';
            document.querySelector(`#${popupId} .Shares_Details`).innerHTML = '<span style="color: red; font-weight: bold;">Under Maintenance 🚧</span>';
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
