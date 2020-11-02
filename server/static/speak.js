const startBtn = document.querySelector('#start-btn');
const stopBtn = document.querySelector('#stop-btn');

SpeechRecognition = webkitSpeechRecognition || SpeechRecognition;
let recognition = new SpeechRecognition();

recognition.lang = 'ja-JP';
recognition.interimResults = true;
recognition.continuous = true;

let finalTranscript = ''; // 確定した(黒の)認識結果
const div_arr=["です","ます","である","だ","ました"]
recognition.onresult = (event) => {
  
  var resultDiv = document.querySelectorAll('.user_say');
  resultDiv = resultDiv[resultDiv.length - 1];
  let interimTranscript = ''; // 暫定(灰色)の認識結果
  for (let i = event.resultIndex; i < event.results.length; i++) {
    let transcript = event.results[i][0].transcript;
    if (event.results[i].isFinal) {
      finalTranscript += transcript;
    } else {
      interimTranscript = transcript;
    }
  }
  let flg=false;
  for(let s of div_arr){
    if(finalTranscript.includes(s)){
      flg=true;
      resultDiv.innerHTML = finalTranscript+"。";
      make_new_user_say();
      finalTranscript='';
    }
  }
    // if(finalTranscript.includes("です"))
  if(!flg){
     resultDiv.innerHTML = finalTranscript + '<i style="color:#ddd;">' + interimTranscript + '</i>';
  }
}
const sleep = msec => new Promise(resolve => setTimeout(resolve, msec));

function rec_start() {
  console.log("rec_start");
  recognition.start();
}

const SEND_STATE_NOTSEND = "not_send"
const SEND_STATE_SENT = "sent"

function make_new_user_say(){
  var elem2 = document.getElementById("make-result");
  elem2.insertAdjacentHTML("beforeend", `
    <div class="bms_message bms_right">
      <div class="bms_message_box">
        <div class="bms_message_content">
          <div class="bms_message_text user_say" Id="result-div" value="not_send"></div>
        </div>
      </div>
    </div>
    <div class="bms_clear"></div>
  `);

}

startBtn.onclick = () => {
  finalTranscript='';
  rec_start();
  // var elem2 = document.getElementById("make-result");
  // elem2.insertAdjacentHTML("beforeend", `
  //   <div class="bms_message bms_right">
  //     <div class="bms_message_box">
  //       <div class="bms_message_content">
  //         <div class="bms_message_text user_say" Id="result-div" value="not_send"></div>
  //       </div>
  //     </div>
  //   </div>
  //   <div class="bms_clear"></div>
  // `);
  make_new_user_say();





  var elem = document.getElementById("make-stop-btn");
  elem.innerHTML = `
    <div class="bms_message bms_left">
      <div class="bms_message_box">
        <div class="bms_message_content">
          <div class="bms_message_text">デバッグ終わろか？</div>
            <div class="buttons">
              <div data-step='2' data-intro='終了で止める。'>
                <a href="#" class="btn-stop" id="stop-btn" onclick=\"stop_rec()\">　終了　</a>
              </div>
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

function stop_rec() {
  console.log("recog end");
  recognition.stop();
}

document.addEventListener('keydown', (event) => {
  const keyName = event.key;

  if (keyName === ',') {
    punctuation += "、";
    return;
  }
  if (keyName === '.') {
    punctuation += "。\n";
    return;
  }
}, false);

// // 送信ボタン
// let send_btn=document.querySelector("#bms_send_btn");
// 送信ボタンはクリックされると、JSON形式でUserがしゃべった言葉をサーバへ送信する処理が行われる
let send_btn = document.querySelector("#bms_send");
console.log(send_btn);
send_btn.onclick = () => {
  // let user_say=document.querySelectorAll("#bms_message_bms_right");
  // let last_say=user_say[user_say.length-1];
  // let text=last_say.textContent;
  // recognition.stop();

  console.log("send start");

  /*送信されてない情報を取得*/
  var ele = document.querySelectorAll(".user_say");
  let servertext = "";

  // var promiss = new Promise(function (a) {
  //   forEach(function (element) {
  //     if (element.getAttribute("value") === SEND_STATE_NOTSEND) {
  //       servertext += element.Text;
  //       console.log(element.Text);
  //       element.setAttribute("value", SEND_STATE_SENT);
  //     }
  //   }
  //   } ) );

  // await promiss();
  for (let element of ele) {
    if (element.getAttribute("value") === SEND_STATE_NOTSEND) {
      servertext += element.textContent;
      console.log(element.textContent);
      element.setAttribute("value", SEND_STATE_SENT);
    }
  }
  




  if (servertext === "") {
    // なにも話していない
    return;
  }

  let first_element=ele[0];
  let idx=0;
  while(servertext.length>10){
    // search div
    let f=0;
    for(let s of div_arr){
      f=servertext.indexOf(s,idx);
      if(f!=-1){
        break;
      }
    }
    idx=f;
    innert_text=servertext.substring(0,idx);
    servertext=servertext.substring(idx,servertext.length);
    // element 代入
   
    
  }



  const obj = { "anal_text": servertext };
  const method = "POST";
  const body = JSON.stringify(obj);

  const headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  };
  fetch("https://3841a23ac114.ngrok.io/anal", { method, headers, body }).then((res) =>
    res.json()).then(ans => {
      console.log("send OK");
      console.log(ans["analed_text"]);
      var text = ans["analed_text"];
      var elem = document.getElementById("make-stop-btn");
      elem.insertAdjacentHTML("beforeend", `
    <div class="bms_message bms_left">
      <div class="bms_message_box">
        <div class="bms_message_content">
          <div class="bms_message_text">${text}</div>
        </div>
      </div>
    </div>
    `);

    }).catch(
      console.error
    );
}
