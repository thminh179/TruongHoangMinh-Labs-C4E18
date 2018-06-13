from gmail import GMail
from gmail import Message

mail = GMail ('minhth.sgs@gmail.com', 'Sgs123456') 
#mail = GMail('A.User <user@gmail.com>','password')

message = Message ("Test", "20130075@student.hust.edu.vn", html= '<b>Hello</b>') 
#message = Message('Test Message',to='xyz <xyz@xyz.com>',text='Hello')

mail.send(message) 
#mail.send(messagep
