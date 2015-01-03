var channelController = (function($){

	var WS_URL = 'ws://127.0.0.1:8001/';
	window.WebSocket = window.WebSocket || window.MozWebSocket;

	//http status codes
	var HTTP_OK = "success",
		HTTP_NOT_MODIFIED = "notmodified";

	var messageTextArea,
		messageSendButton;
		
	var currentChannel = 0;
	var connection = null;
	function changeChannel(channelId){
		currentChannel = channelId;
		if(!connection){
			connection = new WebSocket(WS_URL+channelId);

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
				try{
					var data = JSON.parse(message.data);
					console.log(data);
					messageList.append(data.html);
					messageTextArea.removeAttr('disabled');
					messageSendButton.removeAttr('disabled');
				}
				catch(e){
					console.error('Invalid JSON sent from endpoint.');
					console.error(message.data);
				}
			}
		}
	}

	function sendMessage(text){
		if (!text) {
			return;
		}
		console.log('Attempting to send message: ' + text);

		var msg = {
			opId :  3,
			channelId : currentChannel,
			timestamp : 10000000,
			text : text
		}

		if(connection){
			connection.send(JSON.stringify(msg));
		}

		messageTextArea.val('');
		messageTextArea.attr('disabled', 'disabled');
		messageSendButton.attr('disabled', 'disabled');
	}

	$(function() {
		messageTextArea 	= $('#messageTextArea');
		messageSendButton 	= $('#messageSendButton');
		messageList 		= $('#messageList');

		messageSendButton.click(function(){
			sendMessage(messageTextArea.val());
		});

		messageTextArea.keydown(function(e) {
			if (e.keyCode === 13) {
				sendMessage(messageTextArea.val());
			}
		});
	})

	return {
		changeChannel: changeChannel
	}
})(jQuery);
