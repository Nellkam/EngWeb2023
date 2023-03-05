var http = require('http');
var fs = require('fs');

function getFilename(url){
    path = "./pages/"
    if(url=="/")
        path += "index"
    else
        path += url
    return path.includes(".html") ?  path : path + ".html"
}

const server = http.createServer(function (req, res) {
    console.log(req.url)
    var filename = getFilename(req.url)
    fs.readFile(filename, function(err, data) {
        if (err) {
            res.writeHead(404, {'Content-Type': 'text/html'});
            return res.end("404 Not Found");
        } 
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    return res.end();
    });
});

server.listen(7777)
