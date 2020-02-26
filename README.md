# zabbix-sendmail
zabbix邮件警告发送脚本

1. cd $ZBX_HOME/share/zabbix/alertscripts/
NOTE: ZBX_HOME is where you install ZABBIX

2. git clone git@github.com:zheng11581/zabbix-sendmail.git

3. python -m venv ./zabbix-sendmail/venv

4. source ./zabbix-sendmail/venv/bin/activate

5. pip3 install -r requirements.txt

6. vim zabbix-sendmail/sendmail.py
\#!/opt/python/3.5.2/bin/pyhton3
增加password=xxx参数

7. chmod +x zabbix-sendmail/sendmail.py
