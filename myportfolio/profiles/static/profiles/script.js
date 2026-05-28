console.log("JS Connected");

const form = document.getElementById("userForm");

console.log(form);

const errorMsg = document.getElementById("errorMsg");

form.addEventListener("submit", function (event) {

    console.log("Submit Event Running");

    const name =
        document.getElementById("InputName").value.trim();

    const email =
        document.getElementById("InputEmail1").value.trim();

    const city =
        document.getElementById("InputCity").value.trim();

    errorMsg.innerHTML = "";

    const nameRegex = /^[a-zA-Z\s]+$/;

    const cityRegex = /^[a-zA-Z\s]+$/;

    const emailRegex =
        /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;


    // NAME VALIDATION
    if (!nameRegex.test(name)) {

        event.preventDefault();

        errorMsg.innerHTML =
            "Invalid Name";

        return;
    }


    // EMAIL VALIDATION
    if (!emailRegex.test(email)) {

        event.preventDefault();

        errorMsg.innerHTML =
            "Invalid Email";

        return;
    }


    // CITY VALIDATION
    if (!cityRegex.test(city)) {

        event.preventDefault();

        errorMsg.innerHTML =
            "Invalid City";

        return;
    }

});