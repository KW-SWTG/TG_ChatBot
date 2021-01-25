var count=0;
var parent_id="";
var usr_msg="";

var lastUserMessage = "";


function btn_click()
{
    lastUserMessage = document.getElementById("chatbox").value;

    if(lastUserMessage == "")
    {
        alert("메세지를 입력해주세요");
    }
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

