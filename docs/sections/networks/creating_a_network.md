# Creating a Network

Starting at the dashboard, click on the '+' in the 'Networks' box.

![[networks_51.png]]

   Start a search by adding in the #1 node query field (e.g. HGNC:AKT1), #2 selecting how many steps away from that node is allowed, #3 which direction and #4 if it is a 'Contains' query or not. After submitting your query (#5), #6 search facets will allow you to further refine your edge search results.

![[networks_52.png]]

**Node query field:**  allows a BEL subject or object or a sub-component of a BEL subject or object down to a Namespace:Value (Contains query only). For example, you can enter p(HGNC:AKT1) or HGNC:AKT1.

**Neighbor:**  How many steps out are allowed from the starting node. A->B is one step, A->B->C is two steps, ...

**Direction:**  Is the starting node allowed to be a subject or object or either? OUTBOUND = subject, INBOUND = object, ANY = either

**Contains:**  Does the query node have to be a full BEL subject or object match or can it match on a contained sub-component of the BEL subject or object? A non-Contains query has to be a full node match AND a valid BEL subject or object. A Contains node query can also be just the Namespace:Value, e.g. HGNC:AKT1.

## FACETS 
(In the left column) allow you to filter you search results.

###  Edge Types

**Primary:**  Assertion pulled directly from Nanopub (includes orthologized versions of Nanopub assertions)

**Computed:**  An edge computed from the Nanopub Assertions, e.g. a BEL Subject or Object of act(p(HGNC:AKT1)) results in a computed edge of p(HGNC:AKT1) hasActivity act(p(HGNC:AKT1))

**Causal:**  An edge that represents a BEL Causal edge (increases, decreases, etc)

**Backbone:**  An edge created from backbone or scaffolding knowledge such as g(HGNC:AKT1) transcribedTo r(HGNC:AKT1).

**Orthologized:**  edge created from either a primary or computed edge - orthologized to the species requested (partially orthologized edges are not allowed - all BEL entities that can be orthologized must be for the edge to be created

**Original**  - Unorthologized assertion pulled straight from Nanopub - will be decanonicalized (e.g. use preferred namespaces from the pipeline configuration such as HGNC for human proteins if available)

![[networks_53.jpeg]]

  ##  Selecting edges to create a network
After filtering the edges using the facets, you can then select all remaining edges or select individual edges to create the network.

![[networks_54.png]]

   #1 Selected facets to filter set of edges. You can 'Clear All' facets to reset the filtering and you can also quickly see how many facets have been selected #2. After checking off each edge or selecting all of the remaining edges using the checkbox next to #3 'Subject', you will then be able to click #4 'Create.'

![[networks_55.png]]

  ##  Now add the network name and description and a version number if desired. Then click the Next button.

![[networks_56.png]]

   You do have the option of deleting nodes or edges. #1, click on the side panel of the Network landing page, where it reads 'Edges,' followed by #2 where you will select which edge you'd like to delete, and then finalize by #3 choosing 'Delete Selected Edges.' If you wanted to delete a node, you should follow the same steps except selecting 'Nodes' instead.

![[networks_57.png]]

   After saving it, you can find it by clicking on the search icon #1 and then 'Networks'. To quickly filter to your networks, click the 'Me' checkbox #2 and then you should see your new network #3. Once your networks start building up, you can utilize the facets to narrow down the networks that you've created.
When re-opening a network that you created, you'll notice on the side it says "Add Edges" and "Edit." As the creator of that network, you are the only ones with those options.

![[networks_58.png]]
    
[Extending A Network](https://help.biodati.com/networks/creating-and-editing-networks/extending-a-network)
