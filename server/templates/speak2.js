var box = document.querySelector("#start-btn");
var prevText = "";
var Recflag = false;
var speechInputFlag = false;
var punctuation = ""

//Web Speech APIが使えるかチェック
if (!('webkitSpeechRecognition' in window)) {
  alert("このブラウザでは音声入力識機能を使用できません。");
} else {
  var rec = new webkitSpeechRecognition();
  rec.continuous = true;
  rec.interimResults = true;
  rec.onresult = function (event) {
    speechInputFlag = true;
    var interim_transcript = ''; //入力中の文字列
    var final_transcript = '';  //最終的に確定した文字列

    for (var i = event.resultIndex; i < event.results.length; ++i) {
      if (event.results[i].isFinal) {
        final_transcript += event.results[i][0].transcript + punctuation;
      } else {
        interim_transcript += event.results[i][0].transcript + punctuation;
      }
    }
    box.innerText = prevText + interim_transcript;
    if (final_transcript) {
      prevText += final_transcript;
      box.innerText = prevText;
      punctuation = "";
    }
  }
  punctuation.innerHTML = finalTranscript + '<i style="color:#ddd;">' + interimTranscript + '</i>';
};

//音声入力を開始
function startRec() {
  if (Recflag) return;
  rec.lang = "ja-JP";
  rec.start();

  rec.onstart = () => {
    console.log("音声認識を開始しました。")
    Recflag = true
  };
}

//喋らないとすぐ終了してしまうので、ループさせる。
rec.onend = () => {
  console.log("音声認識を終了しました。");
  Recflag = false;
  startRec();
};

//クリックしたら開始するように設定
box.addEventListener("click", startRec);

//おまけ、キーボードで句読点を入力できるようにした(しゃべっている間は無効)
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