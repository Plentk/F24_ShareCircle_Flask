let searchCategoryAll = document.getElementById("searchCategoryAll");
searchCategoryAll.addEventListener("click", filterAll);
function filterAll() {
    const itemsAll = document.getElementsByClassName("item");
    for (let i = 0; i < itemsAll.length; i++) {
        itemsAll[i].style.display = "block";
    };
};

let searchCategoryFood = document.getElementById("searchCategoryFood");
searchCategoryFood.addEventListener("click", filterFood);
function filterFood() {
    const itemsAll = document.getElementsByClassName("item");
    for (let i = 0; i < itemsAll.length; i++) {
        if (itemsAll[i].classList.contains("itemFood")) {
            itemsAll[i].style.display = "block";
        } else {
            itemsAll[i].style.display = "none";
        };
        
    };
};

let searchCategoryClothes = document.getElementById("searchCategoryClothes");
searchCategoryClothes.addEventListener("click", filterClothes);
function filterClothes() {
    const itemsAll = document.getElementsByClassName("item");
    for (let i = 0; i < itemsAll.length; i++) {
        if (itemsAll[i].classList.contains("itemClothes")) {
            itemsAll[i].style.display = "block";
        } else {
            itemsAll[i].style.display = "none";
        };
        
    };
};

let searchCategoryHousehold = document.getElementById("searchCategoryHousehold");
searchCategoryHousehold.addEventListener("click", filterHousehold);
function filterHousehold() {
    const itemsAll = document.getElementsByClassName("item");
    for (let i = 0; i < itemsAll.length; i++) {
        if (itemsAll[i].classList.contains("itemHousehold")) {
            itemsAll[i].style.display = "block";
        } else {
            itemsAll[i].style.display = "none";
        };
        
    };
};

let searchCategoryOthers = document.getElementById("searchCategoryOthers");
searchCategoryOthers.addEventListener("click", filterOthers);
function filterOthers() {
    const itemsAll = document.getElementsByClassName("item");
    for (let i = 0; i < itemsAll.length; i++) {
        if (itemsAll[i].classList.contains("itemOthers")) {
            itemsAll[i].style.display = "block";
        } else {
            itemsAll[i].style.display = "none";
        };
        
    };
};