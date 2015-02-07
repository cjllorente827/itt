(function($){

	var messageList,
		tabIsOpen = {},
		tabs,
		main;

	function openTab(channelId, channelTitle){
		if(!tabIsOpen[channelId]){
			main.show();
			renderNewTab(channelId, channelTitle);
		}
		gotoTab(channelId);
	}

	function renderNewTab(channelId, channelTitle){
		tabs.append(
			$("<div />", {
				id : "tab_"+channelId,
				class: "tab",
			}).append([
				$('<p />', {
					class : 'tabtext',
					text : channelTitle,
					click : function(){
						gotoTab(channelId);
					},
				}),
				$('<button />', {
					text : 'X',
					click : function(){
						closeTab(channelId);
					},
				}),
			])
		);
		tabIsOpen[channelId] = true;
	}

	function gotoTab(channelId){
		tabs.children(".active").removeClass("active");
		tabs.children("#tab_"+channelId).addClass("active");
		channelController.changeChannel(channelId);
	}

	function closeTab(channelId){
		var removedTab = $('#tab_'+channelId).remove();
		messageList.empty();
		delete tabIsOpen[channelId];
		if(Object.keys(tabIsOpen).length === 0){
			main.hide();
			currentChannel = false;
		}
		else if(removedTab.hasClass('active')){
			for(var key in tabIsOpen){
				gotoTab(key);
				return;
			}
		}
	}

	$(function() {
		messageList = $('#messageList');
		tabs = $('#tabs');
		main = $('#main');

		var channels 	= $('#channelsList > p > a');
		for(var c in channels){
			if(channels[c].id){
				channels[c].onclick = function(){
					openTab(this.id.replace('channel_', ''), this.innerHTML);
				};
			}
		}
	})
})(jQuery);