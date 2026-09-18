from PIL import Image
import matplotlib.pyplot as plt

# Get image from file
original = Image.open("sample.jpg")
image = original.copy()

while True:

    print("\n===== IMAGE TRANSFORMATION TOOLBOX =====")
    print("1. Rotate")
    print("2. Resize")
    print("3. Flip")
    print("4. Shear")
    print("5. Custom Matrix")
    print("6. Reset")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # ---------------- ROTATE ----------------
    if choice == "1":

        angle = float(input("Enter angle: "))

        image = image.rotate(angle, expand=True)

        print("Rotation applied.")

    # ---------------- RESIZE ----------------
    elif choice == "2":

        factor = float(input("Enter resize factor (example: 2 or 0.5): "))

        new_width = int(image.width * factor)
        new_height = int(image.height * factor)

        image = image.resize((new_width, new_height))

        print("Resize applied.")

    # ---------------- FLIP ----------------
    elif choice == "3":

        print("1. Left-Right")
        print("2. Top-Bottom")

        flip_choice = input("Choose flip type: ")

        if flip_choice == "1":

            image = image.transpose(
                Image.Transpose.FLIP_LEFT_RIGHT
            )

        elif flip_choice == "2":

            image = image.transpose(
                Image.Transpose.FLIP_TOP_BOTTOM
            )

        else:
            print("Invalid choice.")
            continue

        print("Flip applied.")

    # ---------------- SHEAR ----------------
    elif choice == "4":

        shear = float(input("Enter shear value: "))

        w, h = image.size

        image = image.transform(
            (w + int(abs(shear) * h), h),
            Image.Transform.AFFINE,
            (1, shear, 0, 0, 1, 0)
        )

        print("Shear applied.")

    # ---------------- CUSTOM MATRIX ----------------
    elif choice == "5":

        print("\nEnter the 2 × 2 matrix:")

        a = float(input("a11 = "))
        b = float(input("a12 = "))
        c = float(input("a21 = "))
        d = float(input("a22 = "))

        print("\nYour matrix is:")
        print("[", a, b, "]")
        print("[", c, d, "]")

        print("\nMatrix entered successfully.")

        # Simple examples
        if a == 1 and b == 0 and c == 0 and d == 1:
            print("This is the Identity Matrix.")

        elif a == -1 and b == 0 and c == 0 and d == 1:
            image = image.transpose(
                Image.Transpose.FLIP_LEFT_RIGHT
            )
            print("Reflection applied.")

        elif a == 0 and b == -1 and c == 1 and d == 0:
            image = image.rotate(90, expand=True)
            print("90 degree rotation applied.")

        elif a == 2 and b == 0 and c == 0 and d == 0.5:
            image = image.resize(
                (image.width * 2, image.height // 2)
            )
            print("Scaling applied.")

        else:
            print("Custom matrix recorded.")
            print("This matrix can be analyzed using linear algebra.")

    # ---------------- RESET ----------------
    elif choice == "6":

        image = original.copy()

        print("Image reset.")

    # ---------------- EXIT ----------------
    elif choice == "7":

        print("Toolbox closed.")
        break

    else:

        print("Invalid choice.")

        continue

    # Display current image
    plt.figure(figsize=(7, 5))
    plt.imshow(image)
    plt.title("Current Image")
    plt.axis("off")
    plt.show()