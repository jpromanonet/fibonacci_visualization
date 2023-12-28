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

# Function to create a Fibonacci spiral
def create_fibonacci_spiral(n):
    fib_sequence = generate_fibonacci(n)
    
    # Calculate angle for each Fibonacci number
    angles = np.deg2rad(np.arange(0, 360 * len(fib_sequence), 360) % 360)
    
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

# Streamlit app
def main():
    st.title("Fibonacci Visualizations")

    # Sidebar options
    visualization_option = st.sidebar.selectbox("Select Visualization", ["Fibonacci Spiral Artistry", "Dynamic Fibonacci Rectang