# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to generate Fibonacci sequence
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Function to create a Fibonacci spiral with varying angles
def create_dynamic_fibonacci_spiral(n):
    fib_sequence = generate_fibonacci(n)
    
    # Calculate angles with varying steps
    angles = np.deg2rad(np.cumsum(np.linspace(0, 180, n + 1)[:-1] % 360))
    
    # Calculate coordinates for each point in the spiral
    x = np.cumsum(np.cos(angles) * fib_sequence)
    y = np.cumsum(np.sin(angles) * fib_sequence)
    
    return x, y

# Function to create dynamic Fibonacci rectangles
def create_dynamic_rectangles(n):
    fib_sequence = generate_fibonacci(n)
    rectangles = []

    for i in range(1, n):
        width = fib_sequence[i - 1]
        height = fib_sequence[i]
        rectangles.append((width, height))

    return rectangles

# Function to simulate Fibonacci in Flora
def simulate_fibonacci_in_flora(n):
    fib_sequence = generate_fibonacci(n)
    
    # Simulate Fibonacci in Flora by plotting points
    fig, ax = plt.subplots()
    for i, fib in enumerate(fib_sequence):
        ax.scatter(i, fib, c='green', marker='o', s=fib*10)  # Increase marker size based on Fibonacci number
    ax.set_xlabel("Term Index")
    ax.set_ylabel("Fibonacci Number")
    st.pyplot(fig)

# Function for Fibonacci in Digital Design: A Visual Exploration
def fibonacci_in_digital_design(n):
    fib_sequence = generate_fibonacci(n)
    
    # Generate a bar chart with Fibonacci numbers
    fig, ax = plt.subplots()
    ax.bar(range(n), fib_sequence, color='orange')
    ax.set_xlabel("Term Index")
    ax.set_ylabel("Fibonacci Number")
    st.pyplot(fig)

# Streamlit app
def main():
    st.title("Fibonacci Visualizations")

    # Sidebar options
    visualization_option = st.sidebar.selectbox("Select Visualization", ["Dynamic Fibonacci Spiral", "Dynamic Fibonacci Rectangles", "Nature's Numeric Harmony: Fibonacci in Flora", "Fibonacci in Digital Design: A Visual Exploration"])

    if visualization_option == "Dynamic Fibonacci Spiral":
        n_terms_spiral = st.sidebar.slider("Number of Fibonacci Terms", min_value=2, max_value=50, value=10)
        x_spiral, y_spiral = create_dynamic_fibonacci_spiral(n_terms_spiral)

        # Plot the dynamic Fibonacci spiral
        fig, ax = plt.subplots()
        ax.plot(x_spiral, y_spiral, marker='o', linestyle='-', markersize=5, color='green')
        ax.set_aspect('equal', adjustable='datalim')
        st.pyplot(fig)

    elif visualization_option == "Dynamic Fibonacci Rectangles":
        n_terms_rectangles = st.sidebar.slider("Number of Fibonacci Terms", min_value=2, max_value=20, value=5)
        rectangles = create_dynamic_rectangles(n_terms_rectangles)

        # Plot the dynamic Fibonacci rectangles
        fig, ax = plt.subplots()
        for i, (width, height) in enumerate(rectangles):
            ax.add_patch(plt.Rectangle((i, 0), width, height, fill=None, edgecolor='blue'))
        ax.set_aspect('equal', adjustable='datalim')
        ax.set_xlim(0, n_terms_rectangles)  # Set x-axis limit based on the number of rectangles
        ax.set_ylim(0, max(rectangles, key=lambda x: x[1])[1])  # Set y-axis limit based on the maximum height
        st.pyplot(fig)

    elif visualization_option == "Nature's Numeric Harmony: Fibonacci in Flora":
        n_terms_flora = st.sidebar.slider("Number of Fibonacci Terms", min_value=2, max_value=20, value=5)
        simulate_fibonacci_in_flora(n_terms_flora)

    elif visualization_option == "Fibonacci in Digital Design: A Visual Exploration":
        n_terms_design = st.sidebar.slider("Number of Fibonacci Terms", min_value=2, max_value=20, value=5)
        fibonacci_in_digital_design(n_terms_design)

# Run the app
if __name__ == "__main__":
    main()
