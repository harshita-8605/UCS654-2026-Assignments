# Learn Probability Density Functions using Roll-Number-Parameterized Non-Linear Model

## Dataset
The India Air Quality dataset from Kaggle was used.  
NO₂ (no2) was taken as the feature for analysis.

## Step 1
The NO₂ values were transformed using the formula provided in the question.  
The values of aᵣ and bᵣ were calculated using the roll number **102317003**.  
The transformed values were stored in a new column named `z`.

## Step 2
The parameters of the given probability density function were learned from the transformed data.  
The values of μ, λ, and c were obtained by fitting the PDF to the data distribution.  
Using these parameters, the predicted probability values p̂(z) were calculated.
