'use strict';

var app = angular.module('BotApp', ['luegg.directives']);

app.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.run(['$rootScope', function($rootScope) {
    $rootScope.nick = '';
}]);

app.controller('LoginCtrl', ['$scope', '$rootScope', 'LoginService', function($scope, $rootScope, LoginService) {
    $scope.nick = '';

    $scope.login = function() {
        LoginService.setNick($scope.nick).then(function(resp) {
            if (resp.result == 1) {
                $rootScope.nick = $scope.nick;
            } else {
                alert(resp.result);
            }
        });
    };
}]);

app.controller('ChatCtrl', ['$scope', '$timeout', 'BotService', 'MessageService', function($scope, $timeout, BotService, MessageService) {
    $scope.parseResponse = function(resp) {
        for(var i = 0; i < resp.messages.length; i++) {
            var chatText = {
                'time': resp.messages[i].time,
                'nick': resp.messages[i].nick,
                'text': resp.messages[i].text,
            };
            $scope.chatText.push(chatText);
        }
    };

    $scope.command = 'Бот, дай мне заголовок сайта http://ya.ru';
    $scope.chatText = [];

    $scope.waitResult = function(task_id) {
        BotService.waitResult(task_id).then(function(result) {
            if (result.result !== -1) {
                $scope.parseResponse(result);
            } else {
                $timeout($scope.waitResult(task_id), 0);
            }
        })
    };

    $scope.send = function() {
        BotService.sendCommand($scope.command).then(function(resp) {
            if (resp.task_id != 0) {
                $scope.waitResult(resp.task_id);
            } else {
                //alert(resp.error);
            }

            $scope.parseResponse(resp);
        });
    };

    MessageService.getAll().then(function(resp) {
        $scope.parseResponse(resp);
    });
}]);
