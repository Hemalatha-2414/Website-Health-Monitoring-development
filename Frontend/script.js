const homeButton =
    document.getElementById("homeButton");

const monitorButton =
    document.getElementById("monitorButton");

const aboutButton =
    document.getElementById("aboutButton");

const loginButton =
    document.getElementById("loginButton");

const loginModal =
    document.getElementById("loginModal");

const closeLogin =
    document.getElementById("closeLogin");


const checkButton =
    document.getElementById("checkButton");

const websiteUrl =
    document.getElementById("websiteUrl");


const status =
    document.getElementById("status");

const responseTime =
    document.getElementById("responseTime");

const statusCode =
    document.getElementById("statusCode");


/* HOME */

homeButton.addEventListener(
    "click",
    () => {

        document
            .getElementById("home")
            .scrollIntoView({
                behavior: "smooth"
            });

    }
);


/* MONITOR */

monitorButton.addEventListener(
    "click",
    () => {

        document
            .getElementById("monitor")
            .scrollIntoView({
                behavior: "smooth"
            });

    }
);


/* ABOUT */

aboutButton.addEventListener(
    "click",
    () => {

        document
            .getElementById("about")
            .scrollIntoView({
                behavior: "smooth"
            });

    }
);


/* LOGIN */

loginButton.addEventListener(
    "click",
    () => {

        loginModal.classList.remove(
            "hidden"
        );

    }
);


/* CLOSE LOGIN */

closeLogin.addEventListener(
    "click",
    () => {

        loginModal.classList.add(
            "hidden"
        );

    }
);


/* WEBSITE CHECK */

checkButton.addEventListener(
    "click",
    () => {

        const url =
            websiteUrl.value.trim();


        if (url === "") {

            alert(
                "Please enter a website URL"
            );

            return;

        }


        status.textContent =
            "Checking...";

        responseTime.textContent =
            "Checking...";

        statusCode.textContent =
            "Checking...";


        checkButton.innerHTML =
            "⏳ Checking...";

        checkButton.disabled = true;


        /*
        Janani's backend API
        will be connected here
        later.
        */


        setTimeout(() => {

            checkButton.innerHTML =
                "🚀 Check Website";

            checkButton.disabled = false;

        }, 1000);

    }
);