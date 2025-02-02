const planPool0xt = { VPX: 510, Tanav: 610, KMX: 20, AKX: 20, Angel: 0, UCI: 0, SSX: 0, PPX: 0 };
const planFarm0xt = { VPX: 460, Tanav: 460, KMX: 0, AKX: 80, Angel: 70, UCI: 0, SSX: 0, PPX: 500 };

const colors = {
    tableHeader: "cyan",
    nameColor: "#ffff00", 
    sharesColor: "white",
    multiplierColor: "red",
    maxSupplyColor: "yellow",
    laColor: "red",
    ffxTextColor: "#ffff00", 
    noteColor: "white",
    captionColor: "#39ff14"
};

const formatNumber = (num) => {
    if (num >= 100000) {
        return (num / 100000).toFixed(5) + ' La';
    } else if (num >= 1000) {
        return (num / 1000).toFixed(3) + ' Th';
    } else {
        return num.toString();
    }
};

const updateLandingPage = () => {
    const sharesTableBody = document.querySelector('#sharesTable tbody');
    const combinedTableBody = document.querySelector('#combinedTable tbody');
    const totalFerroFyInvestments = calculateTotalInvestments();
    const FFXRate = 0.001;

    const calculateFFX = (investment) => {
        const share = (investment / totalFerroFyInvestments) * 75;
        return formatNumber(Math.floor(share / FFXRate));
    };

    let delay = 0;

    for (const person in planPool0xt) {
        setTimeout(() => {
            const ffxValue = calculateFFX(planPool0xt[person] + planFarm0xt[person]);
            let multiplier = '--';
            if (ffxValue.includes('La')) {
                multiplier = 'La';
            } else if (ffxValue.includes('Th')) {
                multiplier = 'Th';
            }
            const formattedValue = ffxValue.replace(multiplier, '').trim();

            const row = sharesTableBody.insertRow();
            row.insertCell(0).innerHTML = `<span style="color: ${colors.nameColor}">${person}</span>`;
            row.insertCell(1).innerHTML = `<span style="color: ${colors.sharesColor}">${formattedValue}</span>`;
            row.insertCell(2).innerHTML = `<span style="color: ${colors.multiplierColor}">${multiplier}</span>`;
        }, delay);
    }

    const rowsData = [
        {
            type: "Circulating Supply",
            amount: "1",
            multiplier: "La"
        },
        {
            type: "Max Supply",
            amount: "--",
            multiplier: "--"
        },
        {
            type: "Investors",
            amount: "75",
            multiplier: "Th"
        },
        {
            type: "Public",
            amount: "25",
            multiplier: "Th"
        }
    ];

    rowsData.forEach((data) => {
        const row = combinedTableBody.insertRow();
        row.insertCell(0).innerHTML = `<span style="color: ${colors.nameColor};">${data.type}</span>`;
        row.insertCell(1).innerHTML = `<span style="color: ${colors.sharesColor};">${data.amount}</span>`;
        row.insertCell(2).innerHTML = `<span style="color: ${colors.multiplierColor};">${data.multiplier}</span>`;
    });
};

const calculateTotalInvestments = () => {
    const totalPool = Object.values(planPool0xt).reduce((sum, val) => sum + val, 0);
    const totalFarm = Object.values(planFarm0xt).reduce((sum, val) => sum + val, 0);
    return totalPool + totalFarm;
};

window.onload = () => {
    updateLandingPage();
};
