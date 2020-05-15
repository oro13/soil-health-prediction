<style>
td {
  font-size: 70px
}
</style>

# Predicting Soil Nutrition with Infrared Spectroscopy

<img alt='working with the soil' src='img/Micro_catchment.jpg' width='50%' height='100%'>

[photo by Malherbe Rossouw, South Africa ](https://commons.wikimedia.org/w/index.php?curid=63653257)

## Motivation:

Soil health is our health. Here we hope to improve our tools of assessing soil health and making them more available.

Infrared spectroscopy has traditionally provided great scientific insight. Now it can improve the quality of life of farmers and their ecosystems.

## Data Source

Data Collected between 2009 and 2013 by [African Soil Information Service (AFSIS)](https://registry.opendata.aws/afsis/) research centers.

Sponsored by:

<img alt='qedlogo' src='img/qed.png' width='90%' height='50%'>

[QED homepage](https://qed.ai/)

[Data Tutorial](https://github.com/qedsoftware/afsis-soil-chem-tutorial)


## Infrared Spectroscopy: Overview

Infering nutrients through Infrared Spectroscopy. Thousands of soil samples have been both scanned with (dry testing) and tested in the lab (wet testing), for a more complete soil profile. The goal is to predict the more detailed nutrient profile by using the coarser, but more efficient and affordable, infrared methods.


## How the Data Was Collected

3 Research Centers Across Africa: CROPNUTS, ICRAF, and RRES. I worked primarily with CROPNUTS due to them having large data set available.

Each research center performed dry teting (infrared and xray scanning) and wet testing (chemical extraction and solutions) on soil sampled from the same sights across the continent.


<img alt='data locations' src='img/map.jpg' width='90%' height='50%'>


## How the Data was Measured:


One infrared scanning tool, the Bruker HTS-XT

<img alt='qedlogo' src='img/HTS-XT_Bruker.png' width='70%' height='50%'>

[more information on Bruker HTS-XT](https://www.bruker.com/products/infrared-near-infrared-and-raman-spectroscopy/ft-ir-routine-spectrometers/hts-xt.html)

The infrared scanner can be configured in a variety of ways, target different spectra ranges:

<img alt='configuring the HTS-XT' src='img/ir_device_workflow.png' width='50%' height='50%'>

The data includes scannings from a variety of infrared methods. Different tools are better at perceiving specific ranges in the infrared spectrum. Running a predictive model on the various tools helped decipher which particles it was better at perceiving.

For soil nutrient molecules near the soil surface, all the infrared tools performed decently. For aspects of the soil harder to depict physically, such as soil eletrical capacitance due to insoluable salt buildup (CONFIRM), certain tools perform better than others.

A research paper considers this more closely:

<img alt='comparing the performance of different tools on different targets' src='img/compare spectra.png' width='50%' height='50%'>

## The Data

### Infrared Data

<img alt='infrared data' src='img/x_before_derivative.png' width='90%' height='50%'>

<img alt='infrared spectra' src='img/wave_visual.png' width='90%' height='50%'>

Take Derivative of Values

<img alt='infrared spectra' src='img/x_after_derivative.png' width='90%' height='50%'>

### Target Values

<img alt='target data' src='img/targets_before_log.png' width='90%' height='50%'>

Take the log to help the computer track tiny values

<img alt='target data' src='img/targets_after_log.png' width='90%' height='50%'>


## XGBoost Model Trained on Bruker HTS-XT Data

### Initialize the Model

<img alt='xgboost start' src='img/basicmodel.png' width='90%' height='40%'>

### Training the Model

<img alt='xgboost code' src='img/final_model.png' width='90%' height='40%'>

## Nutrient Predictions

### Calcium
<img alt='infrared spectra' src='img/final_ca1.png' width='45%' height='50%' align=left>
<img alt='infrared spectra' src='img/final_ca2.png' width='50%' height='50%' alight=right>


### Magnesium

<img alt='infrared spectra' src='img/final_mg1.png' width='45%' height='50%' align=left>
<img alt='infrared spectra' src='img/final_mg2.png' width='50%' height='50%' alight=right>

### Potassium

<img alt='infrared spectra' src='img/final_k1.png' width='45%' height='50%' align=left>
<img alt='infrared spectra' src='img/final_k2.png' width='50%' height='50%' alight=right>

### Phosphorus

<img alt='infrared spectra' src='img/final_p1.png' width='45%' height='50%' align=left>
<img alt='infrared spectra' src='img/final_p2.png' width='50%' height='50%' alight=right>

### Soil pH

<img alt='infrared spectra' src='img/final_ph1.png' width='45%' height='50%' align=left>
<img alt='infrared spectra' src='img/final_ph2.png' width='50%' height='50%' alight=right>

## Next Steps:

Considering geodata in the model. Attempting transfer learning on neural networks using data from other continents.

Best ecological practices of agriculture can be measured and their efficacy can be proven. We can use a cheap and quick method of soil health assessment such as a infrared scanning, made widespread in smartphones.

My hope is this project begins what could become a predictive model robust enough to inform cruder handheld infrared scannings. Such a model would consider global and local datasets, and determine weights based on that location. 

Such a device/application could democratize soil health and demystify the process of knowing your soil's nutrient profile.

Another horizon of interest would be considering ways to easily assess soil microbiology.