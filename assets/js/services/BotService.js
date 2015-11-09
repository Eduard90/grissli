app.service('BotService', ['$q', 'API', function($q, API){
    var path = 'bot/';

    //this.getAll = function() {
    //    var get_path = path;
    //    return API.get(get_path);
    //};

    this.sendCommand = function(command) {
        var get_path = path + 'command/?command='+command;
        return API.get(get_path);
    };

    this.waitResult = function(task_id) {
        var get_path = path + 'command/' + task_id + '/';
        return API.get(get_path);
    };
}]);