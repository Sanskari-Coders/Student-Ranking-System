document.addEventListener('DOMContentLoaded', function() {
  var ctx = document.getElementById('myChart').getContext('2d');

  // Initialize chart with initial data
  var initialData = [
    parseFloat(document.getElementById('itInput').value),
    parseFloat(document.getElementById('bcaInput').value),
    parseFloat(document.getElementById('mathInput').value),
    parseFloat(document.getElementById('zooInput').value),
    parseFloat(document.getElementById('botInput').value),
    parseFloat(document.getElementById('phyInput').value),
    parseFloat(document.getElementById('chemInput').value),
    parseFloat(document.getElementById('topInput').value),
  ];
  
  var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['IT', 'BCA', 'MATH', 'Zoo', 'Bot', 'Phy', 'Chem'],
      datasets: [{
        label: 'CGPA',
        data: initialData,
        backgroundColor: [
          'rgb(91, 97, 217)',
          'rgb(218, 223, 255)',
          'rgb(75, 184, 189)',
          'rgba(220, 24, 84)',
          'rgb(104, 174, 30)',
          'rgb(106,77,170)',
          'rgb(253, 135, 6)'
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

  // Update chart data when the input values change
  document.querySelectorAll('input[type="number"]').forEach(function(input) {
    input.addEventListener('input', function() {
      var newData = [
        parseFloat(document.getElementById('itInput').value),
        parseFloat(document.getElementById('bcaInput').value),
        parseFloat(document.getElementById('mathInput').value),
        parseFloat(document.getElementById('zooInput').value),
        parseFloat(document.getElementById('botInput').value),
        parseFloat(document.getElementById('phyInput').value),
        parseFloat(document.getElementById('chemInput').value),
        parseFloat(document.getElementById('topInput').value),

      ];
      myChart.data.datasets[0].data = newData;
      myChart.update();
    });
  });
});