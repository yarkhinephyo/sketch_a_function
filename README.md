Sketch A Function
========
![GitHub](https://img.shields.io/github/license/yarkhinephyo/sketch_a_function?style=flat-square)

Graphical Functions made from an effortless sketch

Medium: https://towardsdatascience.com/graphical-functions-made-from-an-effortless-sketch-266ccf95c46d

#### Usage
1. Choose functions for consideration
2. Draw the sketch of a function in mind
3. Click "Best Fit" button
4. The function with lowest MSE will be shown

#### User Interface
![Alt desc](https://raw.githubusercontent.com/yarkhinephyo/sketch_a_function/master/app/static/img/sample.jpg)

#### Installation
```
docker build -t sketch:1.0 .
docker run --rm -p 5000:5000 sketch:1.0

# The application will be accessible at localhost:5000
# Custom Models can be added in the "models" package by subclassing BaseModel
```

#### Resources Used
- https://github.com/Leimi/drawingboard.js/
