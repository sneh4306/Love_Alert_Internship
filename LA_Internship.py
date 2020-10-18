import imaplib, email

user = 'email_id' # enter your own email id
password = 'password' # enter your password
imap_url = 'imap.gmail.com'

def search(key, value, conn):
  result, data = conn.uid('search',None, key, '"{}"'.format(value))
  return data

def get_emails(result_bytes):
  msgs = [] # all the email data are pushed inside an array 
  for num in result_bytes[0].split(): 
      typ, data = conn.uid('fetch',num, '(RFC822)') 
      msgs.append(data)
      result = conn.uid('COPY', num, 'job')
      if result[0] == 'OK':
        mov, data = conn.uid('STORE', num , '+FLAGS', '(\Deleted)')
        conn.expunge()
  conn.close()

# this is done to make SSL connnection with GMAIL 
conn = imaplib.IMAP4_SSL(imap_url)  
  
# logging the user in 
conn.login(user, password)  

# Create new label
conn.create('job')

# calling function to check for email under this label 
conn.select('Inbox')  

# fetching emails from this user 
get_emails(search('SUBJECT', r'Thank you for applying', conn))
