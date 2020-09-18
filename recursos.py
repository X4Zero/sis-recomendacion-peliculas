import pandas as pd
import numpy as np
import os
from ast import literal_eval

# Import CountVectorizer and create the count matrix
from sklearn.feature_extraction.text import CountVectorizer
# Compute the Cosine Similarity matrix based on the count_matrix
from sklearn.metrics.pairwise import cosine_similarity

def ObtenerPeliculaCoincidencia(titulo,df):
  titulo=titulo.lower()
  slice_df = df[df['title'].str.lower().str.contains(titulo)]['title']
  return slice_df

def ObtenerRecomendacion(idx,df,cosine_sim,movie_indices):
  # Get the pairwsie similarity scores of all movies with that movie
  sim_scores = list(enumerate(cosine_sim[idx]))

  # Sort the movies based on the similarity scores
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

  # Get the scores of the 10 most similar movies
  sim_scores = sim_scores[1:11]

  # Get the movie indices
  movie_indices = [i[0] for i in sim_scores]

  # Return the top 10 most similar movies
  return df['title'].iloc[movie_indices]


def cargar_variables():
    ruta_base = os.getcwd()
    metadata_prod_final = pd.read_csv(os.path.join(ruta_base,'metadata_prod_final.csv'))
    # print(metadata_prod_final.head())
    # print(metadata_prod_final.shape)

    metadata_subset = metadata_prod_final[:7000]

    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(metadata_subset['soup'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    metadata_subset = metadata_subset.reset_index(drop=True)
    indices = pd.Series(metadata_subset.index, index=metadata_subset['title'])

    print("Tamaño que ocupa cosine_sim: {} MB".format(cosine_sim.nbytes/1024/1024))

    return metadata_subset, indices, cosine_sim
