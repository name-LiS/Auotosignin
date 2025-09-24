import json
import sys
import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from urllib.parse import urlparse



#根目录
def get_base():
    if getattr(sys, 'frozen', False):
        # exe 模式（打包后）
        base = os.path.dirname(sys.executable)
    else:
        # 源码模式（调试时）
        base = os.path.dirname(os.path.abspath(__file__))
    # 设置工作目录为程序所在目录
    #os.chdir(base)

    config_p = os.path.join(base, "config.json")
    urls_p = os.path.join(base, "urls.txt")
    screenshots_p = os.path.join(base, "screenshots")
    log_p = os.path.join(base, "log.txt")
    cookie_dir = os.path.join(base, "cookies")

    return config_p, urls_p, screenshots_p, log_p,cookie_dir
#config_path, urls_path, screenshots_path, log_path = get_base()
#首次登录
def login_save(url,driver,cookie_dir,enabled=True):
    if not enabled:
        print("全部签到已禁用，跳过执行")
        return
#确认cookies文件夹
    os.makedirs(cookie_dir, exist_ok=True)
#定义cookie名字
    domain = urlparse(url).netloc
    cookie_file = os.path.join(cookie_dir, f"{domain}.pkl")
#手动登录
    print("请手动登录...")
    driver.get(url)
    driver.maximize_window()
    print("please log in，60s")
    time.sleep(60)
# 读取cookie
    with open(cookie_file, "wb") as f:
        pickle.dump(driver.get_cookies(), f)
    print("cookies saved")

#加载cookie自动登录
def autolog(url,driver,log_p,cookie_dir):
# 确保 Cookie 文件存在
    domain = urlparse(url).netloc
    cookie_file = os.path.join(cookie_dir, f"{domain}.pkl")
    if not os.path.exists(cookie_file):
        log_save(f"Cookie 文件不存在: {cookie_file}",log_p)
        return False
# 登录
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    cookies = pickle.load(open(cookie_file, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    log_save("auto log in success",log_p)
    return True

#自动签到
def autosignin(driver,log_p):
    try:
        button = driver.find_element(By.XPATH, '//a[contains(text(),"签到")]')
        button.click()
        log_save("签到成功",log_p)
        time.sleep(5)
    except Exception as e:
        log_save(f"未找到签到按钮：{e}",log_p)

#初始化参数
def initialize_parameters():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver
#打印日志
def log_save(msg,log_file):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"{timestamp} - {msg}"
    print(full_msg)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(full_msg + "\n")

#全部签到
def sign_all(driver,s_path,log_p,url_p,cookie_dir,enabled=True):
    if not enabled:
        print("全部签到已禁用，跳过执行")
        return
    urls = load_urls(url_p)
    for url in urls:
        log_save(f"\n处理网址: {url}", log_p)
        # 尝试自动登录
        success = autolog(url, driver,log_p,cookie_dir)
        if not success:
            log_save(f" 自动登录失败，跳过 {url}", log_p)
            continue
        autosignin(driver,log_p)
        screenshot(driver,s_path)
        log_save("screenshot saved",log_p)
        print("screenshot saved")

#读取网址
def load_urls(url_file):
    if not os.path.exists(url_file):
        with open(url_file, "w", encoding="utf-8") as f:
            pass
        return []
    with open(url_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]
    return urls
#保存网址
def save_urls(urls, url_file):
    with open(url_file, "w", encoding="utf-8") as f:
        for url in urls:
            f.write(url.strip() + "\n")

#添加网址
def add_url(new_url, url_file):
    urls = load_urls(url_file)
    if new_url not in urls:
        urls.append(new_url)
        save_urls(urls, url_file)
        print(f"已添加网址: {new_url}")
    else:
        print(f"网址已存在: {new_url}")

#
def load_config(path):
    if not os.path.exists(path):
        # 创建默认配置
        default_config = {"handle_login": False, "auto_sign_all": True}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=4)
    with open(path, "r", encoding="utf-8") as f:
        config = json.load(f)
    return config

#截图
def screenshot(driver, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(folder, filename)
    driver.save_screenshot(filepath)
    print(f" 截图已保存: {filepath}")
    return filepath

