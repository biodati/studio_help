# Custom Namespaces/Terminologies

Custom namespaces allow you to provide completion support when creating new nanopubs or provide validation support for nanopub Assertions and Annotations.

The custom namespaces are created as JSONLines documents and posted on a web accessible location (from the BioDati Studio server). The JSON term documents are validated against this  [JSONSchema](https://github.com/belbio/schemas/blob/master/schemas/terminology-0.1.0.yaml)  . Here are some namespaces supported by the BEL.bio organization that serve as good examples of namespaces: <http://resources.bel.bio/?prefix=data/namespaces/>


Once you have built your namespace, you can POST to the following URL:

URL: <https://belapi.<nickname>.biodati.com/data/namespaces>
Payload: {"resource\_url": "<URL of namespace file>", "forceupdate": false}
  
You can check for it to be loaded by viewing the namespaces loaded in <https://belapi.<nickname>.biodati.com/status>
