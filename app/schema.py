# Scenario 3 - Movies dataset
# Simple Python code with short comments

import pandas as pd
import matplotlib.pyplot as plt

# load dataset
movies = pd.read_csv("imdb_top_1000.csv")

# show first rows
print(movies.head())

# show columns
print(movies.columns)

# check info
print(movies.info())

# check missing values
print(movies.isnull().sum())

# clean runtime column
movies['Runtime'] = movies['Runtime'].str.replace(" min", "")
movies['Runtime'] = pd.to_numeric(movies['Runtime'], errors='coerce')

# average runtime
print(movies['Runtime'].mean())

# average rating by genre
print(movies.groupby("Genre")["IMDB_Rating"].mean())

# average rating by certificate
print(movies.groupby("Certificate")["IMDB_Rating"].mean())

# average rating by director
print(movies.groupby("Director")["IMDB_Rating"].mean().sort_values(ascending=False).head())

# average rating by star
print(movies.groupby("Star1")["IMDB_Rating"].mean().sort_values(ascending=False).head())

# plot ratings by genre
movies.groupby("Genre")["IMDB_Rating"].mean().plot(kind="bar")
plt.title("Average Rating by Genre")
plt.show()

# plot runtime distribution
movies['Runtime'].plot(kind="hist", bins=20)
plt.title("Movie Runtimes")
plt.show()

# plot rating distribution
movies['IMDB_Rating'].plot(kind="hist", bins=20)
plt.title("IMDB Ratings")
plt.show()

# runtime vs rating correlation
print(movies['Runtime'].corr(movies['IMDB_Rating']))

# scatter plot runtime vs rating
movies.plot(kind="scatter", x="Runtime", y="IMDB_Rating")
plt.title("Runtime vs Rating")
plt.show()

# average rating by year
print(movies.groupby("Released_Year")["IMDB_Rating"].mean().head())

# plot ratings by year
movies.groupby("Released_Year")["IMDB_Rating"].mean().plot(kind="line")
plt.title("Average Rating by Year")
plt.show()

# top stars
top_stars = movies.groupby("Star1")["IMDB_Rating"].mean().sort_values(ascending=False).head(10)
top_stars.plot(kind="bar")
plt.title("Top Stars by Rating")
plt.show()

# top directors
top_directors = movies.groupby("Director")["IMDB_Rating"].mean().sort_values(ascending=False).head(10)
top_directors.plot(kind="bar")
plt.title("Top Directors by Rating")
plt.show()

# reflection in code
# data shows patterns but movies are more than numbers
# ratings are opinions, creativity matters too

# keep exploring more columns
print(movies['Genre'].unique())
print(movies['Certificate'].unique())
print(movies['Released_Year'].unique())

# group by genre and year
print(movies.groupby(["Genre","Released_Year"])["IMDB_Rating"].mean().head())

# plot genre vs year ratings
movies.groupby(["Released_Year","Genre"])["IMDB_Rating"].mean().unstack().plot()
plt.title("Ratings by Year and Genre")
plt.show()

# check longest movies
print(movies.sort_values("Runtime", ascending=False).head())

# check shortest movies
print(movies.sort_values("Runtime", ascending=True).head())

# check highest rated movies
print(movies.sort_values("IMDB_Rating", ascending=False).head())

# check lowest rated movies
print(movies.sort_values("IMDB_Rating", ascending=True).head())

# plot runtime vs year
movies.plot(kind="scatter", x="Released_Year", y="Runtime")
plt.title("Runtime vs Year")
plt.show()

# plot rating vs year
movies.plot(kind="scatter", x="Released_Year", y="IMDB_Rating")
plt.title("Rating vs Year")
plt.show()

# reflection
# looking at this makes me think about how movies change over time
# some years have strong stories, some years weaker
# data helps but human creativity is always important