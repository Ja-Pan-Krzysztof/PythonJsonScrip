function wysylkaJSON(){

let name = document.getElementSelector('name');

let xhr = new XMLHttpRequest();
<<<<<<< HEAD
let url = "127.0.0.1/database.py";
=======
let url = "http://192.168.0.199:8000/";
//ip serwera
>>>>>>> a108a83d950d44a043ec9b38fd017872f505549b
xhr.open('GET', url, true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.onreadystatechange = function(){
    if (xhr.readyState === 4 && xhr.status ===200){
        result.innerHTML = JSON.stringify(result);
    }
};
var data =JSON.stringify({"name":name.value});
}