# Creating Networks and Adding Edges

You can open Network Creation from the dashboard or from the creation drop-down in the banner.

![[networks_0.png]]

   The landing page for Network creation will allow you to search for edges to create a new network or extend an existing one. There are three types of searches available to find edges under Network creation.
   
1) Query search

2) Nearest Neighbor search

3) Shortest Path search

![[networks_1.png]]

 **Query Search**
 
A query search is a  **field restricted**  search. General search terms will not work. Search fields include relations, citations, collections, annotations, and edge types. Queries can be joined using: AND, OR, or AND NOT.
Examples:

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

*  collections:saliva AND (relation:biomarkerFor OR relation:decreases)

*  collections:saliva AND relation:["biomarkerFor","decreases"]

*  annotation\_label:saliva OR collections:saliva

*  annotation\_label:"rheumatoid arthritis" AND edge\_type:original

*  annotation\_label:"rheumatoid arthritis" AND NOT edge\_type:computed


**Nearest Neighbor Search**

A Nearest Neighbor search starts from a Node or list of Nodes.

![[networks_2.png]]

   Once you have entered your start nodes, you have several choices to make.
   
a) Number of steps out from your start Node. The larger the number of steps, the larger the network you will return.

b) The direction of those steps. Outbound steps use the Start Node as Subject of an assertion. Inbound steps use the Start Node as the Object of an Assertion.

c) Contains. If the contains box is checked, the start node is expanded to include all the nodes with the identified entity. In the example above, the start node would include p(HGNC:CDK9), and all other nodes that contain p(HGNC:CDK9); deg(p(HGNC:CDK9)), act(p(HGNC:CDK9), ma(kin)), and p(HGNC:CDK9) containing complexes. If the contains box is not checked, p(HGNC:CDK9) would be the only start node.


**Shortest Path Search**

The shortest path search is designed to allow you to find the shortest path (and edges comprising those paths), between nodes. You must enter both the start node(s) and end node(s). If you enter multiple start or end nodes, it will find the shortest paths between all the start and end nodes. If the nodes are too many steps distant from one another, the search may time out and return no results.

![[networks_3.png]]

   Once you enter your search, click SUBMIT to return your edges. Search results may be filtered using ***FACETS***, or the filter function to the right of the Subject, Relation, and Object columns.

![[networks_4.png]]

   Select Edges individually by clicking the adjacent box, or click the whole filtered list by clicking the box at the top left next to the column heading. 
   
   Once your edges have been selected, create Network, add to Active Network, and Add to Active Project options will be enabled.

Click create Network and follow the prompts to create your first Network.  

**If an existing Network is active, you can add new edges to that Network by following the steps above, and clicking add to Network, instead of Create, after your edges have been selected.**
