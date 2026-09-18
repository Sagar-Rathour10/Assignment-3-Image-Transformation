# Assignment 3 – Image Transformation

## Introduction

This project is part of Assignment 3.

The aim of this project is to understand **2-D linear transformations** and apply them to an actual image using Python.

The project contains two questions:

* **Q10:** Apply different transformation matrices to an image.
* **Q11:** Create a simple Image Transformation Toolbox.

---

# Q10 – Image Transformation

In Q10, the following matrices are applied:

### A1 – Scaling

$$
A_1 =
\begin{bmatrix}
2 & 0\\
0 & 0.5
\end{bmatrix}
$$

The image becomes wider and shorter.

### A2 – 90° Rotation

$$
A_2 =
\begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}
$$

The image is rotated by 90 degrees.

### A3 – Horizontal Shear

$$
A_3 =
\begin{bmatrix}
1 & 1\\
0 & 1
\end{bmatrix}
$$

The image becomes slanted horizontally.

### A4 – Reflection in y-axis

$$
A_4 =
\begin{bmatrix}
-1 & 0\\
0 & 1
\end{bmatrix}
$$

The image is reflected from left to right.

### A5 – Projection onto x-axis

$$
A_5 =
\begin{bmatrix}
1 & 0\\
0 & 0
\end{bmatrix}
$$

The y-direction is removed, so information is lost.

For displaying A5, a very small nonzero y-scale is used only for visualization. The actual matrix remains:

$$
\begin{bmatrix}
1 & 0\\
0 & 0
\end{bmatrix}
$$

---

# Q11 – Image Transformation Toolbox

A simple interactive toolbox was created using Python.

The toolbox provides the following options:

1. Rotate
2. Resize
3. Flip
4. Shear
5. Custom Matrix
6. Reset
7. Exit

The user can select an operation from the menu and enter the required value.

---

# Technologies Used

* Python
* NumPy
* Matplotlib
* Pillow

---

# Files in This Repository

```text
Assignment-3/
│
├── Q10.py
├── Q11.py
├── sample.jpg
└── README.md
```

### Q10.py

Contains the code for applying the given transformation matrices and finding:

* T(e1)
* T(e2)
* Rank
* Information loss
* Image transformations

### Q11.py

Contains the interactive Image Transformation Toolbox.

### sample.jpg

The sample image used for testing the programs.

### README.md

This file explains the project.

---

# How to Run

## Step 1

Install the required libraries:

```bash
pip install numpy matplotlib pillow
```

## Step 2

Keep `sample.jpg` in the same folder as the Python files.

## Step 3

Run:

```bash
python Q10.py
```

or

```bash
python Q11.py
```

---

# Example Toolbox Menu

```text
===== IMAGE TRANSFORMATION TOOLBOX =====

1. Rotate
2. Resize
3. Flip
4. Shear
5. Custom Matrix
6. Reset
7. Exit
```

---

# Learning Outcome

Through this project, I learned how matrices can be used to transform images.

I also understood the relationship between:

* Basis vectors
* Transformation matrices
* Rank
* Scaling
* Rotation
* Shearing
* Reflection
* Projection
* Loss of information

---


