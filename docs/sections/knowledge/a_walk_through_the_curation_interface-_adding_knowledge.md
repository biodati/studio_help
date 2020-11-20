# A Walk Through The Curation Interface- Adding Knowledge

To land on the Curation Interface from the Dash Board, click + on the Knowledge field (1), or from the drop-down "+" menu, click Knowledge (2).

![[curation1.jpg]]

   Input the PubMed ID for your nanopub and hit the tab on your keyboard.

![[curation2.jpg]]

The Abstract, and Citation Information fields, excluding the Evidence, will auto-populate. A popup window will allow you to chose which of the PubMed Annotations to include. Click the box next to "label" to select all.

![[curation3.jpg]]

   If you want to return to the PubMed annotations later, click the add annotaions icon (1). 
   If you click the goto page icon (2), the PubMed citation page will open in a new window, so you can refer to it while working.

![[curation4.jpg]]

   Click "More" at the bottom of the citation information, to view the Author and Journal Information (also auto-populated). Clicking "Less" will hide this information.

![[curation5.jpg]]

   If your Citation does not have a PubMed ID, it's not a problem. Click the arrow to the right of CITATION TYPE, to open the drop-down menu and select the tab which is appropriate for your citation. Then just type in the citation information. With inline editing it is easy to click on a field and edit the information!
   
Now, check the species box (1). The form defaults to human. To change species, type the new species into the species box, and select the correct choice from the dropdown selections. It is important to set the species before you add assertions, because the completion engine will suggest standardized identifiers that are species specific as you add your assertions. 

![[curation6.jpg]]

Next, add the evidence on which you will base your assertions.
 
 To add your first Assertion. Click in the subject box. The completion engine will suggest BEL functions for you to select.

![[assertions1.jpg]]

   As you type inside a parenthesis, the completion engine will suggest standardized BEL terms for you to select and display function rules (2).

![[curation8.jpg]]

   Complete your Subject. Select a Relation from the drop down menu, and type in an Object. The completion engine will help you with Objects as well. When done, click  "ADD" at the end of the line to add the Assertion. You may now add another Assertion, or review the Annotations.  For more details please see; [[How to use Completion when Editing or Creating an Assertion]] and [[Assertion Validation]].
   
**Annotations** are used to provide experiemntal context. They are easy to edit and add. 

To add an Annotation, click in the TYPE box, and select the type of Annotation that you would like to ADD from the dropdown menu.

![[curation9.jpg]]

Type within the ID OR Label field and select the appropriate term suggested by the completion engine. The completion Engine will add the label and ID for you. Click "ADD to create your new annotation.

![[curation10.jpg]]

If the term you are looking for does not appear, you can add the ID (namespece:number) and Label manually.  If the namespace is not supported by BioDati Studio, you can use it, but will get a warning for the annotation.  

To the right of each line in the annotation field, you will see two icons. (1) will allow you to copy the annotation. while (2) will delete the Annotation. To Edit an Annotation, just click in the desired field and type. 

![[curation11.jpg]]

Validation of assertions and annotations occurs in the background after you save your nanopub. Click the save icon at the top of the form to save your nanopub.

![[curation12.jpg]]

For more on Validation, see: [[Assertion Validation]].  If you need to edit an assertion or annotation, simply click on the field in the assertion (or annotation) that needs to be edited, and type.  The completion engine will help.  See also: [[Editing Assertions]].

If you wish to add your new nanopub to a collection, you will need to edit the Metadata.
Click on the collections box (1). Click Edit(2). Type in the collection name in the value field (3). Collections are always a "list of strings", even if the nanopub is only added to a single collection. The nanopub can be added to multiple collections by entering multiple names, separated by commas. Click Create/Update (4).  for more details, see: [[Collections-Adding and editing Metadata]]

![[knowledge_27.png]]

Finally you can go back to the top of your completed nanopub and use the drop down menu to update the status. The nanopub will save automatically. Please see [[NanoPub Statuses and What They Mean]]

![[knowledge_28.png]]

## Additional Features of the Knowledge Creation Page:

There are a few more features available to you on the Knowledge Creation page.

   #1  Toggle which shrinks and expands the citation information.
   
   #2  Save the nanopub.
   
   #3  Copy the nanopub.
   
   #4  Pin the nanopub.  See [[Pinning NanoPubs]]
   
   #5  Copy the nanopub URL.
   
   #6  Toggle which shrinks and expands the column containing Comments and Abstract. This creates a wider assertions field.
   
   #7  "More" icon which allows you to Export or Delete your nanopub.  Please see: [[Exporting Nanopubs]]
   
   #8  The "BULK IMPORT" tab, which allows you to upload thousands of assertion at once. Please see: [[Bulk Assertion Uploads]]
   
   #9  The "EXPORT AS TSV" tab, which allows you to export the assertions in your nanopub in TSV format.
   
   ![[curation14.jpg]]



