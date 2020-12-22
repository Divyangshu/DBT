from flask import Flask, request, render_template
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pyodbc
#connection to database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-F10PM3M\SQLEXPRESS;'
                      'Database=MOVIES;'
                      'Trusted_Connection=yes;');

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("script.html")

@app.route("/data", methods = ["GET", "POST"])
def data():
    option = request.form['BB']
    if option == 'option1':
        data=pd.read_sql("SELECT * FROM customers",conn)
        result=data.to_html()
        data2 = pd.read_sql("select Area,count(Area) as Total_Customers from customers group by Area",conn)
        result=data2.to_html()
        sns.barplot(x='Area',y='Total_Customers',data=data2)
        plt.xlabel(' Area')
        plt.ylabel('Number of customers')
        plt.title('Area wise customers')
        plt.savefig('static/customers1.jpg')
        result=append_html(result,['customers1.jpg'])
    elif option == 'option2':
        data = pd.read_sql("SELECT * FROM employees",conn)
        result=data.to_html()
        data2=pd.read_sql("select Employee_first_name,count(EID) as Total_tickets_sold from employees group by Employee_first_name", conn)
        result=data2.to_html()
        sns.barplot(x='Employee_first_name',y='Total_tickets_sold',data=data2)
        plt.xlabel('Employee_first_name')
        plt.ylabel('Number of tickets')
        plt.title('Employee wise tickets')
        plt.savefig('static/employee1.jpg')
        result=append_html(result,['employee1.jpg'])
    elif option == 'option3':
        data = pd.read_sql("SELECT * FROM screen", conn)
        result=data.to_html()
        data2=pd.read_sql("select Screen_type,count(TICKID) as Total_customers from screen group by Screen_type", conn)
        result=data2.to_html()
        sns.barplot(x='Screen_type',y='Total_customers',data=data2)
        plt.xlabel('Screen type')
        plt.ylabel('Number of customers')
        plt.title('Screen wise customers')
        plt.savefig('static/screen1.jpg')
        result=append_html(result,['screen1.jpg'])
    elif option == 'option4':
        data = pd.read_sql("SELECT * FROM shows", conn)
        result=data.to_html()
        data2=pd.read_sql("select Show_type,count(TICKID) as Total_customers from shows group by Show_type", conn)
        result=data2.to_html()
        sns.barplot(x='Show_type',y='Total_customers',data=data2)
        plt.xlabel('Shoq type')
        plt.ylabel('Number of customers')
        plt.title('Show wise customers')
        plt.savefig('static/show1.jpg')
        result=append_html(result,['show1.jpg'])
    elif option == 'option5':
        data = pd.read_sql("SELECT * FROM seats", conn)
        result=data.to_html()
    elif option == 'option6':
        data = pd.read_sql("SELECT * FROM movies", conn)
        result=data.to_html()
        data2=pd.read_sql("select Movie_name,count(TICKID) as Total_customers from movies group by Movie_name", conn)
        result=data2.to_html()
        sns.barplot(x='Movie_name',y='Total_customers',data=data2)
        plt.xlabel('Movie name')
        plt.ylabel('Number of customers')
        plt.title('Movie wise customers')
        plt.savefig('static/movie1.jpg')
        result=append_html(result,['movie1.jpg'])
    elif option == 'option7':
        data = pd.read_sql("SELECT * FROM review", conn)
        result=data.to_html()
    elif option == 'option8':
        data = pd.read_sql("SELECT * FROM customers", conn)
        result=data.to_html()
    elif option == 'option9':
        data = pd.read_sql("SELECT * FROM employees", conn)
        result=data.to_html()
    elif option == 'option10':
        data = pd.read_sql("SELECT * FROM screen", conn)
        result=data.to_html()
    elif option == 'option11':
        data = pd.read_sql("SELECT * FROM movies", conn)
        result=data.to_html()
    elif option == 'option12':
        data = pd.read_sql("SELECT * FROM shows", conn)
        result=data.to_html()
    return result
def append_html(result,image_names):
    for i in image_names:
        result=result+" <img src=\"static/"+i+"\" width=\"600\" height=\"500\">"
    return result

if __name__ == "__main__":
    app.run(debug=True)


