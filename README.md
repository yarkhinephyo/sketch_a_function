## Sketch A Function

Graphical Functions made from an effortless sketch

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
docker run -p 5000:80 sketch:1.0

# The application will be accessible at localhost:5000
# Custom Models can be added in the "models" package by subclassing BaseModel
```

#### Resources Used
- https://github.com/Leimi/drawingboard.js/
