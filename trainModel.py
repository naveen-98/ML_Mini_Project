import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('ps5_game_rating_predictor.pkl')

# Example new data with sample values
new_data = {
    'url': ['https://store.playstation.com/en-us/product/UP0101-PPSA19225_00-0159266583099383'],
    'id': ['1'],
    'publisherName': ['Konami Digital Entertainment, Inc.'],  # Sample publisher
    'releaseDate': ['2024-07-20'],  # Sample release date
    'name': ['Sample Game'],  # Sample game name
    'isAgeRestricted': [False],  # Sample age restriction
    'activeCtaId': ['cta1'],  # Sample activeCtaId
    'starRating/totalRatingsCount': [50]  # Sample total ratings count
}

# Convert new data to DataFrame
new_df = pd.DataFrame(new_data)

# Drop non-numeric columns that were not used in training
non_numeric_cols = ['url', 'id', 'publisherName', 'name', 'releaseDate', 'activeCtaId']
new_df.drop(columns=non_numeric_cols, inplace=True)

# Ensure the correct dtype for isAgeRestricted
new_df['isAgeRestricted'] = new_df['isAgeRestricted'].astype(int)  # Convert boolean to int

# Manually specify the features used during training
# Ensure this list matches exactly the features used during training
training_features = [
    'isAgeRestricted'
]

# Ensure new_df has the same columns as used during training
new_df = new_df[training_features]

# Make prediction
prediction = model.predict(new_df)

# Print the prediction
print(f'Predicted Average Rating: {prediction[0]}')
