function multiplyByTen() {
    var selectElement = document.getElementById("number-input");
    var selectedValue = selectElement.value;
    var result = selectedValue * 10;
    document.getElementById("result").innerHTML = "Result: " + result;
 }  