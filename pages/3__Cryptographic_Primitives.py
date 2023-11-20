import streamlit as st
from cryptography import fernet
import hashlib
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import matplotlib.pyplot as plt

# Utility functions for cryptographic operations
def generate_hash(message, hash_algorithm):
    """Generate a hash for a given message using the specified algorithm."""
    if hash_algorithm == "SHA256":
        return hashlib.sha256(message.encode()).hexdigest()
    elif hash_algorithm == "MD5":
        return hashlib.md5(message.encode()).hexdigest()
    elif hash_algorithm == "SHA1":
        return hashlib.sha1(message.encode()).hexdigest()

def find_hash_collision(hash_algorithm):
    """Find two different messages that produce the same hash value."""
    st.write("Finding a real hash collision is computationally intensive. This is a conceptual demonstration using known MD5 collisions.")

    if hash_algorithm == "MD5":
        # Using known MD5 collision
        message1 = "d131dd02c5e6eec4693d9a0698aff95c"
        message2 = "d131dd02c5e6eec4693d9a0698aff95d"
        hash1 = hashlib.md5(message1.encode()).hexdigest()
        hash2 = hashlib.md5(message2.encode()).hexdigest()
        st.write(f"Message 1: {message1}, Hash: {hash1}")
        st.write(f"Message 2: {message2}, Hash: {hash2}")
        if hash1 == hash2:
            st.write("Collision found!")
        else:
            st.write("No collision found.")

def visualize_hashing_process(message, hash_algorithm):
    """Visualize the hashing process for a message."""
    st.subheader("Hashing Process Visualization")
    st.write("Observe how the hash changes as the message is altered.")

    # Visualize the change in hash with a slight modification in the message
    hash_original = generate_hash(message, hash_algorithm)
    modified_message = message + "x"  # Adding a character to change the message
    hash_modified = generate_hash(modified_message, hash_algorithm)

    st.write(f"Original Message: {message}")
    st.write(f"Hash: {hash_original}")
    st.write(f"Modified Message: {modified_message}")
    st.write(f"Modified Hash: {hash_modified}")

# Streamlit interactive elements and layout for each topic
def hash_functions_intro():
    st.subheader("Introduction to Hash Functions")
    st.markdown("""
    Hash functions are fundamental cryptographic algorithms that convert input data (of any size) 
    into a fixed-size string of characters, which typically represents the data uniquely. 
    Common uses include data integrity checks and password storage.
    """)

def hash_function_calculator():
    st.subheader("Hash Function Calculator")
    message = st.text_area("Enter your message here")
    hash_algorithm = st.selectbox("Select Hash Algorithm", ["SHA256", "MD5", "SHA1"])
    if st.button("Compute Hash"):
        hash_value = generate_hash(message, hash_algorithm)
        st.write("Hash Value:", hash_value)

def collision_finder_calculator():
    st.subheader("Collision Finder")
    hash_algorithm = st.selectbox("Select Hash Algorithm for Collision Finding", ["MD5", "SHA1"])
    st.write("Note: Finding collisions is computationally intensive and not typically done in real-time.")
    if st.button("Find Collision"):
        find_hash_collision(hash_algorithm)

def hash_function_visualization():
    st.subheader("Hash Function Process Visualization")
    message = st.text_area("Enter your message to visualize hashing", "Hello World")
    hash_algorithm = st.selectbox("Select Hash Algorithm for Visualization", ["SHA256", "MD5", "SHA1"])
    if st.button("Visualize Hash"):
        visualize_hashing_process(message, hash_algorithm)

# Main function to control the Streamlit app layout
def main():
    st.title("Module 3: Cryptographic Primitives")

    topic = st.sidebar.selectbox("Choose a topic", [
        "Hash Functions", 
        "Symmetric Key Cryptography", 
        "Asymmetric Key Cryptography", 
        "Digital Signatures", 
        "Random Number Generation"
    ])

    if topic == "Hash Functions":
        hash_functions_intro()
        hash_function_calculator()
        collision_finder_calculator()
        hash_function_visualization()
    # elif statements for other topics would follow...

if __name__ == "__main__":
    main()
