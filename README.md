# ML_Mini_Project
Enhancing User Experience in PS5 Gaming Through Predictive Analysis

Problem: -

Optimizing the user enjoy in gaming systems is critical for each game enthusiasts and publishers. Leveraging the PS5 Games Dataset: 2024 Update from Kaggle, the venture is to pick out and expect elements that make contributions to a sport's achievement and person pride. The aim is to increase a model that may forecast a game's recognition, taking into account diverse capabilities together with release date, publisher, age restrictions, and user scores.

<h1>Full Video For Mini project</h1>

https://github.com/naveen-98/ML_Mini_Project/assets/55675843/34239dd8-ad04-46dd-a0f0-112dda9ecfdf



<h2>Data Preparation and Analysis</h2>

1. Loading and Inspecting the Dataset
The first step involves loading the dataset and performing an initial inspection to understand its structure and contents:

![1](https://github.com/naveen-98/ML_Mini_Project/assets/55675843/6a666b06-c628-4904-9cbb-f7266abb247c)

•	Displaying the first few rows and summary statistics: This helps understand the dataset's features and data types, providing an initial overview of the data.
•	Checking for missing values: This ensures the dataset is complete and ready for analysis. Missing values can impact the model's performance and need to be addressed.

2. Handling Missing Values and Duplicates
To ensure data quality, missing values, and duplicates are addressed:

![2](https://github.com/naveen-98/ML_Mini_Project/assets/55675843/6cdb5ce5-c543-42fa-b688-e740e3a0c49d)


• Dropping or filling lacking values: This keeps the integrity of the dataset via ensuring that no incomplete records is used in the evaluation.
•	Removing duplicates: This prevents any redundant information from skewing the analysis.

3. Converting Data Types and Feature Engineering
   
The release date column is converted to a Date Time format, and additional features such as the release year and month are extracted:

![3](https://github.com/naveen-98/ML_Mini_Project/assets/55675843/f24d3bae-c8c9-41ef-9245-56e94d9003a8)

•	Converting releaseDate to datetime: Ensures the date values are in the correct format for analysis.
•	Extracting year and month: Provides additional temporal features that can be useful in understanding trends and patterns over time.

<h2>Data Visualization</h2>

1. User Ratings Over the Years and Distribution of User Ratings by Release Month
A line plot visualizes user scores over time to perceive developments:

![4](https://github.com/naveen-98/ML_Mini_Project/assets/55675843/14464f4e-2310-4d1a-8f57-88de3a979451)

• User Ratings Over the Years: This visualization enables tune changes in user scores over the years, offering insights into how sport rankings have developed.
•	Distribution of User Ratings by Release Month: This analysis exhibits the impact of release timing on consumer delight, assisting to become aware of capacity seasonality consequences.

2. Top Publishers by Average Rating
Identifying top publishers by average rating provides insights into industry leaders:

![5](https://github.com/naveen-98/ML_Mini_Project/assets/55675843/c27e50b6-8418-4277-8ebc-9d990bfff24f)

• Top Publishers with the aid of Average Rating: This highlights publishers who always produce highly-rated video games, guiding strategic decisions for game improvement and publishing.

<h2>Machine Learning Prediction</h2>

1. Loading the Pre-Trained Model
The pre-trained machine learning model is loaded to make predictions:

![6](https://github.com/naveen-98/ML_Mini_Project/assets/55675843/61f3d64b-cea6-418e-a686-6da8215e32ba)

2. Preparing New Data for Prediction
New data is prepared by dropping irrelevant columns and ensuring correct data types:

![7](https://github.com/naveen-98/ML_Mini_Project/assets/55675843/0fc6db67-134f-4b74-b019-ff5dbee73589)

• Preparing New Data: This entails formatting the new recreation records to in shape the structure of the training statistics, ensuring that the version can method it effectively.

3. Making Predictions
The model is used to predict the average rating for the new game:

![8](https://github.com/naveen-98/ML_Mini_Project/assets/55675843/e9bdcf38-0a78-437b-b2d3-0afb207266ab)

Making Predictions: The version makes use of the organized statistics to forecast the game's common score, imparting an estimate of its capability success.



