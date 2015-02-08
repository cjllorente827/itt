

//Dependencies
var http = require('http'),
	sqlite3 = require('sqlite3').verbose(),
	websocket = require('websocket').server,
	channelController = require('./channelController')(),
	Settings = require('./settings')();


var db = new sqlite3.Database(Settings.DatabaseUrl, sqlite3.OPEN_READWRITE | sqlite3.OPEN_CREATE, function(error){
	if(error){
		console.error(error);
	}
});

var server = http.createServer(function (request, response) {
	console.log(request);
}).listen(Settings.Port, Settings.Address);

var ws = new websocket({
    httpServer: server
});

var writeSQL = 'INSERT INTO channel_message \
				(text, channel_id, timestamp, op_id) \
				VALUES ($text, $channelId, $timestamp, $opId)';

ws.on('request', function(request){
	var conn = request.accept(null, request.origin);
	
	conn.on('message', function(msg){
		if(msg.type === 'utf8'){
			console.log('Message received');
			console.log(msg);
			msg = JSON.parse(msg.utf8Data);
			db.run(writeSQL, {
				$text : msg.text,
				$channelId : msg.channelId,
				$timestamp : msg.timestamp,
				$opId : msg.opId
			});
			channelController.sendMessage(msg);
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

console.log('Server running at http://' + Settings.Address + ':' + Settings.Port);

