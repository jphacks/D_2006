const startBtn = document.querySelector('#start-btn');
const stopBtn = document.querySelector('#stop-btn');

SpeechRecognition = webkitSpeechRecognition || SpeechRecognition;
let recognition = new SpeechRecognition();

recognition.lang = 'ja-JP';
recognition.interimResults = true;
recognition.continuous = true;

let finalTranscript = ''; // 確定した(黒の)認識結果

recognition.onresult = (event) => {
  const resultDiv = document.querySelector('#result-div');
  let interimTranscript = ''; // 暫定(灰色)の認識結果
  for (let i = event.resultIndex; i < event.results.length; i++) {
    let transcript = event.results[i][0].transcript;
    if (event.results[i].isFinal) {
      finalTranscript += transcript;
    } else {
      interimTranscript = transcript;
    }
  }

  resultDiv.innerHTML = finalTranscript + '<i style="color:#ddd;">' + interimTranscript + '</i>';
}
const sleep = msec => new Promise(resolve => setTimeout(resolve, msec));

function rec_start(){
  console.log("rec_start");
  recognition.start();
}

const SEND_STATE_NOTSEND="not_send"
const SEND_STATE_SENT="sent"


startBtn.onclick = () => {
  
  rec_start();
  var elem2 = document.getElementById("make-result");
  elem2.insertAdjacentHTML( "beforeend",`
    <div class="bms_message bms_right">
      <div class="bms_message_box">
        <div class="bms_message_content">
          <div class="bms_message_text user_say" Id="result-div" value="not_send"></div>
        </div>
      </div>
    </div>
    <div class="bms_clear"></div>
  `);
  
  var elem = document.getElementById("make-stop-btn");
  elem.innerHTML = `
    <div class="bms_message bms_left">
      <div class="bms_message_box">
        <div class="bms_message_content">
          <div class="bms_message_text">デバッグ終わろか？</div>
            <div class="buttons">
              <a href="#" class="btn-stop" id="stop-btn" onclick=\"stop_rec()\">　終了　</a>
            </div>
        </div>
      </div >
    </div >
    <div class="bms_clear"></div>

    <div class="bms_message bms_left">
      <div class="bms_message_box">
        <div class="bms_message_content">
          <div class="bms_message_text">送信押してくれ</div>
        </div>
      </div >
    </div >
    <div class="bms_clear"></div>
  `;
}

function stop_rec(){
  console.log("recog end");
  recognition.stop();
}

// // 送信ボタン
// let send_btn=document.querySelector("#bms_send_btn");
// 送信ボタンはクリックされると、JSON形式でUserがしゃべった言葉をサーバへ送信する処理が行われる
let send_btn=document.querySelector("#bms_send");
console.log(send_btn);
send_btn.onclick=()=>{
  // let user_say=document.querySelectorAll("#bms_message_bms_right");
  // let last_say=user_say[user_say.length-1];
  // let text=last_say.textContent;
  // recognition.stop();

  console.log("send start");

  /*送信されてない情報を取得*/
  var ele=document.querySelectorAll(".user_say");
  let servertext="初期";
  const tmp= async()=>{
    for(let element of ele ){
      if(element.getAttribute("value")===SEND_STATE_NOTSEND){
        servertext+=element.textContent+"baka";
        element.setAttribute("value",SEND_STATE_SENT);
      }
    }
  };


  await tmp();
  const obj = {"anal_text": servertext};
  const method = "POST";
  const body = JSON.stringify(obj);

  const headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
  };
  fetch("https://3841a23ac114.ngrok.io/anal", {method, headers, body}).then((res)=> 
    res.json()).then(ans=>{
    console.log("send OK");
    console.log(ans["analed_text"]);
    var text=ans["analed_text"];
    var elem = document.getElementById("make-stop-btn");
    elem.insertAdjacentHTML("beforeend",`
    <div class="bms_message bms_left">
      <div class="bms_message_box">
        <div class="bms_message_content">
          <div class="bms_message_text">${text}</div>
        </div>
      </div>
    </div>
    `);
                            
  } ).catch(
    console.error
    );


}