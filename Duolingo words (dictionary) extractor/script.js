"use strict";

// you can either press to first button to get the result
// and be able to preview/modify it
// or simply click the download button which will execute
// both getting and downloading the result

const spanish = document.querySelectorAll(".PAtlL div h3"); //spanish word path
const english = document.querySelectorAll(".PAtlL div p"); // english translation path
const getResultButton = document.querySelector(".getResult"); //get result
const downloadResultButton = document.getElementById("getResultFile"); //download result
const resultArea = document.querySelector("#resultArea"); //result from textarea
let result = ""; //result

//format them nicely to a string, separated by |
getResultButton.addEventListener("click", function () {
  for (let i = 0; i < spanish.length; i++) {
    result += `${spanish[i].textContent}|${english[i].textContent}\n`;
  }
  resultArea.value = result;
});

// source for download function: https://www.geeksforgeeks.org/how-to-trigger-a-file-download-when-clicking-an-html-button-or-javascript/
//download function and button
function download(file, text) {
  //creating an invisible element

  var element = document.createElement("a");
  element.setAttribute(
    "href",
    "data:text/plain;charset=utf-8, " + encodeURIComponent(text)
  );
  element.setAttribute("download", file);
  document.body.appendChild(element);
  element.click();

  document.body.removeChild(element);
}

// Start file download.
downloadResultButton.addEventListener(
  "click",
  function () {
    convert();
    var text = document.getElementById("resultArea").value;
    var filename = "words.txt";

    download(filename, text);
  },
  false
);

//alt file dowload button by me
// downloadResultButton.addEventListener(
//   "click",
//   function () {
//     convert();
//     download("words.txt", result);
//   },
//   false
// );
