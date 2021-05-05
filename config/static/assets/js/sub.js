window.onload=function(){

const workerOptions = {
        OggOpusEncoderWasmPath: 'https://cdn.jsdelivr.net/npm/opus-media-recorder@0.8.0/OggOpusEncoder.wasm',
        WebMOpusEncoderWasmPath: 'https://cdn.jsdelivr.net/npm/opus-media-recorder@0.8.0/WebMOpusEncoder.wasm'
    };
    //polyfill mediarecorder.
    window.MediaRecorder = OpusMediaRecorder;

    //DB에는 msg만 저장?
    var textInput = document.getElementById("chatbox");
    var recordBtn = document.getElementsByClassName("some_btn");
    var record_state=false;

    function hasGetUserMedia() {
        return !!(navigator.getUserMedia || navigator.webkitGetUserMedia ||
        navigator.mozGetUserMedia || navigator.msGetUserMedia);
    }

    if (hasGetUserMedia() ){
        var constraints = { audio:true, video:false }
        navigator.mediaDevices.getUserMedia(constraints)
        .then(stream => {streamHandlerFunction(stream)})
        .catch(function(err) {
            //disable the record button if getUserMedia() fails
            console.log(`error on access getUserMedia : ${err.message}`);
            recordBtn.disabled = true;
        })
    }
    else {
        console.log("cant access getUserMedia");
    }


    function streamHandlerFunction(stream) {
        rec = new MediaRecorder(stream, {mimeType : 'audio/ogg'},workerOptions);
        rec.ondataavailable = e =>{
            console.log("Recording started");
            var audioBinary = [];
            audioBinary.push(e.data);
            if( rec.state == "inactive"){
                console.log("Recording end");
                let blob = new Blob( audioBinary, {type:'audio/ogg'});
                sendData(blob);
            }
        }
    }


    function sendData(data){
        var request = new XMLHttpRequest();
        var fd = new FormData();
        fd.append("audio_data", data, "audiodata.ogg");
        request.open("POST","stt/",true);
        request.onreadystatechange = function (){
            if(request.readyState == XMLHttpRequest.DONE) {
                console.log("stt done;");
                console.log(request.responseText);
                textInput.value = request.responseText;
            } else {}
        }
        console.log("sending data to server")
        request.send(fd);
    }

    //녹음버튼
    $('.some_btn').click(function(){
        record_state=!record_state
        if(record_state)
        {
        //녹음시작
            $('.some_btn').css("background","red")
            console.log("start recording btn clicked");
            rec.start();
        }
        else if(!record_state)
        {
        //녹음 끝!
            $('.some_btn').css("background", "#05728f")
            console.log("stopButton clicked");
            rec.stop();
        }
    })
    var count=1;
    var name_id="id_s"+count;
     function msg_send_fnc()
    {
        if($('#chatbox').val()=="")
        {
            alert("내용을 입력해주세요")
        }

        else{
        let date=new Date();
        var date_txt=date.toLocaleTimeString();
        var $new=$("<div class='outgoing_msg'>"+"<div class='sent_msg'>"+"<p>"+ $('#chatbox').val()+"</p>"+"<span class='time_date'>"+date_txt+"</span>"+"</div>"+"</div>")

////////*---------챗봇 답변 with 로딩---------*///////////
        $('#msg_list_bx_real').append($new);
        name_id="id_s"+count;
        $('#msg_list_bx_real').append("<div class='incoming_msg'><div class='received_msg'><div class='received_withd_msg' id="+name_id+"><div class='loader_box'><div class='loader10'></div></div></div></div></div>");
        $('.msg_history').scrollTop($('.msg_history')[0].scrollHeight);
        $('#chatbox').attr("disabled",true);
        $.ajax({
            url:'/model',
            type:"POST",
            data:{'x': $('#chatbox').val()},
            dataType:'json',
            error:function(request, status, error)
            {
              $('.loader_box').remove();
              $('#'+name_id).append("<p>"+error+"</p>");
              $('.msg_history').scrollTop($('.msg_history')[0].scrollHeight);
            },
            success:function(data){
              //alert(data.result);
              //let date_out=new Date();
              //var date_out_txt=date_out.toLocaleTimeString();
              $('.loader_box').remove();
              $('#'+name_id).append("<p>"+data.result+"</p>");
              $('.msg_history').scrollTop($('.msg_history')[0].scrollHeight);
               // tts result str
               speech(data.result);
            },
            complete:function(){
                $('#chatbox').attr("disabled",false);
            }
        })
        $('#chatbox').val("");
        }

    }

    $(document).keydown(function(e){
        if(e.keyCode == '13'){
            count=count+1;
            msg_send_fnc();
        }
    })
    $('.msg_send_btn').click(function(){
        count=count+1;
        msg_send_fnc();
    })

// tts script
    var voices = [];
    function setVoiceList() {
        voices = window.speechSynthesis.getVoices();
    }
    setVoiceList();
    if (window.speechSynthesis.onvoiceschanged !== undefined) {
        window.speechSynthesis.onvoiceschanged = setVoiceList;
    }

    function speech(txt) {
        console.log("trying tts")

        if(!window.speechSynthesis) {
            alert("browser does not support tts");
            return;
        }
        var lang = 'ko-KR';
        var TtsObject = new SpeechSynthesisUtterance(txt);

        // find ko-KR or ko_KR and link it
        var voiceFound = false;
        for(var i = 0; i < voices.length ; i++) {
            if(voices[i].lang.indexOf(lang) >= 0 || voices[i].lang.indexOf(lang.replace('-', '_')) >= 0) {
                TtsObject.voice = voices[i];
                voiceFound = true;
            }
        }
        if(!voiceFound) {
            alert('voice not found');
            return;
        }

        TtsObject.lang = lang;
        TtsObject.pitch = 1;
        TtsObject.rate = 1.1; //속도
        window.speechSynthesis.speak(TtsObject);
    }

}