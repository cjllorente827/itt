var IP_ADDR = '127.0.0.1',
	PORT 	= 8001;

var http = require('http');

var sqlite3 = require('sqlite3').verbose();
var DB_MODE = sqlite3.OPEN_READWRITE | sqlite3.OPEN_CREATE;
var db = new sqlite3.Database('C:\\Users\\CJ\\Projects\\itt\\db.sqlite3', DB_MODE, db_log);

http.createServer(function (request, response) {
	route(request, response);
	//getMessages(response, 3);
}).listen(PORT, IP_ADDR);

function db_log(err){
	if(err){
		console.error(err);
	}
}

function route(request, response){
	var args = request.url.split('/');
	
	getMessages(response, args[4], args[6]);
}

function getMessages(response, channelId, timestamp){
	
	var result = [];
	var query = '	SELECT text, op_id, timestamp \
					FROM channel_message \
					WHERE channel_id = $id \
						AND timestamp > $timestamp\
					ORDER BY timestamp DESC\
					LIMIT 30';
	response.writeHead(200, {'Content-type' : 'text/html'});
	db.each(query, {$id : channelId, 
			$timestamp : timestamp
		}, 
		//gets called on each row
		function(err, row){
			if(err){
				db_log(err);
				return;
			}
			result.push( '<span class="author">'+row.op_id+
						'</span><span class="timestamp">'+row.timestamp+
						'</span><p>'+row.text+'</p>');
		}, 
		//gets called on completion
		function(){
			var reversed = result.reverse();
			var str = '';
			for(var i in reversed){
				str += reversed[i];
			}
			response.end(str);
		});

	return result;
}

console.log('Server running at http://'+IP_ADDR+':'+PORT);

