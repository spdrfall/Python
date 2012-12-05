
#! /usr/local/bin/python

import sys


from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)
from email.MIMEText import MIMEText

#This object will house the data used in making the SMTP connection. I did this
#In an attempt to have some security
class _Data (object):
    SMTPserver  = '[SMTP Host Address]'
    sender      = '[Sending from Address]'
    USERNAME    = "[Enter Username Here]"
    PASSWORD    = "[Enter Password Here]"
    # typical values for text_subtype are plain, html, xml
    text_subtype = 'plain'

#Create an instance of the object, so we can use it
d = _Data()

/*This is the function that will actually send the email
  Call it with the following arguments:
  content     -> The message body of the email
  subject     -> Subject of the email
  destination -> Email addy of the recipient
*/
def send_email(content,subject,destination):
    try:
        msg = MIMEText(content,d.text_subtype)
        msg['Subject']= subject
        msg['From']   = d.sender # some SMTP servers will do this automatically, not all
    
        conn = SMTP(d.SMTPserver)
        conn.set_debuglevel(False)
        conn.login(d.USERNAME, d.PASSWORD)
        try:
            conn.sendmail(d.sender, destination, msg.as_string())
        finally:
            conn.close()
    
    except Exception, exc:
        sys.exit( "mail failed; %s" % str(exc) ) # give a error message
        