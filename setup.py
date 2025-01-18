#
# ==============================================================================
# Author: Michael Gene Brockus (Dreamer)
# Email: michaelbrockus@gmail.com
# Organization: Fossil Logic
# Description:
#     This file is part of the Fossil Logic project, where innovation meets
#     excellence in software development. Michael Gene Brockus, also known as
#     "Dreamer," is a dedicated contributor to this project. For any inquiries,
#     feel free to contact Michael at michaelbrockus@gmail.com.
# ==============================================================================
#
from setuptools import setup, find_packages

setup(
    name="meson-ui",
    version="0.1.0",
    author="Michael Gene Brockus (Dreamer)",
    author_email="michaelbrockus@gmail.com",
    description="Meson build GUI by Fossil Logic",
    long_description="The Meson Build GUI stands as a comprehensive graphical user interface (GUI) tool designed to streamline and enhance the process of building Meson projects. Developed using the Tkinter library in Python, this tool provides an intuitive and user-friendly interface, minimizing the complexities associated with setting up, compiling, testing, and installing Meson projects.",
    url="https://github.com/fossil-logic/meson-ui",
    packages=find_packages(),  # Automatically find and include all packages
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apchie 2.0 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    python_requires=">=3.7",  # Specify the minimum Python version required
)
