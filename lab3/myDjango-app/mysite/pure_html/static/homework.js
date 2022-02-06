let nameHTML = document.getElementById("name");
let showBtn = document.getElementById("show-btn");
let clearBtn = document.getElementById("clear-btn");

console.log(data);

let myName = "";

nameHTML.innerHTML = myName.toString();

const updateCountDom = (value) => {
    nameHTML.innerHTML = value;
};

showBtn.addEventListener("click", () => {
    console.log(data);
    for (let d = 0; d < data.length; d++) {
        myName += "<li>" + data[d] + "</li>";
    }
    clearBtn.style.display = "block";
    updateCountDom(myName);
});

clearBtn.addEventListener("click", () => {
    myName = "";
    clearBtn.style.display = "none";
    updateCountDom(myName);
});