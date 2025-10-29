# -Mini-E-Commerce-Order-Processor

Total 10 Team from Programming of Data Analysis



\# 🛒 Mini E-Commerce Order Processor



A modular Python project that simulates a real-world \*\*e-commerce checkout system\*\*.  

The system validates a shopping cart, applies discounts, calculates taxes and shipping, awards loyalty points, and produces both a receipt and exportable files.



---



\## 📦 Overview



\*\*Given:\*\*

\- A product \*\*catalog\*\*

\- A \*\*customer\*\* profile

\- A \*\*shopping cart\*\*

\- And available \*\*stock\*\*



\*\*The program:\*\*

1\. Validates and loads the catalog  

2\. Cleans and normalizes the cart  

3\. Checks inventory  

4\. Calculates subtotal  

5\. Applies discount rules  

6\. Computes taxes  

7\. Estimates shipping  

8\. Awards loyalty points  

9\. Generates a receipt  

10\. Exports order data (JSON + CSV)



This project is divided into \*\*10 functional teams\*\*, each implementing a pure function, coordinated by the `process\_order()` pipeline.



---



\## 🧩 Project Structure



checkout/

│

├── \_\_init\_\_.py 

├── src/

│ ├── \_\_init\_\_.py 

│ ├── team1\_catalog.py

│ ├── team2\_cart.py

│ ├── team3\_inventory.py 

│ ├── team4\_subtotal.py 

│ ├── team5\_discounts.py 

│ ├── team6\_tax.py 

│ ├── team7\_shipping.py 

│ ├── team8\_loyalty.py 

│ ├── team9\_receipt.py 

│ ├── team10\_export.py

│ └── pipeline.py # contains process\_order (integration)│

├── tests/

│ ├── test\_team1.py

│ ├── test\_team2.py

│ ├── ...

│ └── test\_integration.py

│

├── main.py # Main entry point

└── README.md # Project documentation







---



\## 🚀 How to Run



1\. \*\*Install Anaconda Distrubitur\*\*  

&nbsp;  Ensure Anaconda Distrubitur is installed and added to PATH.



2\. \*\*Run from the project root:\*\*

&nbsp;   Run Anaconda and launch Jupiter on anaconda.

&nbsp;   Then create New File \*Notebook\*.

&nbsp;   run code. 





