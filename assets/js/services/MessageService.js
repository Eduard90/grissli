app.service('MessageService', ['$q', 'API', function($q, API){
    var path = 'message/';

    this.getAll = function() {
        var get_path = path;
        return API.get(get_path);
    };
}]);