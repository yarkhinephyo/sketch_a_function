var myBoard = new DrawingBoard.Board("canvas", {
    background: false,
    color: "#000000",
    size: 1,
    controls: false,
    webStorage: 'local'
});

async function get_best_fit(){
    console.log("Submitting drawing...");
    var img = myBoard.getImg();
    var imgInput = (myBoard.blankCanvas == img) ? '' : img;

    const response = await fetch('/get_best_fit', {
        method: 'POST',
        body: JSON.stringify({'imgInput': imgInput}), 
        headers: {'Content-Type': 'application/json'}
    });

    const myJson = await response.json(); //extract JSON from the http response

    if(!myJson["error"]){
        const display_canvas = document.getElementById("display_canvas");
        display_canvas.src = "data:image/png;base64," + myJson["imgOutput"];
    }
}

function erase_drawing(){
    myBoard.reset({ background: true });
}
