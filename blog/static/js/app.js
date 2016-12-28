angular.module("app", [
	'ngRoute',
	'ngResource',
	'nvd3',
	'barChart',
	'totalSales'
])
.controller("main", function($scope) {
  $scope.name = "Hello World!";
})
.config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider){
  $locationProvider.html5Mode({
    enabled:true,
    requireBase: false
  })

  $routeProvider.
    when("/bar-chart", {
      template: "<bar-chart></bar-chart>"
    }).
    when("/total-sales", {
      template: "<total-sales></total-sales>"
    }).
    otherwise({
      redirectTo: "/"
    })
}]);

