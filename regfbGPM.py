from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as WebWait
from selenium.webdriver.support import expected_conditions as EC
import time, requests, json ,string ,random,os
import requests
def Reg(stt,MK,NoiChuaprofile,proxy,haiepakhong,ten):
	def generate_random_password(length=15):
	    if length < 2:
	        raise ValueError("Length must be at least 2 to include a special character")
	    # Danh sách các ký tự
	    letters_and_digits = string.ascii_letters + string.digits
	    special_characters = string.punctuation

	    # Tạo mật khẩu ngẫu nhiên
	    password = ''.join(random.choice(letters_and_digits) for _ in range(length-1))
	    
	    # Chèn một ký tự đặc biệt vào mật khẩu
	    password += random.choice(special_characters)
	    
	    # Trộn ngẫu nhiên các ký tự trong mật khẩu
	    password = list(password)
	    random.shuffle(password)
	    
	    return ''.join(password)

	if MK == '':
		MK=generate_random_password()
		print("Mật khẩu ngẫu nhiên là:", MK)
	try:
		xx=stt*(800*1)
		yy=0
		if xx >= (3200*1) :
			xx= (stt-4)*(800*1)
			yy=600
		if xx >= (3200*2):
			xx= (stt-8)*(800*1)
			yy=1200

		def get_messages(login, domain):
			url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
			response = requests.get(url)
			if response.status_code == 200:
				return response.json()
			else:
				return None
		def gen_random_mailbox():
			ccccccc = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1000").json()
			for x in ccccccc:
				if 'rteet' in x:return x
		   

		emails = gen_random_mailbox()
		print(emails)

		url = 'http://127.0.0.1:19995/api/v3/profiles/create'  # Replace with your actual API endpoint
		mailll=str(emails)

		headers = {
			'Content-Type': 'application/json',
			# Add any other headers if needed
		}

		data = {
			"profile_name": "RegFb","group_name": "RegFb","browser_core": "chromium","browser_name": "Chrome","browser_version": "119.0.6045.124","is_random_browser_version": False,"raw_proxy": "","startup_urls": "","is_masked_font": True,"is_noise_canvas": False,"is_noise_webgl": False,"is_noise_client_rect": False,"is_noise_audio_context": True,"is_random_screen": False,"is_masked_webgl_data": True,"is_masked_media_device": True,"is_random_os": False,"os": "Windows 11","webrtc_mode": 2,"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
		}
		try:response = requests.post(url, json=data, headers=headers)
		except:
			for hhh in range(10):
				print("Lỗi GPMM")		
		if response.status_code == 200:
			result = response.json()
			print("Profile created successfully:")
			print(f"Profile ID: {result['data']['id']}")
			print(f"Profile Name: {result['data']['name']}")
			print(f"Profile Path: {result['data']['profile_path']}")
			# Add more fields as needed
		else:
			print(f"Failed to create profile: {response.status_code} - {response.reason}")
		profile_path=result['data']['profile_path']

		options = Options()
		dd=str(NoiChuaprofile.replace('\\', '\\\\'))+'\\'+profile_path
		options.add_argument(f"user-data-dir={dd}")
		prefs = {
			"credentials_enable_service": False,
			"profile.password_manager_enabled": False
		}
		options.add_experimental_option("prefs", prefs)
		if len(proxy) >= 10:options.add_argument(f'--proxy-server={proxy}')
		options.add_argument("--disable-blink-features=AutomationControlled")
		options.add_experimental_option("excludeSwitches", ["enable-automation"])
		options.add_argument(f"window-position={xx},{yy}")
		options.add_argument("--force-device-scale-factor=0.5")
		options.add_argument(f'--app=https://www.facebook.com/reg')
		options.add_argument(f"window-size=800,600")
		driver = webdriver.Chrome(options=options)
		WebWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/div[1]/input")))
		name=requests.get("https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/male?count=5").json()['data'][1]['name']
		driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/div[1]/input").send_keys(name.split(" ")[0]+' '+name.split(" ")[1])
		driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/input").send_keys(name.split(" ")[2])
		driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input").send_keys(emails)
		driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div/div/div[1]/input").send_keys(emails)
		driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input").send_keys(MK)
		dropdown = driver.find_element(By.ID, "year")
		dropdown.find_element(By.XPATH, "//option[. = '2001']").click()
		driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input").click()
		driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[11]/button").click()
		try:
			WebWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/span/span")))
			print("Dieeeeeeeeeeeee")
		except:
			try:driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[11]/button").click()
			except:pass
			WebWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[1]/div[1]/label/div/input")))
			time.sleep(10)
			while True:
				dau=mailll.split("@")[0]
				dit=mailll.split("@")[1]
				messages = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={dau}&domain={dit}").text
				if 'FB-' in messages:break
				else:time.sleep(2)
			messages=messages.split('FB-')[1].split(' ')[0]
			driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[1]/div[1]/label/div/input").send_keys(messages)
			driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/button").click()
			# WebWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div[3]/div/")))

			# driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div[3]/div/a").click()
			time.sleep(5)
			driver.get('https://www.facebook.com/me')
			B='61'+str(driver.get_cookies()).split("'61")[1].split("'}")[0]
			if haiepakhong == 'y' or haiepakhong == "Y":
				driver.get("https://accountscenter.facebook.com/password_and_security")
				WebWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/main/div/div/div[2]/div[1]/div[2]/div/div/div[2]/a/div[1]/div/div[1]/div/div/span")))
				driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/main/div/div/div[2]/div[1]/div[2]/div/div/div[2]/a/div[1]/div/div[1]/div/div/span").click()
				WebWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/span[1]/div")))
				driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/span[1]/div").click()
				WebWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div[3]")))
				time.sleep(5)
				driver.find_element(By.XPATH, "//input").send_keys(MK)
				WebWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[4]/div[3]/div/div/div/div/div/div/div/div")))
				driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[4]/div[3]/div/div/div/div/div/div/div/div").click()
				WebWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[4]/div[3]/div/div/div/div/div/div/div/div")))
				driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[4]/div[3]/div/div/div/div/div/div/div/div").click()
				time.sleep(10)
				towFa = driver.page_source.split('''%3Fsecret%3D''')[1].split('%')[0]
				WebWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[3]/div/div[4]/div[3]/div/div/div/div/div/div/div/div")))
				driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[3]/div/div[4]/div[3]/div/div/div/div/div/div/div/div").click()
				WebWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/div[4]/div/div/div[2]/div")))
				ma=requests.get(f"https://2fa.live/tok/{towFa}").json()['token']
				print(ma)
				time.sleep(10)
				driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[4]/div/div[3]/div[2]/div[4]/div/div/div[2]/div/div/div[1]/input").send_keys(ma)
				WebWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[4]/div/div[4]/div[3]/div/div/div/div/div/div/div")))
				driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[4]/div/div[4]/div[3]/div/div/div/div/div/div/div").click()

			else:towFa=''
			with open("FacebookLive.txt", "a+", encoding="utf-8") as file:
				file.write(f"{B}|{MK}|{towFa}|{mailll}\n")
		time.sleep(3)
	except:pass
	driver.quit()
MK=input("Nhập Pass FB (Enter Để Random): ")
proxy=input("Nhập Tệp Proxy (Enter Để K chạy Proxy): ")
NoiChuaprofile=input("Nhập Nơi Chứa Profiles GPM: ")
luong=input("Nhập Số Luồng Muốn chạy : ")
haiepakhong=input("Bật 2fa (y/n) : ")
ten=int(input("Tên Nước Ngoài [1] | Tên Việt Name [2] : "))
requests.get(f"https://api.telegram.org/bot7055705243:AAFIdPKDh2Npaz0LtGkujlCd_YU5MdIqLQ8/sendMessage?chat_id=5724397112&text=[REGFBv2] Tool Đang chạy : \n Luồng : {luong}")
if len(proxy) >= 10:
	with open(proxy, 'r+', encoding='utf-8') as file:
		AAAA=file.read().split()
for x in range(int(luong)):
	def run(x,MK,NoiChuaprofile,proxy,haiepakhong,ten):
		x=int(x)
		while True:
			if len(proxy) >= 10:
				proxy=random.choice(AAAA)
				print('Proxy : ',proxy)
			Reg(x,MK,NoiChuaprofile,proxy,haiepakhong,ten)
	Thread(target=run,args=(str(x),MK,NoiChuaprofile,proxy,haiepakhong,ten)).start()
