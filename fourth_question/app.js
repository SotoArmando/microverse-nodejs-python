const users_controller = require("./controllers/users/users_controller");
const cors = require('cors');


const express = require('express');
const app = express();

app.set('view engine', 'ejs');
app.set('views', './public');

app.use(cors({
  origin: function (origin, callback) {
    callback(null, '*');
  }
}));

app.use("/users", users_controller);

app.get('/', (req, res) => {
  res.render('index');
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
