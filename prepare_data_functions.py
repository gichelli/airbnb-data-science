import pandas as pd
import numpy as np
from collections import defaultdict
# import prepare_data as s # come back to here

# def display_gif(fn):
#     return '<img src="{}">'.format(fn)

#create a dataframe of each string you want to search for in each row
def total_count(df, col1, col2, look_for):
    new_df = defaultdict(int)
    #loop through list of ed types
    for val in look_for:
        #loop through rows
        for idx in range(df.shape[0]):
            #if the ed type is in the row add 1
            if val in df[col1][idx]:
                new_df[val] += int(df[col2][idx])
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [col1, col2]
    new_df.sort_values('count', ascending=False, inplace=True)
    return new_df


#function to clean data and plot

def clean_plot(df, title, col_name, look_for, plot):  
    clean = df[col_name].value_counts().reset_index()
    clean.rename(columns={'index': 'ammount', col_name: 'count'}, inplace=True)
    clean_lf = total_count(clean, 'ammount', 'count', look_for)
    clean_lf.set_index('ammount', inplace=True)
    if plot:
        (clean_lf/clean_lf.sum()).plot(kind='bar', legend=None);
        plt.title(title);
        plt.show()
    props_clean_lf = clean_lf/clean_lf.sum()
    return props_clean_lf

# def test(df, raya):
#   new_df = defaultdict(int)
#   return new_df
#   #return "hi"

# def weekly_price_clean1(no_null_week, title, plot):
#     weekly_price = no_null_week['weekly_price'].value_counts().reset_index()
#     weekly_price.rename(columns={'index': 'ammount', 'weekly_price': 'count'}, inplace=True)
#     price_lf = t.total_count(weekly_price, 'ammount', 'count', look_for_wprice)

#     price_lf.set_index('ammount', inplace=True)
#     if plot:
#         (price_lf/price_lf.sum()).plot(kind='bar', legend=None);
#         plt.title(title);
#         plt.show()
#     props_price_lf = price_lf/price_lf.sum()
#     return props_price_lf


#function to get values from a column
# def get_strings(str_values):
#     '''
#     INPUT:
#     values - should be a set of all descriptions in the dataset - each description should be a string.  You should not need to change the values variable at all if your function works correctly.

#     This function will print a statement related to whether or not you provided the correct solution for the get_description function
#     '''
#     val_type = type(next(iter(values)))
#     if values == s.values:
#         print("Nice job it looks like your function works correctly!")
#     elif val_type != str:
#         print("Oops - Looks like your column descriptions aren't strings.")
#     else:
#         print("Though you did provide the correct data type, your result does not match what we were expecting.  Try again.\n\n  Your function should return the description for any column name passed to it.")

# def get_strings(column_name, schema=listings):
#     '''
#     INPUT - schema - pandas dataframe with the schema of the developers survey
#             column_name - string - the name of the column you would like to know about
#     OUTPUT - 
#             desc - string - the description of the column
#     '''
#     desc = list(schema[schema['Column'] == column_name]['Question'])[0]
#     return desc

#test your code
#Check your function against solution - you shouldn't need to change any of the below code
#get_description(df.columns[0]) # This should return a string of the first column description



## A Look at the Data
# Question 1
def check_rows_cols(num_rows, num_cols):
    '''
    INPUT:
    num_rows - int the number of rows in df
    num_cols - int the number of cols in df

    This function will print a statement related to whether or not you provided the correct number of rows and columns of the dataset.
    '''
    if num_rows == s.num_rows:
        print("Nice job there are {} rows in the dataset!".format(num_rows))
    else:
        print("That doesn't look like what we were expecting for the number of rows.")

    if num_cols == s.num_cols:
        print("Nice job there are {} columns in the dataset!".format(num_cols))
    else:
        print("That doesn't look like what we were expecting for the number of columns.")


# Question 2
def no_null_cols(no_nulls):
    '''
    INPUT:
    no_nulls - a set of columns with no missing values

    This function will print a statement related to whether or not you provided the correct set of columns with no missing values
    '''
    if no_nulls == s.no_nulls:
        print("Nice job that looks right!")
        return display_gif('https://bit.ly/2K9X0gD')
    else:
        print("That doesn't look like for the set of no nulls.  There should be {} columns in your list".format(len(s.no_nulls)))
        return display_gif('https://bit.ly/2Hog74V')
        

# Question 3
def most_missing_cols(most_missing_cols):
    '''
    INPUT:
    most_missing_cols - a set of columns with more than 75% of the values in the column missing

    This function will print a statement related to whether or not you provided the correct set of columns with more than 75% of the values in the column missing
    '''
    if most_missing_cols == s.most_missing_cols:
        print("Nice job that looks right!")
    else:
        print("That doesn't look like for the set of most nulls.  There should be {} columns in your list".format(len(s.most_missing_cols)))

















