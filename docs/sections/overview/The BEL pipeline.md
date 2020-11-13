# The BEL pipeline- The Edge Report and Edge Types

When a nanopub nanopub is processed through the BEL pipeline, the assertions become edges in the Edge Store.
There are more edges created that there are assertions in the nanopub.  The Edge Report shows you all the edges created from that nanopub in the Edge store.  

The Edge Report can be accessed by clicking the hover icon that appears above any nanopub on the Knowledge Search page, when your cursor hovers over a nanopub in the nanopub list.  

![[edges1.jpg]]

Below is an example Edge Report.

![[edges2.jpg]]

Each assertion is canonicalized during processing. BEL requires the use of a namespace and identifier for every object.  This allows us to find object equivalences in multiple namespaces, so we can combine information from divergent sources. 

The BEL pipeline adds **Orthologized Edges**- equivalent edges in different species- usually mouse, rat, or human.  In the example above, *this adds two new edges*.

**Computed Edges** are computer generated edges added to aid Network building.  They include hasMember, hasComponent, hasActivity, hasModification, hasFragment, hasLocation, equivalentTo, hasReactant and hasProduct relationships. They are also orthologized, in this case, hasActivityedges are added, generating *three new edges*, for a total of six edges from this one assertion.  

**Backbone Edges**, translatedTo and transcribedTo edges, are computer generated edges available in the Edge Store to aid Network building.  They are not associated with specific nanopubs.

## Special Edges

BEL allows **Subject Only** assertions.  These are simple statements that an entity exists.  The pipeline translates these assertions into original edges with “null” relationships.

BEL also allows for **Nested Assertions**, where the object of the assertion is itself an assertion. If all parts of the Nested Assertion are causal, the computer will use logic to generate additional original causal edges.  Correlation is not causation, so correlative relationships will not generate additional edges.

For example, the assertion: a(A) increases (a(B) decreases a(C))

Will produce the following original edges:

     a(A) increases (a(B) decreases a(C))
     
     a(A) increases a(B)
     
     a(A) decreases a(C)

