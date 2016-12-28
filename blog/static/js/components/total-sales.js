angular.module('totalSales', ['nvd3'])
  .component('totalSales', {
	template:'<h1>Total Sales</h1><nvd3 options="options" data="data"></nvd3>',
	controller: ['$scope', '$http', function($scope, $http) {
		$http.get('/api/kaggle/summary/?form=d3&min_year=1985&max_year=2016')
		  .then(function(res){		
			$scope.data = res.data;
			$scope.options = {
			  chart: {
				  type: 'multiBarChart',
				  height: 450,
				  margin : {
					  top: 20,
					  right: 20,
					  bottom: 45,
					  left: 45
				  },
				  clipEdge: true,
				  //staggerLabels: true,
				  duration: 500,
				  stacked: true,
				  xAxis: {
					  axisLabel: 'Year',
					  showMaxMin: false,
					  tickFormat: function(d){
						  return d3.format(',f')(d);
					  }
				  },
				  yAxis: {
					  axisLabel: 'Total Sales (millions)',
					  axisLabelDistance: -20,
					  tickFormat: function(d){
						  return d3.format(',.1f')(d);
					  }
				  }}
				};             
		});
	}]
});