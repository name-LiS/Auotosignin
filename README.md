# Auotosignin
  这是一个自动签到脚本，可以帮助用户在指定网站上自动完成签到操作。
## 功能
- 自动登录指定网站
- 自动签到
- 支持多账号
- 可保存 Cookie，减少重复登录
- 可以配合自动计划定时登录
## 教程
### 下载安装
    下载源码安装相关依赖或使用打包好的exe文件
### 使用教程
#### 配置说明
  将exe文件部署到指定文件，首次运行会在当前文件路径下生成config文件，文件格式如下：

  {

      "handle_login": false,
    
      "auto_sign_all": true
  }

  第一项为是否手动登录并保存cookie（在初次登录某网站时使用），选取后手动登录并等待自动保存cookie，记得在后续使用时关闭

  第二项为是否启动自动登录，开启后会自动读取urls文件中的网址，并读取cookies文件中的对于cookie登录并自动签到

#### 自动签到
  结合windows的自动计划可以方便实现定时登录/签到
  使用Windows+R键运行：taskschd.msc 打开任务计划程序
#### 依赖
 ##### 浏览器自动化
selenium

 ###### ChromeDriver 自动管理
webdriver-manager
需要安装chrome浏览器
