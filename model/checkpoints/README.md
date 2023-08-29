# Model pretrained parameters

These models have been trained using the [LazyQSAR package](https://github.com/ersilia-os/lazy-qsar)
Upon 5-fold crossvalidation on train test splits (80-20%) with balanced classes, we obtain the following performance:


| **Model**       | **Data** | **Frac Actives (%)** | **Fingerprints** | **AUROC ± STDev** |
|-----------------|----------|------------------|------------------|-------------------|
| ic50_nf54_ldh_72h         | 1349   | 26.61   | Eosce   | 0.726 ± 0.039 |
| ic50_nf54_ldh_72h         | 1349   | 26.61   | Morgan   | 0.771 ± 0.023 |
| perc_nf54_ldh_72h         | 4810   | 8.46   | Eosce   | 0.800 ± 0.025 |
| perc_nf54_ldh_72h         | 4810   | 8.46   | Morgan   | 0.830 ± 0.037 |
| perc_nf54_lum_72h         | 19133   | 4.53   | Eosce   | 0.905 ± 0.016 |
| perc_nf54_lum_72h         | 19133   | 4.53   | Morgan   | 0.877 ± 0.016 |

Upon request we are happy to provide full models developed with [ZairaChem](https://github.com/ersilia-os/zaira-chem) as a downloadable. Please note that running these require installation of the Ersilia and the ZairaChem software

| **Model**       | **Data** | **Frac Actives (%)** | **AI tool** | **AUROC ± STDev** |
|-----------------|----------|------------------|------------------|-------------------|
| ic50_nf54_ldh_72h         | 1349   | 26.61   | Zairachem   | 0.782 ± 0.026 |
| perc_nf54_ldh_72h         | 4810   | 8.46   | Zairachem   | 0.864 ± 0.022 |
| perc_nf54_lum_72h         | 19133   | 4.53   | Zairachem   | 0.882 ± 0.011 |
