document.addEventListener('DOMContentLoaded', function() {
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['IT', 'BCA', 'MATH', 'Zoo', 'Bot','Phy','Chem'],
        datasets: [{
          label: 'hide',
          data: [8.5,4,7,9,5,6.5,9, 10],
          backgroundColor: [
            'rgb(91, 97, 217)',
            'rgb(218, 223, 255)',
            'rgb(75, 184, 189)',
            'rgba(220, 24, 84)',
            'rgb(104, 174, 30)',
            'rgb(106,77,170)',
            'rgb(253, 135, 6)',
            
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
  