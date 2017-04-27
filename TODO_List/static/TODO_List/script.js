function nag(nagThreshold) {
    var todos = document.getElementsByTagName('li');
    
    if (todos.length >= nagThreshold) {
        var div = document.createElement('div');
        var p = document.createElement('p');
        p.textContent = "Looks like you have a lot to do! Get cracking!";
        p.setAttribute("class", "nag");
        
        div.appendChild(p);
        document.body.appendChild(div);
    }
}

window.onload = function() {
    nag(3);
}