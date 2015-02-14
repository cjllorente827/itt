var channelController = (function($){

	window.WebSocket = window.WebSocket || window.MozWebSocket;

	//http status codes
	var HTTP_OK = "success",
		HTTP_NOT_MODIFIED = "notmodified";

	var messageTpl = {
		author: '<span class="author">',
		timestamp: '</span><span class="timestamp">',
		text: '</span><p>', 
		end: '</p>'
	};

	var messageTextArea,
		messageSendButton;
		
	var currentChannel = 0;
	var connection = null;
	function changeChannel(channelId){
		currentChannel = channelId;

		$.ajax({
			url : '/c/api/channel/'+currentChannel+'/messages',
			method : 'GET',
			success : function(response, status, xhr){
				console.log(response);
				if(status == HTTP_OK){
					messageList.empty();
					messageList.append(response);
				}
				else{
					console.log(status);
					console.log(response);
				}
			}
		});

		if(!connection){
			connection = new WebSocket(Settings.WebSocketURL+channelId);

			connection.onopen = function(){
				console.log('Connection opened');
			};

			connection.onclose = function(){
				console.log('Connection closed');
			};

			connection.onerror = function(error){
				console.error('An error occurred establishing the connection');
				console.error(error);
			}

			connection.onmessage = function(message){
				var data;
				try{
					data = JSON.parse(message.data);
				}
				catch(e){
					console.error('Invalid JSON sent from endpoint.');
					console.error(message.data);
					return;
				}

				var timeString = (new Date(data.timestamp)).toLocaleString();
				var html = [messageTpl.author, data.content.opName, messageTpl.timestamp, timeString, messageTpl.text, data.content.text, messageTpl.end].join('');

				messageList.append(html);
			}
		}
	}

	function sendMessage(text){
		if (!text) {
			return;
		}

		var msg = {
			opName :  getCookie('username'),
			opId : getCookie('userId'),
			channelId : currentChannel,
			text : text
		}

		if(connection){
			connection.send(JSON.stringify(msg));
		}

		messageTextArea.val('');
	}

	$(function() {
		messageTextArea 	= $('#messageTextArea');
		messageSendButton 	= $('#messageSendButton');
		messageList 		= $('#messageList');

		messageSendButton.click(function(){
			sendMessage(messageTextArea.val());
		});

		messageTextArea.keyup(function(e) {
			if (e.keyCode === 13) {
				sendMessage(messageTextArea.val());
			}
		});
	})

	return {
		changeChannel: changeChannel
	}
})(jQuery);
