const express = require("express");
const router = express.Router();




// About page route.
router.get("/login", function (req, res) {

    data = [
        {
            "login": "sotoarmando",
            "password": "sotoarmandopw"
        }
    ]

    const { password: user_password, login: user_login } = req.query;
    if (data.find(user => user.login == user_login && user.password == user_password)) {
        res.send(true);
    } else {
        res.send(false);
    }
    
});

module.exports = router;