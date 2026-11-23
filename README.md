# Antimalarial activity (MMV Data)

Predicts in vitro antimalarial activity against the Plasmodium falciparum NF54 strain with four LazyQSAR classifiers trained by Ersilia on 72-hour screening data from Medicines for Malaria Venture, one per readout (lactate dehydrogenase or luminescence) and cut-off (IC50 below 1 uM, or at least 50% inhibition at 2 uM). Five-fold out-of-fold validation gives AUROC 0.79 and 0.72 for the IC50 tasks and 0.89 and 0.91 for the single-point tasks. Outputs are ranks against 50,000 drug-like molecules. Agreement between the two readouts is more convincing than either alone.

This model was incorporated on 2023-08-24.
Last packaged on 2026-11-19.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4rta`
- **Slug:** `malaria-mmv`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Malaria`
- **Target Organism:** `Plasmodium falciparum`
- **Tags:** `Antiparasitic activity`, `IC50`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `4`
- **Output Consistency:** `Fixed`
- **Interpretation:** Four ranks of predicted Plasmodium falciparum NF54 inhibition (IC50 below 1 uM and 50% single-point, by lactate dehydrogenase and luminescence) against 50,000 drug-like molecules; 0.65 is better than 99% of them.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| ic50_nf54_ldh_72h_1um_rank | float | high | Rank score of the compound's predicted inhibition of Plasmodium falciparum NF54 at an IC50 cut-off of 1 uM (72 h, lactate dehydrogenase readout), calibrated against a reference library of 50K drug-like molecules so that 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| ic50_nf54_lum_72h_1um_rank | float | high | Rank score of the compound's predicted inhibition of Plasmodium falciparum NF54 at an IC50 cut-off of 1 uM (72 h, luminescence readout), calibrated against a reference library of 50K drug-like molecules so that 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| perc_nf54_ldh_72h_50_rank | float | high | Rank score of the compound's predicted inhibition of Plasmodium falciparum NF54 of at least 50% in a single-point assay at 2 uM (72 h, lactate dehydrogenase readout), calibrated against a reference library of 50K drug-like molecules so that 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| perc_nf54_lum_72h_50_rank | float | high | Rank score of the compound's predicted inhibition of Plasmodium falciparum NF54 of at least 50% in a single-point assay at 2 uM (72 h, luminescence readout), calibrated against a reference library of 50K drug-like molecules so that 0.65 is better than 99% of them. Recommended threshold: 0.65. |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4rta](https://hub.docker.com/r/ersiliaos/eos4rta)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4rta.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4rta.zip)
- **Apptainer**: [https://models-sif.s3.eu-north-1.amazonaws.com/eos4rta_v2.sif](https://models-sif.s3.eu-north-1.amazonaws.com/eos4rta_v2.sif)

### Resource Consumption
- **Model Size (Mb):** `106`
- **Environment Size (Mb):** `6954`
- **Image Size (Mb):** `4095.06`

**Computational Performance (seconds):**
- 10 inputs: `72.48`
- 100 inputs: `65.1`
- 10000 inputs: `702.23`

### References
- **Source Code**: [https://github.com/ersilia-os/lazy-qsar](https://github.com/ersilia-os/lazy-qsar)
- **Publication**: [https://ersilia.io](https://ersilia.io)
- **Publication Type:** `Other`
- **Publication Year:** `2023`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4rta
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4rta
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
