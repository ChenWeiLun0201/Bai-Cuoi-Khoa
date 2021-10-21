from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

product = "giày"
url = "https://tiki.vn/?src=header_tiki"
# Khai báo biến browser
browser = webdriver.Chrome(executable_path="chromedriver.exe")

# Mở thử trang web
browser.get(url)

# Nhập tìm kiếm
txtItem = browser.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[1]/div/div[1]/div[2]/div/input")
txtItem.send_keys(product)

# Chọn tìm kiếm
txtItem = browser.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[1]/div/div[1]/div[2]/div/button")
txtItem.click()
sleep(3)

item_info = browser.find_elements_by_class_name("info")

# Lấy thông tin về
f = open("crawler.txt", "w", encoding="utf-8")
for item in item_info:
    result = item.find_element_by_css_selector("div.name span").text + "\n" + item.find_element_by_css_selector("div.price-discount div.price-discount__price").text
    f.write(f'Thông tin {product} từ trang tiki:\n\n\n {result}')
f.close()

# Chờ 3s
sleep(3)

# Đóng trình duyệt
browser.close()
