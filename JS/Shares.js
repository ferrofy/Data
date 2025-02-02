const planPool0xt = { VPX: 510, Tanav: 610, KMX: 20, AKX: 20, Angel: 0, UCI: 0, SSX: 0, PPX: 0 };
const planFarm0xt = { VPX: 460, Tanav: 460, KMX: 0, AKX: 80, Angel: 70, UCI: 0, SSX: 0, PPX: 500 };

const colors = {
    nameColor: "yellow",
    ffxTextColor: "#39ff14",
    ffxLabelColor: "red",
    backgroundColor: "#1d1f21",
    textColor: "white",
    accentColor: "#39ff14",
    finalTextColor: "cyan",
    suffixColor: "darkpink",
    noteColor: "white"
};

const Animation_Delay = 15;

const formatNumber = (num) => {
    if (num >= 10000000) {
        return (num / 10000000).toFixed(7) + ' Cr';
    } else if (num >= 100000) {
        return (num / 100000).toFixed(5) + ' La';
    } else if (num >= 1000) {
        return (num / 1000).toFixed(3) + ' Th';
    } else {
        return num.toString();
    }
};

const updateLandingPage = () => {
    const investmentsContent = document.getElementById('investmentsContent');
    const totalFerroFyInvestments = calculateTotalInvestments();
    const FFXRate = 0.000001;

    const calculateFFX = (investment) => {
        const share = (investment / totalFerroFyInvestments) * 75;
        return formatNumber(Math.floor(share / FFXRate));
    };

    let delay = 0;

    const shareAnimation = [];

    for (let i = 0; i <= 100; i++) {
        let dots = ''.repeat(i % 3 + 1);
        let hashes = '#'.repeat(Math.floor(i / 10));
        let spaces = ' '.repeat(10 - hashes.length);
        let percentage = `${i}%`;

        shareAnimation.push(`Calculating... ${dots} [${hashes}${spaces}] ${percentage}`);
    }

    console.log(shareAnimation);


    for (const person in planPool0xt) {
        setTimeout(() => {
            investmentsContent.innerHTML += `<p style="color: ${colors.nameColor}" id="${person}">${person}: ${shareAnimation[0]}</p>`;
        }, delay);

        delay += Animation_Delay;

        for (let i = 1; i < shareAnimation.length; i++) {
            setTimeout(() => {
                document.getElementById(person).innerHTML = `${person}: ${shareAnimation[i]}`;
            }, delay);
            delay += Animation_Delay;
        }

        setTimeout(() => {
            const ffxValue = calculateFFX(planPool0xt[person] + planFarm0xt[person]);
            let suffix = '';
            if (ffxValue.includes('Cr')) {
                suffix = 'Cr';
            } else if (ffxValue.includes('La')) {
                suffix = 'La';
            } else if (ffxValue.includes('Th')) {
                suffix = 'Th';
            }
            const formattedValue = ffxValue.replace(suffix, '').trim();
            document.getElementById(person).innerHTML =
                `<span style="color: ${colors.nameColor}">${person}</span> : 
                <span style="color: ${colors.textColor}">${formattedValue}</span> 
                <span style="color: ${colors.ffxLabelColor}">${suffix}</span> 
                <span style="color: ${colors.ffxTextColor}">FFX</span>`;
        }, delay);

        delay += Animation_Delay;
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
