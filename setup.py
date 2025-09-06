from setuptools import setup, find_packages

setup(
    name="python-calculator-app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask==2.3.3",
    ],
    extras_require={
        "dev": [
            "pytest==7.4.3",
            "pytest-cov==4.1.0",
            "bandit==1.7.5",
        ]
    }
)
