from setuptools import setup, find_packages

setup(
    name="syzygy",
    version="0.1.0",
    description="A simple macroeconomic simulation environment with DSGE models",
    author="Sudeepto Saha",
    packages=find_packages(),  # Automatically finds syzygy/
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    extras_require={
        "dev": [
            "pytest"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
