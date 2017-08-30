mkdir source

# IANA
wget "https://raw.githubusercontent.com/datasets/media-types/master/media-types.csv" -O source/media-types.csv

# ISO 4217
wget "https://raw.githubusercontent.com/datasets/currency-codes/master/data/codes-all.csv" -O source/currencies.csv

# ISO 3166
wget "https://raw.githubusercontent.com/datasets/country-codes/master/data/country-codes.csv" -O source/countries.csv

# ISO 639-1
wget "https://raw.githubusercontent.com/datasets/language-codes/master/data/language-codes-full.csv" -O source/languages.csv

# DAC CRS
wget "https://raw.githubusercontent.com/datasets/dac-crs-codes/master/data/aid_types.csv" -O source/aid_types.csv
wget "https://raw.githubusercontent.com/datasets/dac-crs-codes/master/data/aid_type_categories.csv" -O source/aid_type_categories.csv
wget "https://raw.githubusercontent.com/datasets/dac-crs-codes/master/data/collaboration_types.csv" -O source/collaboration_types.csv
wget "https://raw.githubusercontent.com/datasets/dac-crs-codes/master/data/channel_codes.csv" -O source/channel_codes.csv
wget "https://raw.githubusercontent.com/datasets/dac-crs-codes/master/data/finance_types.csv" -O source/finance_types.csv
wget "https://raw.githubusercontent.com/datasets/dac-crs-codes/master/data/finance_type_categories.csv" -O source/finance_type_categories.csv
wget "https://raw.githubusercontent.com/datasets/dac-crs-codes/master/data/flow_types.csv" -O source/flow_types.csv
wget "https://raw.githubusercontent.com/datasets/dac-crs-codes/master/data/recipients.csv" -O source/recipients.csv
wget "https://raw.githubusercontent.com/datasets/dac-crs-codes/master/data/sectors.csv" -O source/sectors.csv
wget "https://raw.githubusercontent.com/datasets/dac-crs-codes/master/data/sector_categories.csv" -O source/sector_categories.csv
