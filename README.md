浙江理工大学计算机协会预约维修系统\填报表单\信息收集

基于flask的简易网页\表单

## 怎么用

### 环境

```bash
pip install -r requirements.txt
```

### 运行

```bash
# 本地调试
python form.py
# 服务器
python form.py runserver --host=0.0.0.0
```

### 目录介绍

```bash
-rwxrwxrwx 1 root root 1.2K Apr  2 18:05 README.md
-rwxrwxrwx 1 root root  718 Apr  2 18:09 bookform.py
-rwxrwxrwx 1 root root  512 Apr  2 18:07 config.py
-rwxrwxrwx 1 root root 1.5K Apr  2 18:08 form.py
-rwxrwxrwx 1 root root   56 Apr  2 18:08 requirements.txt
-rwxrwxrwx 1 root root  629 Apr  2 18:09 savedata.py
-rwxrwxrwx 1 root root 2.9K Apr  2 18:05 sendmail.py
drwxrwxrwx 1 root root 4.0K Apr  2 18:05 templates
```

#### form.py

系统主文件

#### bookform.py

报表设计，可以复制添加

#### sendmail.py

邮件

#### config.py

一些配置，包括邮箱配置，后续会有数据库配置

#### savedata.py

数据存入数据库