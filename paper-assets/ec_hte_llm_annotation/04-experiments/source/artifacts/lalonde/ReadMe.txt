REPLICATION FILES
——————————————————

	Empathy-based counterspeech can reduce racist hate speech in a social media field experiment
	
	PNAS 2021
	
	Dominik Hangartner, Gloria Gennaro, Sary Alasiri, Nicholas Bahrich, Alexandra Bornhoft, Joseph Boucher, Buket Buse Demirci, Laurenz Derksen, Aldo Hall, Matthias Jochum, Maria Murias Munoz, Marc Richter, Franziska Vogel, Salomé Wittwer, Felix Wüthrich, Fabrizio Gilardi, and Karsten Donnay

	Please contact Gloria Gennaro if you have any questions about the replication material. For updated contact details, see https://gloriagennaro.rbind.io


OVERVIEW
——————————————————

The replication material includes the following folders:

1/ code: includes all the code to reproduce the paper results, plus additional robustness checks:
	- subfolder "1 Paper" includes all code to replicate the results in the paper
	- Subfolder "2 Additional analysis" includes all code used to produce additional robustness checks - more details are provided in the individual scripts

2/ data: includes all dataset to reproduce the results in the paper:
	- "main_dataset.csv" includes the main variables
	- "data_lasso2.RDS" includes all controls that are used as input for the lasso-based double selection procedure
	- "attrition.csv" includes additional variables on attrition for each user
	- The "auxiliary" subfolder includes intermediate output of the code snippet "1_main_results.R"

3/ results: includes all results reported in the paper. 



SESSION INFO
——————————————————

R version 4.1.2 (2021-11-01)Platform: x86_64-apple-darwin17.0 (64-bit)Running under: macOS Catalina 10.15.7


PACKAGES
——————————————————
broom_0.7.10     readxl_1.3.1     psych_2.1.9      Hmisc_4.6-0      Formula_1.2-4    survival_3.2-13 lattice_0.20-45  stringr_1.4.0    systemfit_1.1-24 lmtest_0.9-39    zoo_1.8-9        car_3.0-12      carData_3.0-4    foreign_0.8-81   stargazer_5.2.2  xtable_1.8-4     ggpubr_0.4.0     ggplot2_3.3.5   estimatr_0.30.4  glmnet_4.1-3     Matrix_1.3-4     readr_2.1.0      tidyr_1.1.4      dplyr_1.0.7     plyr_1.8.6       hdm_0.3.1        packrat_0.7.0   