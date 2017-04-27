function nag(nagThreshold) {
    var todos = document.getElementsByTagName('li');
    
    if (todos.length > nagThreshold) {
        var div = document.createElement('div');
        var p = document.createElement('p');
        p.textContent = "Looks like you have a lot to do! Get cracking!";
        p.setAttribute("class", "nag");
        
        div.appendChild(p);
        document.getElementsByClassName('nagoptions')[0].prepend(div);
    }
}

function updateText(node) {
    
    var forms = document.getElementsByClassName('nagoptions');
    var p = forms[0].getElementsByTagName('p');
    var slider = forms[0].getElementsByTagName('input');
    p[0].textContent = "Nag if more than " + slider[0].value + " TODOs are present.";
    return slider[0].value;
}

function updateTextAndNag(node) {
    var theNag = document.getElementsByClassName('nag');
    if (theNag.length > 0) {
        theNag[0].remove();
    }
    
    var threshold = updateText(node);
    nag(threshold);
}

window.onload = function() {
    nag(5);
}