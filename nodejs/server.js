

//Dependencies
var http = require('http'),
	sqlite3 = require('sqlite3').verbose(),
	websocket = require('websocket').server,
	channelController = require('./channelController')();

//Constants
var IP_ADDR = '127.0.0.1',
	PORT 	= 8001,
	DB_MODE = sqlite3.OPEN_READWRITE | sqlite3.OPEN_CREATE,
	DB_URL = 'C:\\Users\\CJ\\Projects\\itt\\db.sqlite3';

var db = new sqlite3.Database(DB_URL, DB_MODE, db_log);

var server = http.createServer(function (request, response) {
	console.log(request);
}).listen(PORT, IP_ADDR);

var ws = new websocket({
    httpServer: server
});

ws.on('request', function(request){
	var conn = request.accept(null, request.origin);
	
	conn.on('message', function(msg){
		if(msg.type === 'utf8'){
			console.log('Message received');
			console.log(msg);
			channelController.sendMessage(JSON.parse(msg.utf8Data));
		}
		else{
			console.log('Message was not UTF 8');
		}
	});

	conn.on('close', function(conn){
		console.log('Connection closed');
	});

	channelController.addConnection(request.resource.replace('/', ''), conn);
});

function db_log(err){
	if(err){
		console.error(err);
	}
}

// function getMessages(response, channelId, timestamp){
	
// 	var result = [];
// 	var query = '	SELECT text, op_id, timestamp \
// 					FROM channel_message \
// 					WHERE channel_id = $id \
// 						AND timestamp > $timestamp\
// 					ORDER BY timestamp DESC\
// 					LIMIT 30';
// 	response.writeHead(200, {'Content-type' : 'text/html'});
// 	db.each(query, {$id : channelId, 
// 			$timestamp : timestamp
// 		}, 
// 		//gets called on each row
// 		function(err, row){
// 			if(err){
// 				db_log(err);
// 				return;
// 			}
// 			result.push( '<span class="author">'+row.op_id+
// 						'</span><span class="timestamp">'+row.timestamp+
// 						'</span><p>'+row.text+'</p>');
// 		}, 
// 		//gets called on completion
// 		function(){
// 			var reversed = result.reverse();
// 			var str = '';
// 			for(var i in reversed){
// 				str += reversed[i];
// 			}
// 			response.end(str);
// 		});

// 	return result;
// }

console.log('Server running at http://'+IP_ADDR+':'+PORT);

