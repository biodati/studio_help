# Creating an Orthologized Network

To create an orthologized network you first start by selecting the set of nanopubs you'd like work from (e.g. metadata:project=x or network neighborhood of p(HGNC:AKT1)).
You can then select the Edge Species that you’d like to work with.  *NOTE: This is not the species listed in the nanopub annotations- it is the species associated with the edge.*

![[networks_62.png]]

After selecting the species, you can then look at the edge types and note that some edges are from other species (e.g. orthologized) and some are originally from the selected species (mouse in this case).

![[networks_63.png]]

##  Background
Below is a diagram depicting the generation of (orthologized) edges from Nanopub Assertions.

![[networks_64.jpeg]]

For more information, see [[The BEL pipeline]].

