from A01_module import Employee, ReceivedInvoice, IssuedInvoice
import csv
from datetime import datetime

employee_list = []
received_invoice = []
issued_invoice = []

with open('Employee.csv', 'r') as f1:
    reader1 = csv.reader(f1)
    for row in reader1:
        employee_list.append(Employee(row[0], row[1], row[2]))

with open('ReceivedInvoice.csv', 'r') as f2:
    reader2 = csv.reader(f2)
    for row in reader2:
        received_invoice.append(ReceivedInvoice(row[0], row[1]))

with open('IssuedInvoice.csv', 'r') as f3:
    reader3 = csv.reader(f3)
    for row in reader3:
        issued_invoice.append(IssuedInvoice(row[0], row[1]))

salary = 0
for employee in employee_list:
    salary += float(employee.salary)

monthly_received_invoice = {}
for invoice in received_invoice:
    d = datetime.strptime(invoice.date, '%d-%m-%Y')
    if d.month in monthly_received_invoice:
        monthly_received_invoice[d.month] += float(invoice.amount)
    else:
        monthly_received_invoice[d.month] = float(invoice.amount) + salary

monthly_issued_invoice = {}
for invoice in issued_invoice:
    d = datetime.strptime(invoice.date, '%d-%m-%Y')
    if d.month in monthly_issued_invoice:
        monthly_issued_invoice[d.month] += float(invoice.amount)
    else:
        monthly_issued_invoice[d.month] = float(invoice.amount)

for i in range(1, 13):
    print("Miesiąc:", i, "Wydatki: ", monthly_received_invoice[i], " Przychody: ", monthly_issued_invoice[i], " Bilans: ", round(monthly_issued_invoice[i]-monthly_received_invoice[i], 2))