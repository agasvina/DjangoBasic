angular.module('eventTimeline', ['ngCookies','ngRoute'])
  .component('eventTimeline', {
  templateUrl:'/api/templates/event-timeline.html',
  controller: ['$scope', '$http', '$cookies','$location', '$compile', function($scope, $http, $cookies, $location, $compile) {

    
    $scope.items;

    $scope.bummer = function($event) {
      $event.stopPropagation();
      console.log("Bummer");
    }

    //GET THE TIMELINE:
    $scope.getTimeline = function(id) {
      $scope.items = new vis.DataSet([]);
      $scope.items.patient = id;

      $http.get('/api/patient/main/?id='+id)
          .then(function(res){
            elements = []
            res.data.forEach(function(element) {
              element["id"] = "main-"+element.index
              element["content"] = "<a href='/timeline#"+element["id"]+"' ng-click='bummer($event)' target='_blank'>Diagnosis</a>"
              element["start"] = element.anndate.substring(0,10)
              element["style"] = "background-color:grey;"
              elements.push(element)

              if(element.datdeath != null) {
                //Create Death timeline:
                dElement = {
                  id: "death-" + element.index,
                  content: "<p id='death-"+element.index+ "' target='_blank'>Death</p>",
                  // content: $compile("<a href='' class='btn btn-primary' ng-click='bummer()'>Death</a>")($scope),
                  start: element.datdeath.substring(0,10),
                  style: "background-color:red",
                  stateOfDeath : element.stateOfDeath,
                }
                elements.push(dElement)
              }
            });
            $scope.items.add(elements)
        });
      };


    $scope.option = {}

  }],
}).directive("visTimeline", function( $compile) {
  return {
    restrict: "AE",
    transclude: true,
    link: function(scope, element, attrs) {

      var timeline = null;
      scope.$watch('items', function(newVal, oldVal) {
        container = element[0];
        
        if(oldVal != null && (oldVal.length != newVal.length || newVal.patient != oldVal.patient) && newVal.length > 0) {
          if(timeline != null) {
            timeline.destroy();
          }

          timeline = new vis.Timeline(container, newVal, scope.option);

          scope.bummer = function($event) {
                console.log("Bummer");
          }

          var $elem = angular.element(document.querySelector( '#death-6' ) );
          $elem.replaceWith($compile("<span ng-click='bummer()'>Death</span>")(scope));
        }
      }, true);
    }
  };
});