const startBtn = document.querySelector('#start-btn');
const pauseBtn = document.querySelector("#pause-btn");
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
const sleep = msec => new Promise(resolve => setTimeout(resolve, msec));
startBtn.onclick = () => {
  console.log("3");
  let welcom=welcome.textContent;
  welcome.textContent = "3";
  await sleep(1000);
  welcome.textContent = "2";
  console.log("2");
  await sleep(1000);
  console.log("1");
  welcome.textContent = "1";
  await sleep(1000);

  recognition.start();
}
pauseBtn.onclick = () => {
  recognition.stop();
}
stopBtn.onclick = () => {
  recognition.stop();
}