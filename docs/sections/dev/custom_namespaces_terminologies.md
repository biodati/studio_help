# Custom Namespaces/Terminologies

Custom namespaces allow you to provide completion support when creating new nanopubs or provide validation support for nanopub Assertions and Annotations.

The custom namespaces are created as JSONLines documents and posted on a web accessible location (from the BioDati Studio server). The JSON term documents are validated against this  [JSONSchema](https://github.com/belbio/schemas/blob/master/schemas/terminology-0.1.0.yaml). Here are some namespaces supported by the BEL.bio organization that serve as good examples of namespaces: <http://resources.bel.bio/?prefix=data/namespaces/>

Once you have built your namespace, you can POST to the following URL:

http://nanopubstore.NICKNAME.biodati.com/docs#/BEL%20Resources/post_update_resources_resources_update_post
