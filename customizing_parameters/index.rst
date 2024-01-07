Customized API Paramaters
==================================


Welcome to the Focalx Customization Documentation. This guide is designed to provide customer with all the necessary information regarding custmizing the parts, damage types, category codes to seamleasly integrate with customer.

Purpose:

This documentation is intended for developers, system integrators, and technical project managers who are looking to leverage Focalx's capabilities within their own applications.


Part Customization
--------------------

Developers or customers can provide a part ID or name, which can then be mapped to the corresponding part IDs existing in their database.

Focalx will supply an Excel spreadsheet containing a list of part names. Customers are required to enter their corresponding IDs in this spreadsheet. If no specific IDs are provided, Focalx will default to using its standard part names and IDs.

Example Table Format
--------------------

The following table illustrates an example format. Here, the 'Customer ID' and 'Customer Part Name' columns can be customized by the customer. If they are not customized, the default Focalx part ID and name will be displayed.

+--------------------------------------+-------------+------------------+----+------------+
| Focalx Part ID                       | Customer ID | Customer Part Name | ID | Position   |
+======================================+=============+===================+====+============+
| 10fd44ce-ddbc-400c-8816-7ee9566c786d | 123         | Windscreen         | 35 | Left Front |
+--------------------------------------+-------------+-------------------+----+------------+
| 0bce82b9-3acb-4b87-9b9d-5ae696c05a40 | 183         | Door edge          | 35 | Left Front |
+--------------------------------------+-------------+-------------------+----+------------+


Here's a grid table followed by a simple table:

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+----------+----------+
| body row 5             | Cells may also be     |          |
|                        | empty: ``-->``        |          |