function nag(nagThreshold) {
    var todos = document.getElementsByTagName('li');
    
    if (todos.length > nagThreshold) {
        var div = document.createElement('div');
        var p = document.createElement('p');
        p.textContent = "Looks like you have a lot to do! Get cracking!";
        p.setAttribute("class", "nag");
        
        div.appendChild(p);
        document.body.appendChild(div);
    }
}

function updateButton(node) {
    var forms = document.getElementsByClassName('nagoptions');
    var button = forms[0].getElementsByTagName('button');
    var slider = forms[0].getElementsByTagName('input');
    button[0].textContent = "Nag if more than " + slider[0].value + " TODOs are present.";
}

window.onload = function() {
    nag(5);
}