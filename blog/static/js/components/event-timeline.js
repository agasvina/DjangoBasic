angular.module('eventTimeline', ['ngCookies','ngRoute'])
  .component('eventTimeline', {
  templateUrl:'/api/templates/event-timeline.html',
  controller: ['$scope', '$http', '$cookies','$location', '$compile', function($scope, $http, $cookies, $location, $compile) {

    $scope.showDetail = false;
    $scope.items;

    //GET THE TIMELINE:
    $scope.getTimeline = function(id) {
      $scope.items = new vis.DataSet([]);
      $scope.items.patient = id;
      var death = false;

      $http.get('/api/patient/main/?id='+id)
          .then(function(res){
            $scope.showDetail = true;
            var elements = []
            res.data.forEach(function(element) {
              element["id"] = "main-"+element.index
              element["content"] = "<span id='main-"+element.index+"'>Diagnosis</span>"
              element["start"] = element.anndate.substring(0,10)
              element["style"] = "background-color:grey;"
              elements.push(element)

              if(element.datdeath != null && !death) {
                death = true;
                //Create Death timeline:
                dElement = {
                  id: "death-" + element.index,
                  content: "<span id='death-"+element.index+ "'>Death:" + element.stateOfDeath+"</span>",
                  start: element.datdeath.substring(0,10),
                  style: "background-color:red",
                }
                elements.push(dElement)
              }
            });
            $scope.items.add(elements)
      });
      
      $http.get('/api/patient/followup/?id='+id)
          .then(function(res){
            var elements = []
            res.data.forEach(function(element){
              fElement = {
                id : "followUp-"+ element.index,
                content: [ "<span>FU:",
                            element.futype.split("-")[1],
                            "-P",
                            element.primary,
                            "-E",
                            element.episode,
                            "</span>"
                         ].join(""),
                start : element.fudate.substring(0,10),
                style : "background-color:aqua",
              }
              elements.push(fElement);
            });
            $scope.items.add(elements)
      });

      $http.get('/api/patient/hormone/?id='+id)
          .then(function(res){
            var elements = []
            res.data.forEach(function(element){
              hElement = {
                id : "hormone-"+ element.index,
                content: ["<span id='hormone-"+element.index+"'>hormone</span>"].join(""),
                // content: [ "<span id='hormone-",
                //             element.index,
                //             "'>Hormone:<b>",
                //             element.material.split("-")[1],
                //             "-P",
                //             element.primary,
                //             "-E",
                //             element.episode,
                //             "</b></span>"
                //          ].join(""),
                start : element.stdate.substring(0,10),
                style : "background-color:greenyellow;",
                //Extra information:
                material: element.material.split("-")[1],
                method: element.method.split("-")[1],
                primary: element.primary,
                episode: element.episode
              }
              if(element.enddate != null) {
                hElement["end"] = element.enddate.substring(0,10)
              }
              elements.push(hElement);
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

          scope.showDetail = function(event) {
                var data_template = event.target.id.split('-')[0]; 
                var value = newVal._data[event.target.id];
                var $elem = angular.element(document.querySelector( '#event-timeline-detail' ) );
                console.log(data_template)
                if(data_template == 'main') {
                  $elem.replaceWith(generateDiagnosisDetail(value));
                } else if(data_template == 'hormone') {
                  $elem.replaceWith(generateHormoneDetail(value));
                }
          }

          var generateDiagnosisDetail = function(data) {
            return [ 
              '<div id="event-timeline-detail" class="well"><span class="pull-right"><i><h4>Diagnosis detail</h4></i></span><p></br>',
              'Anniversary Date: <b>',
              data.anndate.substring(0,10),
              '</b></p><p> Site: <b>',
              data.siteMeaning,
              '</b></p><p> Performance Status: <b>',
              data.performanceStatus,
              '</b></p><p> Stage: <b>',
              data.stage,
              '<b></p></div>'
            ].join("")
          }

          var generateHormoneDetail = function(data) {
            return [ 
              '<div id="event-timeline-detail" class="well"><span class="pull-right"><i><h4>Hormone detail</h4></i></span><p></br>',
              'Start Date: <b>',
              data.start,
              data["end"]? '</b><p>End Date: <b>': "",
              data["end"]? data.end: "",
              '</b></p><p> Primary: <b>',
              data.primary,
              '</b></p><p> Episode: <b>',
              data.episode,
              '</b></p><p> Material: <b>',
              data.material,
              '</b></p><p> Method: <b>',
              data.method,
              '<b></p></div>'
            ].join("")
          }

          for(id of Object.keys(newVal._data)) {
            var data = newVal._data[id];
            var dataType = id.split('-')[0]; 
            var $elem = angular.element(document.querySelector('#'+id));
            if(dataType == 'main'){
              $elem.replaceWith($compile("<span id='"+id+"' ng-click='showDetail($event)'>Diagnosis</span>")(scope));
            } 
            else if(dataType == 'hormone') {
              var content = [ "<span id='",
                            data.id,
                            "' ng-click='showDetail($event)' >Hormone:",
                            data.material,
                            "-P",
                            data.primary,
                            "-E",
                            data.episode,
                            "</span>"
                         ].join("")
              console.log(content)
              $elem.replaceWith($compile(content)(scope));
            }
          }

        }
      }, true);
    }
  };
});