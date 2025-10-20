# programmatic_mode_lab

## Motivation
To interact with GLADOS without having to access your browser, we are introducing our new **Programatic mode**. Within this mode, the user can declare their experiment by implementing a class which contains all of their code and configurations to be run by the system.

## Objective
At the end of this lab, you will be able to utilize the given experiment template to run your experiment locally and on GLADOS, our Automating Science Pipeline

## Setup

#### 1. To activate the virtual environment, my_evn, run the following command:

```python 
python3 -m venv my_env
source venv/bin/activate
```

#### [⭐] For windows users, run the following command instead:

```python 
python -m venv my_env
.\my_env\Scripts\activate 
```

#### 2. To download all necessary requirements to run this lab, run the following command:

```python 
pip install -r requirements.txt
```

## Tutorial
To learn how to start your own experiment, we will implement the function: `y = mx + b`.

### 1. Copy from the template
You are provided with the template file `exp_template.py`. Make a new file called `my_slope_exp.py` in the root directory. Copy the contents of `exp_template.py` into `my_slope_exp.py`.

### 2. Declare Hyperparameters
Hyperparameters are defined using a dictionary of `string` to `tuple`, where the *tuple* defines the start, stop, and step of the variable. For our implementation of `y = mx + b`, we will declare our hyperparameter as:

```python
hyperparams = {
        #variable : (start, stop, step_size)
            "x" : (0, 50, 1),
            "b" : (2, 2, 0),
            "m" : (0.5, 0.5, 0)
        }
```

The snippet above declares the variables `x`, `b`, and `m` with the ranges:

- `0 <= x <= 50` with increments of `1`
- `2 <= b <= 2` with increments of `0`
- `0.5 <= m <= 0.5` with increments of `0`

### 2.5 Declare csv name (Optional)
Say you want to save the output csv of the result under a different name other than "output.csv". You can do it by declaring the new filename in the call to the super class like so:

```python
super().__init__(
                hyperparams,
                csv_name="My_new_name.csv")
```

### 3. Implement `process_trial()`

The `process_trial()` method takes in `data`, which is a dictionary and outputs a dictionary of results. To implement `y = mx + b`, we can simply do:

```python

    def process_trial(self, data):
        y = (data["m"] * data["x"]) + data["b"]

        return {"y" : y}
```

The snippet above define the variable  `y` to be equals to `(m * x) + b`, and returns y as a result entry. You can collect more results if needed for your experiment as long as `process_trial()` returns a dictionary of String to Any.

> [🤔] Keep in mind that your inputs are collected automatically, you do not have to include `m`, `x`, or `b` in your function returns. You will have access to both inputs and outputs later for graphing

### 4. Implement `graph_result()`

The `graph_result()` function is given for you to implement graph with the data collected from the experiment. For this lab, you can use `matplotlib` to graph the results with x axis = "x" and y axis = "y = mx + b". This function will open a `matplotlib` window displaying the graph of the results.

#### [⭐] Keep in mind that the shape of `data` now looks something like this:

```python
data = {
    'x' = [0, 1, 2, ..., 50],
    'm' = [0.5, 0.5, 0.5, ...],
    'b' = [2, 2, 2, ...],
    'y' = [2, 2.5, 3, 3.5, ...]
}
```

#### 1. Include the `matplotlib` library at the top of your file.

```python
import matplotlib.pyplot as plt
```

#### 2. Set up the graph with matplotlib.

```python
    plt.plot(
            data["x"],
            data["y"], 
            marker='o', 
            linestyle='--', 
            color='blue'
            )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("test_graph")
    plt.grid(True) # Add a grid
        
    plt.show()
```

### 5. Run your experiment
```python
    python3 my_slope_exp.py
```

#### [⭐] For windows users, run the following command instead:

```python
    python my_slope_exp.py
```