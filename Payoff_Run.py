import pandas as pd
import Payoff_Draft


# Load the Excel file into a DataFrame
file_path = 'Payoff_Pricing.xlsx'
all_parameters = pd.read_excel(file_path, sheet_name='Main_Sheet')

# Extract generic parameters from the first two rows
num_simulation = int(all_parameters[all_parameters['Parameter'] == 'No. of Simulations']['Value'].values[0])
num_assets = int(all_parameters[all_parameters['Parameter'] == 'No. of Assets']['Value'].values[0])

# Initialize a list to store results
results = []

# Initialize a dictionary to store each asset's parameters and values
asset_details = {}

# Start processing after the first two columns (Parameters and Values)
# Asset details start from column index 2 (3rd column in Excel)
for asset_num in range(1, num_assets + 1):
    # Calculate the parameter and value column indices for each asset
    param_col_index = 2 + (asset_num - 1) * 2  # 3rd, 5th, 7th, etc.
    value_col_index = 3 + (asset_num - 1) * 2  # 4th, 6th, 8th, etc.

    # Get the column names based on these indices
    param_col = all_parameters.columns[param_col_index]
    value_col = all_parameters.columns[value_col_index]

    # Initialize a dictionary to hold this asset's parameter-value pairs
    asset_info = {}

    # Loop through the DataFrame rows to extract parameters and values for this asset
    for index, row in all_parameters.iterrows():
        parameter = row[param_col]  # Get parameter from param_col
        value = row[value_col]  # Get corresponding value from value_col

        # Only add the parameter if it has a valid (non-null) value
        if pd.notnull(parameter) and pd.notnull(value):
            asset_info[parameter] = value

    # Store the asset info in the main asset_details dictionary
    asset_details[f'Asset_{asset_num}'] = asset_info
    # Create a Payoff object using the entire asset_info dictionary
    payoff = Payoff_Draft.Payoff(asset_info,num_simulation)  # pass the dictionary

    # Calculate the price for the asset
    price = payoff.price()

    # Append results to the list
    results.append({
        'Asset': f'Asset_{asset_num}',
        'Price': price,
    })

# Convert results to a DataFrame
results_df = pd.DataFrame(results)

# Save results to a CSV file
results_df.to_csv('asset_prices.csv', index=False)

print("Asset pricing results saved to 'asset_prices.csv'.")


