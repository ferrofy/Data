const planPool0xt = { VPX: 510, Tanav: 610, KMX: 20, AKX: 20, Angel: 0, UCI: 0, SSX: 0, PPX: 0 };
const planFarm0xt = { VPX: 291, Tanav: 291, KMX: 0, AKX: 80, Angel: 70, UCI: 0, SSX: 0, PPX: 500 };

const colors = {
    nameColor: "yellow",
    ffxTextColor: "white",
    ffxLabelColor: "red",
    backgroundColor: "#1d1f21",
    textColor: "#eceff1",
    accentColor: "#39ff14",
    finalTextColor: "cyan",
    suffixColor: "cyan"
};

const formatNumber = (num) => {
    if (num >= 10000000) {
        return (num / 10000000).toFixed(7) + ' <span style="color: ${colors.suffixColor}"> Cr </span>';
    } else if (num >= 100000) {
        return (num / 100000).toFixed(5) + ' <span style="color: ${colors.suffixColor}"> La </span>';
    } else if (num >= 1000) {
        return (num / 1000).toFixed(3) + ' <span style="color: ${colors.suffixColor}"> Th </span>';
    } else {
        return num.toString();
    }
};

const updateLandingPage = () => {
    const investmentsContent = document.getElementById('investmentsContent');
    const totalFerroFyInvestments = calculateTotalInvestments();
    const FFXRate = 0.0000001;

    const calculateFFX = (investment) => {
        const share = (investment / totalFerroFyInvestments) * 75;
        return formatNumber(Math.floor(share / FFXRate));
    };

    let delay = 0;
    let firstPerson = true;

    const shareAnimation = ["Calculating", "Calculating.", "Calculating..", "Calculating..."];

    for (const person in planPool0xt) {
        setTimeout(() => {
            investmentsContent.innerHTML += `<p style="color: ${colors.nameColor}" id="${person}">${person}: ${shareAnimation[0]}</p>`;
        }, delay);

        delay += 500;

        for (let i = 1; i < shareAnimation.length; i++) {
            setTimeout(() => {
                document.getElementById(person).innerHTML = `${person}: ${shareAnimation[i]}`;
            }, delay);
            delay += 500;
        }

        setTimeout(() => {
            const ffxValue = calculateFFX(planPool0xt[person] + planFarm0xt[person]);
            document.getElementById(person).innerHTML = `${person}: <span style="color: ${colors.ffxTextColor}">${ffxValue} <span style="color: ${colors.ffxLabelColor}">FFX</span></span>`;
        }, delay);

        delay += 500;
    }

    setTimeout(() => {
        investmentsContent.innerHTML += `<p style="color: ${colors.finalTextColor}">1 FFX = 0.0000001% Of FerroFy</p>`;
    }, delay);
};

const calculateTotalInvestments = () => {
    const totalPool = Object.values(planPool0xt).reduce((sum, val) => sum + val, 0);
    const totalFarm = Object.values(planFarm0xt).reduce((sum, val) => sum + val, 0);
    return totalPool + totalFarm;
};

window.onload = () => {
    updateLandingPage();
};
