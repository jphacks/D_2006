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
const sleep = msec => new Promise(resolve => setTimeout(resolve, msec));

// const welcome = document.querySelector("#countdown")
startBtn.onclick = () => {
  // var dt = new Date();
  // var sec=3;
  
  // console.log("Start: ", dt);
  // // 終了時刻を開始日時+カウントダウンする秒数に設定
  // var endDt = new Date(dt.getTime() + sec * 1000);
  // console.log("End : ", endDt);
  // welcome.textContent=sec;
  // var cnt = 3;
  // var id = setInterval(function(){
  //   cnt--;
  //   console.log(cnt+1);
  //   welcome.textContent=cnt;
  //   // 現在日時と終了日時を比較
  //   dt = new Date();
  //   if(dt.getTime() >= endDt.getTime()){
  //     clearInterval(id);
  //     console.log("Finish!");
  //     welcome.textContent="START";
  //   }
  // }, 1000);
  recognition.start();

}

stopBtn.onclick = () => {
  recognition.stop();
}

// 送信ボタン
let send_btn=document.querySelector("#bms_send_btn");

// send_btn.onclick=()=>{
//   let user_say=document.querySelectorAll("#bms_message bms_right");
//   let last_say=user_say[user_say.length-1];
//   let text=last_say.textContent;
//   recognition.stop();
//   var req=new XMLHttpRequest();
//   req.open();
// }