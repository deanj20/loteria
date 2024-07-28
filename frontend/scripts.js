const socket = io();

document.getElementById('start-game').addEventListener('click', startGame);
document.getElementById('join-game-btn').addEventListener('click', joinGame);
document.getElementById('call-card').addEventListener('click', callCard);

let gameId;
let playerId;

// Fetch active games on load
window.onload = function() {
    fetch('/active_games')
        .then(response => response.json())
        .then(data => {
            const gameIdSelect = document.getElementById('game-id');
            data.active_games.forEach(id => {
                const option = document.createElement('option');
                option.value = id;
                option.text = id;
                gameIdSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error:', error));
};

function startGame() {
    fetch('/start_game', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            gameId = data.game_id;
            console.log('Game started with ID:', gameId);  // Add logging
            alert(`Game started with ID: ${gameId}`);
            document.getElementById('call-card').style.display = 'block';

            // Add the new game to the dropdown
            const gameIdSelect = document.getElementById('game-id');
            const option = document.createElement('option');
            option.value = gameId;
            option.text = gameId;
            gameIdSelect.appendChild(option);
        })
        .catch(error => console.error('Error:', error));
}

function joinGame() {
    const playerName = document.getElementById('player-name').value;
    gameId = document.getElementById('game-id').value;  // Use selected game ID
    console.log('Joining game with game_id:', gameId);  // Add logging
    fetch('/join_game', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player_name: playerName, game_id: gameId }) // Ensure game_id is included
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            playerId = data.player_id;
            displayCard(data.card);
            socket.emit('join', { player_id: playerId });
        }
    })
    .catch(error => console.error('Error:', error));
}

function callCard() {
    fetch('/call_card', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ game_id: gameId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            console.log('Called card:', data.called_card);
            displayCalledCard(data.called_card);
            markPlayerCard(data.called_card);
        }
    })
    .catch(error => console.error('Error:', error));
}

function displayCard(card) {
    const playerCardDiv = document.getElementById('player-card');
    playerCardDiv.innerHTML = '';
    card.forEach(filename => {
        const img = document.createElement('img');
        img.src = `/static/images/cards/${filename}`;
        img.dataset.filename = filename;  // Store the filename for later reference
        img.addEventListener('click', toggleMarkCard);
        playerCardDiv.appendChild(img);
    });
}

function displayCalledCard(card) {
    const calledCardDiv = document.getElementById('called-card');
    calledCardDiv.innerHTML = '';
    const img = document.createElement('img');
    img.src = `/static/images/cards/${card}`;
    console.log('Displaying called card image:', img.src);
    calledCardDiv.appendChild(img);
}

function toggleMarkCard(event) {
    const img = event.target;
    img.classList.toggle('marked');
}

function markPlayerCard(calledCard) {
    const playerCardDiv = document.getElementById('player-card');
    const imgs = playerCardDiv.querySelectorAll('img');
    imgs.forEach(img => {
        if (img.dataset.filename === calledCard) {
            img.classList.add('marked');
        }
    });
}

// Real-time event handlers
socket.on('player_joined', (data) => {
    console.log('Player joined:', data);
    if (data.player_id === playerId) {
        displayCard(data.card);
    }
});

socket.on('card_called', (data) => {
    console.log('Card called:', data);
    displayCalledCard(data.called_card);
    markPlayerCard(data.called_card);
});

socket.on('player_won', (data) => {
    console.log('Player won:', data);
    alert(`${data.player_name} has won the game!`);
});

