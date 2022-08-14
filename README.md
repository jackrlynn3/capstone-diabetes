# Diabetes in USA: *Who is at risk?*

Non-communicable diseases dominate disease burden within the developed world; diabetes has the seventh largest disease burden in the United States and continues to grow year-by-year. [[1]](https://vizhub.healthdata.org/gbd-compare/) Like most non-communicable diseases, genetic, lifestyle, and community factors differentially potentiate diabetes incidence. **To advocate effectively for diabetes as a public health burden, one must determine the communities most affected by it, the underlying medical risk factors that increase the likelihood of development, and its current maintenance and treatment methods.** In this capstone project, we are creating a holistic narrative of the disease burden of diabetes in the United States from a public health perspective. First, CDC [[2]](https://www.kaggle.com/datasets/cdc/national-health-and-nutrition-examination-survey) [[3]](https://www.cdc.gov/nccdphp/dnpao/data-trends-maps/index.html) [[4]](https://chronicdata.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-Diabetes/f8ti-h92k/data), Census [[5]](https://data.census.gov/cedsci/table?q=education%20by%20state&tid=ACSDT5Y2020.B06009) [[6]](https://data.census.gov/cedsci/table?q=S1901&tid=ACSST5Y2020.S1901), and Department of Agriculture [[7]](https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-u-s/interactive-charts-and-highlights/) data are used to determine who is most affected by diabetes, including special interest explorations of race, ethnicity, sex, age, income, food security, and exercise. Second, the Rui-Ci Health Center's diabetes and medical characteristics dataset [[8]](https://doi.org/10.5061/dryad.ft8750v) is used in machine learning models to predict the underlying physical characteristics that coincide with diabetes diagnoses, emphasizing the connection between community demographics and health manifestations. Third, deep learning techniques are used on Jaeb Center blood glucose traces [[9]](https://public.jaeb.org/dataset/563) to develop a tool for tracking and alerting diabetic individuals of blood glucose spikes, thus creating a holistic view of diabetes patients pre- and post-diagnosis. All project methods emphasize the use of cheap data science techniques to refine and target diabetes disease burden control within the United States, with special emphasis on creating a holistic view of diabetes from a public health perspective. The findings of this project can then be used for efficient and effective targeted advocacy for those most affected.

This capstone project is the creation of [**Temesgen Fekadu**](https://github.com/TemesgenFekadu01), [**Jack Lynn**](https://github.com/jackrlynn3), [**Hayden Muscha**](https://github.com/HaydenKMuscha), and [**Sam Wainright**](https://github.com/wainrightsamantha), in coordination with the [**Dev10 Data Bootcamp**](https://www.genesis10.com/).

### Essential Questions
1. Which demographics are most likely to develop diabetes in the US?  
2. What measurable bodily attributes contribute to the indication of diabetes?  
3. How are diabetes patients' blood glucose levels tracked in real time?  
4. Which demographics are exhibiting higher spikes in blood glucose levels?  
5. Looking at specific regions within the US, how do different lifestyles contribute to diabetes prevalence?  
6. Does food scarcity impact diabetes incidence?  
7. Can we predict diabetes diagnoses based on readily available medical vitals, such as blood pressure, mineral levels, and body mass index? 
8. Can we predict warning notifications for dangerous blood glucose spikes based on real time blood glucose levels of Type-1 diabetes patients? 

## Table of Contents
1. **[Datasets](#datasets)**
2. **[Project Structure](#project-structure)**
3. **[SQL Database](#sql-database)**
4. **[Machine Learning](#machine-learning)**
5. **[Deep Learning](#deep-learning)**
6. **[Visualizations](#visualizations)**
7. **[Website Deployment](#website-deployment)**
8. **[References](#references)**

<a name="datasets"></a>
## Datasets

[**"A Randomized Clinical Trial to Assess the Efficacy and Safety of Continuous Glucose Monitoring in Youth < 8 with Type 1 Diabetes", from JAEB Center:**](https://public.jaeb.org/dataset/563) Medical profiles and blood glucose traces from Type-1 diabetes patients in clinical trial for blood glucose monitoring device; used to track blood glucose levels in real time and predict hazardous blood glucose spikes using deep learning

[**Aerobic Activity by State:**](https://www.cdc.gov/nccdphp/dnpao/data-trends-maps/index.html) CDC ongoing study investigating health trends by state in the US; used to assess the proportion of state populations that participate in at least 150 minutes of aerobic activity weekly

[**"Association of body mass index and age with incident diabetes in Chinese adults: a population-based cohort study", from Ruici Healthcare:**](https://datadryad.org/stash/dataset/doi:10.5061/dryad.ft8750v) Large Chinese sample (>200,000 subjects) describing medical vitals and diabetes diagnoses; used to train machine learning model to predict diabetes diagnoses based on basic medical measurements

[**B06009: Place of Birth by Educational Attainment in the United States:**](https://data.census.gov/cedsci/table?q=education%20by%20state&tid=ACSDT5Y2020.B06009) U.S. Census data describing educational attainment by state; used to assess potential connections between educational attainment and diabetes diagnoses

[**Food Security in the US:**](https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-u-s/interactive-charts-and-highlights/) U.S. Department of Agriculture dataset tracking food security by state; used to assess potential connections between food security by states and diabetes diagnoses

[**National Health and Nutrition Examination Survey (NHAINES):**](https://www.kaggle.com/datasets/cdc/national-health-and-nutrition-examination-survey) CDC program designed to assess health and nutritional conditions of adults in the United States; used to assess the health statuses of demographic groups

[**S1901: Income in the Past 12 Months (In 2020 Inflation-Adjusted Dollars):**](https://data.census.gov/cedsci/table?q=S1901&tid=ACSST5Y2020.S1901) U.S. Census data describing income brackets by state; used to assess potential connections between income brackets and diabetes diagnoses 

[**U.S. Chronic Disease Indicators: Diabetes:**](https://chronicdata.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-Diabetes/f8ti-h92k/data) CDC tracking of diabetes prevalence by state, race, and ethnicty; used to describe what demographic groups are make up the United States diabetic population

<a name="project-structure"/></a>
## Project & File Structure

[Network Diagram](https://user-images.githubusercontent.com/105175430/184555367-4a6e7227-f7a0-404a-8064-5fc0ebe45f15.png)
*Network diagram describing the flow and transformation of data and the tools used at each point.*

#### Data Extraction, Transformation, and Loading

*A full ETL description document can be found under [`/report/RepeatableETLReport.pdf`](https://github.com/jackrlynn3/capstone-diabetes/blob/main/report/RepeatableETLReport.pdf).*

Data collections are sourced from the CDC, JAEB, Ruici Healthcare, U.S. Census Department, and U.S. Department of Agriculture; a full description of each dataset can be seen [here](#datasets). All datasets are downloaded directly from their respective websites and saved locally as `.csv` files.

Each file is transformed using `.ipyn` notebooks run on local machines; these notebooks can be found in their dataset's respective directories under [`/datasets/`](https://github.com/jackrlynn3/capstone-diabetes/tree/main/datasets). The files heavily use the `numpy` and `pandas` libraries and typically conver the following transformations: (1) null fields, (2) column drops, (3) inconsistent/unusable typing, (4) outlier handling, and (5) schema simplifcation. Finally, all of these files are saved as `.csv` files and uploaded to this group's Azure Data Lake.

Each file is then transformed again and loaded into Azure SQL Databases using Azure Databricks; a full description of the SQL schema can be found [here](#sql-database). Each respective database is first loaded into the Azure Database using SQL inquiries in Azure Data Studio, which can be found under [`/datasets/sql-queries/`](https://github.com/jackrlynn3/capstone-diabetes/tree/main/datasets/sql-queries). Kafka files in Azure Databricks then take in the corresponding `.csv` files from the Azure Data Lake, transforms them into the schema of the SQL database, and then loads this group's Azure SQL database; these Kafka files can be found in [`/datasets/kafka/`](https://github.com/jackrlynn3/capstone-diabetes/tree/main/datasets/kafka).

#### Streaming

All data streaming is handled through Azure Data Factories. Two streams handle the updates of all databases.

<img width="948" alt="Screen Shot 2022-08-14 at 16 23 14" src="https://user-images.githubusercontent.com/105175430/184555453-7e256196-17a3-467b-b29c-2abd4f7686e9.png">
*`Static Data Stream` structure on Azure Data Factory.*

`Static Data Stream` updates the `CensusStat`, `Demographic`, `DiabetesPop`, `GlucoseMeter`, `Metric`, `NHAINESStat`, and `State` SQL databases. Each update follows the standard structure of first ensuring that the database's corresponding CSV file is present in the Azure Data Lake and then executing its corresponding Kafka file to load the file. A serielized order is followed because certain Kafka files edited the same SQL databases and need to be run a specific order. This data stream is triggered every 24 hours, reflecting any changes made to the base data on a daily basis.

<img width="345" alt="Screen Shot 2022-08-14 at 16 22 15" src="https://user-images.githubusercontent.com/105175430/184555471-c68f0271-631c-47e0-b5c2-028951ffad88.png">
*`CGM Data Stream` structure on Azure Data Factory.*

`CGM Data Stream` updates only the  `CGM_Stream` database. The data stream contains separation activations of producer and consumer Kafka files; the consumer is time offset. This data stream is used to simulate the follow of blood glucose readings in real time.

#### Machine Learning

#### Visualizations

#### Website Presentation

<a name="sql-database"/></a>
## SQL Database

<a name="machine-learning"/></a>
## Machine Learning

<a name="deep-learning"/></a>
## Deep Learning

<a name="visualizations"/></a>
## Visualizations

<a name="website-deployment"/></a>
## Website Deployment

<a name="references"/></a>
## References

[1] Institute for Health Metrics and Evaluation. (2019). GBD compare. Data Visualizations. Retrieved August 8, 2022, from https://vizhub.healthdata.org/gbd-compare/

[2] Centers for Disease Control and Prevention. (2017, January 26). National Health and Nutrition Examination Survey. Retrieved August 5, 2022, from Kaggle website: https://www.kaggle.com/datasets/cdc/national-health-and-nutrition-examination-survey 

[3] Centers for Disease Control and Prevention. (2021, June 3). National Center for Chronic Disease Prevention and Health Promotion, Division of Nutrition, Physical Activity, and Obesity. Data, Trend and Maps [online]. Retrieved August 5, 2022, from CDC website: https://www.cdc.gov/nccdphp/dnpao/data-trends-maps/index.html 

[4] Centers for Disease Control and Prevention. (2022, March 24). U.S. Chronic Disease Indicators: Diabetes | Chronic Disease and Health Promotion Data & Indicators. Retrieved August 5, 2022, from Socrata website: https://chronicdata.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-Diabetes/f8ti-h92k/data

[5] United States Census Bureau. (2022a, March 17). American Community Survey: B06009: PLACE OF BIRTH BY EDUCATIONAL ATTAINMENT IN THE UNITED STATES. Retrieved August 5, 2022, from Census website: https://data.census.gov/cedsci/table?q=education%20by%20state&tid=ACSDT5Y2020.B06009 

[6] United States Census Bureau. (2022b, March 17). American Community Survey: S1901: INCOME IN THE PAST 12 MONTHS (IN 2020 INFLATION-ADJUSTED DOLLARS) U.S. Census Bureau (2020). Retrieved from Census website: https://data.census.gov/cedsci/table?q=S1901&tid=ACSST5Y2020.S1901 

[7] U.S. Department of Agriculture. (2021, September 8). Food Security in the U.S. USDA (2019). Retrieved from www.ers.usda.gov website: https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-u-s/interactive-charts-and-highlights/

[8] Chen, Y., Zhang, X.-P., Yuan, J., Cai, B., Wang, X.-L., Wu, X.-L., … Li, X.-Y. (2018, August 21). Data from: Association of body mass index and age with incident diabetes in Chinese adults: a population-based cohort study. Retrieved August 5, 2022, from Datadryad website: https://doi.org/10.5061/dryad.ft8750v 

[9] JAEB Center for Health Research. (2019). A Randomized Clinical Trial to Assess the Efficacy and Safety of Continuous Glucose Monitoring in Youth < 8 with Type 1 Diabetes. Retrieved August 5, 2022, from JAEB website: https://public.jaeb.org/dataset/563 
