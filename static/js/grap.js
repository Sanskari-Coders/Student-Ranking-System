document.addEventListener('DOMContentLoaded', function() {
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['IT', 'BCA', 'MATH', 'phy', 'Chem','zoolgy','bot'],
        datasets: [{
          label: 'hide',
          data: [8.5,4,7,9,5,6.5,9, 10],
          backgroundColor: [
            'rgb(91, 97, 217)',
            'rgb(218, 223, 255)',
            'rgb(220, 24, 84)',
            'rgba(106,77,170)',
            'rgb(253, 135, 6)',
            'rgb(205,255,143)',
            'rgb(206, 253, 255)'
            
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
  