## PDF Estimation using GAN

This assignment explores how an unknown probability distribution can be learned using data samples without assuming any predefined mathematical form.

The NO₂ values from the India Air Quality dataset are used as the input feature. These values are first transformed using a non-linear function to obtain a new variable. Since the analytical probability distribution of the transformed variable is unknown, a simple one-dimensional Generative Adversarial Network (GAN) is used to learn its distribution.

The assignment follows these main steps:
- Loading and preprocessing the NO₂ data
- Applying the given transformation to generate the variable `z`
- Training a 1-D GAN using real and generated samples
- Generating samples from the trained generator
- Estimating and visualizing the probability density function using generated samples

All implementation details, plots, and observations are included directly in the notebook.  
