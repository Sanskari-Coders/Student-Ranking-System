
document.addEventListener('DOMContentLoaded', function() {
  var ctx = document.getElementById('myChart').getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['IT', 'BCA', 'MATH', 'phy', 'Chem','zoolgy','bot'],
      datasets: [{
        label: 'Sales',
        data: [9,8,4,9,5,6.5,9],
        backgroundColor: [
          'rgb(218,223,255)',
          'rgb(205,255,143)',
          'rgb(254, 222, 133)',
          'rgba(255, 213, 224)',
          'rgb(156, 175, 170)',
          'rgb(239, 188, 155)',
          'rgb(142, 122, 181)'
          
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      }
    }
  });
});
