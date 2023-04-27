function incrementValue() {
    var inputField = document.getElementById("myInput");
    var value = parseInt(inputField.value);
    inputField.value = isNaN(value) ? 1 : value + 1;
    multiplyByTen();
}

function decrementValue() {
    var inputField = document.getElementById("myInput");
    var value = parseInt(inputField.value);
    inputField.value = isNaN(value) ? 1 : value - 1;
    multiplyByTen();
}

function multiplyByTen() {
    var inputField = document.getElementById("myInput");
    var selectedValue = parseInt(inputField.value);
    var result = selectedValue * 10;
    document.getElementById("result").value = result;
}