# Time women and men spend on leisure - Data package

This data package contains the data that powers the chart ["Time women and men spend on leisure"](https://ourworldindata.org/grapher/time-women-and-men-spend-on-leisure?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website.

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For normal countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The remaining columns are the data columns, each of which is a time series. If the CSV data is downloaded using the "full data" option, then each column corresponds to one time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data columns are transformed depending on the chart type and thus the association with the time series might not be as straightforward.

## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

### How we process data at Our World In Data
All data and visualizations on Our World in Data rely on data sourced from one or several original data providers. Preparing this original data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/)

## Detailed information about each time series


## Women's leisure time
Average minutes women spent on leisure activities out of 24 hours (1440 minutes). Average minutes spent in different activities includes both weekdays and weekends.

Leisure includes sports, participating/attending events, visiting or entertaining friends,  TV or radio at home, and other leisure activities.


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
OECD Gender Data (2020) – processed by Our World in Data

#### Full citation
OECD Gender Data (2020) – processed by Our World in Data. “Women's leisure time” [dataset]. OECD Gender Data (2020) [original data].
Source: OECD Gender Data (2020) – processed by Our World In Data

### Additional information about this data
Australia, Belgium, Estonia, Greece, Hungary, Lithuania, Luxembourg, Mexico, Poland, Sweden, Turkey, and China time use estimates are not fully comparable, due to differences in the age of reference. The remaining countries' age of reference are between 15-64.

Note: Data are normalized to 1440 minutes per day. In other words, for those countries for which the time use does not sum up to 1440 minutes, the missing minutes are equally distributed across all activities. 

The survey years also differ amongst the countries included. The second link above includes a breakdown of the minutes spent in sub-activities that make up each of the five activities in this dataset: paid work or study, unpaid work, personal care, leisure, and other (which includes religious/spiritual activities and civic obligations).

Survey year used by country:
Australia	(2006); Austria	(2008/09); Belgium (2013); Canada	(2015); Denmark (2001); Estonia (2009/10); Finland (2009/10); France (2009/10); Germany (2012/13); Greece (2013); Hungary (2010); Ireland (2005); Italy (2013/14); Japan (2016); Korea (2014); Latvia (2003); Lithuania (2003); Luxembourg (2013); Mexico (2014); Netherlands (2016); New Zealand (2009/10); Norway (2010/11); Poland	(2013); Portugal (1999); Slovenia (2000/01); Spain (2009/10); Sweden (2010); Turkey (2014/15); UK (2014/15); US (2018); China (2008); India (1998/99); South Africa (2010).

OECD estimates based on national time use surveys. Methodological documentation on national time-use surveys used for the estimates is in Miranda V. (2011) "Cooking, Caring and Volunteering: Unpaid Work Around the World" available at: https://www.oecd-ilibrary.org/social-issues-migration-health/cooking-caring-and-volunteering-unpaid-work-around-the-world_5kghrjm8s142-en


## Men's leisure time
Average minutes men spent on leisure activities out of 24 hours (1440 minutes). Average minutes spent in different activities includes both weekdays and weekends.

Leisure includes sports, participating/attending events, visiting or entertaining friends,  TV or radio at home, and other leisure activities.


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
OECD Gender Data (2020) – processed by Our World in Data

#### Full citation
OECD Gender Data (2020) – processed by Our World in Data. “Men's leisure time” [dataset]. OECD Gender Data (2020) [original data].
Source: OECD Gender Data (2020) – processed by Our World In Data

### Additional information about this data
Australia, Belgium, Estonia, Greece, Hungary, Lithuania, Luxembourg, Mexico, Poland, Sweden, Turkey, and China time use estimates are not fully comparable, due to differences in the age of reference. The remaining countries' age of reference are between 15-64.

Note: Data are normalized to 1440 minutes per day. In other words, for those countries for which the time use does not sum up to 1440 minutes, the missing minutes are equally distributed across all activities. 

The survey years also differ amongst the countries included. The second link above includes a breakdown of the minutes spent in sub-activities that make up each of the five activities in this dataset: paid work or study, unpaid work, personal care, leisure, and other (which includes religious/spiritual activities and civic obligations).

Survey year used by country:
Australia	(2006); Austria	(2008/09); Belgium (2013); Canada	(2015); Denmark (2001); Estonia (2009/10); Finland (2009/10); France (2009/10); Germany (2012/13); Greece (2013); Hungary (2010); Ireland (2005); Italy (2013/14); Japan (2016); Korea (2014); Latvia (2003); Lithuania (2003); Luxembourg (2013); Mexico (2014); Netherlands (2016); New Zealand (2009/10); Norway (2010/11); Poland	(2013); Portugal (1999); Slovenia (2000/01); Spain (2009/10); Sweden (2010); Turkey (2014/15); UK (2014/15); US (2018); China (2008); India (1998/99); South Africa (2010).

OECD estimates based on national time use surveys. Methodological documentation on national time-use surveys used for the estimates is in Miranda V. (2011) "Cooking, Caring and Volunteering: Unpaid Work Around the World" available at: https://www.oecd-ilibrary.org/social-issues-migration-health/cooking-caring-and-volunteering-unpaid-work-around-the-world_5kghrjm8s142-en


## Population
Population by country, available from 10,000 BCE to 2023, based on data and estimates from different sources.
Last updated: July 15, 2024  
Next update: July 2026  
Date range: 10000 BCE – 2023 CE  
Unit: people  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
HYDE (2023); Gapminder (2022); UN WPP (2024) – with major processing by Our World in Data

#### Full citation
HYDE (2023); Gapminder (2022); UN WPP (2024) – with major processing by Our World in Data. “Population – HYDE, Gapminder, UN – Long-run data” [dataset]. PBL Netherlands Environmental Assessment Agency, “History Database of the Global Environment 3.3”; Gapminder, “Population v7”; United Nations, “World Population Prospects”; Gapminder, “Systema Globalis” [original data].
Source: HYDE (2023); Gapminder (2022); UN WPP (2024) – with major processing by Our World In Data

### What you should know about this data
* Population is the most commonly used metric throughout Our World in Data. It is used directly to understand population growth over time, and indirectly to calculate per-capita indicators, making it easier to compare countries of different sizes.
* We construct this indicator by combining multiple sources covering different periods.
  - HYDE v3.3 (2023): historical estimates from 10,000 BCE to 1799.
  - Gapminder v7 (2022): for 1800-1949.
  - UN World Population Prospects (2024): for 1950 onwards, including 2100 projections.
  - Gapminder Systema Globalis (2023): additional source for former countries (Yugoslavia, USSR, etc.)
* Breaks in the data may occur at the boundaries between sources due to their methodological differences.
* You can read more about the sources and methodology in our [dedicated article](https://ourworldindata.org/population-sources). We also provide a table of sources showing the source we use for each country-year.
* We calculate geographical aggregates (continents, income groups, etc.) by summing individual country populations. For years before 1800, we rely directly on HYDE's values for continents to ensure historical consistency.

### Sources

#### PBL Netherlands Environmental Assessment Agency – History Database of the Global Environment
Retrieved on: 2024-01-02  
Retrieved from: https://doi.org/10.24416/UU01-AEZZIT  

#### Gapminder – Population
Retrieved on: 2023-03-31  
Retrieved from: http://gapm.io/dpop  

#### United Nations – World Population Prospects
Retrieved on: 2024-07-11  
Retrieved from: https://population.un.org/wpp/downloads/  

#### Gapminder – Systema Globalis
Retrieved on: 2023-03-31  
Retrieved from: https://github.com/open-numbers/ddf--gapminder--systema_globalis  

#### Notes on our processing step for this indicator
### Combination of different sources
We construct our long-run population data by combining multiple sources:

- 10,000 BCE–1799: historical estimates by HYDE (v3.3).

- 1800–1949: historical estimates by Gapminder (v7).

- 1950–2023: population records from the United Nations World Population Prospects (2024 revision).

**Geographical aggregates**

- For most years, we calculate aggregates by summing the population of member countries.
- We do this based on [our definition of continents](https://ourworldindata.org/world-region-map-definitions#our-world-in-data) and the [World Bank’s income groups](https://ourworldindata.org/grapher/world-bank-income-groups).
- The only exception is before 1800, where we use HYDE's estimates for continents (but not income groups).

For most of the years, we've estimated regional aggregates by summing the population of countries in each region. We've relied on [our continents](https://ourworldindata.org/world-region-map-definitions#our-world-in-data) and [World Bank income group definitions](https://ourworldindata.org/grapher/world-bank-income-groups). The only exception is before 1800, where we've used HYDE's estimates on continents (but not income groups).

**World**
- Before 1800: we use data from HYDE.
- 1800-1950: we estimate the global population by summing all available countries in the dataset.
- After 1950, we rely on estimates from the United Nations World Population Prospects.


## World regions according to OWID
Regions defined by Our World in Data, which are used in OWID charts and maps.
Last updated: January 1, 2023  
Date range: 2023–2023  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Our World in Data – processed by Our World in Data

#### Full citation
Our World in Data – processed by Our World in Data. “World regions according to OWID” [dataset]. Our World in Data, “Regions” [original data].
Source: Our World in Data

### Source

#### Our World in Data – Regions


    