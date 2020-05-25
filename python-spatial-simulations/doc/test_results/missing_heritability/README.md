# Calculating missing heritability

This directory holds preliminary results.

A `NumPy` byte array containing float values for the fraction of missing heritability captured by sampling from the spatial simulation with selection.

The array is called `H_var_centered_pop_size_100000.0_mu_0_s_0.001_m_0.1_label_021820.npy`. It can be read into memory with `np.load()`.

The array has dimensions *(50,50,1)*.
Axes 1 and 2 represent spatial coordinates (*1 dimensional spatial environment*  with length **L = 50**).
Axis 0 contains subarrays representing fractional heritability **H** values as a function of ![$\sigma$](https://render.githubusercontent.com/render/math?math=%24%5Csigma%24).

![$\sigma$](https://render.githubusercontent.com/render/math?math=%24%5Csigma%24) ranges from *(0, L)* by steps of 1.

The values in each subarray can be computed as follows:

![$ H_{var}(\sigma) = \frac{\sum_{k=1}^{numreps} f_k(1-f_k) \bf{P}}{\sum_{k=1}^{numreps} f_k(1-f_k)} $](https://render.githubusercontent.com/render/math?math=%24%20H_%7Bvar%7D(%5Csigma)%20%3D%20%5Cfrac%7B%5Csum_%7Bk%3D1%7D%5E%7Bnumreps%7D%20f_k(1-f_k)%20%5Cbf%7BP%7D%7D%7B%5Csum_%7Bk%3D1%7D%5E%7Bnumreps%7D%20f_k(1-f_k)%7D%20%24)

**P** is a matrix which contains the probability of sampling the allele at each deme, *numreps* represents the number of independent replicate simulations performed for each set of population parameters, ![$\sigma$](https://render.githubusercontent.com/render/math?math=%24%5Csigma%24) is the standard deviation of the gaussian sampling kernel, and ![$f_k$](https://render.githubusercontent.com/render/math?math=%24f_k%24) is the allele frequency at a focal deme selected to be some distance from the center of the sampling kernel. This distance is represented in the elements of axis 1 of the array. As we move further away from the center of the distribution, we are increasing the distance between the focal deme and the center of the sampling kernel. **![$\bf{H_{var}}$](https://render.githubusercontent.com/render/math?math=%24%5Cbf%7BH_%7Bvar%7D%7D%24)
decreases as distance from the sampling center increases.**


The following parameter values were used to generate the simulation sampled from:
  * Selection coefficient ![$s = 10^{-3}$](https://render.githubusercontent.com/render/math?math=%24s%20%3D%2010%5E%7B-3%7D%24)

  * Migration rate ![$m = 10^{-1}$](https://render.githubusercontent.com/render/math?math=%24m%20%3D%2010%5E%7B-1%7D%24)

  * Population size ![$N = 10^{5}$](https://render.githubusercontent.com/render/math?math=%24N%20%3D%2010%5E%7B5%7D%24)

  * Sample size ![$n = 10^{2}$](https://render.githubusercontent.com/render/math?math=%24n%20%3D%2010%5E%7B2%7D%24)


The simulation uses reflecting boundaries for frequency trajectories. Once the focal allele goes extinct in the spatial environment, a new allele is introduced at a frequency of ![$\frac{1}{N}$](https://render.githubusercontent.com/render/math?math=%24%5Cfrac%7B1%7D%7BN%7D%24)
. This removes the need to explicitly provide a mutation rate.

The [figure](/H_plot_s_0.0001_m_0.1_pop_size_1e-5.png) included in this directory was made by plotting **H** on the *y-axis* over the range of ![$\sigma$](https://render.githubusercontent.com/render/math?math=%24%5Csigma%24). The *x-axis* is distance from the focal deme to the center of the sampling kernel. ![$\sigma$](https://render.githubusercontent.com/render/math?math=%24%5Csigma%24) increases from *0* at the lightest color curve, to *L* at the darkest curve.

<img src="H_plot_s_0.0001_m_0.1_pop_size_1e-5.png">
