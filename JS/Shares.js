const planPool0xt = { VPX: 510, Tanav: 610, KMX: 20, AKX: 20, Angel: 0, UCI: 0, SSX: 0, PPX: 0 };
const planFarm0xt = { VPX: 460, Tanav: 460, KMX: 0, AKX: 80, Angel: 70, UCI: 0, SSX: 0, PPX: 500 };
const discounts = { VPX: 0, Tanav: 0, KMX: 0, AKX: 0, Angel: 0, UCI: 0, SSX: 0, PPX: 0 };
const otherCompanyProfits = { VPX: 0, Tanav: 0, KMX: 0, AKX: 0, Angel: 0, UCI: 0, SSX: 0, PPX: 0 };

const calculateTotalPerPerson = (plan) => {
  return Object.values(plan).reduce((acc, value) => acc + value, 0);
};

const planTotal0xt = calculateTotalPerPerson(planPool0xt) + calculateTotalPerPerson(planFarm0xt) + calculateTotalPerPerson(discounts) + calculateTotalPerPerson(otherCompanyProfits);
const totalPerPerson = {
  VPX: planPool0xt.VPX + planFarm0xt.VPX + discounts.VPX + otherCompanyProfits.VPX,
  Tanav: planPool0xt.Tanav + planFarm0xt.Tanav + discounts.Tanav + otherCompanyProfits.Tanav,
  KMX: planPool0xt.KMX + planFarm0xt.KMX + discounts.KMX + otherCompanyProfits.KMX,
  AKX: planPool0xt.AKX + planFarm0xt.AKX + discounts.AKX + otherCompanyProfits.AKX,
  Angel: planPool0xt.Angel + planFarm0xt.Angel + discounts.Angel + otherCompanyProfits.Angel,
  UCI: planPool0xt.UCI + planFarm0xt.UCI + discounts.UCI + otherCompanyProfits.UCI,
  SSX: planPool0xt.SSX + planFarm0xt.SSX + discounts.SSX + otherCompanyProfits.SSX,
  PPX: planPool0xt.PPX + planFarm0xt.PPX + discounts.PPX + otherCompanyProfits.PPX
};

const smallShares = Object.entries(totalPerPerson).filter(([user, invested]) => (invested / planTotal0xt) * 100 < 5);
const userShares = Object.entries(totalPerPerson).map(([user, value]) => ({
  user,
  value,
  percentage: value === 0 ? '____' : ((value / planTotal0xt) * 75).toFixed(4)
}));

const updateTotalInvestedTable = () => {
  const tableBody = document.querySelector('#totalInvestedTable tbody');

  userShares.forEach(({ user, value, percentage }) => {
    const row = tableBody.insertRow();
    const cell1 = row.insertCell(0);
    const cell2 = row.insertCell(1);
    const cell3 = row.insertCell(2);

    cell1.textContent = user;
    cell1.style.color = (user === 'VPX') ? '#ff0000' : (user === 'Tanav') ? '#00ff00' : (user === 'PPX') ? '#ffd700' : (smallShares.some(([u, _]) => u === user)) ? '#00ced1' : '#fff';
    cell2.textContent = value;
    cell2.style.color = '#fff';
    cell3.textContent = `${percentage}%`;
    cell3.style.color = '#fff';
  });
};

const createPieChart = () => {
  const ctx = document.getElementById('pieChart').getContext('2d');

  const publicShares = 25;  // Fixed at 25%
  const data = {
    labels: userShares.map(share => share.user).concat('Public Shares'),
    datasets: [{
      data: userShares.map(share => parseFloat(share.percentage)).concat(publicShares),
      backgroundColor: userShares.map(share => 
        (parseFloat(share.percentage) < 5) ? '#00ced1' : 
        (share.user === 'VPX') ? '#ff0000' : 
        (share.user === 'Tanav') ? '#00ff00' : 
        (share.user === 'PPX') ? '#ffd700' : '#fff').concat('#a9a9a9')
    }]
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      tooltip: {
        callbacks: {
          label: function(context) {
            const label = context.label || '';
            const value = context.raw || 0;
            const percentage = (value === 0) ? 'NaN%' : value.toFixed(4) + '%';
            return `${label}: ${percentage}`;
          }
        }
      },
      legend: {
        display: false
      }
    },
    layout: {
      padding: 10
    },
    animation: {
      animateScale: true,
      animateRotate: true
    }
  };

  new Chart(ctx, {
    type: 'doughnut',
    data: data,
    options: options
  });
};

window.onload = () => {
  updateTotalInvestedTable();
  createPieChart();
};
