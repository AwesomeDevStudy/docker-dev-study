const http = require('http');
const os = require('os');


const content = (req, res) => {
     console.log(`requset from [${req.socket.remoteAddress}]`);
     return res.end('This is it!' + '\n' + `${os.hostname()}` + '\n');
}

const web = http.createServer(content);
console.log('start server --------------------------');
web.listen(8002);

