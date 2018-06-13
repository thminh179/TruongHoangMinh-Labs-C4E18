from gmail import GMail
from gmail import Message
import random
import schedule
import time

def job():

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

    reason = random.choice(sickness)

    html_content = html_content.replace("{{ốm}}", reason)

    message = Message ("Test", "20130075@student.hust.edu.vn", html= html_content) 

    mail.send(message) 

schedule.every().day.at("19:00").do(job)

schedule.run_pending()
time.sleep(60)
