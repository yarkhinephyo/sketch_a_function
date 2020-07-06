$(document).ready(function() {

    const $valueSpan = $('.valueSpan');
    const $value = $('#slider');
    $valueSpan.html($value.val());
    $value.on('input change', () => {
        $valueSpan.html($value.val());
    });
});

var myBoard = new DrawingBoard.Board("canvas", {
    background: false,
    color: "#000000",
    size: 1,
    controls: false,
    webStorage: 'local'
});

var slider = document.getElementById("slider");
var equation_string = document.getElementById("equation_string");
var model_name = document.getElementById("model_name");
var mse = document.getElementById("mse");

async function get_best_fit(){
    console.log("Submitting drawing...");
    var img = myBoard.getImg();
    var imgInput = (myBoard.blankCanvas == img) ? '' : img;
    var complexity = slider.value;

    const response = await fetch('/get_best_fit', {
        method: 'POST',
        body: JSON.stringify({
            'imgInput': imgInput,
            'complexity': complexity
        }), 
        headers: {'Content-Type': 'application/json'}
    });

    const myJson = await response.json(); //extract JSON from the http response

    if(!myJson["error"]){
        const display_canvas = document.getElementById("display_canvas");
        display_canvas.src = "data:image/png;base64," + myJson["imgOutput"];
        equation_string.innerHTML = myJson["equation_string"];
        model_name.innerHTML = myJson["model_name"];
        mse.innerHTML = myJson["mse"];
    } else {
        erase_drawing()
    }
}

function erase_drawing(){
    myBoard.reset({ background: true });
}
