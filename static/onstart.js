var myBoard = new DrawingBoard.Board("canvas", {
    background: false,
    color: "#000000",
    size: 1,
    controls: [
        { Navigation: { back: false, forward: false } }
    ],
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
    console.log(myJson);
}
