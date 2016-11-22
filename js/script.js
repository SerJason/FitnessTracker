var User = {
  load: function () {
    $.get("../py/getUser.py", function (data) {
          User.name = data.name;
          User.username = data.username;
        }, "json");
  }
};

$(function () {
  User.load();
});
