#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mini_project():
    #First of all import numpy, pandas, matplotlib and seaborn as these libraries are important for data analysis.
    import os
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import getpass
    
    print("\n\t\tDATA ANALYSIS MOBILE DATA SET") #Topic that will be shown on the top.
    print("\n\t\t\tWELCOME\n")
    userid = input("User ID: ")
    password= getpass.getpass("Password: ")
    if(userid=='admin' and password=='admin'):
        path = input("Enter the csv file path : ") #Ask user to enter the file path that should be in csv format only.
        path_n = path.replace('"','')
        print("\nYour file path is ",path_n) #It will show the path entered by the user.
        print("="*120)

        try:
            print("Does your data have any seperator?\n1-Yes\n2-No")
            data = input("Enter your choice: ")
            if(data=='1'):
                sep1 = input("Enter your seperator: ")
                df = pd.read_csv(path_n,sep=sep1) #It will read that csv file which was entered by the user.
            elif(data=='2'):
                df = pd.read_csv(path)

        except:
            path_new = path_n.replace(os.sep,'/')
            print("Does your data have any seperator?\n1-Yes\n2-No")
            data = input("Enter your choice: ")
            if(data=='1'):
                sep1 = input("Enter your seperator: ")
                df = pd.read_csv(path_new,sep1)
            elif(data=='2'):
                df = pd.read_csv(path_new)

        print(df) #It will show the data in tabular format to the user.
        print("="*120)

        steps = ['1','2','3','4','5']

        for i in steps:
            print("\nPress 1 to check Basic Info, Top 5, Bottom 5, Shape and Description of your Data.") #It will ask user to print basic analisis of their data.
            print("\nPress 2 to check if your data has null values or not.") #It will ask user if he/she is want to check null values present or not in their data.
            print("\nPress 3 to check the columns present in your data")
            print("\nPress 4 to plot the graphs")
            print("\nPress 5 to find correlation")
            print("\nPress 6 to exit")

            choice = input("\nEnter your choice : ") 

            if(choice=='1'): #if user enter 1 in their keyboard then this program will shoe the basic analysis which was mentioned above.
                print("\n\t\tBasic Info\n",df.info())
                print("="*120)
                print("\n\t\tTop 5 Data\n",df.head())
                print("="*120)
                print("\n\t\tBottom 5 Data\n",df.tail())
                print("="*120)
                print("\n\t\tShape = ",df.shape)
                print("="*120)
                print("\n\t\tSize = ",df.size)
                print("="*120)
                print("\n\t\tDescription\n",df.describe())
                print("="*120)
            elif(choice=='2'): #It will check the null values present in the data.
                print(df.isnull())
                if(df.isnull().sum().sum()!=0): #If null values are present this program will ask user what to do next.
                    print("\nYour data has null values.\nDo you want the sum of null values?\n1-Yes\n2-No")
                    choose = input("\nEnter your choice : ")
                    if(choose=='1'):
                        print("\nSum of null vaues = ",df.isnull().sum())
                    elif(choose=='2'):
                        print("\nHave a good analysis mate.")
                    print("\nDo you want to fill the null values?\n1-Yes\n2-No")
                    Choose = input("\nEnter your choice : ")
                    if(Choose=='1'): #It will fill all the null values with the help of pad method
                        df = df.fillna(method="pad")
                        print(df)
                else:
                    print("\n\t\tWoah!! Congratulations...\nYour data has no null values, we are good to go.")
                    print("="*120)
            elif(choice=='3'):
                print(df.columns) #It will show all the colummns present in the dataset
                print("="*120)
                regressive = [i for i in df.columns if df[i].dtype!='O']
                print("\nRegressive columns are: ", regressive)
                print("="*120)
                classified = [i for i in df.columns if df[i].dtype=='O']
                print("\nClassified columns are: ", classified)
                print("="*120)
                col_name = input("\nEnter a column name to get insights: ")
                print(df[col_name].unique())
            elif(choice=='4'):
                print("\nConsider the following to get the graph.")
                print("Press 1 for Scatter PLot")
                print("Press 2 for Box PLot")
                print("Press 3 for Line PLot")
                print("Press 4 for Distribution PLot")
                print("Press 5 for Count PLot")
                print("Press 6 for Heat Map")
                print("Press 7 to exit")
                graph_list = ['1','2','3','4','5','6','7']
                for i in graph_list:
                    plot = input("\nEnter your graph choice : ")
                    if(plot=='1'): #It will plot the scatterplot graph.
                        try:
                            Col1 = input("Enter the first column : ")
                            Col2 = input("Enter the second column : ")
                            if Col1 and Col2 in df.columns:
                                plt.scatter(df[Col1],df[Col2])
                                plt.title('Scatterplot for {} and {}'.format(Col1,Col2))
                                plt.show()
                                print("Do you want to see more graphs?\n1-Yes\n2-No")
                                graph = input("Enter your choice : ")
                                if(graph=='1'):
                                    continue
                                else:
                                    break
                            else:
                                print("\nPlease enter a valid choice!!")
                        except:
                            print("It is not possible to plot this graph.")
                    elif(plot=='2'): #It will plot the boxplot graph.
                        try:
                            Col1 = input("Enter the column : ")
                            #Col2 = input("Enter the second column : ")
                            if Col1 in df.columns:
                                sns.boxplot(x=Col1,data=df)
                                plt.title('Boxplot for {}'.format(Col1))
                                plt.show()
                                print("Do you want to see more graphs?\n1-Yes\n2-No")
                                graph = input("Enter your choice : ")
                                if(graph=='1'):
                                    continue
                                else:
                                    break
                            else:
                                print("\nPlease enter a valid choice")
                        except:
                            print("It is not possible to plot this graph.")                                
                    elif(plot=='3'): #It will plot the lineplot graph.
                        try:
                            Col1 = input("Enter the column : ")
                            if Col1 in df.columns:
                                sns.lineplot(df[Col1])
                                plt.title('Lineplot for {}'.format(Col1))
                                plt.show()
                                print("Do you want to see more graphs?\n1-Yes\n2-No")
                                graph = input("Enter your choice : ")
                                if(graph=='1'):
                                    continue
                                else:
                                    break
                            else:
                                print("\nPlease enter a valid choice")
                        except:
                            print("It is not possible to plot this graph.")
                    elif(plot=='4'): #It will plot the distribution plot graph.
                        try:
                            Col1 = input("Enter the column : ")
                            #Col2 = input("Enter the second column : ")
                            if Col1 in df.columns:
                                sns.distplot(df[Col1])
                                plt.title('Distribution Plot for {}'.format(Col1))
                                plt.show()
                                print("Do you want to see more graphs?\n1-Yes\n2-No")
                                graph = input("Enter your choice : ")
                                if(graph=='1'):
                                    continue
                                else:
                                    break
                            else:
                                print("\nPlease enter a valid choice") 
                        except:
                            print("It is not possible to plot this graph.")
                    elif(plot=='5'): #It will plot the countplot graph.
                        try:
                            Col1 = input("Enter the column : ")
                            #Col2 = input("Enter the second column : ")
                            if Col1 in df.columns:
                                sns.countplot(x=Col1, data = df)
                                plt.xticks(rotation='vertical')
                                plt.title('Count Plot for {}'.format(Col1))
                                plt.show()
                                print("Do you want to see more graphs?\n1-Yes\n2-No")
                                graph = input("Enter your choice : ")
                                if(graph=='1'):
                                    continue
                                else:
                                    break
                            else:
                                print("\nPlease enter a valid choice")
                        except:
                            print("It is not possible to plot this graph.")
                    elif(plot=='6'): #It will print the heat map.
                        try:
                            #Col1 = input("Enter the first column : ")
                            #Col2 = input("Enter the second column : ")
                            sns.heatmap(df)
                            plt.show()
                            print("Do you want to see more graphs?\n1-Yes\n2-No")
                            graph = input("Enter your choice : ")
                            if(graph=='1'):
                                continue
                            else:
                                break
                        except:
                            print("It is not possible to plot this map.")
                    elif(plot=='7'):
                        break
                    else:
                        print("\n\t\tOops!! Please enter a valid choice.")
                print("Do you want to save your analised data in other file?\n1-Yes\n2-No")
                save = input("Enter your choice : ")
                if(save=='1'):
                    to_path = input("Enter the path and file name to save your file : ")
                    print("Your path is ",to_path)
                    df.to_csv(to_path) #It will save a csv file to the given path.
                else:
                    quit()
            elif(choice=='5'):
                print(df.corr())
            elif(choice=='6'):
                break
            else:
                print("\n\t\tOops!! Please enter a valid choice.")

        print("\n\t\tThank you!!")
    else:
        print("\nInvalid User ID and Password")
        
        
                    
mini_project()


# In[ ]:





# In[ ]:




