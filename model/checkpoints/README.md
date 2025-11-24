# Model pretrained parameters

These models have been trained using the [LazyQSAR package](https://github.com/ersilia-os/lazy-qsar)
Upon 5-fold crossvalidation on train test splits (80-20%) with balanced classes, we obtain the following performance:


| **Model**       | **Data** | **Frac Actives (%)** | **AUROC ± STDev** |
|-----------------|----------|------------------|-------------------|
| ic50_nf54_ldh_72h_1uM   | 1349   | 26.6   |  0.76 ± 0.02 |
| ic50_nf54_lum_72h_1uM   | 1350   | 18.22   |  0.70 ± 0.03 |
| perc_nf54_ldh_72h_50   | 4810   | 8.46   |  0.86 ± 0.01 |
| perc_nf54_lum_72h_50   | 226901   | 0.3   |  0.90 ± 0.01 |
