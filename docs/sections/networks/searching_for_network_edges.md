# Searching for Network Edges

## Finding edges to add to your network.

Searching for edges allows you to find edges that match your requirements (if they are available in the EdgeStore). You can find edges based on:

*  edge metadata created from the source Nanopub (  **Search Query**  )

*  by stepping out to neighboring nodes in the EdgeStore database from a set of given nodes (  **Network Neighborhood**  )

*  by providing two sets of network nodes and getting all of the shortest paths between them (  **Shortest Path**  )

NOTE: Searches are limited to 10000 edges per search type (search string, neighborhood search, or shortest path) so facet results are only based on the 10000 to 20000 max number of returned edges.

**NOTE2: The Search Query is an OR search with the neighborhood/shortest path search. These two query results will be combined together. There is currently no way to filter the shortest path or neighborhood search with the search query capabilities.**

NOTE3: If there is a space between words in a value, it must be surrounded by quotes. Smart quotes will break a search query.

###  Search Query

Search string searches are not general purpose queries. They currently have to be field-restricted searches as seen below in the Example search string components.

Example search string components (use  **AND**  ,  **OR**  , or  **AND NOT**  to join them):

*  relation:increases
*  relations:['increases', 'decreases']
*  citation:PMID:17511588
*  nanopub\_id:SELV\_117188
*  nanopub\_id:["SELV\_117188","SELV\_117189"]
*  collections:saliva
*  annotation\_type:Anatomy
*  annotation\_label:"skeletal muscle tissue"
*  annotation\_id:'UBERON:"female gonad"'
*  edge\_type:causal
*  edge\_types:["causal", "computed"]
*  collections:saliva  **AND**  (relation:biomarkerFor  **OR**  relation:decreases)
*  collections:saliva  **AND**  relation:["biomarkerFor","decreases"]
*  annotation\_label:saliva  **OR**  collections:test1
*  annotation\_label:"rheumatoid arthritis"  **AND**  edge\_type:original
*  annotation\_label:"rheumatoid arthritis"  **AND NOT**  edge\_type:computed
*  species_labels:human
*  species_ids:TAX:9606  
*  species:TAX:9606 
*  annotation_label:human

**NOTE: species_labels:human will return edges that contain human components (human edges), while annotaion_label:human will return the edges from nanopubs that are annotated as human, regardless of edge species.

![[networks_59.png]]

###  Network Neighborhood
  
Network neighborhood searches start with a given set of nodes and then expand out by the given number of steps.

You can also start with a subcomponent of the node if you check the  ***contains***  box.

For example: complex(p(HGNC:ITGAV), p(HGNC:ITGB5)) has the following components:

*  p(HGNC:ITGAV)
*  p(HGNC:ITGB5)

You can search for nodes containing p(HGNC:ITGB5) for example to get any nodes containing that protein.

You can also set the number of steps (1 - 5). However, more steps will cause the query to run for a longer time and may explode the number of edges returned.

![[networks_60.png]]

###  Shortest Path
  
Shortest path queries look for the shortest paths between two nodes. If you add nodes to the start and end nodes lists, it will find the shortest paths (and edges comprising those paths) between all of the nodes in the start nodeset versus the end nodeset.

![[networks_61.png]]

###  Edge Types

One of the search facets that can be used to filter the edges in your search is called edge\_types. The different edge types are listed below:

*   **primary**  - Assertion pulled directly from a nanopub (includes orthologized versions of nanopub assertions)

*   **original**  - Unorthologized assertion pulled straight from a nanopub.

*   **orthologized**  - edge created from either a primary or computed edge - orthologized to the species requested (partially orthologized edges are not allowed - all BEL entities that can be orthologized must be for the edge to be created

*   **computed**  - edge created from the assertion by list expansion. (either orthologized or primary) - e.g. hasActivity, hasComponent relationships

*   **causal**  - edge must be a causal edge - e.g. BEL causal relationships such as increases, decreases, etc

*   **backbones** - backbone or foundational edges, e.g. gene transcribedTo mRNA, mRNA translatedTo protein edges, etc. These are created from a separate collection of backbone nanopubs managed by the Studio Admins.

[[The BEL pipeline]]
