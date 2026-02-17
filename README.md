Objective
------------------------------------------------------------

To implement the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method for ranking alternatives based on multiple criteria.

Methodology
------------------------------------------------------------

The following steps were used to implement TOPSIS:

1. Read the input CSV file.
2. Normalize the decision matrix using square root of sum of squares.
3. Multiply normalized values with given weights.
4. Determine ideal best and ideal worst values based on impacts (+/-).
5. Compute distance from ideal best and ideal worst.
6. Calculate TOPSIS score:
   Score = S- / (S+ + S-)
7. Rank alternatives based on score (higher score = better rank).

Part I: Command Line Program
------------------------------------------------------------

File:
topsis.py

Usage:
python topsis.py <input_file> <weights> <impacts> <output_file>

The output file contains:
- Topsis Score
- Rank

Part II: Python Package
------------------------------------------------------------

The command-line implementation is converted into a Python package
using setup.py. The source distribution (sdist) is generated successfully.
Package files are included in the repository.

Part III: Web Service (FastAPI)
------------------------------------------------------------

A FastAPI-based web service is implemented.

Features:
- Upload CSV file
- Provide weights and impacts
- Compute TOPSIS score

Endpoint:
POST /topsis

The result CSV file is returned directly.

Observations & Results
------------------------------------------------------------

- Normalization makes criteria comparable.
- Weights influence ranking results.
- Alternatives closer to the ideal solution receive higher ranks.
- Consistent results were obtained across CLI, package, and web service versions.

