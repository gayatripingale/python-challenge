
## Heroes Of Pymoli Data Analysis ##
* Trend 1: Number of male players exceeds the number of female players almost 5:1.(80%+ are males)
* Trend 2: Players int the age group of 15 to 30 years spend far more than the players in any other age group.
* Trend 3: Item ID 34 is the most profitable item, whereas Item ID 39 and 84 tied for the most purchased items.



```python
# Import Dependencies
import pandas as pd
import numpy as np
```


```python
# Import purchase_data.json as a DataFrame
purchase_df= pd.read_json('purchase_data.json')
purchase_df.head()


```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>



### Player Count ###



```python
# Total Number of Players
players= purchase_df["SN"].unique()
players_cnt = len(players)
players_cnt

```




    573




```python
# creating a Dataframe for Player Count
player_df = pd.DataFrame([{"Total Plyers":players_cnt}])
player_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Plyers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



### #Purchasing Analysis (Total) ####


```python
# To find :
# Number of Unique Items
# Average Purchase Price
# Total Number of Purchases
# Total Revenue
```


```python
# Dropping Duplicates 
no_dup= purchase_df.drop_duplicates(["Item ID"], keep='last')
no_dup.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>17</th>
      <td>22</td>
      <td>Female</td>
      <td>59</td>
      <td>Lightning, Etcher of the King</td>
      <td>1.65</td>
      <td>Aenarap34</td>
    </tr>
    <tr>
      <th>21</th>
      <td>15</td>
      <td>Male</td>
      <td>3</td>
      <td>Phantomlight</td>
      <td>1.79</td>
      <td>Iaralrgue74</td>
    </tr>
    <tr>
      <th>59</th>
      <td>15</td>
      <td>Male</td>
      <td>2</td>
      <td>Verdict</td>
      <td>3.40</td>
      <td>Ila44</td>
    </tr>
    <tr>
      <th>63</th>
      <td>23</td>
      <td>Male</td>
      <td>28</td>
      <td>Flux, Destroyer of Due Diligence</td>
      <td>3.04</td>
      <td>Ryanara76</td>
    </tr>
    <tr>
      <th>88</th>
      <td>23</td>
      <td>Male</td>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>Undotesta33</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Two wasys to count Number of Unique Items
# 1. Using count() 
unique_cnt=no_dup["Item ID"].count()
```


```python
#Number of Unique Items
# 2.using unique()
num_unq_items = purchase_df["Item ID"].unique()
unique_items=len(num_unq_items)
unique_items
```




    183




```python
# Total Number of Purchases
# You can find this by using count() function on any column. I am doing it on "Item ID" here

total_pur = purchase_df["Item ID"].count()
```


```python
# Total Revenue

total_rev = round(purchase_df["Price"].sum(),2)
total_rev
```




    2286.33




```python
#Average Purchase Price

avg_price = total_rev/total_pur
avg_price
```




    2.9311923076923074




```python
# Creating Purchse Analysis DataFrame to get a quick review

purchase_analysis_df = pd.DataFrame([{
    "Number of Unique Items": unique_items,
    "Average Purchase Price": round(avg_price,2),
    "Number of Purchases": total_pur,
    "Total Revenue": total_rev}],
columns = ["Number of Unique Items","Average Purchase Price","Number of Purchases","Total Revenue"])
# Adding "$" symbol

purchase_analysis_df.style.format({'Average Purchase Price': '${:.2f}', 'Total Revenue': '${:,.2f}'})
```




<style  type="text/css" >
</style>  
<table id="T_2b9e17b8_0fc2_11e8_97d9_a8667f3c136d" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Number of Unique Items</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Number of Purchases</th> 
        <th class="col_heading level0 col3" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_2b9e17b8_0fc2_11e8_97d9_a8667f3c136dlevel0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_2b9e17b8_0fc2_11e8_97d9_a8667f3c136drow0_col0" class="data row0 col0" >183</td> 
        <td id="T_2b9e17b8_0fc2_11e8_97d9_a8667f3c136drow0_col1" class="data row0 col1" >$2.93</td> 
        <td id="T_2b9e17b8_0fc2_11e8_97d9_a8667f3c136drow0_col2" class="data row0 col2" >780</td> 
        <td id="T_2b9e17b8_0fc2_11e8_97d9_a8667f3c136drow0_col3" class="data row0 col3" >$2,286.33</td> 
    </tr></tbody> 
</table> 



 ### Gender Demographics ###
 


```python
# In this we are finding:

# Percentage and Count of Male Players
# Percentage and Count of Female Players
# Percentage and Count of Other / Non-Disclosed

```


```python
# droping the duplicte names i.e SN
no_dup_players = purchase_df.drop_duplicates("SN")
no_dup_players.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Percentage and Count of Male Players
gender_cnt = no_dup_players['Gender'].value_counts().reset_index()
gender_cnt['% of Players'] = (gender_cnt['Gender']/players_cnt) * 100
gender_cnt.rename(columns = {'index': 'Gender', 'Gender': '# of Players'}, inplace = True)
gender_cnt.set_index(['Gender'], inplace = True)
gender_cnt.style.format({"% of Players": "{:.1f}%"})
```




<style  type="text/css" >
</style>  
<table id="T_2ba8669e_0fc2_11e8_af79_a8667f3c136d" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" ># of Players</th> 
        <th class="col_heading level0 col1" >% of Players</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_2ba8669e_0fc2_11e8_af79_a8667f3c136dlevel0_row0" class="row_heading level0 row0" >Male</th> 
        <td id="T_2ba8669e_0fc2_11e8_af79_a8667f3c136drow0_col0" class="data row0 col0" >465</td> 
        <td id="T_2ba8669e_0fc2_11e8_af79_a8667f3c136drow0_col1" class="data row0 col1" >81.2%</td> 
    </tr>    <tr> 
        <th id="T_2ba8669e_0fc2_11e8_af79_a8667f3c136dlevel0_row1" class="row_heading level0 row1" >Female</th> 
        <td id="T_2ba8669e_0fc2_11e8_af79_a8667f3c136drow1_col0" class="data row1 col0" >100</td> 
        <td id="T_2ba8669e_0fc2_11e8_af79_a8667f3c136drow1_col1" class="data row1 col1" >17.5%</td> 
    </tr>    <tr> 
        <th id="T_2ba8669e_0fc2_11e8_af79_a8667f3c136dlevel0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_2ba8669e_0fc2_11e8_af79_a8667f3c136drow2_col0" class="data row2 col0" >8</td> 
        <td id="T_2ba8669e_0fc2_11e8_af79_a8667f3c136drow2_col1" class="data row2 col1" >1.4%</td> 
    </tr></tbody> 
</table> 



### Purchasing Analysis (Gender) ###



```python
# The below each broken by gender:

# Purchase Count
# Average Purchase Price
# Total Purchase Value
# Normalized Totals
```


```python
# Purchase Count
gen_pur_cnt_df = pd.DataFrame(purchase_df.groupby("Gender")['Gender'].count())
gen_pur_cnt_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# creating gender total df
gen_pur_total_df = pd.DataFrame(purchase_df.groupby('Gender')['Price'].sum())
gen_pur_total_df 
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merging two dataframes gen_pur_cnt_df and gen_pur_total_df 
gen_pur_combined = pd.merge(gen_pur_cnt_df,gen_pur_total_df,left_index = True, right_index = True)
gen_pur_combined
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
# renaming the columns
gen_pur_combined.rename(columns = {'Gender': '# of Purchases', 'Price':'Total Purchase Value'}, inplace=True)
gen_pur_combined
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># of Purchases</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
#adds column for average purchase price.

gen_pur_combined['Average Purchase Price'] = gen_pur_combined['Total Purchase Value']/gen_pur_combined['# of Purchases']
gen_pur_combined
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># of Purchases</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
      <td>2.815515</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
      <td>2.950521</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
      <td>3.249091</td>
    </tr>
  </tbody>
</table>
</div>




```python
#merging gender counts into current df 
gen_pur_combined = gen_pur_combined.merge(gender_cnt, left_index = True, right_index = True)
gen_pur_combined
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># of Purchases</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase Price</th>
      <th># of Players</th>
      <th>% of Players</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
      <td>2.815515</td>
      <td>100</td>
      <td>17.452007</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
      <td>2.950521</td>
      <td>465</td>
      <td>81.151832</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
      <td>3.249091</td>
      <td>8</td>
      <td>1.396161</td>
    </tr>
  </tbody>
</table>
</div>




```python
# calculating and adding normalized total
gen_pur_combined['Normalized Totals'] = gen_pur_combined['Total Purchase Value']/gen_pur_combined['# of Players']
gen_pur_combined
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># of Purchases</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase Price</th>
      <th># of Players</th>
      <th>% of Players</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
      <td>2.815515</td>
      <td>100</td>
      <td>17.452007</td>
      <td>3.829100</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
      <td>2.950521</td>
      <td>465</td>
      <td>81.151832</td>
      <td>4.016516</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
      <td>3.249091</td>
      <td>8</td>
      <td>1.396161</td>
      <td>4.467500</td>
    </tr>
  </tbody>
</table>
</div>




```python
#deleting unwnted columns
del gen_pur_combined['% of Players']
del gen_pur_combined['# of Players']
gen_pur_combined
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># of Purchases</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase Price</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
      <td>2.815515</td>
      <td>3.829100</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
      <td>2.950521</td>
      <td>4.016516</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
      <td>3.249091</td>
      <td>4.467500</td>
    </tr>
  </tbody>
</table>
</div>




```python
# adding $ before the values
gen_pur_combined.style.format({'Total Purchase Value': '${:.2f}', 'Average Purchase Price': '${:.2f}', 'Normalized Totals': '${:.2f}'})
```




<style  type="text/css" >
</style>  
<table id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136d" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" ># of Purchases</th> 
        <th class="col_heading level0 col1" >Total Purchase Value</th> 
        <th class="col_heading level0 col2" >Average Purchase Price</th> 
        <th class="col_heading level0 col3" >Normalized Totals</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136dlevel0_row0" class="row_heading level0 row0" >Female</th> 
        <td id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136drow0_col0" class="data row0 col0" >136</td> 
        <td id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136drow0_col1" class="data row0 col1" >$382.91</td> 
        <td id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136drow0_col2" class="data row0 col2" >$2.82</td> 
        <td id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136drow0_col3" class="data row0 col3" >$3.83</td> 
    </tr>    <tr> 
        <th id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136dlevel0_row1" class="row_heading level0 row1" >Male</th> 
        <td id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136drow1_col0" class="data row1 col0" >633</td> 
        <td id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136drow1_col1" class="data row1 col1" >$1867.68</td> 
        <td id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136drow1_col2" class="data row1 col2" >$2.95</td> 
        <td id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136drow1_col3" class="data row1 col3" >$4.02</td> 
    </tr>    <tr> 
        <th id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136dlevel0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136drow2_col0" class="data row2 col0" >11</td> 
        <td id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136drow2_col1" class="data row2 col1" >$35.74</td> 
        <td id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136drow2_col2" class="data row2 col2" >$3.25</td> 
        <td id="T_2bdd525c_0fc2_11e8_a181_a8667f3c136drow2_col3" class="data row2 col3" >$4.47</td> 
    </tr></tbody> 
</table> 



### Age Demographics ###


```python
#The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
#Purchase Count
#Average Purchase Price
#Total Purchase Value
#Normalized Totals
```


```python
#creates a column 'age_bin' based on conditional of age range
purchase_df.loc[(purchase_df['Age'] < 10), 'age_bin'] = "< 10"
purchase_df.loc[(purchase_df['Age'] >= 10) & (purchase_df['Age'] <= 14), 'age_bin'] = "10 - 14"
purchase_df.loc[(purchase_df['Age'] >= 15) & (purchase_df['Age'] <= 19), 'age_bin'] = "15 - 19"
purchase_df.loc[(purchase_df['Age'] >= 20) & (purchase_df['Age'] <= 24), 'age_bin'] = "20 - 24"
purchase_df.loc[(purchase_df['Age'] >= 25) & (purchase_df['Age'] <= 29), 'age_bin'] = "25 - 29"
purchase_df.loc[(purchase_df['Age'] >= 30) & (purchase_df['Age'] <= 34), 'age_bin'] = "30 - 34"
purchase_df.loc[(purchase_df['Age'] >= 35) & (purchase_df['Age'] <= 39), 'age_bin'] = "35 - 39"
purchase_df.loc[(purchase_df['Age'] >= 40), 'age_bin'] = "> 40"
purchase_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>age_bin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>35 - 39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>20 - 24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>30 - 34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>20 - 24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>20 - 24</td>
    </tr>
  </tbody>
</table>
</div>




```python
purchase_df[['age_bin', 'Age']].count()
```




    age_bin    780
    Age        780
    dtype: int64




```python
# purchase counts by age bin 
agebin_pur_cnt_df = pd.DataFrame(purchase_df.groupby('age_bin')['SN'].count())

```


```python
#Average Purchase Price by age bin
agebin_avg_price_df = pd.DataFrame(purchase_df.groupby('age_bin')['Price'].mean()) 

```


```python
#Total Purchase Value
agebin_total_purchse_df = pd.DataFrame(purchase_df.groupby('age_bin')['Price'].sum())

```


```python
#Normalized Totals. For this we need to do the following data manipulations.

# 1 drop the duplicates and find the unique values
no_dup_agebin_df = pd.DataFrame(purchase_df.drop_duplicates('SN', keep = 'last').groupby('age_bin')['SN'].count())

```


```python
#2 Merge the various dataframes
merge_agebin_df = pd.merge(agebin_pur_cnt_df, agebin_avg_price_df, left_index = True, right_index = True).merge(agebin_total_purchse_df, left_index = True, right_index = True).merge(no_dup_agebin_df, left_index = True, right_index = True)

```


```python
# 3 renames columns to the meaningful names
merge_agebin_df.rename(columns = {"SN_x": "# of Purchases", "Price_x": "Average Purchase Price", "Price_y": "Total Purchase Value", "SN_y": "# of Purchasers"}, inplace = True)

```


```python
# And now calculates normalized totals
merge_agebin_df['Normalized Totals'] = merge_agebin_df['Total Purchase Value']/merge_agebin_df['# of Purchasers']
merge_agebin_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># of Purchases</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th># of Purchasers</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>35</td>
      <td>2.770000</td>
      <td>96.95</td>
      <td>23</td>
      <td>4.215217</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>133</td>
      <td>2.905414</td>
      <td>386.42</td>
      <td>100</td>
      <td>3.864200</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>336</td>
      <td>2.913006</td>
      <td>978.77</td>
      <td>259</td>
      <td>3.779035</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>125</td>
      <td>2.962640</td>
      <td>370.33</td>
      <td>87</td>
      <td>4.256667</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>64</td>
      <td>3.082031</td>
      <td>197.25</td>
      <td>47</td>
      <td>4.196809</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>42</td>
      <td>2.842857</td>
      <td>119.40</td>
      <td>27</td>
      <td>4.422222</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>28</td>
      <td>2.980714</td>
      <td>83.46</td>
      <td>19</td>
      <td>4.392632</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>17</td>
      <td>3.161765</td>
      <td>53.75</td>
      <td>11</td>
      <td>4.886364</td>
    </tr>
  </tbody>
</table>
</div>




```python
#resting the  index for 
merge_agebin_df.index.rename("Age", inplace = True)


```


```python
# Styling and Formating the df
# formats
merge_agebin_df.style.format({'Average Purchase Price': '${:.2f}', 'Total Purchase Value': '${:.2f}', 'Normalized Totals': '${:.2f}'})
merge_agebin_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># of Purchases</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th># of Purchasers</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>35</td>
      <td>2.770000</td>
      <td>96.95</td>
      <td>23</td>
      <td>4.215217</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>133</td>
      <td>2.905414</td>
      <td>386.42</td>
      <td>100</td>
      <td>3.864200</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>336</td>
      <td>2.913006</td>
      <td>978.77</td>
      <td>259</td>
      <td>3.779035</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>125</td>
      <td>2.962640</td>
      <td>370.33</td>
      <td>87</td>
      <td>4.256667</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>64</td>
      <td>3.082031</td>
      <td>197.25</td>
      <td>47</td>
      <td>4.196809</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>42</td>
      <td>2.842857</td>
      <td>119.40</td>
      <td>27</td>
      <td>4.422222</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>28</td>
      <td>2.980714</td>
      <td>83.46</td>
      <td>19</td>
      <td>4.392632</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>17</td>
      <td>3.161765</td>
      <td>53.75</td>
      <td>11</td>
      <td>4.886364</td>
    </tr>
  </tbody>
</table>
</div>



### Top Spenders ### 


```python
## Identify the 5 most popular items by purchase count, then list (in a table):
# SN
# Purchase Count
# Average Purchase Price
# Total Purchase Value

```


```python
#Identify the 5 most popular items by purchase count, then list (in a table):


# gets a count of each item by grouping by Item ID and counting the number of each IDs occurances
pop5_SN = pd.DataFrame(purchase_df.groupby('SN')['SN'].count())
#sort from high to low total purchase count
pop5_SN.sort_values('SN', ascending = False, inplace = True)
#keep the first 6 rows because there is a tie
pop5_SN = pop5_SN.iloc[0:6][:]


```


```python
# gets a count of each item by grouping by Item ID and counting the number of each IDs occurances
pop5_SN = pd.DataFrame(purchase_df.groupby('Item ID')['Item ID'].count())
#sort from high to low total purchase count
pop5_SN.sort_values('Item ID', ascending = False, inplace = True)
#keep the first 6 rows because there is a tie
pop5_SN = pop5_SN.iloc[0:6][:]
#find the total purchase value of each item
pop5_items_total = pd.DataFrame(purchase_df.groupby('Item ID')['Price'].sum())
#merge purcahse count and total purcahse value 
pop5_items = pd.merge(pop5_SN, pop5_items_total, left_index = True, right_index = True)
#drop duplicate items from original Df
no_dup_items = purchase_df.drop_duplicates(['Item ID'], keep = 'last')
# merge to get all other info from the pop 6 using the no dup df
pop5_merge_ID = pd.merge(pop5_items, no_dup_items, left_index = True, right_on = 'Item ID')
#keep only neede columns
pop5_merge_ID = pop5_merge_ID[['Item ID', 'Item Name', 'Item ID_x', 'Price_y', 'Price_x']]
#reset index as item ID for aesthetics
pop5_merge_ID.set_index(['Item ID'], inplace = True)
# rename columns
pop5_merge_ID.rename(columns =  {'Item ID_x': 'Purchase Count', 'Price_y': 'Item Price', 'Price_x': 'Total Purchase Value'}, inplace=True)
#format
pop5_merge_ID.style.format({'Item Price': '${:.2f}', 'Total Purchase Value': '${:.2f}'})


```




<style  type="text/css" >
</style>  
<table id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136d" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Item Name</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Item Price</th> 
        <th class="col_heading level0 col3" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item ID</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136dlevel0_row0" class="row_heading level0 row0" >39</th> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow0_col0" class="data row0 col0" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow0_col1" class="data row0 col1" >11</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow0_col2" class="data row0 col2" >$2.35</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow0_col3" class="data row0 col3" >$25.85</td> 
    </tr>    <tr> 
        <th id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136dlevel0_row1" class="row_heading level0 row1" >84</th> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow1_col0" class="data row1 col0" >Arcane Gem</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow1_col1" class="data row1 col1" >11</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow1_col2" class="data row1 col2" >$2.23</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow1_col3" class="data row1 col3" >$24.53</td> 
    </tr>    <tr> 
        <th id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136dlevel0_row2" class="row_heading level0 row2" >31</th> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow2_col0" class="data row2 col0" >Trickster</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow2_col1" class="data row2 col1" >9</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow2_col2" class="data row2 col2" >$2.07</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow2_col3" class="data row2 col3" >$18.63</td> 
    </tr>    <tr> 
        <th id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136dlevel0_row3" class="row_heading level0 row3" >175</th> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow3_col0" class="data row3 col0" >Woeful Adamantite Claymore</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow3_col1" class="data row3 col1" >9</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow3_col2" class="data row3 col2" >$1.24</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow3_col3" class="data row3 col3" >$11.16</td> 
    </tr>    <tr> 
        <th id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136dlevel0_row4" class="row_heading level0 row4" >13</th> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow4_col0" class="data row4 col0" >Serenity</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow4_col1" class="data row4 col1" >9</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow4_col2" class="data row4 col2" >$1.49</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow4_col3" class="data row4 col3" >$13.41</td> 
    </tr>    <tr> 
        <th id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136dlevel0_row5" class="row_heading level0 row5" >34</th> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow5_col0" class="data row5 col0" >Retribution Axe</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow5_col1" class="data row5 col1" >9</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow5_col2" class="data row5 col2" >$4.14</td> 
        <td id="T_2c3d2346_0fc2_11e8_9fd6_a8667f3c136drow5_col3" class="data row5 col3" >$37.26</td> 
    </tr></tbody> 
</table> 




```python
del pop5_merge_ID["Item Name"]

```

### Most Popular Items ###



```python
# Identify the 5 most popular items by purchase count, then list (in a table):
# Item ID
# Item Name
# Purchase Count
# Item Price
# Total Purchase Value
```


```python
# Item ID
# grouping by Item ID and counting the number of each IDs 
top5_items_ID = pd.DataFrame(purchase_df.groupby('Item ID')['Item ID'].count())
#sort from high to low total purchase count
top5_items_ID.sort_values('Item ID', ascending = False, inplace = True)
top5_items_ID = top5_items_ID.iloc[0:6][:]

```


```python
# Item Name
#find the total purchase value of each item
top5_items_total = pd.DataFrame(purchase_df.groupby('Item ID')['Price'].sum())

```


```python
#merge purcahse count and total purcahse value 
top5_items = pd.merge(top5_items_ID, top5_items_total, left_index = True, right_index = True)

```


```python
#drop duplicate items from original Df
no_dup_items = purchase_df.drop_duplicates(['Item ID'], keep = 'last')

```


```python
# merge to get the info from the top 6 using the no dup df
top5_merge_ID = pd.merge(top5_items, no_dup_items, left_index = True, right_on = 'Item ID')
#keep only neede columns
top5_merge_ID = top5_merge_ID[['Item ID', 'Item Name', 'Item ID_x', 'Price_y', 'Price_x']]

```


```python
#reset index as item ID 
top5_merge_ID.set_index(['Item ID'], inplace = True)
# rename columns
top5_merge_ID.rename(columns =  {'Item ID_x': 'Purchase Count', 'Price_y': 'Item Price', 'Price_x': 'Total Purchase Value'}, inplace=True)
#format
top5_merge_ID.style.format({'Item Price': '${:.2f}', 'Total Purchase Value': '${:.2f}'})
```




<style  type="text/css" >
</style>  
<table id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136d" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Item Name</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Item Price</th> 
        <th class="col_heading level0 col3" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item ID</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136dlevel0_row0" class="row_heading level0 row0" >39</th> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow0_col0" class="data row0 col0" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow0_col1" class="data row0 col1" >11</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow0_col2" class="data row0 col2" >$2.35</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow0_col3" class="data row0 col3" >$25.85</td> 
    </tr>    <tr> 
        <th id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136dlevel0_row1" class="row_heading level0 row1" >84</th> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow1_col0" class="data row1 col0" >Arcane Gem</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow1_col1" class="data row1 col1" >11</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow1_col2" class="data row1 col2" >$2.23</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow1_col3" class="data row1 col3" >$24.53</td> 
    </tr>    <tr> 
        <th id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136dlevel0_row2" class="row_heading level0 row2" >31</th> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow2_col0" class="data row2 col0" >Trickster</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow2_col1" class="data row2 col1" >9</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow2_col2" class="data row2 col2" >$2.07</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow2_col3" class="data row2 col3" >$18.63</td> 
    </tr>    <tr> 
        <th id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136dlevel0_row3" class="row_heading level0 row3" >175</th> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow3_col0" class="data row3 col0" >Woeful Adamantite Claymore</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow3_col1" class="data row3 col1" >9</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow3_col2" class="data row3 col2" >$1.24</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow3_col3" class="data row3 col3" >$11.16</td> 
    </tr>    <tr> 
        <th id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136dlevel0_row4" class="row_heading level0 row4" >13</th> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow4_col0" class="data row4 col0" >Serenity</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow4_col1" class="data row4 col1" >9</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow4_col2" class="data row4 col2" >$1.49</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow4_col3" class="data row4 col3" >$13.41</td> 
    </tr>    <tr> 
        <th id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136dlevel0_row5" class="row_heading level0 row5" >34</th> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow5_col0" class="data row5 col0" >Retribution Axe</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow5_col1" class="data row5 col1" >9</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow5_col2" class="data row5 col2" >$4.14</td> 
        <td id="T_2c5f273a_0fc2_11e8_b02c_a8667f3c136drow5_col3" class="data row5 col3" >$37.26</td> 
    </tr></tbody> 
</table> 



### Most Profitable Items ###


```python
# Most Profitable Items

# Identify the 5 most profitable items by total purchase value, then list (in a table):
# Item ID
# Item Name
# Purchase Count
# Item Price
# Total Purchase Value
```


```python
# Identify the 5 most profitable items by total purchase value, then list (in a table):

# find total purcahse value and sort by decending order
top5_profit = pd.DataFrame(purchase_df.groupby('Item ID')['Price'].sum())
top5_profit.sort_values('Price', ascending = False, inplace = True)
# Top 5
top5_profit = top5_profit.iloc[0:5][:]

```


```python
#Item purchase count
pur_count_profit = pd.DataFrame(purchase_df.groupby('Item ID')['Item ID'].count())

```


```python
#Merging
top5_profit = pd.merge(top5_profit, pur_count_profit, left_index = True, right_index = True, how = 'left')
top5_merge_profit = pd.merge(top5_profit, no_dup_items, left_index = True, right_on = 'Item ID', how = 'left')
top5_merge_profit = top5_merge_profit[['Item ID', 'Item Name', 'Item ID_x', 'Price_y','Price_x']]

```


```python
#setting indes at Item IDtop5_merge_profit.set_index(['Item ID'], inplace=True)
top5_merge_profit.rename(columns = {'Item ID_x': 'Purchase Count', 'Price_y': 'Item Price', 'Price_x': 'Total Purchase Value'}, inplace = True)

#Styling and formating
top5_merge_profit.style.format({'Item Price': '${:.2f}', 'Total Purchase Value': '${:.2f}'})
```




<style  type="text/css" >
</style>  
<table id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136d" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Item ID</th> 
        <th class="col_heading level0 col1" >Item Name</th> 
        <th class="col_heading level0 col2" >Purchase Count</th> 
        <th class="col_heading level0 col3" >Item Price</th> 
        <th class="col_heading level0 col4" >Total Purchase Value</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136dlevel0_row0" class="row_heading level0 row0" >746</th> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow0_col0" class="data row0 col0" >34</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow0_col1" class="data row0 col1" >Retribution Axe</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow0_col2" class="data row0 col2" >9</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow0_col3" class="data row0 col3" >$4.14</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow0_col4" class="data row0 col4" >$37.26</td> 
    </tr>    <tr> 
        <th id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136dlevel0_row1" class="row_heading level0 row1" >705</th> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow1_col0" class="data row1 col0" >115</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow1_col1" class="data row1 col1" >Spectral Diamond Doomblade</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow1_col2" class="data row1 col2" >7</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow1_col3" class="data row1 col3" >$4.25</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow1_col4" class="data row1 col4" >$29.75</td> 
    </tr>    <tr> 
        <th id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136dlevel0_row2" class="row_heading level0 row2" >657</th> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow2_col0" class="data row2 col0" >32</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow2_col1" class="data row2 col1" >Orenmir</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow2_col2" class="data row2 col2" >6</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow2_col3" class="data row2 col3" >$4.95</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow2_col4" class="data row2 col4" >$29.70</td> 
    </tr>    <tr> 
        <th id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136dlevel0_row3" class="row_heading level0 row3" >716</th> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow3_col0" class="data row3 col0" >103</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow3_col1" class="data row3 col1" >Singed Scalpel</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow3_col2" class="data row3 col2" >6</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow3_col3" class="data row3 col3" >$4.87</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow3_col4" class="data row3 col4" >$29.22</td> 
    </tr>    <tr> 
        <th id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136dlevel0_row4" class="row_heading level0 row4" >779</th> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow4_col0" class="data row4 col0" >107</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow4_col1" class="data row4 col1" >Splitter, Foe Of Subtlety</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow4_col2" class="data row4 col2" >8</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow4_col3" class="data row4 col3" >$3.61</td> 
        <td id="T_2c7f55d4_0fc2_11e8_a825_a8667f3c136drow4_col4" class="data row4 col4" >$28.88</td> 
    </tr></tbody> 
</table> 


