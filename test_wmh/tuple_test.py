#-*- coding:utf-8 -*-
#创建空元组
temp1 = ();
#如果元祖中只包含一个值，需用逗号隔开消除歧义
temp1=(1,)

#元祖的基本操作
#访问元祖，可以使用下标索引访问元素的值
temp1=('hello','world')
print temp1[1]
#world
temp1=(1,2,3,5,7,6)
print temp1[1:5]