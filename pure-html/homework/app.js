let nameHTML = document.getElementById("name");
let showBtn = document.getElementById("show-btn");
let clearBtn = document.getElementById("clear-btn");

let myName = "";

nameHTML.innerHTML = myName.toString();

const updateCountDom = (value) => {
    nameHTML.innerHTML = value;
};

showBtn.addEventListener("click", () => {
    myName = "Mufaddal Enayath";
    clearBtn.style.display = "block";
    updateCountDom(myName);
});

clearBtn.addEventListener("click", () => {
    myName = "";
    clearBtn.style.display = "none";
    updateCountDom(myName);
});