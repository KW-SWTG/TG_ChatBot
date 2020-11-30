var count=0;
var parent_id="";
var usr_msg="";

var lastUserMessage = "";

function create()
{
    var element=document.createElement("div");
    element.setAttribute("class",arguments[0]);
    element.setAttribute("id",arguments[1]);
    arguments[2].appendChild(element);
    return element;//parent를 위해 만들어진 element를 리턴받기
}

function btn_click()
{
    count=count+1;

    lastUserMessage = document.getElementById("chatbox").value;
    parent_id=document.getElementById("msg_list_bx_real");//여기에다가 메세지를 만들어 줄거다! parent_id.appendChild("d")l해서
    var outgm=create("outgoing_msg","outgoing_msg"+count, parent_id);
    var sentmsg=create("sent_msg","sent_msg", outgm);
    var text=document.createTextNode(lastUserMessage);
    var p_1=document.createElement('p');
    sentmsg.appendChild(p_1);
    p_1.appendChild(text);


    let date=new Date();
    var date_txt=date.toLocaleTimeString();
    var date_time=document.createElement("span");
    date_time.setAttribute("class", "time_date");
    var text_date=document.createTextNode(date_txt);
    sentmsg.appendChild(date_time);
    date_time.appendChild(text_date);
    //2.챗봇 메세지 보이기

    setTimeout(function() {
    parent_id=document.getElementById("msg_list_bx_real");//여기에다가 메세지를 만들어 줄거다! parent_id.appendChild("d")l해서
    var incmsg=create("incoming_msg", "incoming_msg"+count,parent_id);
    var reciev=create("received_msg","received_msg"+count,incmsg);

    var recieve_wth=create("received_withd_msg","received_withd_msg",reciev);

    var text_chat=document.createTextNode(lastUserMessage);
    var p_2=document.createElement('p');
    recieve_wth.appendChild(p_2);
    p_2.appendChild(text_chat);

    let date=new Date();
    var date_txt=date.toLocaleTimeString();
    var date_time=document.createElement("span");
    date_time.setAttribute("class", "time_date");
    var text_date=document.createTextNode(date_txt);
    recieve_wth.appendChild(date_time);
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
    btn_click();
  }
}

