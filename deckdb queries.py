#!/usr/bin/env python
# coding: utf-8

# In[1]:


import duckdb
con = duckdb.connect(database=':memory:')
con = duckdb.connect(database='abhishekdb.duckdb',read_only=False)


# In[ ]:


con.execute("CREATE TABLE workers(std_id INTEGER, firstname VARCHAR, lastname VARCHAR, email VARCHAR, city VARCHAR, income INTEGER)")
con.execute("INSERT INTO workers VALUES (1,'Abhi', 'Vishwakarma','abhi@gmail.com','dto',10000), (2,'Ravi', 'Verma', 'ravi@gmail.com','Ranchi',20000), (3,'Pankaj', 'Prajapati', 'pankaj@gmail.com','Rehla',15000), (4,'Jeetu', 'Mishra', 'jeetu@gmail.com','Bhopal',50000),(5, 'Sapna', 'Sharma', 'sapna@gmail.com','Garhwa',22000),(6, 'Suhani', 'Vishwakarma', 'suhani@gmail.com','Indore',35000),(7, 'Arti', 'Sahu', 'arti@gmail.com','Bhopal',25000)")
con.execute("SELECT * FROM workers")
print(con.fetchall())


# In[3]:


con.execute("SELECT DISTINCT firstname FROM workers")
print(con.fetchall())


# In[4]:


con.execute("select count(*) from workers")
print(con.fetchall())


# WHERE CLAUSE

# In[5]:


con.execute("Select * from workers where std_id=7")
print(con.fetchall())


# GROUP BY

# In[ ]:


con.execute("select city, count(*) from workers GROUP BY city")
print(con.fetchall())


# In[ ]:


con.execute("select lastname, firstname from workers GROUP BY lastname,firstname")
print(con.fetchall())


# GROUPING SETS

# In[6]:


con.execute("select lastname, city from workers GROUP BY GROUPING SETS ((lastname,city), (city), (lastname))")
print(con.fetchall())


# HAVING

# In[ ]:


con.execute("select city, COUNT(*) FROM workers GROUP BY city HAVING COUNT(*) > 4")
print(con.fetchall())


# ORDER BY

# In[ ]:


con.execute("select * from workers order by city")
print(con.fetchall())


# In[ ]:


con.execute("select * from workers order by income DESC")
print(con.fetchall())


# LIMIT

# In[ ]:


con.execute("select * from workers limit 5")
print(con.fetchall())


# SAMPLE 

# In[ ]:


con.execute("select * from workers USING SAMPLE 2")
print(con.fetchall())


# UNNEST

# In[ ]:


con.execute("select UNNEST([1,2,3]), UNNEST([10,11,12])")
print(con.fetchall())


# In[ ]:


con.execute("select UNNEST([1,2,3]),10")
print(con.fetchall())


# WITH

# In[8]:


con.execute("WITH cte AS(SELECT 42 AS x) SELECT * FROM cte")
print(con.fetchall())


# In[9]:


con.execute("WITH cte as(select 42 as i),cte2 as (select i*100 as x from cte) SELECT * FROM cte2")
print(con.fetchall())


# WINDOWS 

# In[20]:


con.execute("SELECT Std_id, firstname, lastname, email, city, income, Avg(income) OVER(PARTITION BY city ORDER BY Std_id) AS Avg_income FROM workers")
print(con.fetchall())


# In[18]:


con.execute("select std_id, firstname, lastname, email, city, income, Max(income) OVER(PARTITION BY email ORDER BY Std_id) AS Max_income FROM workers")
print(con.fetchone())


# In[26]:


con.execute("select std_id, firstname, lastname, email, city, income, Min(income) OVER(PARTITION BY lastname ORDER BY firstname) AS Min_income FROM workers")
print(con.fetchall())


# In[ ]:




