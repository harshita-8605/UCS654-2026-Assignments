from setuptools import setup

setup(
    name="Topsis-Harshita-102317003",
    version="0.0.1",
    author="Harshita",
    description="TOPSIS implementation in Python",
    packages=["topsis_harshita_102317003"],
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis-harshita-102317003=topsis_harshita_102317003.topsis:main"
        ]
    }
)
