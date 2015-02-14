
module.exports = function(){
	//Channels use a Linked List structure to track connections to faciliate quick add and removal
	function Channel(channelId, conn){
		var id = channelId,
			head = conn;
		head.next = null;
		head.prev = null;

		function addConnection(conn){
			head.prev = conn;
			conn.next = head;
			head = head.prev;
		}

		function removeConnection(conn){
			//if at the head of the list
			if(conn.prev == null){
				head = conn.next;
				conn.next.prev = null;
			}
			//else if at the tail of the list
			else if(conn.next == null){
				conn.prev.next = null;
			}
			else{
				conn.prev.next = conn.next;
				conn.next.prev = conn.prev;
			}
		}

		function sendMessage(msg){

			var message = JSON.stringify({
				error: null,
				content: msg,
				timestamp: Date.now()
			});

			var conn = head;
			while(conn != null){
				conn.send(message);
				conn = conn.next;
			}
		}

		return {
			addConnection : addConnection,
			removeConnection : removeConnection,
			sendMessage : sendMessage
		};
	}

	var channels = {};
	var messageBuffer = [];

	

	return {
		addConnection : function(channelId, conn){
			if (!channels[channelId]){
				channels[channelId] = new Channel(channelId, conn);
				console.log('Channel created with id: ' + channelId);
			}
			else{
				channels[channelId].addConnection(conn);
			}
			console.log('Connection added to channel ' + channelId);
		},

		removeConnection : function(channelId, conn){
			//if we remove the last connection in the list, destroy the channel
			if(conn.prev == null && conn.next == null){
				delete channels[channelId];
				return;
			}
			else{
				channels[channelId].removeConnection(conn);
			}
		},

		sendMessage : function(msg){
			if(channels[msg.channelId]){
				channels[msg.channelId].sendMessage(msg);
			}
		}
	}
};