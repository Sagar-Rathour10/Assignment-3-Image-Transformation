from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Read image from file
img = Image.open("sample.jpg")

# Transformation matrices
A1 = np.array([[2, 0],
               [0, 0.5]])

A2 = np.array([[0, -1],
               [1, 0]])

A3 = np.array([[1, 1],
               [0, 1]])

A4 = np.array([[-1, 0],
               [0, 1]])

A5 = np.array([[1, 0],
               [0, 0]])

# Basis vectors
e1 = np.array([1, 0])
e2 = np.array([0, 1])

matrices = [A1, A2, A3, A4, A5]

# Print required information
for i, A in enumerate(matrices, 1):

    print("A" + str(i))
    print("T(e1) =", A @ e1)
    print("T(e2) =", A @ e2)
    print("Rank =", np.linalg.matrix_rank(A))

    if np.linalg.matrix_rank(A) < 2:
        print("Information lost: YES")
    else:
        print("Information lost: NO")

    print()



# A1 - Scaling
image1 = img.resize(
    (img.width * 2, img.height // 2)
)

# A2 - Rotation
image2 = img.rotate(90, expand=True)

# A3 - Shear
w, h = img.size

image3 = img.transform(
    (w + h // 2, h),
    Image.Transform.AFFINE,
    (1, -0.5, 0, 0, 1, 0)
)

# A4 - Reflection
image4 = img.transpose(
    Image.Transpose.FLIP_LEFT_RIGHT
)

# A5 - Projection
# True matrix = [[1,0],[0,0]]
# Small height only for visualization
image5 = img.resize(
    (img.width, max(2, img.height // 50))
)


images = [image1, image2, image3, image4, image5]

titles = [
    "A1 - Scaling",
    "A2 - Rotation",
    "A3 - Horizontal Shear",
    "A4 - Reflection",
    "A5 - Projection"
]

for image, title in zip(images, titles):

    plt.figure(figsize=(6, 4))
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()