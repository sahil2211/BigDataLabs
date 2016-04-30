Part 1 - Using a database for spatial queries
-------

1. Load the taxi data into MySQL.

2. Run a query to identify all trips whose drop-off points are in JFK. Report the result size and query execution time.

3. Run a query to identify all trips whose drop-off points are in LaGuardia. Report the result size and query execution time.

4. Now, create a spatial index on drop-off points.

5. Re-run the above two queries, and report the result sizes and query execution times. 

Part 2 - Using custom code for spatial queries
------

1. Read the taxi data using python.

2. Using the provided functions, identify all trips whose drop-off points are in JFK. Report the result size and query execution time.
This is accomplished by iterating through all trips, and for each trip checking whether the drop-off location is within the query polygon of not. 

3. Identify all trips whose drop-off points are in LaGuardia, using the same technique as above. Report the result size and query execution time.

4. Create a R-tree index on drop-off locations using the Rtree module.

5. Execute the above two queries using the Rtree. As mentioned in the lab, the Rtree only supports rectangular queries. So a polygonal query can be executed as follows:
	a. Obtain the bound of a given polygon
	b. Query on Rtree using this bound
	c. For each resulting point, check if that point is within the polygon or not (using a loop, similar to (2) above).

6. Report the result sizes and running times. Briefly discuss why the running times are different between (2,3) and (5).


Deliverable:
Due Monday, May 2, 2016 at 12:00pm (noon).
Submit 
1. A text file to NYU Classes that gives your answers to Part I,#2,#3,#5 and Part II,#2,#3,#5,#6.  
2. A text file with SQL commands used for Part 1
3. Python code for Part 2. 

