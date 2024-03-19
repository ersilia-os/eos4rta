# Antimalarial activity (MMV)

Prediction of the in vitro antimalarial potential of small molecules. This model has been developed by Ersilia thanks to experimental data provided by MMV. The model provides the probability of inhibition of the malaria parasite (NF54) measured both as percentage of inhibition (with luminescence and LDH) and IC50. 5-fold crossvalidation of the models shows AUROC>0.75 in all models.

## Identifiers

* EOS model ID: `eos4rta`
* Slug: `malaria-mmv`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability of inhibiting the malaria parasite (strain NF54) in IC50 (threshold 1uM) and percentage of inhibition (50%, measured by LDH and Lum)

## References

* [Publication](https://ersilia.io)
* [Source Code](https://github.com/ersilia-os/lazy-qsar)
* Ersilia contributor: [GemmaTuron](https://github.com/GemmaTuron)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos4rta)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4rta.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos4rta) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://ersilia.io) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!