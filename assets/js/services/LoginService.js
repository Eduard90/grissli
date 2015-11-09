app.service('LoginService', ['$q', 'API', function($q, API){
    var path = 'login/';

    this.setNick = function(nick) {
        var get_path = path + '?nick=' + nick;
        return API.get(get_path);
    };
}]);