from function import login_save, initialize_parameters, sign_all, add_url, load_config, get_base
#获取根目录
config_path, urls_path, screenshots_path, log_path, cookie_dir= get_base()#初始化参数
config = load_config(path=config_path)
driver = initialize_parameters()
#输入网址并手动登录
if config.get("handle_login", False):
    url = input("请输入要签到的网址（留空使用默认 https://www.baidu.com）：").strip() \
          or 'https://www.baidu.com'
    add_url(url,urls_path)
    login_save(url,driver,cookie_dir,enabled=True)
#自动签到
sign_all(driver,screenshots_path,log_path,urls_path,cookie_dir,enabled=config.get("auto_sign_all", True))
driver.quit()

exit()