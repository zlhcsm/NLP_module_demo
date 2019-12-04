> 下载社区版，neo4j

##　使用命令
    1,添加实体和关系
    neo4j-admin import --nodes xx.csv





## APOC插件
- 文本和索引查找
- 使用函数
- 图算法
- 空间函数
- 数据集成
- 图形重构
- 虚拟节点、关系
- cypher操作
- 触发器

## APOC数据集成-JDBC
语句
```$xslt
call  
apoc.load.jdbc("jdbc:mysql://{IP}:{PORT)/{DBNAME}?user={USERNAME}&password={PASSWORD}","{TABLENAME}")
yield row
creat
(b:Black{number:row.black_id, type:row.type})
```

## cypher学习
    １，match相当于SQL select
    match
        (node) - [relationship] -> (node)
    where
        (node | relationship)
    return
        (node | relationship)
    ２，创建实体
    create (n:Person{name:"alan"})-[:FEAR{level:1}] ->(t:Tiger{Type:"dongbeihu"})
    ３，孤立实体增加关系
    create (n:Person{name:"zhangsan"})
    create (n:Person{name:"lisi"})
    MATCH (n:Person{name:"lisi"}) , (m:Person{name:"zhangsan"}) return n,m
    MATCH (n:Person{name:"lisi"}) , (m:Person{name:"zhangsan"}) create (n)-[k:Know]->(m) return k
    4，merge
    有则修改，无则新加
    ５，删除关系
    MATCH (n:Person{name:"alan"})-[f:FEAR]->(t:Tiger) delete f
    ６，删除实体
    MATCH (n:Person{name:"alan"}) delete n
    ７，删除实体和关系
    MATCH (n:Person{name:"alan"})-[f:FEAR]->(t:Tiger) delete n,f,t
    ８，修改实体的一个属性
    MATCH (t:Tiger) where id(t)=709 set t.age=10 return t
    9，给关系增加属性
    MATCH (n:Person)-[l:Love]->(:Person) set l.time="1990" return n,l
    10,查询多个朋友
    MATCH (p:Person)-[:Friend_OF]-(p1:Person)-[:Friend_OF]-[p2:Person] where p.name="alan"
    11,查询两个关系以内的关系
    MATCH (p:Person)-[]-(p1:Person)-[]-[p2:Person] where p.name="alan"
    12,查询最短路径
    match (p1:Person{name:"alan"}),(p2:Person{name:"alan1"}),p=shortestpath((p1)-[*..10]-(p2)) return p
    
> 一个实体有多个标签 

## 索引
    创建在属性上
    create index on :Person(name)
    删除
    drop index on :Person(name)
    创建唯一约束
    create constraint on (p:Person) assert (p.name) is unique
    删除唯一约束
    drop constraint on (p:Person) assert (p.name) is unique

    
## 问题总结

---
1,Neo4j Server shutdown initiated by request  
[解决方案1](https://blog.csdn.net/u010687164/article/details/88975560)  
无效  
[问题集合](https://wkq278276130.oschina.io/2017/06/01/neo4j-error-notes/)  
问题说明：  
下载的plugins中apoc有问题，下载最新版本即可解决问题，我的版本是(apoc-3.5.0.4.jar)
2,
```$xslt
WARNING Import failed. The store files in /usr/neo4j/data/databases/graph.db are left as they are, although they are likely in an unusable state. Starting a database on these store files will likely fail or observe inconsistent records so start at your own risk or delete the store manually
unexpected error: org.neo4j.io.pagecache.impl.FileLockException: This file is locked by another process, please ensure you don't have another Neo4j process or tool using it: '/usr/neo4j/data/databases/graph.db/neostore'.'

```
导入数据时一定要关掉neo4j服务
3,
```$xslt
WARNING Import failed. The store files in /usr/neo4j/data/databases/graph.db are left as they are, although they are likely in an unusable state. Starting a database on these store files will likely fail or observe inconsistent records so start at your own risk or delete the store manually
unexpected error: /usr/neo4j/data/databases/graph.db already contains data, cannot do import here
```
neo4j导入数据时，只能导入一次，因此需要你一次import你所有的数据u
4，
```$xslt
Exception in thread "Thread-8" java.lang.RuntimeException: org.neo4j.unsafe.impl.batchimport.cache.idmapping.string.
DuplicateInputIdException: Id '刘平' is defined more than once in group 'global id space'

```
如果确定自己的数据没有问题，那么请查看[编码格式](https://blog.csdn.net/lbyd2016/article/details/84554424)
[链接](https://neo4j.com/docs/operations-manual/3.5/tools/import/file-header-format/#import-tool-id-spaces)
被动解决方案就是忽略这个问题。在import时加入
>--ignore-duplicate-nodes=true