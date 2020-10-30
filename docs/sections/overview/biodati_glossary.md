# BioDati Glossary

**BEL**
[Biological Expression Language](http://bel.bio)  this is an open-standard language for capturing biological knowledge in a share-able and computable format. It allows you to state molecular to macro-level relationships - everything from cell signaling to population-level relationships.
**Nanopub**  Short for  Nanopublication, it is defined as the smallest unit of BEL publishable information. It is comprised of Assertions,
Annotations, Citation and Metadata.
(For more information, check out  [http://nanopub.org](http://nanopub.org/)  - we follow the principles stated by the Nanopub Organization, but we have taken liberties with the data structure using a JSON format defined by a  [JSONSchema](https://github.com/belbio/schemas/blob/master/schemas/nanopub_bel-1.0.0.yaml)  definition)
**Edge**  An edge consists of a subject, a relationship and an object created from BEL assertions that are accessible for building networks or running analytics.
**Node**
The point at which the edges intersect or branch.
**Network**
A subset of the BEL Edges in the EdgeStore that are selected for connectivity and environmental context, e.g. BEL Edges connected to p(HGNC:EGFR) for lung cancer in humans.
**Namespace**
A terminology used to unambiguously identify a gene/protein, biological process, pathology, cell line, etc. The terms in BEL Namespace have a namespace prefix such as  **HGNC**  for Human Gene Nomenclature Committee human gene symbols or GO for Gene Ontology. The Namespace definition may contain equivalents to other namespaces; it may also contain hierarchical structure such as an Anatomy namespace or the Gene Ontology.
**Annotations**
Annotations capture the context of the Assertions such as the experimental context, what organism, disease state, experimental method, etc.  **Assertion**  The key assertion(s) being made in a BEL Nanopub. It is an expression that represents knowledge of the existence of biological entities and relationships between them that are known to be observed within a particular experiment context (i.e. Annotations), based on some source of prior knowledge such as a scientific publication or newly generated experimental data.
**Pinned**  An easily accessible area to store your NanoPubs and Networks for later use.
**Facets**  An area you will find on the left hand side of the screen used to filter for optimum search results. Facets provide summarized search results to help filter the search results.
**EdgeStore**
A database for storing Edges which are searchable via Studio. It is a graph database which allows for network neighborhood and shortest path queries between nodes as well as edge attributes.
