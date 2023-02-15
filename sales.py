import pandas

# My algorithm is to calculate Euclidean distance (vectorized)
# then use Panda's methods to find the smallest
# then filter the input

# The calculation of Euclidean distance should be pretty fast
# the operations are element-wise and so highly parallelizable
# in particular the subtraction, addition, and exponentiation
# should be "constant" time wrt the length of the data frame
# assuming that the operations can be computed in parallel

# Next is finding the elements with the shortest distance
# I believe `nsmallest` to have a complexity bounded by O(n*m)
# where n is the number of closest properties to find
# and m is the number of rows in the data frame
#
# Furthermore, turning the series into a hashset
# should be linear in m

# Finally we have to filter the data frame by `lowest`
# I think this is bounded by O(m) because the function:
# loops over each row, and performs a constant-time
# inclusion check on the set

def find_closest_sales(n: int, sales_df: pandas.DataFrame, lat: int, long: int) -> pandas.DataFrame:
  # Euclidean distance
  sales_df["dist"] = (sales_df["lat"] - lat)**2 + (sales_df["long"] - long)**2

  # Get the n closest
  lowest = sales_df.nsmallest(n, "dist")

  # Hashset for more efficient lookup
  lowest = set(lowest["id"])

  # Filter, output won't be ordered
  return sales_df.loc[sales_df["id"].isin(lowest)]

# load data
df = pandas.read_csv("sales.csv")

# sample population
population = df.sample(n=100)

# remove sampled points from the sales
df = pandas.concat([df, population]).drop_duplicates(keep=False)

# select 3 to test
for _, property in population.sample(n=3).iterrows():
  print(f"Finding properties closest to id [{property['id']}]")

  closest = find_closest_sales(10, df, property["lat"], property["long"])
  print(closest, "\n")
