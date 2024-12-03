# Experimenting With Datasets

See division of labour at bottom of this sheet.

## New Dataset

Our previous dataset was lacking magnitude, depth, and context. So, we made a few changes.

- Incorporated many more years

    - Every ~5 years since 1871

- Incorporated many more leagues

    - Previously, we had solely the MLB
    - Now, we have every single baseball major league, active and inactive
    
        - Including various regional and segregated leagues.

- Incorporated many more variables

    - For each year, we collected all available data regarding batting, pitching, and league team rankings.

- Including metadata

    - Minimal cleaning and filtering


## Dataset Utility

By combining records from different sources, leagues, and eras, we can observe differences in how data was recorded and kept between leagues and over time.

### Examining Data
- We can examine the variables used to measure performance between different leagues; is it true that less popular leagues performed worse?
- We can examine changes in variables over time; has overall performance increased over time, in parallel with rising popularity?

### Examining Metadata
- We can examine the amount parameters recorded in any given year between the Major League Baseball (MLB) and National Negro League (NNL). 
- Similarly, we can compare the amount of missing values between leagues. 

### Future Use (TO BE COMPLETED)

## Computational Methods (TO BE COMPLETED)


## Division of Labour

- **Data Collection:** We overhauled our dataset. There exist APIs that may have been useful in this process, however the individuals that designed these APIs hand-picked which pieces of data are accessible via the APIs (they cannot be used for our purposes, as they do not preserve the metadata). Therefore, we had to manually collect the data by using various websites' built-in export features. 

    - **Ethan, Nick, and Yosef** all equally worked to manually collect the data.

- **Data Cleaning:** Additionally, these export features work quite poorly, exporting in inconsistent formats. So, we had to manually clean a lot of the data. Lastly, since the website only allows exporting (to CSV) of data one league and one year at a time, we had to figure out a way to combine the CSVs (with inconsistent variables, missing values, and inconsistent formatting) into one CSV, all while preserving each individual record's metadata. This process took many hours.

    - **Ethan, Yosef, and Kohta** worked to clean the data and write python scripts to combine the CSVs into one. This process can be seen, beginning in the "raw_data" folder, using the scripts in "scripts" folder, and the final product in the "combined_data" folder. 

- **Data Visualization:** (TO BE COMPLETED)