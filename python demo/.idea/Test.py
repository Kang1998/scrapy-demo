import pymysql

# �����ݿ�����
db = pymysql.connect("localhost", "root", "cwk646202", "Test")

# ʹ�� cursor() ��������һ���α���� cursor
cursor = db.cursor()

# ʹ�� execute()  ����ִ�� SQL ��ѯ
cursor.execute("SELECT VERSION()")

# ʹ�� fetchone() ������ȡ��������.
data = cursor.fetchone()

print("Database version : %s " % data)

# �ر����ݿ�����
db.close()