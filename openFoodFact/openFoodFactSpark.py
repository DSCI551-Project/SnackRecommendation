import pyspark

#Data Cleaning for OpenFoodFact

spark = pyspark.sql.session.SparkSession.builder.appName("openFoodFact").getOrCreate()
openFoodFact = spark.read.csv('en.openfoodfacts.org.products.tsv')

#drop if missing value more than 30%
food_cleaned = openFoodFact.na.drop(thresh=106800) 

#group the data by country to check 
grouped = food_cleaned.select(food_cleaned.countries_en, food_cleaned.product_name).groupby(food_cleaned.countries_en).count(food_cleaned.product_name)
# grouped.show()

#only keep food in United States
food_cleaned = food_cleaned[food_cleaned.countries_en == "United States" ]
#drop less common attributes
food_cleaned = food_cleaned.na.drop(subset = ['code', 'creator', 'created_t', 'created_datetime',
       'last_modified_t', 'last_modified_datetime', 'quantity', 'brands_tags', 'countries', 'countries_tags', 'additives_n', 'additives',
       'additives_tags', 'additives_en', 'ingredients_from_palm_oil_n', 'nutrition_grade_fr',
       'ingredients_that_may_be_from_palm_oil_n',
       'pnns_groups_1', 'pnns_groups_2', 'states', 'states_tags', 'states_en', 'saturated-fat_100g', 'trans-fat_100g',
       'cholesterol_100g', 'sodium_100g', 'vitamin-a_100g', 'calcium_100g', 'iron_100g', 'nutrition-score-fr_100g'])
#drop products with missing values in the selected columns 
food_cleaned = food_cleaned.na.drop(thresh = 15)

food_cleaned.show()