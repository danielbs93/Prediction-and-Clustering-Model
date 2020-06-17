from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import pyplot as plt
import resource
import os
import plotly.express as px
from scipy.spatial import distance


class DataClustering:
    data_frame = ""
    number_of_runs = 5  # Default
    number_of_k_clusters = 3  # Default

    def __init__(self, df, n_init, n_clusters):
        self.data_frame = df
        self.number_of_runs = n_init
        self.number_of_k_clusters = n_clusters

    # =================================================

    def runClustering(self):
        df_values = self.data_frame.values
        X = df_values[:, 1:].astype(float)

        # ===================== K-Means Uses ======================================

        kmeans = KMeans (n_clusters=self.number_of_k_clusters, init='k-means++', max_iter=300, n_init=self.number_of_runs, random_state=0)
        kmeans.fit(X)
        y_kmeans = kmeans.predict(X)
        self.data_frame['Cluster'] = y_kmeans

        # ================== Creating dictionary for each cluster-classification with their matched centroid ============================

        # label_center_dict = {i: kmeans.cluster_centers_[i] for i in range(kmeans.n_clusters)}
        # cluster_centroids = list()
        # for i in self.data_frame['Cluster']:
        #     cluster_centroids.append(label_center_dict.get(self.data_frame['Cluster'][i]))

        # ================= Inserting Cluster Centroids column to data ==========================================================
        # self.data_frame['Cluster Centroids'] = cluster_centroids

        # ========= Creating distance between each tuple to its matching cluster_centroid =======
        # centroids_vector = pd.DataFrame(cluster_centroids).values
        # distance_centroid_to_tuple = list()
        # for i in range(0, len(X)):
        #     distance_centroid_to_tuple.append(distance.euclidean(X[i], centroids_vector[i]))
        #
        # self.data_frame['Distance centroids-tuple'] = distance_centroid_to_tuple

        # ================= Creating iso alpha 3 countries code ==================================================
        # importing all countries and thier shortcuts represented as ISO-alpha-3 for choropleth map

        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
        all_countries = pd.DataFrame(df)
        iso_alpha_3 = {k: v for k, v in zip(all_countries.values[:, 0], all_countries.values[:, 2])}
        countries_code_list = list()

        for i in range(0, len(self.data_frame)):
            countries_code_list.append(iso_alpha_3.get(self.data_frame['country'][i]))

        # ========== Adding column of country code to data frame ================================
        self.data_frame['Country Code'] = countries_code_list

        # ============ Writing data to xlsx file for testing ====================================
        # out_path_clustered = os.path.join(resource.__path__[0], "dataAfterClustering.xlsx")
        # with pd.ExcelWriter(out_path_clustered) as writer:
        #     self.data_frame.to_excel(writer, sheet_name='Sheet1')

        # ======================== Scatter Graph: Generosity as function of Social Support ====================================

        plt.scatter(X[:, 2], X[:, 5], c=y_kmeans, s=30)
        plt.scatter(kmeans.cluster_centers_[:, 4],
                    kmeans.cluster_centers_[:, 7],
                    s=80,
                    c='black',
                    alpha=0.5)
        plt.title('K-Means Clustering for Generosity as function of Social Support')
        plt.xlabel('Social Support')
        plt.ylabel('Generosity')
        # plt.show()
        # if os.path.exists("../resource/scatter.png"):
        #     os.remove("../resource/scatter.png")
        plt.savefig("../resource/scatter.png", dpi=100)

        # ====================== Choropleth Map ============================

        fig = px.choropleth(self.data_frame, locations="Country Code",
                            color="Cluster",
                            hover_name="country",
                            color_continuous_scale=px.colors.sequential.Plasma)

        fig.update_layout(
            title_text='K-Means Clustering Visualization',
        )
        # fig.show()
        # import plotly.plotly as py
        # py.sign_in("erantout", "TdZKHT7nCXU2om6Z6GTy")
        # py.image.save_as(fig, filename='choroplethMap.png')