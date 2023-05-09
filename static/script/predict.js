
const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");
const BOT_IMG = "/static/images/surgeon-with-mask-svgrepo-com.svg";
const PERSON_IMG = "/static/images/kasndasndal.svg";
const BOT_NAME = "    MediBot";
const PERSON_NAME = "You";
appendMessage(BOT_NAME, BOT_IMG, "left", "Hi, welcome to ChatBot! Go ahead and send me a message. 😄")
userName = ""
msgerForm.addEventListener("submit", event => {
  event.preventDefault();

  const msgText = msgerInput.value;
  if (!msgText) return;

  appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
  msgerInput.value = "";
  botResponse(msgText);
});

function appendMessage(name, img, side, text) {
  //   Simple solution for small apps
  const msgHTML = `
<div class="msg ${side}-msg">
<div class="msg-img" style="background-image: url(${img})"></div>

<div class="msg-bubble">
<div class="msg-info">
  <div class="msg-info-name">${name}</div>
  <div class="msg-info-time">${formatDate(new Date())}</div>
</div>

<div class="msg-text">${text}</div>
</div>
</div>
`;

  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
  msgerChat.scrollTop += 500;
}
function nameExtractor(words) {
  word = words.split(" ");
  return word[word.length - 1]
}

function botResponse(rawText) {
  $.get("/get", { msg: rawText }).done(function (data) {
    
    appendMessage(BOT_NAME, BOT_IMG, "left", data);
    appendMessage(BOT_NAME, BOT_IMG, "left", "If your weight is <50kg (women) or <55kg (men) then consider dimidiating the dosage or for kids below age 8 use on quarter dosage");
  });
}

function get(selector, root = document) {
  return root.querySelector(selector);
}

function formatDate(date) {
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();

  return `${h.slice(-2)}:${m.slice(-2)}`;
}


