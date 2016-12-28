angular.module('barChart', ['nvd3'])
  .component('barChart', {
  template:'<h1>Total Games</h1><nvd3 options="options" data="data"></nvd3>',
  controller: ['$scope', '$http', function($scope, $http) {
    $http.get('/api/kaggle/total/?form=d3')
      .then(function(response){
      $scope.data = response.data
               
      $scope.options = {
        chart: {
          type: 'discreteBarChart',
          height: 450,
          margin : {
            top: 20,
            right: 20,
            bottom: 50,
            left: 55
          },
          x: function(d){return d.platform;},
          y: function(d){return d.total;},
          showValues: true,
          valueFormat: function(d){
            return d3.format(',')(d);
          },
          duration: 500,
          xAxis: {
            axisLabel: 'Platforms'
          },
          yAxis: {
            axisLabel: 'Total games',
            axisLabelDistance: -10
          }
        }
      };             
    
    });
  }]
});
