let attempts = 8;

const usersWithAccess = [" ' VPX ' " , " ' Tanav ' "];

function togglePasswordVisibility() {
    const passwordInput = document.getElementById("password");
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}

function formatNamesList(names) {
    if (names.length === 1) return names[0];
    return names.slice(0, -1).join(", ") + " & " + names[names.length - 1];
}

function highlightNames(names) {
    return names.map(name => `${name}`).join(", ");
}

function checkPassword() {
    let password = document.getElementById("password").value.toLowerCase();
    const allowedPasswords = ["team_ferrofy", "private_data"];
    if (allowedPasswords.includes(password)) {
        document.getElementById("privateContent").style.display = "block";
        document.getElementById("password").style.display = "none";
        document.querySelector(".eye-button").style.display = "none";
        document.querySelector(".submit-button").style.display = "none";
    } else {
        attempts--;
        const alertBox = document.createElement("div");
        alertBox.style.backgroundColor = "#39FF14"; // Neon green background
        alertBox.style.color = "black"; // Black text color
        alertBox.style.fontWeight = "bold";
        alertBox.style.position = "fixed";
        alertBox.style.top = "50%";
        alertBox.style.left = "50%";
        alertBox.style.transform = "translate(-50%, -50%)";
        alertBox.style.padding = "20px";
        alertBox.style.zIndex = "1000";
        alertBox.style.cursor = "pointer";
        alertBox.style.textAlign = "center"; // Center the text

        let formattedNames = formatNamesList(usersWithAccess);
        let highlightedNames = highlightNames(usersWithAccess);

        let textContent = `Invalid Password\nAttempts Left - ${attempts}\nThen You will Go to Home Page\nOnly ${highlightedNames} Have Access\nThank You For Your Time, User`;
        let i = 0;
        let speed = 50;

        function typeWriter() {
            if (i < textContent.length) {
                if (textContent.charAt(i) === '\n') {
                    alertBox.innerHTML += '<br>';
                } else {
                    alertBox.innerHTML += textContent.charAt(i);
                }
                i++;
                setTimeout(typeWriter, speed);
            } else {
                setTimeout(() => alertBox.remove(), 3000);
            }
        }

        alertBox.onclick = () => alertBox.remove();
        document.body.appendChild(alertBox);

        typeWriter();

        if (attempts <= 0) {
            window.location.href = "https://ferrofy.github.io/Home";
        }
    }
}

document.getElementById("password").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        checkPassword();
    }
});
