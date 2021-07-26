import smtplib
#smtp -simple mail transfer protocol

conn = smtplib.SMTP(host='smtp.gmail.com',port=587)
conn.ehlo()
conn.starttls()
conn.connect('srilakshmi.maddali@gmail.com','feb42012')
conn.sendmail('srilakshmi.maddali@gmail.com','srilakshmi.maddali@gmail.com','Subject: From my Python\n\n This is from my python code.\n\n Srilakshmi')