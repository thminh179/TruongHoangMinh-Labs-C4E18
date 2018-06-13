from gmail import GMail
from gmail import Message
import random

mail = GMail ('minhth.sgs@gmail.com', 'Sgs123456') 
#mail = GMail('A.User <user@gmail.com>','password')

html_content = """
<p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p style="text-align: left;">K&iacute;nh gửi: Thầy</p>
<p style="text-align: left;">T&ecirc;n em l&agrave; Minh.</p>
<p style="text-align: left;">H&ocirc;m nay em xin nghỉ học vì {{ốm}}.</p>
<p style="text-align: left;">Minh</p>
"""

sickness = ["đau bụng", "ẩy chỉa", "sốt xuất huyết"]

reason = random.choice(sickness) #randomly pick an item in a list

html_content = html_content.replace("{{ốm}}", reason) #replace string content <string>.replace()

#placeholder 

message = Message ("Test", "20130075@student.hust.edu.vn", html= html_content) 
#message = Message('Test Message',to='xyz <xyz@xyz.com>',text='Hello')

mail.send(message) 
#mail.send(message)