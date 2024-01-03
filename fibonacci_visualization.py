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

# Function for Interactive Fibonacci Sequence Explorer
def interactive_fibonacci_explorer():
    st.sidebar.markdown("# Interactive Fibonacci Sequence Explorer")

    # Sidebar options
    n_terms_explorer = st.sidebar.slider("Number of Fibonacci Terms", min_value=2, max_value=50, value=10)
    show_values = st.sidebar.checkbox("Show Fibonacci Values", value=True)

    # Generate Fibonacci sequence
    fib_sequence = generate_fibonacci(n_terms_explorer)

    # Plot the interactive Fibonacci sequence explorer
    fig, ax = plt.subplots()
    ax.plot(fib_sequence, marker='o', linestyle='-', markersize=5, color='purple')
    
    if show_values:
        for i, fib_value in enumerate(fib_sequence):
            ax.text(i, fib_value, str(fib_value), ha='center', va='bottom', fontsize=8, color='black')

    ax.set_xlabel("Term Index")
    ax.set_ylabel("Fibonacci Number")
    st.pyplot(fig)

# Function for Golden Ratio Unveiled: Fibonacci Patterns in Art
def fibonacci_patterns_in_art(n):
    fib_sequence = generate_fibonacci(n)
    
    # Generate a plot to unveil Fibonacci patterns related to the Golden Ratio
    fig, ax = plt.subplots()
    ax.plot(fib_sequence[:-1], fib_sequence[1:], marker='o', linestyle='-', markersize=5, color='gold')
    ax.set_xlabel("Fibonacci Number (n)")
    ax.set_ylabel("Fibonacci Number (n+1)")
    st.pyplot(fig)

# Function for Mathematical Beauty: Visualizing Infinite Fibonacci
def visualize_infinite_fibonacci(n):
    # Generate an infinite Fibonacci sequence
    fib_sequence = generate_fibonacci(n)

    # Plot the infinite Fibonacci sequence
    fig, ax = plt.subplots()
    ax.plot(fib_sequence, marker='o', linestyle='-', markersize=5, color='blue')
    ax.set_xlabel("Term Index")
    ax.set_ylabel("Fibonacci Number")
    st.pyplot(fig)

# Function for Architectural Symmetry: Fibonacci in Building Design
def fibonacci_in_building_design(n, a, b):
    # Generate a hyperbolic curve based on Fibonacci numbers
    fib_sequence = generate_fibonacci(n)

    # Create a hyperbolic curve using Fibonacci numbers
    x = np.linspace(-np.pi, np.pi, n)
    y = a * np.sinh(b * x)

    # Plot the hyperbolic curve
    fig, ax = plt.subplots()
    ax.plot(x, y, color='red')
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    st.pyplot(fig)

# Function for Data Visualization: Fibonacci Trends Over Time
def fibonacci_trends_over_time(n):
    # Generate Fibonacci numbers over time
    fib_sequence = generate_fibonacci(n)

    # Plot Fibonacci trends over time
    fig, ax = plt.subplots()
    ax.plot(range(1, n+1), fib_sequence, marker='o', linestyle='-', markersize=5, color='purple')
    ax.set_xlabel("Time")
    ax.set_ylabel("Fibonacci Number")
    st.pyplot(fig)

# Function for Fibonacci and Fractals: Exploring Infinite Complexity
def fibonacci_and_fractals(n, iterations):
    # Generate Fibonacci numbers
    fib_sequence = generate_fibonacci(n)

    # Create a fractal using Fibonacci numbers
    fig, ax = plt.subplots()
    x = np.linspace(-2, 2, 800)
    y = np.linspace(-2, 2, 800)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X + fib_sequence[-1]) + np.cos(Y + fib_sequence[-2])
    fractal = ax.contourf(X, Y, Z, cmap='viridis', levels=iterations)
    fig.colorbar(fractal, ax=ax)
    ax.set_title("Fibonacci and Fractals")
    st.pyplot(fig)

# Streamlit app
def main():
    st.title("Fibonacci Visualizations")

    # Sidebar options
    visualization_option = st.sidebar.selectbox(
        "Select Visualization",
        ["Dynamic Fibonacci Spiral", "Dynamic Fibonacci Rectangles", "Nature's Numeric Harmony: Fibonacci in Flora", "Fibonacci in Digital Design: A Visual Exploration", "Interactive Fibonacci Sequence Explorer", "Golden Ratio Unveiled: Fibonacci Patterns in Art", "Mathematical Beauty: Visualizing Infinite Fibonacci", "Architectural Symmetry: Fibonacci in Building Design", "Data Visualization: Fibonacci Trends Over Time", "Fibonacci and Fractals: Exploring Infinite Complexity"]
    )

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

    elif visualization_option == "Interactive Fibonacci Sequence Explorer":
        interactive_fibonacci_explorer()

    elif visualization_option == "Golden Ratio Unveiled: Fibonacci Patterns in Art":
        n_terms_art = st.sidebar.slider("Number of Fibonacci Terms", min_value=2, max_value=20, value=5)
        fibonacci_patterns_in_art(n_terms_art)

    elif visualization_option == "Mathematical Beauty: Visualizing Infinite Fibonacci":
        n_terms_infinite = st.sidebar.slider("Number of Fibonacci Terms", min_value=2, max_value=1000, value=100)
        visualize_infinite_fibonacci(n_terms_infinite)

    elif visualization_option == "Architectural Symmetry: Fibonacci in Building Design":
        n_terms_building = st.sidebar.slider("Number of Fibonacci Terms", min_value=2, max_value=100, value=10)
        a_value = st.sidebar.slider("Value of 'a'", min_value=0.1, max_value=2.0, value=1.0)
        b_value = st.sidebar.slider("Value of 'b'", min_value=0.1, max_value=2.0, value=1.0)
        fibonacci_in_building_design(n_terms_building, a_value, b_value)

    elif visualization_option == "Data Visualization: Fibonacci Trends Over Time":
        n_terms_trends = st.sidebar.slider("Number of Fibonacci Terms", min_value=2, max_value=100, value=10)
        fibonacci_trends_over_time(n_terms_trends)

    elif visualization_option == "Fibonacci and Fractals: Exploring Infinite Complexity":
        n_fractals = st.sidebar.slider("Number of Fibonacci Terms", min_value=2, max_value=100, value=10)
        iterations = st.sidebar.slider("Number of Iterations", min_value=10, max_value=100, value=50)
        fibonacci_and_fractals(n_fractals, iterations)

# Run the app
if __name__ == "__main__":
    main()