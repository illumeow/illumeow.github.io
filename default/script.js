function multiplyByTen() {
    var inputField = document.getElementById("number-input");
    var selectedValue = parseInt(inputField.value);
    var result = selectedValue * 10;
    document.getElementById("result").value = result;
}