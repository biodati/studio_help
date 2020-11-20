# BEL Namespaces

We use standardized namespaces so that we can identify an object unambiguously. This allows us to identify the same object in different namespaces, identify orthologs, and check for consistency in BEL statements.

E.g. BEL Assertion: a(CHEMBL:water)

1.  CHEMBL:water is a chemical compound and is valid to have in a() function

2.  CHEMBL:water is canonicalized to CHEBI:water so that we only have one edge for a(CHEMBL:water) and a(CHEBI:water)

3.  Queries against the edgestore would then include a search for CHEMBL:water converted to CHEBI:water

E.g. The human g(HGNC:ACE2) is orthologous to mouse g(MGI:Ace2).

E.g. In this example of metabolomics data, there are contradictory BEL statements:

![[knowledge_12.png]]

   When we click on the Nanopub URL(s) and Review the nanopubs, we learn that the first Assertion is derived from saliva samples.

![[knowledge_13.png]]

   The second Assertion is from the same paper, but the metabolites are derived from tissue samples. Both Assertions are valid, but which Assertion is relevant is determined by the biological context.

![[knowledge_14.png]]

## Some useful Namespace databases: This list is *not* all inclusive. ##

GO <http://geneontology.org/>

MGI <http://www.informatics.jax.org/mgihome/GO/querying.shtml>

MESH <https://www.ncbi.nlm.nih.gov/mesh>

CHEBI <https://www.ebi.ac.uk/chebi/advancedSearchFT.do>

CHEMBL <https://www.ebi.ac.uk/chembl/>

HGNC <https://www.genenames.org/tools/search/#!/genes?query=>

DO <https://disease-ontology.org/>

TAX <https://www.ncbi.nlm.nih.gov/taxonomy>

UBERON <https://www.ebi.ac.uk/ols/ontologies/uberon>

CL	<https://bioportal.bioontology.org/ontologies/CL>

CLO <http://www.clo-ontology.org/>

[[Custom Namespaces Terminologies]]
