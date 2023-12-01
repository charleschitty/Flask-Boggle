"use strict";

const $playedWords = $("#words");
const $form = $("#newWordForm");
const $wordInput = $("#wordInput");
const $message = $(".msg");
const $table = $("table");

let gameId;


/** Start */

async function start() {
  const response = await fetch(`/api/new-game`, {
    method: "POST",
  });
  const gameData = await response.json();

  gameId = gameData.gameId;
  let board = gameData.board;

  displayBoard(board);
}

/** Display board */

function displayBoard(board) {
  // $table.empty();
  // loop over board and create the DOM tr/td structure
}


// async function scoreWord() {
//   const response = await fetch(`/api/score-word`, {
//     method: "POST",
//     body: JSON.stringify({ /** your data goes here */ }),
//     headers: {
//       "content-type": "application/json",
//     }
//   });

//   const { result } = await response.json();
// }

start();