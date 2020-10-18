# Love_Alert_Internship
Scrape emails having subject "Thank You for applying" and filter them out to a category "Job" on gmail. 
# For this, following steps are required.  

1. The user has to enable imap setting in his/her gmail account.  
    1. Click on settings.  
    2. Select the tab “Forwarding and POP/IMAP.  
    3. Select “Enable IMAP.  
    4. Click on Save Changes.  
2. The user also has to enable “Less Secure Apps Access”.  
    1. Click on profile picture of gmail account and click on manage google account.  
    2. Select Security Tab from left side menu.  
    3. Now select Less Secure App Access and drag the slider to “ON”.  
3. After both the above steps are done, the code will be able to login into gmail and filter out specific emails.   

# Moving  to the code.  

1. The user has to give his/her email address and also password to be able to login via code.  
2. An imap url is also mentioned in your google account which is used.  
3. SSL connection is required to login.  
4. The connection variable selects the folder from where you want to search (Inbox in this case).  
5. A new label is also created (Job).  
6. The inbox is then searched for emails with the subject containing “Thank You for applying”.  
7. This search is carried out on all emails and the unique id of emails satisfying this condition are extracted.  
8. After the search, the emails are fetched according to the unique id extracted in the above step.  
9. These emails are copied and stored in the category created in Step 5.  
10. The connection is then expunged i.e. all the changes are updated on the server.  
11. There is a setting for expunge in google settings where we can select whether to auto expunge or expunge explicitly.  
12. Lastly, the connection is closed.  

# Libraries and Coding Language used.  

1. Python 3.6 has been used for this purpose.  
2. Libraries - imaplib,email.  

# Execution of code.  

1. Enter your own email id and password in the code.  
2. Save it.  
3. Open command prompt/ terminal.  
4. You need to pip install libraries if not already present.  
    1. pip install imaplib  
    2. pip install email  
5. Go to the directory where the code is saved.  
6. To run the code  
    1. python LA_Internship.py  
7. Go to your gmail account and refresh the page to see the category with the filtered out emails.  

