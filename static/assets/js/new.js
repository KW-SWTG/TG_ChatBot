var count=0;
var parent_id="";
var usr_msg="";
var whyrano="";


var messages = [], //array that hold the record of each string in chat
  lastUserMessage = "", //keeps track of the most recent input string from the user
  botName = 'Chatbot';//name of the chatbot



function newEntry() {
  //if the message from the user isn't empty then run
  if (document.getElementById("chatbox").value != "") {
    lastUserMessage = document.getElementById("chatbox").value;
    document.getElementById("chatbox").value = "";
    messages.push(lastUserMessage);
    messages.push("<b>" + botName + ":</b> " + lastUserMessage);
    for (var i = 1; i < 8; i++) {
      if (messages[messages.length - i])
        document.getElementById("chatlog" + i).innerHTML = messages[messages.length - i];
    }
  }
}

function btn_click()
{
    count=count+1;

    lastUserMessage = document.getElementById("chatbox").value;

    var for_user_one=document.createElement("div");
    for_user_one.setAttribute("class", "outgoing_msg");
    for_user_one.setAttribute("id", "outgoing_msg"+count);
    parent_id=document.getElementById("msg_list_bx_real");//여기에다가 메세지를 만들어 줄거다! parent_id.appendChild("d")l해서
    parent_id.appendChild(for_user_one);
  //create("outgoing_msg","outgoing_msg"+count, parent_id);

    var for_user=document.createElement("div");
    for_user.setAttribute("class", "sent_msg");
    for_user.setAttribute("id", "sent_msg");
    parent_id=document.getElementById("outgoing_msg"+count);//여기에다가 메세지를 만들어 줄거다! parent_id.appendChild("d")l해서
    parent_id.appendChild(for_user);
    //create("sent_msg","sent_msg", parent_id);
    var text=document.createTextNode(lastUserMessage);
    var p_1=document.createElement('p');
    for_user.appendChild(p_1);
    p_1.appendChild(text);

    let date=new Date();
    var date_txt=date.toLocaleTimeString();
    //alert(date.toLocaleTimeString());
    var date_time=document.createElement("span");
    date_time.setAttribute("class", "time_date");
    var text_date=document.createTextNode(date_txt);
    for_user.appendChild(date_time);
    date_time.appendChild(text_date);
    //2.챗봇 메세지 보이기

    setTimeout(function() {
    var for_chat_one=document.createElement("div");
    for_chat_one.setAttribute("class", "incoming_msg");
    for_chat_one.setAttribute("id", "incoming_msg"+count);
    parent_id=document.getElementById("msg_list_bx_real");//여기에다가 메세지를 만들어 줄거다! parent_id.appendChild("d")l해서
    parent_id.appendChild(for_chat_one);
    //create("incoming_msg", "incoming_msg"+count,parent_id);
    var for_chat=document.createElement("div");
    for_chat.setAttribute("class", "received_msg");
    for_chat.setAttribute("id", "received_msg"+count);
    parent_id=document.getElementById("incoming_msg"+count);//여기에다가 메세지를 만들어 줄거다! parent_id.appendChild("d")l해서
    parent_id.appendChild(for_chat);
    //create("received_msg","received_msg"+count,parent_id);
    var for_chat_last=document.createElement("div");
    for_chat_last.setAttribute("class", "received_withd_msg");
    for_chat_last.setAttribute("id", "received_withd_msg");
    parent_id=document.getElementById("received_msg"+count);
    parent_id.appendChild(for_chat_last);
    //create("received_withd_msg","received_withd_msg", parent_id);
    var text_chat=document.createTextNode(lastUserMessage);
    var p_2=document.createElement('p');
    for_chat_last.appendChild(p_2);
    p_2.appendChild(text_chat);

    let date=new Date();
    var date_txt=date.toLocaleTimeString();
    var date_time=document.createElement("span");
    date_time.setAttribute("class", "time_date");
    var text_date=document.createTextNode(date_txt);
    for_chat_last.appendChild(date_time);
    date_time.appendChild(text_date);
    }, 1000);


    document.getElementById("chatbox").value = "";


}


document.onkeypress = keyPress;
//if the key pressed is 'enter' runs the function newEntry()
function keyPress(e) {
  var x = e || window.event;
  var key = (x.keyCode || x.which);
  if (key == 13 || key == 3) {
    //runs this function when enter is pressed
    //add_msg();
//입력하고 엔터치면 나옴....아마 document가 다 로드된다음에 속성을 가져올 수 있어서 그런듯
    //newEntry();
    //outgoing_msg
    //1. 유저 메세지 보이기
    count=count+1;

    lastUserMessage = document.getElementById("chatbox").value;

    var for_user_one=document.createElement("div");
    for_user_one.setAttribute("class", "outgoing_msg");
    for_user_one.setAttribute("id", "outgoing_msg"+count);
    parent_id=document.getElementById("msg_list_bx_real");//여기에다가 메세지를 만들어 줄거다! parent_id.appendChild("d")l해서
    parent_id.appendChild(for_user_one);
  //create("outgoing_msg","outgoing_msg"+count, parent_id);

    var for_user=document.createElement("div");
    for_user.setAttribute("class", "sent_msg");
    for_user.setAttribute("id", "sent_msg");
    parent_id=document.getElementById("outgoing_msg"+count);//여기에다가 메세지를 만들어 줄거다! parent_id.appendChild("d")l해서
    parent_id.appendChild(for_user);
    //create("sent_msg","sent_msg", parent_id);
    var text=document.createTextNode(lastUserMessage);
    var p_1=document.createElement('p');
    for_user.appendChild(p_1);
    p_1.appendChild(text);

    let date=new Date();
    var date_txt=date.toLocaleTimeString();
    alert(date.toLocaleTimeString());
    var date_time=document.createElement("span");
    date_time.setAttribute("class", "time_date");
    var text_date=document.createTextNode(date_txt);
    for_user.appendChild(date_time);
    date_time.appendChild(text_date);
    //2.챗봇 메세지 보이기

    setTimeout(function() {
    var for_chat_one=document.createElement("div");
    for_chat_one.setAttribute("class", "incoming_msg");
    for_chat_one.setAttribute("id", "incoming_msg"+count);
    parent_id=document.getElementById("msg_list_bx_real");//여기에다가 메세지를 만들어 줄거다! parent_id.appendChild("d")l해서
    parent_id.appendChild(for_chat_one);
    //create("incoming_msg", "incoming_msg"+count,parent_id);
    var for_chat=document.createElement("div");
    for_chat.setAttribute("class", "received_msg");
    for_chat.setAttribute("id", "received_msg"+count);
    parent_id=document.getElementById("incoming_msg"+count);//여기에다가 메세지를 만들어 줄거다! parent_id.appendChild("d")l해서
    parent_id.appendChild(for_chat);
    //create("received_msg","received_msg"+count,parent_id);
    var for_chat_last=document.createElement("div");
    for_chat_last.setAttribute("class", "received_withd_msg");
    for_chat_last.setAttribute("id", "received_withd_msg");
    parent_id=document.getElementById("received_msg"+count);
    parent_id.appendChild(for_chat_last);
    //create("received_withd_msg","received_withd_msg", parent_id);
    var text_chat=document.createTextNode(lastUserMessage);
    var p_2=document.createElement('p');
    for_chat_last.appendChild(p_2);
    p_2.appendChild(text_chat);

    let date=new Date();
    var date_txt=date.toLocaleTimeString();
    var date_time=document.createElement("span");
    date_time.setAttribute("class", "time_date");
    var text_date=document.createTextNode(date_txt);
    for_chat_last.appendChild(date_time);
    date_time.appendChild(text_date);
    }, 1000);


    document.getElementById("chatbox").value = "";
    //2. 챗봇 메세지 보이기

    //3. 날짜 추가

  }
}//<span class="time_date">p다음에 ㅠㅠ
//arguments[i]로 arguments들을 불러올수 있다.
//arguments.length
function placeHolder() {
  document.getElementById("chatbox").placeholder = "";
}
function create()
{
    var element=document.createElement("div");
    element.setAttribute("class",arguments[0]);
    element.setAttribute("id",arguments[1]);
    arguments[2].appendChild(element);
}

