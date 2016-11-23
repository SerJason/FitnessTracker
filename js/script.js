var User = {
  load: function () {
    User.jqXHR = $.getJSON("../py/getUser.py", function (data) {
          User.name = data.name;
          User.username = data.username;
        });
  }
};

$(function () {
  User.load();
});
