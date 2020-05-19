import pymongo

client = pymongo.MongoClient('localhost',27017)
db = client['bookshop'] #获取名字的数据库
book = db['book'] #获取名字的集合
publisher = db['publisher']
order = db['order']

# book.insert_one({'title':'时间简史2','isbn':'1231561456123','price':'666','author':'霍金','count':55})
# book.insert_one({'title':'时间简史1','isbn':'1231561456123','price':'666','author':'霍金','count':12})
# book.insert_one({'title':'时间简史3','isbn':'1231561456123','price':'666','author':'霍金','count':45})
# publisher.insert_one({'name':'邮电出版社','address':'邮电大学'})
# order.insert_one({'username':'asdasd','orderdate':'2016-4-11','totalprice':55})

# book.update({'title':'母猪产后护理'},{'$set':{'title':'时间简史'}})
# book.remove({'title':'母猪产后护理'})

for each in book.find({'price':'666'}):
    print(each['title'])
# print(book.find({'price':'666'}))