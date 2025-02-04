let attempts = 5;

function togglePasswordVisibility() {
    const passwordInput = document.getElementById("password");
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}

function checkPassword() {
    const password = document.getElementById("password").value;
    const allowedPasswords = ["Team_FerroFy", "Tanav_FerroFy" , "VPX_FerroFy"];
    if (allowedPasswords.includes(password)) {
        document.getElementById("privateContent").style.display = "block";
        document.getElementById("password").style.display = "none";
        document.querySelector(".eye-button").style.display = "none";
        document.querySelector(".submit-button").style.display = "none";
    } else {
        attempts--;
        const alertBox = document.createElement("div");
        alertBox.style.backgroundColor = "#00c853";
        alertBox.style.color = "black";
        alertBox.style.fontWeight = "bold";
        alertBox.style.position = "fixed";
        alertBox.style.top = "50%";
        alertBox.style.left = "50%";
        alertBox.style.transform = "translate(-50%, -50%)";
        alertBox.style.padding = "20px";
        alertBox.style.zIndex = "1000";
        alertBox.style.cursor = "pointer";
        alertBox.textContent = `Invalid Password User. Attempts Left - ${attempts}`;
        alertBox.onclick = () => alertBox.remove();
        document.body.appendChild(alertBox);
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
