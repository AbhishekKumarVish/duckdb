DuckDB is a relational table-oriented database management system and supports SQL queries for producing analytical result.
It also comes with various features that are useful for data analytics.
 
For DuckDB, there is no DBMS server software to install, update and maintain.
DuckDB can process foreign data without copying.
DuckDB Python package can run queries directly on pandas data without ever importing any data.
 
DuckDB provides serious data management features. There is extensive support for complex queries in SQL with a large function library, windows functions etc.
 
DuckDB is deeply integrated into Python and R for efficient interactive data analysis.
 
The DuckDB Python API can be installed using pip install duckdb.
Standard DuckDB Python API provides a SQL interface 
 
 
 
DuckDB support three nested data types: LIST, STRUCT and MAP.
 
LIST : An ordered sequence of data values of the same type.
Each row must have the same data type within each LIST, but can have any number of elements.
 
List are similar to Postgres's ARRAY type. DuckDB uses the list terminology, but some array functions are provided for postgres compatibility
 
List can be created using the LIST_VALUE(exp,…)
CREATE TABLE list_table (int_list INT[], varchar_list VARCHAR[])
 
Retrieving one or more values from a list can be accomplished using brackets and slicing notation, or through list_functions like list_extract.
 
STRUCT : A dictionary of multiple named values, where each key is a string but the  
Value can be a different type for each key.
 
STRUCT are typically used to nest multiple columns into a single column, and the nested column can be of any type, including other STRUCT and LIST.
 
Struct can be created using the STRUCT_PACK(name expr,…..)
Retriving a values from a struct can be accomplished using dot notation, brackets notation, or through struct function like struct_extract.
 
MAP :  A dictionary of multiple named values, each key having the same type and each value
 having the same type. Keys and values can be different types from one another.
 
Creating Maps
CREATE TABLE map_table (map_col MAP(INT,DOUBLE));
 
Retrieving from Maps
Map use brackets notation for retriving values. This is due to the variety of types that can be used as a map key.
 
 
 
Transferring large datasets to and from DuckDB uses a separate API built around NumPy and Pandas, or Apache Arrow.
 
This works with entire columns of data instead of scalar values and is therefore far more efficient.
<<Duckdb.py>>

