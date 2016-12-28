angular.module("app", [
	'ngRoute',
	'ngResource',
  'ngCookies',
	'nvd3',
	'barChart',
	'totalSales',
  'todoList',
  'loginDetail',
])
.controller("main", function($scope, $cookies) {
  $scope.name = "";
  $scope.userLoggedIn = false;
  $scope.$watch(function() {
    var token = $cookies.get("token");
    if(token) {
     //Verify token:
     $scope.userLoggedIn = true
     $scope.name = $cookies.get("username");
     console.log($scope.userLoggedIn)
    } else {
      $scope.userLoggedIn = false;
    }
  })
})
.config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider){
  $locationProvider.html5Mode({
    enabled:true,
    requireBase: false
  })

  $routeProvider.
    when("/", {
      template: "<todo-list></todo-list>"
    }).
    when("/bar-chart", {
      template: "<bar-chart></bar-chart>"
    }).
    when("/total-sales", {
      template: "<total-sales></total-sales>"
    }).
    when("/login", {
      template: "<login-detail></login-detail>"
    }).
    when("/logout", {
      redirectTo: "/login"
    }).
    otherwise({
      redirectTo: "/"
    })
}]);

