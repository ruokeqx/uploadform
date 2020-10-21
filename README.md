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
drwxr-xr-x 1 ruokeqx 197121    0 10月 21 23:19 ./
drwxr-xr-x 1 ruokeqx 197121    0 10月 20 00:50 ../
drwxr-xr-x 1 ruokeqx 197121    0 10月 21 23:16 .git/
drwxr-xr-x 1 ruokeqx 197121    0 10月 18 13:44 .vscode/
-rw-r--r-- 1 ruokeqx 197121  629 10月 21 23:19 bookform.py
-rw-r--r-- 1 ruokeqx 197121  476 10月 21 23:11 config.py
-rw-r--r-- 1 ruokeqx 197121 1.4K 10月 20 01:03 form.py
-rw-r--r-- 1 ruokeqx 197121  142 10月 21 23:19 README.md
-rw-r--r-- 1 ruokeqx 197121   47 10月 20 01:00 requirements.txt
-rw-r--r-- 1 ruokeqx 197121 2.9K 10月 20 00:53 sendmail.py
drwxr-xr-x 1 ruokeqx 197121    0 10月 19 23:17 templates/
```

#### form.py

系统主文件

#### bookform.py

报表设计，可以复制添加

#### sendmail.py

邮件

#### config.py

一些配置，包括邮箱配置，后续会有数据库配置

