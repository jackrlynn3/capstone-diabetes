# Diabetes in USA: *Who is at risk?*

Non-communicable diseases dominate disease burden within the developed world; diabetes contributes the seventh largest number of DALYs in the United States and continues to grow year-by-year. [[1]](https://vizhub.healthdata.org/gbd-compare/) Like most non-communicable diseases, genetic, lifestyle, and community factors differentially potentiate diabetes incidence. **To advocate effectively for diabetes as a public health burden, one must determine the communities most affected by it, the underlying medical risk factors that increase the likelihood of development, and its current maintenance and treatment methods.** In this capstone project, we are creating a holistic narrative of the disease burden of diabetes in the United States from a public health perspective. First, CDC [[2]](https://www.kaggle.com/datasets/cdc/national-health-and-nutrition-examination-survey) [[3]](https://www.cdc.gov/nccdphp/dnpao/data-trends-maps/index.html) [[4]](https://chronicdata.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-Diabetes/f8ti-h92k/data), Census [[5]](https://data.census.gov/cedsci/table?q=education%20by%20state&tid=ACSDT5Y2020.B06009) [[6]](https://data.census.gov/cedsci/table?q=S1901&tid=ACSST5Y2020.S1901), and Department of Agriculture [[7]](https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-u-s/interactive-charts-and-highlights/) data are used to determine who is most affected by diabetes, including special interest explorations of race, ethnicity, sex, age, income, food security, and exercise. Second, the Rui-Ci Health Center's diabetes and medical characteristics dataset [[8]](https://doi.org/10.5061/dryad.ft8750v) is used in machine learning models to predict the underlying physical characteristics that coincide with diabetes diagnoses, emphasizing the connection between community demographics and health manifestations. Third, deep learning techniques are used on Jaeb Center blood glucose traces [[9]](https://public.jaeb.org/dataset/563) to develop a tool for tracking and alerting diabetic individuals of blood glucose spikes, thus creating a holistic view of diabetes patients pre- and post-diagnosis. All project methods emphasize the use of cheap data science techniques to refine and target diabetes disease burden control within the United States, with special emphasis on creating a holistic view of diabetes from a public health perspective. The findings of this project can then be used for efficient and effective targeted advocacy.

This capstone project is the creation of [**Temesgen Fekadu**](https://github.com/TemesgenFekadu01), [**Jack Lynn**](https://github.com/jackrlynn3), [**Hayden Muscha**](https://github.com/HaydenKMuscha), and [**Sam Wainright**](https://github.com/wainrightsamantha), in coordination with the [**Dev10 Data Bootcamp**](https://www.genesis10.com/).

### Essential Questions
1. Which demographics are most likely to develop diabetes in the US?  
2. What measurable bodily attributes suggest the presence of diabetes?  
3. How are diabetes patients' blood glucose levels tracked in real time?   
4. Are certain regions of the United States more affected by diabetes than others?
5. Does food scarcity impact diabetes incidence?  
6. Can we predict diabetes diagnoses based on readily available medical vitals, such as blood pressure, mineral levels, and body mass index? 
7. Can we predict blood glucose levels of Type-1 diabetes patients at least 30 minutes ahead in order to warn about incoming hazardous spikes?

## Table of Contents
1. **[Datasets](#datasets)**
2. **[Project Structure](#project-structure)**
3. **[SQL Database](#sql-database)**
4. **[Machine Learning](#machine-learning)**
5. **[Deep Learning](#deep-learning)**
6. **[Visualizations](#visualizations)**
7. **[Dash Deployment](#dash-deployment)**
8. **[References](#references)**

<a name="datasets"></a>
## Datasets

[**"A Randomized Clinical Trial to Assess the Efficacy of Real-Time Continuous Glucose Monitoring in the Management of Type 1 Diabetes", from JAEB Center:**](https://public.jaeb.org/dataset/563) Medical profiles and blood glucose traces from Type-1 diabetes patients in a clinical trial for a blood glucose monitoring device; used to track blood glucose levels in real time and predict hazardous blood glucose spikes using deep learning

[**Aerobic Activity by State:**](https://www.cdc.gov/nccdphp/dnpao/data-trends-maps/index.html) CDC ongoing study investigating health trends by state in the U.S.; used to assess the proportion of state populations that participate in at least 150 minutes of aerobic activity weekly

[**"Association of body mass index and age with incident diabetes in Chinese adults: a population-based cohort study", from Ruici Healthcare:**](https://datadryad.org/stash/dataset/doi:10.5061/dryad.ft8750v) Large Chinese sample (>200,000 subjects) describing medical vitals and diabetes diagnoses; used to train machine learning model to predict diabetes diagnoses based on basic medical measurements

[**B06009: Place of Birth by Educational Attainment in the United States:**](https://data.census.gov/cedsci/table?q=education%20by%20state&tid=ACSDT5Y2020.B06009) U.S. Census data describing educational attainment by state; used to assess potential connections between educational attainment and diabetes diagnoses

[**Food Security in the US:**](https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-u-s/interactive-charts-and-highlights/) U.S. Department of Agriculture dataset tracking food security by state; used to assess potential connections between food security by states and diabetes diagnoses

[**National Health and Nutrition Examination Survey (NHAINES):**](https://www.kaggle.com/datasets/cdc/national-health-and-nutrition-examination-survey) CDC program designed to assess health and nutritional conditions of adults in the United States; used to assess the health statuses of demographic groups

[**S1901: Income in the Past 12 Months (In 2020 Inflation-Adjusted Dollars):**](https://data.census.gov/cedsci/table?q=S1901&tid=ACSST5Y2020.S1901) U.S. Census data describing income brackets by state; used to assess potential connections between income brackets and diabetes diagnoses 

[**U.S. Chronic Disease Indicators: Diabetes:**](https://chronicdata.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-Diabetes/f8ti-h92k/data) CDC tracking of diabetes prevalence by state, race, and ethnicity; used to describe what demographic groups make up the U.S. diabetic population

<a name="project-structure"/></a>
## Project & File Structure

![network-diagram drawio](https://user-images.githubusercontent.com/105175430/184555690-c79eb433-fa29-4fcc-9773-e830424ff5b4.png)

_Network diagram describing the flow and transformation of data and the tools used at each point._

### Data Extraction, Transformation, and Loading

*A full ETL description document can be found under [`/project-specifications/RepeatableETLReport.pdf`](https://github.com/jackrlynn3/capstone-diabetes/blob/main/project-specifications/RepeatableETLReport.pdf).*

Data collections are sourced from the CDC, JAEB, Ruici Healthcare, U.S. Census Department, and U.S. Department of Agriculture; a full description of each dataset can be seen [here](#datasets). All datasets are downloaded directly from their respective websites and saved locally as `.csv` files.

Each file is transformed using `.ipyn` notebooks run on local machines; these notebooks can be found in their datasets' respective directories under [`/etl/`](https://github.com/jackrlynn3/capstone-diabetes/tree/main/etl). The files heavily use the `numpy` and `pandas` libraries and typically cover the following transformations: (1) null fields, (2) column drops, (3) inconsistent/unusable typing, (4) outlier handling, and (5) schema simplifcation. Finally, all of these files are saved as `.csv` files and uploaded to this group's Azure Data Lake.

Each file is then transformed again and loaded into Azure SQL Databases using Azure Databricks; a full description of the SQL schema can be found [here](#sql-database). Each respective database is first loaded into the Azure Database using SQL inquiries in Azure Data Studio, which can be found under [`/etl/sql-queries/`](https://github.com/jackrlynn3/capstone-diabetes/tree/main/etl/sql-queries). Kafka files in Azure Databricks then take in the corresponding `.csv` files from the Azure Data Lake, transform them into the schema of the SQL database, and then load them this group's Azure SQL database; these Kafka files can be found in [`/etl/kafka/`](https://github.com/jackrlynn3/capstone-diabetes/tree/main/etl/kafka).

### Streaming

All data streaming is handled through Azure Data Factories. Two streams handle the updates of all databases.

<img width="948" alt="Screen Shot 2022-08-14 at 16 23 14" src="https://user-images.githubusercontent.com/105175430/184555453-7e256196-17a3-467b-b29c-2abd4f7686e9.png">

_`Static Data Stream` structure on Azure Data Factory._

`Static Data Stream` updates the `CensusStat`, `Demographic`, `DiabetesPop`, `GlucoseMeter`, `Metric`, `NHAINESStat`, and `State` SQL databases. Each update follows the standard structure of first ensuring that the database's corresponding `.csv` file is present in the Azure Data Lake and then executing its corresponding Kafka file to load the file. A serielized order is followed because certain Kafka files edit the same SQL databases and need to be run in a specific order. This data stream is triggered every 24 hours, reflecting any changes made to the base data on a daily basis.

<img width="345" alt="Screen Shot 2022-08-14 at 16 22 15" src="https://user-images.githubusercontent.com/105175430/184555471-c68f0271-631c-47e0-b5c2-028951ffad88.png">

_`CGM Data Stream` structure on Azure Data Factory._

`CGM Data Stream` updates only the `CGM_Stream` database. The data stream contains seperate activations of producer and consumer Kafka files; the consumer is time offset. This data stream is used to simulate blood glucose readings taken in real time, providing readings every 5-15 sec.

### Analysis of Data

Three analysis methods are used to synthesize the data to create a holistic narrative around diabetes care in the U.S.: (1) visualizations, (2) machine learning, and (3) deep learning. Visualizations are stored as a `Dash` dashboard and is stored under the [`/dashboard/`](https://github.com/jackrlynn3/capstone-diabetes/tree/main/dashboard) directory. To view the visualizations, run [`/dashboard/app.py`](https://github.com/jackrlynn3/capstone-diabetes/blob/main/dashboard/app.py) using a Python interpreter. All learning models are stored in the [`/models/`](https://github.com/jackrlynn3/capstone-diabetes/tree/main/models) directory, each with their own subdirectories. Machine learning models are trained on local devices and then uploaded to the `Dash` interface while deep learning models are trained using Google Colab's parallelized GPU computing services. Visualizations and proof of concepts for all components can be viewed on the `Dash` dashboard.

*NOTE: Originally the `Dash` dashboard was going to be deployed to Heroku, but time constraints limited the ability to do so.*

*Full descriptions of [machine learning](#machine-learning), [deep learning](#deep-learning), [visualizations](#visualizations), and [website deployment](#website-deployment) can be seen below.*

### Reporting

The procedures and findings of this project can be found in one of several reports found under [`/project-specifications/`](https://github.com/jackrlynn3/capstone-diabetes/tree/main/project-specifications) directories. Summaries of the reports are the following:

1. [`ExecutiveSummary.pdf`:](https://github.com/jackrlynn3/capstone-diabetes/blob/main/project-specifications/ExecutiveSummary.pdf) Description of the high-level aims of the project, including introduction to project, key questions, datasets, and sources
2. [`ExploratoryQuestions.pdf`:](https://github.com/jackrlynn3/capstone-diabetes/blob/main/project-specifications/ExploratoryQuestions.pdf) Description of all essential exploratory questions that are answered by this project.
3. [`RepeatableETLReport.pdf`:](https://github.com/jackrlynn3/capstone-diabetes/blob/main/project-specifications/RepeatableETLReport.pdf) In-depth description of ETL process to get from raw data sourcing to loaded SQL database.
4. [`VisualizationsDashboardNapkinsAndFeedback.pdf`:](https://github.com/jackrlynn3/capstone-diabetes/blob/main/project-specifications/VisualizationsDashboardNapkinsAndFeedback.pdf) Napkin drawing for all dashboards used in the project and their respective peer feedback.
5. [`ProjectTechnicalReport.pdf`](): Full report describing methods, results, and analysis of all methods within this project.
6. [`CapstonePresentationSlides.pdf`](): Presentation slide deck describing the results of this project.

<a name="sql-database"/></a>
## SQL Database

![erd drawio](https://user-images.githubusercontent.com/105175430/184557987-8e5fe866-120e-4fef-bf3a-3e14bdf5ed56.png)

*ERD describing the SQL file structure.*

The SQL database is hosted on Azure SQL Databases and has restricted access to those with Dev10 credentials; please contact Jack Lynn (jackrlynn@gmail.com) to get the `config.py` to get access to the database. The following tables belong to the database:

1. **`CensusStat`:** This table is a genaralized format to hold data for different demographic information using the U.S. Census format. Each row has `year` and `value` columns describing the year the statistic is taken and value that statistic has. This table is connected to three other tables via foreign keys: (1) `State` (`stateID`), which descibes the geographic location of the statistic; (2) `Metric` (`metricID`), which describes what the statistic is measuring; and (3) `Demographic` (`demoID`), which describes the demographic group the statistic belongs to.
2. **`CGM_Stream`:** This table is the same as `GlucoseMeter` but uses Azure Data Factory pipelines to simulate the data being produced in real time.
3. **`Demographic`:** This table holds all demographic groups explored within project, including sex, race, ethnicity, smoking status, and more. `demo_group` describes the specific demographic of the group whereas `category` describes the type of demographic that is being tracked.
4. **`DiabetesPop`:** This table holds medical characteristics of a Chinese population in which some people are diabetic (`diabetes`). This table has a number of measurable medical vitals, including age (`age`), diastolic and systolic blood pressure (`dbp`/`sbp`), and others. Additionally, four foreign keys--`sexID`, `smokerID`, `drinkerID`, and `famhistID`--all correspond to instances in `Demographic` describing sex, smoking status, drinking status, and family history of diabetes, respectively.
5. **`GlucoseMeter`:** This table holds all blood glucose readings (`glucose_lvl`) and their corresponding times (`time`) and patients (`ptID`). `ptID` is connected to the `Patient` table as a foreign key to hold patient demographics.
6. **`Metric`:** This table describes the type of statistics being tracked by a `CensusStat`. `metric` is a description of what the statistic measures, and `unit` is the units to that statistic.
7. **`NHAINESStat`:** This table follows similar structure to `DiabetesPop` but rather uses data from the NHAINES study. It similarly has foreign keys to describe demographic groups: drinking status (`drinkerID`), sex (`sexID`), smoking status (`smokerID`), ethnicity (`ethnicityID`), educational level (`educationID`), and income bracket (`incomeID`).
8. **`Patient`:** This table is a companion to `GlucoseMeter` and describes the demographics of the readings. Five foreign keys--`sexID`, `raceID`, `ethnicityID`, `educationID`, and `smokerID`--correspond to the `Demographic` table and describe sex, race, ethnicity, education level, and smoking status, respectively.
9. **`State`:** This table holds name of states (`name`) and their corresponding abbreviations (`stateID`).

<a name="machine-learning"/></a>
## Machine Learning

Machine learning (ML) is used to assess the ability to predict a diabetes diagnosis on readily available medical vitals and demographic information such as blood pressure, body mass index, age, and sex. Machine learning models utilize the `scikit-learn` library.

[`scikit-learn`](https://scikit-learn.org/stable/) is built upon SciPy, NumPy, and matplotlib making it ideal for machine learning algorithms like classification, regression, and clustering. The library also provides tools for evaluating models, tuning hyperparameters, and pre-processing data. Since `scikit-learn` is open source and commercially useable ML tasks are accessible to the public.

`.ipynb` in [Visual Studio Code](https://code.visualstudio.com/) is used for ETL, EDA, and model training. 
The dataset used, along with the ML’s task presented require that the method used by the model is adequate for supervised learning on classification-based tasks. Following EDA, data over- and under-sampling is utilized but ultimately abandoned in favor of a cost-sensitive algorithm. Logistic regression and Support Vector Machines (SVM) are used. The dataset has an imbalance in diagnosis classification where a positive diabetes diagnosis only accounts for 2% of the dataset.

Logistic regression, like many other machine learning models, is designed and demonstrated on problems that assume equal distribution of classes. For this reason, logistic regression is used as a comparison against SVC, which can be updated to take the importance of the minority class into consideration when training.

Models are evaluated on their ROC AUC and precision-recall metrics. Following a `GridSearch` for tuning the algorithm, LinearSVC and SVC produced similar results and ultimately LinearSVC is chosen because of its faster processing time and ability to reduce the number of false negatives.

<a name="deep-learning"/></a>
## Deep Learning

Deep learning (DL) is used to predict when Type I diabetes patients have hazardous and dangerous blood glucose spikes (defined here as 180 mmol/L and 300 mmol/L, respectively) at before they happen. The tools used to form the DL models are `TensorFlow` and Google Colab.

[`TensorFlow`](https://www.tensorflow.org/) is the choosen libray for DL because it contains a wide breadth of tools for training all types of DL models quickly and simply; additionally, all major DL layer types are covered by the library. `.ipynb` in [Google Colab](https://colab.research.google.com/?utm_source=scs-index) is the primary training space for DL models primarily for its GPU-accelerated training capabilities and its built in environment for `TensorFlow`. Training DL networks with GPU capacities can reduce training time by around 85%, with much less memory and RAM demands. [[10]](https://datamadness.github.io/TensorFlow2-CPU-vs-GPU)

Given that this is a time series problem, recurrent neural network (RNN) layers are used. The two layers tested are long short-term memory (LSTM) and gated recurrent unit (GRU); RNN layers are not tested do their backpropagation and long-term memory issues. All models are created using `TensorFlow`'s `Sequential` model function, in which layers are created in sequence. [Two model frameworks](https://github.com/jackrlynn3/capstone-diabetes/blob/main/models/deep_learning/diabetes_DL_exploration.ipynb) were initially consistered: (1) predicting problematic peaks and their preceding upslopes; and (2) predicting blood glucose values a certain number of timesteps before. Ultimately, the latter model structure is chosen due its lower loss values and consistency.

![optimal_model drawio](https://user-images.githubusercontent.com/105175430/184986320-67554d5e-6e9e-48fc-a964-a503d54e258b.png)

*Structure of the optimal used for blood glucose level prediction, including diagrams for LSTM and GRU layers.*

Several different model parameter sets are tested, optimizing for [layer composition & layer depth](https://github.com/jackrlynn3/capstone-diabetes/blob/main/models/deep-learning/optimization/diabetes_DL_model_test.ipynb), [training size](https://github.com/jackrlynn3/capstone-diabetes/blob/main/models/deep_learning/optimization/diabetes_DL_training_test.ipynb), [window size](https://github.com/jackrlynn3/capstone-diabetes/blob/main/models/deep-learning/optimization/diabetes_DL_width_test.ipynb), and [time delay](https://github.com/jackrlynn3/capstone-diabetes/blob/main/models/deep-learning/optimization/diabetes_DL_delay_time_test.ipynb). The [best model](https://github.com/jackrlynn3/capstone-diabetes/blob/main/models/deep_learning/diabetes_DL_final_model.ipynb) is then trained and its parameters and structure are saved [here](https://github.com/jackrlynn3/capstone-diabetes/tree/main/models/deep_learning/saved-models/optimum_model); all other models are saved under [`/models/deep-learning/saved-models/`](https://github.com/jackrlynn3/capstone-diabetes/tree/main/models/deep-learning/saved-models). This parameter set can then be read later into our website for real time blood glucose spike predictions. A sample of what that would look like can be found [here](https://github.com/jackrlynn3/capstone-diabetes/blob/main/models/deep-learning/demo_dl.ipynb).

<a name="visualizations"/></a>
## Visualizations

The graphs and visualizations for the `Dash` environment are made using a mixture of Python methods. 

For the visualization of the Machine Learning model, [seaborne](https://seaborn.pydata.org/)--a Python data visualization library based on `matplotlib`--is utilized. It provides a high-level interface for drawing attractive and informative statistical graphics. `seaborne` is chosen as it integrates closely with [pandas](https://pandas.pydata.org/) data structures. For these images they are created inside Python and exported as `.png` files where the raw image is directly referenced by url. These images can be found [here](https://github.com/jackrlynn3/capstone-diabetes/tree/main/visualizations/deep-learning).

The images of the Deep Learning model were created inside of [Google Colab](https://colab.research.google.com/?utm_source=scs-index) using `matplotlib` directly and exported as `.png` files to Github where there raw image urls are directly referenced in the code. These images can be found [here](https://github.com/jackrlynn3/capstone-diabetes/tree/main/visualizations/machine-learning).

For the maps, bar graphs, and line graphs, [plotly express](https://plotly.com/python/plotly-express/) is utilized for its native integration with [`Dash`],(https://plotly.com/dash/) a product created by Plotly. A rough overview of `plotly` graphs and their implementation can be found [here](https://plotly.com/python/plotly-express/#gallery).

<a name="website-deployment"/></a>
## Dash Deployment

`Dash` deploymen utilizes a combination of Python code and bootstrapping components, as documented [here](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/).

For the Deployment of `Dash` the most helpful resource has been [Adam Schroeder](https://www.linkedin.com/in/adam-schroeder-17b5a819/), a Community Manager at Plotly. His YouTube channel [Charming Data](https://www.youtube.com/c/CharmingData) provides a large sum of tutorials on all things `Dash`. For a specific tutorial on Dash Bootstrap see [this video](https://www.youtube.com/watch?v=0mfIK8zxUds).

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

[10] DataMadness. (2019, October 27). Tensorflow 2 - CPU vs GPU performance comparison. DATAmadness. Retrieved August 14, 2022, from https://datamadness.github.io/TensorFlow2-CPU-vs-GPU 
