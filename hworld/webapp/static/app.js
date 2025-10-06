// hworld/webapp/static/app.js
// last updated: 10-5-25
// credit: Claude Sonnet 4.5

let currentUsername = null;

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const testBtn = document.getElementById('testBtn');
    const logoutBtn = document.getElementById('logoutBtn');

    loginForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        try {
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password })
            });

            const data = await response.json();

            if (data.success) {
                currentUsername = data.username;
                showStatus('Login successful!', 'success');
                showMainSection();
            } else {
                showStatus('Login failed: ' +
                    (data.error || 'Invalid credentials'), 'error');
            }
        } catch (error) {
            showStatus('Error: ' + error.message, 'error');
        }
    });

    testBtn.addEventListener('click', async function() {
        try {
            const response = await fetch('/api/test', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            const data = await response.json();

            if (data.success) {
                addOutput('Server ping successful! Pong received.');
            } else {
                addOutput('Server ping failed: ' + data.error);
            }
        } catch (error) {
            addOutput('Error: ' + error.message);
        }
    });

    logoutBtn.addEventListener('click', function() {
        currentUsername = null;
        showLoginSection();
        showStatus('Logged out', 'success');
    });
});

function showMainSection() {
    document.getElementById('loginSection').style.display = 'none';
    document.getElementById('mainSection').style.display = 'block';
    document.getElementById('currentUser').textContent = currentUsername;
    document.getElementById('output').innerHTML = '';
}

function showLoginSection() {
    document.getElementById('loginSection').style.display = 'block';
    document.getElementById('mainSection').style.display = 'none';
    document.getElementById('loginForm').reset();
}

function showStatus(message, type) {
    const status = document.getElementById('status');
    status.textContent = message;
    status.className = type;
    setTimeout(() => {
        status.textContent = '';
        status.className = '';
    }, 3000);
}

function addOutput(message) {
    const output = document.getElementById('output');
    const timestamp = new Date().toLocaleTimeString();
    output.innerHTML +=
        `[${timestamp}] ${message}<br>`;
}
