// ==============================
// PAGE ELEMENTS
// ==============================

const signupPage =
    document.getElementById("signupPage");

const loginPage =
    document.getElementById("loginPage");

const dashboardPage =
    document.getElementById("dashboardPage");


// ==============================
// SIGN UP ELEMENTS
// ==============================

const signupButton =
    document.getElementById("signupButton");

const goToLogin =
    document.getElementById("goToLogin");


// ==============================
// LOGIN ELEMENTS
// ==============================

const signinButton =
    document.getElementById("signinButton");

const goToSignup =
    document.getElementById("goToSignup");


// ==============================
// SIGN UP → LOGIN
// ==============================

signupButton.addEventListener("click", () => {

    const name =
        document
        .getElementById("signupName")
        .value
        .trim();

    const email =
        document
        .getElementById("signupEmail")
        .value
        .trim();

    const password =
        document
        .getElementById("signupPassword")
        .value
        .trim();


    if (
        name === "" ||
        email === "" ||
        password === ""
    ) {

        alert(
            "Please fill in all fields"
        );

        return;

    }


    // Demo flow
    // Backend authentication later

    signupPage.classList.add("hidden");

    loginPage.classList.remove("hidden");

});


// ==============================
// GO TO LOGIN
// ==============================

goToLogin.addEventListener("click", () => {

    signupPage.classList.add("hidden");

    loginPage.classList.remove("hidden");

});


// ==============================
// GO TO SIGNUP
// ==============================

goToSignup.addEventListener("click", () => {

    loginPage.classList.add("hidden");

    signupPage.classList.remove("hidden");

});


// ==============================
// SIGN IN → DASHBOARD
// ==============================

signinButton.addEventListener("click", () => {

    const email =
        document
        .getElementById("loginEmail")
        .value
        .trim();

    const password =
        document
        .getElementById("loginPassword")
        .value
        .trim();


    if (
        email === "" ||
        password === ""
    ) {

        alert(
            "Please enter email and password"
        );

        return;

    }


    loginPage.classList.add("hidden");

    dashboardPage.classList.remove("hidden");

});


// ==============================
// LOGOUT
// ==============================

const logoutButton =
    document.getElementById("logoutButton");


logoutButton.addEventListener("click", () => {

    dashboardPage.classList.add("hidden");

    loginPage.classList.remove("hidden");

});


// ==============================
// NAVIGATION
// ==============================

const homeButton =
    document.getElementById("homeButton");

const monitorButton =
    document.getElementById("monitorButton");

const aboutButton =
    document.getElementById("aboutButton");


homeButton.addEventListener("click", () => {

    document
        .getElementById("homeSection")
        .scrollIntoView({
            behavior: "smooth"
        });

});


monitorButton.addEventListener("click", () => {

    document
        .getElementById("monitorSection")
        .scrollIntoView({
            behavior: "smooth"
        });

});


aboutButton.addEventListener("click", () => {

    document
        .getElementById("aboutSection")
        .scrollIntoView({
            behavior: "smooth"
        });

});


// ==============================
// WEBSITE CHECK
// ==============================

const checkButton =
    document.getElementById("checkButton");

const websiteUrl =
    document.getElementById("websiteUrl");


checkButton.addEventListener("click", () => {

    const url =
        websiteUrl.value.trim();


    if (url === "") {

        alert(
            "Please enter a website URL"
        );

        return;

    }


    document
        .getElementById("status")
        .textContent =
        "Checking...";


    document
        .getElementById("responseTime")
        .textContent =
        "...";


    document
        .getElementById("statusCode")
        .textContent =
        "...";


    /*
    Actual backend API connection
    will be added here.
    */

});