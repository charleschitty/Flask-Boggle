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
  const board_length = gameId.board_size //5

  $table.empty()

  $tbody = $("<tbody>")

  $table.append($tbody)

  for (let row_index = 0; row_index < board_length; row_index++){
    const $row = $("<tr>")

    for (let cell = 0; cell < board_length; cell++){
      const $cell = $("<td>")

      $table.append($cell)
    }

    $table.append($row)
  }

  board.append($table)



  // $table.empty();
  // loop over board and create the DOM tr/td structure
}


//create handleSubmit function for event handling form submission

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