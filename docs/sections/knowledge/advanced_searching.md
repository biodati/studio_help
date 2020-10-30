# Advanced Searching

Advanced searches take advantage of field labels to search only BEL subjects for example. You can use wildcards as well as regular expressions in your search requests.
Go to Nanopub Search by clicking on either button:

![[knowledge_48.png]]

   You will enter your advanced search queries above the search information box outlined in red.

![[knowledge_49.png]]

  ##  Query String Syntax
[Elasticsearch Query String Syntax documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html#query-string-syntax)
###  Note: Boolean AND, OR, and NOT have to be capitalized.
Parentheses should be used whenever multiple operators are used together to form sub-queries: (quick OR brown) AND fox.
This works using a hierarchal algorithm, “AND” being higher in power than "OR," the parenthesis allows the “OR” to move up in priority to the same level of importance to supply you with an accurate search. This is also true with "NOT."  When your search contains multiple of only one component, parenthesis are not necessary as it doesn't interfere with the order of hierarchy.
**Reserved Characters:**  If you need to use any of the characters which function as operators in your query (but not as operators), then you need to escape them with  **ONE**  leading backslash. To search for  (1+1)=2  , you would need to write your query as  \(1\+1\)\=2  . Using JSON for the request body,  **TWO**  preceding backslashes (  \\  ) are required; the backslash is a reserved escaping character in JSON strings.
The reserved characters are:  + - = && || > < ! ( ) { } [ ] ^ " ~ * ? : \ /
**Wildcard Searches**  : A wildcard operator is a placeholder that matches one or more characters, which means you can use  ?  to replace a single character, and  *  to replace zero or more characters.
**NOTE:**  Avoid BEGINNING patterns with  *  or  ?  . This can increase the iterations needed to find matching terms and slows the search performance.
##  Example Searches
Statement searches (note that '(' and ':' are reserved characters and have to be quoted - list of reserved characters is in the Query String Syntax documentation). You
statement:act\(p\(HGNC?FOX*
statement:act\(p\(HGNC\:FOX* AND isPublished:true AND relation:decreases
subject:act\(p\(HGNC\:FOX*   Search for annotations (note this can cross-match an Annotation with Anatomy:heart with Disease:lung - we do not have the ability yet to specify nested queries which would allow Anatomy:lung only matches)
annotationtype:"Anatomy" AND annotationlabel:"lung"
Search for Nanopubs by an author
nanopub.citation.authors:*Natarajan*  Search for specific phrase in citation title
nanopub.citation.title:"Inflammatory cytokines"  Search for specific nanopub creator
nanopub.metadata.gd\_creator:Selventa  Search for nanopubs in a date range
nanopub.metadata.gd\_createTS: [ 2018-07-01 TO 2018-07-20 ]
Search for specific project in metadata section
nanopub.metadata.project:selv\_large\_corpus
or NOT in that project
-nanopub.metadata.project:selv\_large\_corpus
or to exactly match the characters in project name - note the .keyword at the end and the comma and space - a regular text match (without the .keyword) would not be able to distinguish between 'Test Model' and 'Test Model, '
nanopub.metadata.project.keyword: "Test Model, "  Example Regular expression search (must match entire string which is why the example starts and ends with '.*'
object:/.*HGNC.AKT.*/
##  Fields that can be used in searches
*  statement (full BEL statement as a searchable string)
*  subject
*  relation
*  object
*  annotationtype
*  annotationlabel
*  isDeleted
*  isPublished
*  nanopub.id
*  nanopub.type.version (e.g. 2.0.0)
*  nanopub.citation.database.id
*  nanopub.citation.authors
*  nanopub.citation.title
*  nanopub.evidence
*  nanopub.metadata.X (substitute metadata keys for X)
*  nanopub.metadata.X.keyword (exact match - no text processing such as removing punctuation, spaces etc - see project metadata example above)
**NOTE:**  subject:bp\(MESH\:"Sleep Deprivation"\) should be translated into the search input as subject:path* AND subject:*MESH* AND subject:*Sleep?Deprivation*
This approach allows you to control how things are tokenized and managed and it's probably easier to understand. One thing to note is that the Quoted phrases - e.g. "Sleep Deprivation" in the BEL Assertions require exact matching in case.
