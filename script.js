function wysylkaJSON(){

let name = document.getElementSelector('name');
let surname = document.getElementSelector('suname');


let xhr = new XMLHttpRequest();
let url = "http://192.168.0.199:8000/";

//ip serwera
xhr.open('GET', url, true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.onreadystatechange = function(){
    if (xhr.readyState === 4 && xhr.status === 200){
        result.innerHTML = JSON.stringify(result);
    }
};
var data = JSON.stringify({
    "name":name.value,
    "surname":surname.value
});
}