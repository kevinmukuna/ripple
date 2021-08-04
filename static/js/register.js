// create form variable using query selectors

const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid_feedback");
const emailField = document.querySelector("#emailField");
const emailFeedBackArea = document.querySelector(".emailFeedBackArea");
const passwordField = document.querySelector("#passwordField");
const passwordFeedBackArea = document.querySelector(".passwordFeedBackArea")
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const submitBtn = document.querySelector(".submit-btn");

const handleToggleInput = (e) => {
    if (showPasswordToggle.textContent === "SHOW PASSWORD") {
        showPasswordToggle.textContent = "HIDE PASSWORD";
        passwordField.setAttribute("type", "text");
    } else {
        showPasswordToggle.textContent = "SHOW PASSWORD";
        passwordField.setAttribute("type", "password");
    }
};

showPasswordToggle.addEventListener("click", handleToggleInput);

// event listeners --> in this case when a user start typing
emailField.addEventListener("keyup", (e) => {
    // above ^ type of event is keyup and what we listening to is event
    // below we are storing the event into a variable
    const emailVal = e.target.value;

    //
    emailField.classList.remove("is-invalid");
    emailFeedBackArea.style.display = "none";

    // we only want to start listening if the value in the field is greater then 0
    if (emailVal.length > 0) {
        // the fetch method returns a promise ans then you to use the .then method, whhich then return a response and
        // from that response is when we are going to get data
        fetch("/validate-email", {
            // the body contain the key, and value, which we are using to validate and store if it exits or not
            // stringfying ensures that the js object is properly returned for json to be sent over a network
            body: JSON.stringify({ email: emailVal }),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                // these few lines are used to avoid sql injection when invalid characters are passed into the fields
                if (data.email_error) {
                    submitBtn.disabled = true;
                    emailField.classList.add("is-invalid");
                    emailFeedBackArea.style.display = "block";
                    emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
                } else {
                    submitBtn.removeAttribute("disabled");
                }
            });
    }
});

// event listeners --> in this case when a user start typing
usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;

    usernameField.classList.remove("is-invalid");
    feedBackArea.style.display = "none";

    if (usernameVal.length > 0) {
        fetch("/validate-username", {
            body: JSON.stringify({ username: usernameVal }),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                if (data.username_error) {
                    usernameField.classList.add("is-invalid");
                    feedBackArea.style.display = "block";
                    feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
                    submitBtn.disabled = true;
                } else {
                    submitBtn.removeAttribute("disabled");
                }
            });
    }
});


// event listeners --> in this case when a user start typing
passwordField.addEventListener("keyup", (e) => {
    const passwordVal = e.target.value;

    passwordField.classList.remove("is-invalid");
    passwordFeedBackArea.style.display = "none";

    if (passwordVal.length < 8) {
        passwordField.classList.add("is-invalid");
        passwordFeedBackArea.style.display = "block";
        passwordFeedBackArea.innerHTML = `<p>Password must be at least 8 character long.</p>`;      
    }
});
