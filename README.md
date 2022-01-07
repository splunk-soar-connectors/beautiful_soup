[comment]: # "Auto-generated SOAR connector documentation"
# Beautiful Soup Utilities

Publisher: Robert Martin  
Connector Version: 1\.0\.3  
Product Vendor: Generic  
Product Name: Beautiful Soup Utilities  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 3\.0\.251  

Implements basic BeautifulSoup functions for UI access

### Supported Actions  
[find strings](#action-find-strings) - Finds the strings in html data  
[remove attributes](#action-remove-attributes) - Removes the tag attributes provided in a comma separated list  
[remove tags](#action-remove-tags) - Removes the tags provided in a comma separated list  
[extract tags](#action-extract-tags) - Uses SoupStrainer to return the tags from a comma separated list  
[wrap tags](#action-wrap-tags) - Wraps the specified tag with a new tag  
[unwrap tags](#action-unwrap-tags) - Unwraps the specified tags from all instances  
[get urls](#action-get-urls) - Finds URLs in given HTML code  
[extract tag](#action-extract-tag) - Removes a tag or string from the tree\. It returns the first instance of the tag or string that was extracted  
[transform to table](#action-transform-to-table) - Returns a HTML table from dictionary or list of dictionaries  
[get pretty](#action-get-pretty) - Returns the data after applying the Beautiful Soup Prettify function  
[find all](#action-find-all) - Returns a list of all the instances found  
[get text](#action-get-text) - Returns the text from an HTML string source  

## action: 'find strings'
Finds the strings in html data

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**search\_string** |  required  | String to search for | string | 
**source\_string** |  required  | HTML source to search for string in | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.parameter\.search\_string | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.status | string | 
action\_result\.summary | string | 
action\_result\.data\.\*\.strings | string |   

## action: 'remove attributes'
Removes the tag attributes provided in a comma separated list

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**source\_string** |  required  | HTML source string | string | 
**tag\_attributes\_list** |  required  | Comma separated values to remove from tags | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.results | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.parameter\.tag\_attributes\_list | string | 
action\_result\.status | string | 
action\_result\.summary | string |   

## action: 'remove tags'
Removes the tags provided in a comma separated list

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**source\_string** |  required  | HTML source string | string | 
**tag\_list** |  required  | Comma separated values of tags to remove | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.results | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.parameter\.tag\_list | string | 
action\_result\.status | string | 
action\_result\.summary | string |   

## action: 'extract tags'
Uses SoupStrainer to return the tags from a comma separated list

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**source\_string** |  required  | HTML source string | string | 
**tag\_list** |  required  | Comma separated values of tags to return | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.results | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.parameter\.tag\_list | string | 
action\_result\.status | string | 
action\_result\.summary | string |   

## action: 'wrap tags'
Wraps the specified tag with a new tag

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**source\_string** |  required  | HTML source string | string | 
**tag** |  required  | Tag to be wrapped | string | 
**wrap\_tag** |  required  | Tag to wrap around existing tag | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.results | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.parameter\.tag | string | 
action\_result\.parameter\.wrap\_tag | string | 
action\_result\.status | string | 
action\_result\.summary | string |   

## action: 'unwrap tags'
Unwraps the specified tags from all instances

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**source\_string** |  required  | HTML source string | string | 
**tag\_list** |  required  | List of comma separated tags to unwrap | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.results | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.parameter\.tag\_list | string | 
action\_result\.status | string | 
action\_result\.summary | string |   

## action: 'get urls'
Finds URLs in given HTML code

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**source\_string** |  required  | HTML source string\. | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.status | string | 
action\_result\.summary | string | 
action\_result\.data\.\*\.urls | string |   

## action: 'extract tag'
Removes a tag or string from the tree\. It returns the first instance of the tag or string that was extracted

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**source\_string** |  required  | HTML source string | string | 
**tag** |  required  | Tag to extract and return | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.results | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.parameter\.tag | string | 
action\_result\.status | string | 
action\_result\.summary | string |   

## action: 'transform to table'
Returns a HTML table from dictionary or list of dictionaries

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**source\_string** |  required  | HTML source string\. | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.status | string | 
action\_result\.summary | string | 
action\_result\.data\.\*\.table | string |   

## action: 'get pretty'
Returns the data after applying the Beautiful Soup Prettify function

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**source\_string** |  required  | HTML source string\. | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.status | string | 
action\_result\.summary | string | 
action\_result\.data\.\*\.pretty | string |   

## action: 'find all'
Returns a list of all the instances found

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**source\_string** |  required  | HTML source string\. | string | 
**find\_field** |  required  | HTML tag to find | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.parameter\.find\_field | string | 
action\_result\.status | string | 
action\_result\.summary | string | 
action\_result\.data\.\*\.field\_list | string |   

## action: 'get text'
Returns the text from an HTML string source

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**source\_string** |  required  | Source string\. | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.status | string | 
action\_result\.summary | string | 
action\_result\.data\.\*\.plain\_text | string | 