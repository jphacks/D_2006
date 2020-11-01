const startBtn = document.querySelector('#start-btn');
const stopBtn = document.querySelector('#stop-btn');
const resultDiv = document.querySelector('#result-div');

SpeechRecognition = webkitSpeechRecognition || SpeechRecognition;
let recognition = new SpeechRecognition();

recognition.lang = 'ja-JP';
recognition.interimResults = true;
recognition.continuous = true;

let finalTranscript = ''; // 確定した(黒の)認識結果

recognition.onresult = (event) => {
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
const welcome = document.querySelector("#welcom")
startBtn.onclick = () => {
  var dt = new Date();
  var sec=3;
  console.log("Start: ", dt);
  // 終了時刻を開始日時+カウントダウンする秒数に設定
  var endDt = new Date(dt.getTime() + sec * 1000);
  console.log("End : ", endDt);
  welcome.textContent=endDt;
  var cnt = 3;
  var id = setInterval(function(){
    cnt--;
    console.log(cnt);
    welcome.textContent=cnt;
    // 現在日時と終了日時を比較
    dt = new Date();
    if(dt.getTime() >= endDt.getTime()){
      clearInterval(id);
      console.log("Finish!");
    }
  }, 1000);
  recognition.start();

}

stopBtn.onclick = () => {
  recognition.stop();
}

// 送信ボタンはクリックされると、JSON形式でUserがしゃべった言葉をサーバへ送信する処理が行われる
let send_btn=document.querySelector("#bms_send");
console.log(send_btn);
send_btn.onclick=()=>{
  // let user_say=document.querySelectorAll("#bms_message_bms_right");
  // let last_say=user_say[user_say.length-1];
  // let text=last_say.textContent;
  // recognition.stop();

  console.log("send start");

  const obj = {"anal_text": "test"};
  const method = "POST";
  const body = JSON.stringify(obj);

  const headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
  };
  fetch("http://localhost:5000/anal", {method, headers, body}).then((res)=> 
    res.json()).then(ans=>{console.log(ans["analed_text"]);
                            
  } ).catch(
    console.error
    );


}