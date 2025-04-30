"""
This is a collection of useful functions
to be used for graph analysis
"""

import pprint as pprint
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


### Basic properties of a graph

# MultiGraph: Undirected graphs with self loops and parallel edges
# https://networkx.org/documentation/stable/reference/classes/index.html

def basic_properties(G):

    pprint.pprint({'is_multigraph':G.is_multigraph(), 
        'is_directed':G.is_directed(), 
        'number_of_nodes': G.number_of_nodes(), 
        'number_of_edges':G.number_of_edges(),
         '------' : '------',
        'is connected': nx.is_connected(nx.to_undirected(G)), 
        'components': len(list(nx.connected_components(nx.to_undirected(G)))),
        'density': nx.density(G)}, sort_dicts=False)



### Remove the attributes listed in a Python list from all nodes

# attrs_to_remove : the list of attribute names

def remove_node_attributes(G, attrs_to_remove):
    for node in G.nodes():
        for attr in attrs_to_remove:
            if attr in G.nodes[node]:
                del G.nodes[node][attr]



###  Describe and plot distribution of integers' list

def describe_plot_integers_distribution(il, width, heigth):

    sl_id = pd.Series(il)
    print(sl_id.describe())

    ## Distribution of the indegree
    df_l = pd.DataFrame(sl_id.groupby(by=sl_id).size().items())
    df_l.columns=['value', 'number']

    fig, ax = plt.subplots(1,1, figsize=(width,heigth))

    plt.bar(df_l.value, df_l.number)

    ax.yaxis.get_major_locator().set_params(integer=True)
    ax.bar_label(ax.containers[-1])
    plt.xticks(size=8)
    plt.xlabel('Indegree', size=9)
    plt.yticks(size=8)
    plt.ylabel('Number of nodes', size=9)
    plt.title('Indegree Distribution', size=10)

    plt.show()           