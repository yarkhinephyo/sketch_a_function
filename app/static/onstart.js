$(document).ready(function() {

    const $valueSpan = $('.valueSpan');
    const $value = $('#slider');
    $valueSpan.html($value.val());
    $value.on('input change', () => {
        $valueSpan.html($value.val());
        get_best_fit();
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
var model_checkboxes = document.getElementsByName('model_checkboxes');
var display_canvas = document.getElementById("display_canvas");

async function get_best_fit(){
    console.log("Submitting drawing...");
    var img = myBoard.getImg();
    var imgInput = (myBoard.blankCanvas == img) ? '' : img;
    var complexity = slider.value;

    model_name.innerText = "Loading...";
    const response = await fetch('/get_best_fit', {
        method: 'POST',
        body: JSON.stringify({
            'imgInput': imgInput,
            'complexity': complexity,
            'selected_models': get_selected_models()
        }), 
        headers: {'Content-Type': 'application/json'}
    });
    model_name.innerText = "";

    const myJson = await response.json(); //extract JSON from the http response

    if(myJson["error"] === "None"){
        display_canvas.src = "data:image/png;base64," + myJson["imgOutput"];
        display_canvas.style.display = "block";
        display_equation_string(myJson["equation_string"]);
        model_name.innerHTML = myJson["model_name"];
        mse.innerHTML = "MSE: " + myJson["mse"];
    } else {
        erase_model();
        mse.innerHTML = "Error: " + myJson["error"];
    } 
}

function get_selected_models(){
    let checkbox_array = [...model_checkboxes];
    if(checkbox_array.length === 0){
        erase_drawing();
        erase_model();
        return '';
    }

    let selected_models = checkbox_array.filter(checkbox => 
        checkbox.checked
    ).map(checkbox => 
        checkbox.value
    );

    return selected_models.toString();
}

function erase_model(){
    display_canvas.style.display = "none";
    equation_string.innerHTML = "";
    model_name.innerHTML = "";
    mse.innerHTML = "";
}

function erase_drawing(){
    myBoard.reset({ background: true });
    erase_model();
}

async function display_equation_string(input_string) {
    equation_string.innerHTML = "";

    MathJax.texReset();
    var options = MathJax.getMetricsFor(equation_string);

    // The promise returns the typeset node, then document is updated
    MathJax.tex2chtmlPromise(input_string, options).then(function (node) {
      equation_string.appendChild(node);
      MathJax.startup.document.clear();
      MathJax.startup.document.updateDocument();

    }).catch(function (err) {
      equation_string.appendChild(document.createElement('pre')).appendChild(document.createTextNode(err.message));
    });
  }