function wysylkaJSON(){

let name = document.getElementSelector('name');

let xhr = new XMLHttpRequest();
let url = "database.py";
xhr.open('GET', url, true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.onreadystatechange = function(){
    if (xhr.readyState === 4 && xhr.status ===200){
        result.innerHTML = JSON.stringify(result);
    }
};
var data =JSON.stringify({"name":name.value});
}