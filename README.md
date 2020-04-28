# MOG_cosmology

This project aims to test if the cosmological predictions of the MOG theory can fit different observational data. The project is part of my PhD thesis.

## The MOG theory

The MOG (MOdified Gravity) theory was created by J. Moffat and is a modification of Einstein theory. The goal of this alternative theory is explain the gravity in all scales without the introduction of dark components (matter and energy). We can obtain the theorical H(z) for  the MOG solving the modified FLRW equations. To solve this equations, we have to set a value for H_0 and the autopotential of the theory V_G. In this project, we take as an imput a table with H(z) values for every H_0 and V_G considered.

## The imput

The theoretical tables for H(z) are named with a code:
- 6737 means H_0=67.37, 7348 mean H_0=73.48
- If there is nothing after the H_0 number it means that the value for V_G is the one given by Moffat.
- _ 0 means V_G=0
- +(-) means 10% more(less) than the value given by moffat
- ++(--) means 20% more(less) than the value given by moffat
- --- means 40% less than the value given by moffat

## Observational data
We will use three sets of observational data

### H(Z) obtained by the cosmic chronometers method
In this case we have the observational values for H(z) stored in the file CC.dat. We calculate the chi squared with the cc.py script that give us the value for each theoretical table (the name of the imput table has to be changed by hand) via terminal. Then we can make a plot of the theoretical predictions and the data using the plotCC.py script.

### SNIa data
To be completed

### BAO data
To be completed

## Results
To be published
