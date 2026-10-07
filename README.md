# Antimalarial activity (MMV Data)

Predicts in vitro antimalarial activity against the Plasmodium falciparum NF54 strain with four classifiers Ersilia trained with its LazyQSAR package on 72-hour screening data contributed by Medicines for Malaria Venture, one per cut-off and readout, an IC50 below 1 uM and a single-point inhibition of at least 50%, each measured by lactate dehydrogenase and by luminescence. Five-fold cross-validation gave AUROC above 0.70 for all four. Agreement between the two detection methods is more convincing than either alone.

This model was incorporated on 2023-08-24.Last packaged on 2025-11-24.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4rta`
- **Slug:** `malaria-mmv`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Malaria`
- **Target Organism:** `Plasmodium falciparum`
- **Tags:** `Malaria`, `P.falciparum`, `IC50`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `4`
- **Output Consistency:** `Fixed`
- **Interpretation:** Four Plasmodium falciparum NF54 inhibition probabilities, IC50 below 1 uM and 50% single-point, by lactate dehydrogenase and luminescence.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| ic50_nf54_ldh_72h_1uM | float | high | Classification score for Pfalciparum NF54 inhibition based on an IC50 cut-off of 1uM measured by LDH |
| ic50_nf54_lum_72h_1uM | float | high | Classification score for Pfalciparum NF54 inhibition based on an IC50 cut-off of 1uM measured by luminiscence |
| perc_nf54_ldh_72h_50 | float | high | Classification score for Pfalciparum NF54 inhibition based on a percentage of inhibition at single point cut-off of 50% measured by LDH |
| perc_nf54_lum_72h_50 | float | high | Classification score for Pfalciparum NF54 inhibition based on a percentage of inhibition at single point cut-off of 50% measured by luminiscence |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4rta](https://hub.docker.com/r/ersiliaos/eos4rta)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4rta.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4rta.zip)

### Resource Consumption
- **Model Size (Mb):** `146`
- **Environment Size (Mb):** `7610`
- **Image Size (Mb):** `7767.58`

**Computational Performance (seconds):**
- 10 inputs: `42.05`
- 100 inputs: `61.83`
- 10000 inputs: `915.44`

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
