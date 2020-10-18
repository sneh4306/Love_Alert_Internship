# Love_Alert_Internship
Scrape emails having subject "Thank You for applying" and filter them out to a category Job on gmail. 
**For this, following steps are required.  

-The user has to enable imap setting in his/her gmail account.  
--Click on settings.  
--Select the tab “Forwarding and POP/IMAP.  
--Select “Enable IMAP.  
--Click on Save Changes.  
-The user also has to enable “Less Secure Apps Access”.  
--Click on profile picture of gmail account and click on manage google account.  
--Select Security Tab from left side menu.  
--Now select Less Secure App Access and drag the slider to “ON”.  
-After both the above steps are done, the code will be able to login into gmail and filter out specific emails.   

**Moving  to the code.  

-The user has to give his/her email address and also password to be able to login via code.  
-An imap url is also mentioned in your google account which is used.  
-SSL connection is required to login.  
-The connection variable selects the folder from where you want to search (Inbox in this case).  
-A new label is also created (Job).  
-The inbox is then searched for emails with the subject containing “Thank You for applying”.  
-This search is carried out on all emails and the unique id of emails satisfying this condition are extracted.  
-After the search, the emails are fetched according to the unique id extracted in the above step.  
-These emails are copied and stored in the category created in Step 5.  
-The connection is then expunged i.e. all the changes are updated on the server.  
-There is a setting for expunge in google settings where we can select whether to auto expunge or expunge explicitly.  
-Lastly, the connection is closed.  

**Libraries and Coding Language used.  

-Python 3.6 has been used for this purpose.  
-Libraries - imaplib,email.  

**Execution of code.  

-Enter your own email id and password in the code.  
-Save it.  
-Open command prompt/ terminal.  
-You need to pip install libraries if not already present.  
--pip install imaplib  
--pip install email  
-Go to the directory where the code is saved.  
-To run the code  
--python LA_Internship.py  
-Go to your gmail account and refresh the page to see the category with the filtered out emails.  

