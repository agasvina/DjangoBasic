angular.module('loginDetail', ['ngCookies','ngRoute'])
  .component('loginDetail', {
  templateUrl:'/api/templates/login-detail.html',
  controller: ['$scope', '$http', '$cookies','$location', function($scope, $http, $cookies, $location) {
    
    var loginUrl = "/api-token-auth/"
    $scope.user = {}

    var tokenExists = $cookies.get("token")
    if(tokenExists) {
      //Verify token
      $cookies.remove("token")
    }

    $scope.doLogin = function(user) {
      var requestConfig = {
        method : "POST",
        url: loginUrl,
        data: {
          username: user.username,
          password: user.password
        },
        headers: {}
      }

      var requestAction = $http(requestConfig)
      requestAction.success(function(r_data, r_status, r_headers, r_config){
        $cookies.put("token", r_data.token)
        $cookies.put("username", user.username)
        $location.path("/")
      })
      requestAction.error(function(r_data, r_status, r_headers, r_config){
      })
    }
  }],
});
