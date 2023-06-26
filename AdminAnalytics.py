import tkinter as tk
import matplotlib.pyplot as plt  # to create a graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # to plot the graph in the GUI
from pandas import DataFrame  # to store the data
from DBHelper import *



class Analytics:
    def __init__(self,frame,frame2,res):
        self.temp_root=frame
        self.temp_root2=frame2
        self.res2=res
        self.add_bar_graph("Total spent per day")
        self.add_pie_graph("Total spent per day")
        # self.add_line_graph("Total orders per day")

    def get_weekly_expense(self):
        x=self.res2['UserId']
        query = f""" Select today, amt
                    from expense_tracker.expense
                    where UserId=%s order by today limit 7
                """


        result =get_all_data(query,x)
        print(result)

        df1 = DataFrame(result[1:], columns=result[0]).groupby("today").sum()
        return df1
    def get_monthly_expense(self):
        x=self.res2['UserId']
        query = f""" Select amt as amount_spent_per_day
                    from expense_tracker.expense
                    where UserId=%s order by today limit 30
                """


        result =get_all_data(query,x)
        print(result)

        df1 = DataFrame(result[1:], columns=result[0])
        print(df1)
        return df1

    # def get_total_orders_data(self):
    #     query = """ Select OrderDate, FoodOrderId
    #                 from food_ordering.foodorder
    #                 order by OrderDate
    #             """
    #     result = get_all_data(query)
    #
    #     df = DataFrame(result[1:], columns=result[0]).groupby("OrderDate").count()
    #     return df

    def add_bar_graph(self, title):
        #1. get the data from db and create the dataframe
        #2. create the figure
        #2. create a subplot in the figure
        #3. create the GUI graph and link figure(2)
        # Plot the dataframe(1) in the subplot (2)



        # put the data in the data frame and give it back
        df1 = self.get_weekly_expense()

        #create the graph
        figure1 = plt.Figure(figsize=(9, 3), dpi=100)
        #create the subplot to store it in the figure
        ax1 = figure1.subplots()

        bar1 = FigureCanvasTkAgg(figure1, self.temp_root)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        #bar, barh, line,area,pie
        df1.plot(kind='bar', legend=True, ax=ax1, fontsize=5)
        ax1.set_title(title)

    def add_pie_graph(self, title):

        # 1. get the data from db and create the dataframe
        # 2. create the figure
        # 2. create a subplot in the figure
        # 3. create the GUI graph and link figure(2)
        # Plot the dataframe(1) in the subplot (2)

        # put the data in the data frame and give it back
        df1 = self.get_monthly_expense()

        # create the graph
        figure1 = plt.Figure(figsize=(5, 4.5), dpi=100)
        # create the subplot to store it in the figure
        ax1 = figure1.subplots()
        # plot = df1.plot(startangle=0,subplots=True)
        # plt.ylabel('')
        # percents = df1.to_numpy() * 100 / df1.to_numpy().sum()
        # plt.legend(bbox_to_anchor=(1.35, 1.1), loc='upper right',
        #            labels=['%s, %1.1f %%' % (l, s) for l, s in zip(df1.index, percents)])


        bar1 = FigureCanvasTkAgg(figure1, self.temp_root2)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        # bar, barh, line,area,pie
        col_list = df1[df1.columns[0]].values.tolist()
        print(col_list)

        df1.plot(kind='pie', ax=ax1,autopct="%.1f%%", fontsize=6,subplots=True,legend=False,labels=None)
        # plt.legend(legend, title="Percentage", bbox_to_anchor=(1.05, 0.5), loc="center right", fontsize=10)
        ax1.set_title("")
        # plt.pie( col_list,startangle=90, shadow=True,
        #         autopct='%1.2f%%')
        # plt.axis('equal')
        #
        # plt.show()
    # def add_line_graph(self, title):
    #     df2 = self.get_total_orders_data()
    #
    #     figure2 = plt.Figure(figsize=(7, 4), dpi=100)
    #     ax2 = figure2.subplots()
    #
    #     line2 = FigureCanvasTkAgg(figure2, self.temp_root)
    #     line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    #     df2.plot(kind='line', legend=True, ax=ax2, color='red', marker='o', fontsize=10)
    #     ax2.set_title(title)
    #

# r=tk.Tk()
# a=Analytics()
# r.mainloop()
