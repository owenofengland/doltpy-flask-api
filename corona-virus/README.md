# Novel Coronavirus (COVID-19) Dataset 

This dataset is an import of data from John Hopkins University CSSE. The source of this data is [this GitHub Repository](https://github.com/CSSEGISandData/COVID-19). Additionally, there are tables on disease characteristics sourced from the [China Center for Disease Control Feb. 11, 2020 report](http://weekly.chinacdc.cn/en/article/id/e53946e2-c6c4-41e9-9a9b-fea8db1a8f51). Lastly, there is individual case details sourced from [the Singapore government](https://www.wuhanvirus.sg/cases/search), [the Hong Kong government](https://wars.vote4.hk/en/cases), [the South Korean government](https://github.com/jihoo-kim/Coronavirus-Dataset/), and [the Philippines government](https://coronavirus-ph-api.now.sh/cases). This data updates hourly.

On the [case_details_virological_dot_org branch](https://www.dolthub.com/repositories/Liquidata/corona-virus/data/case_details_virological_dot_org), we have imported [data from virological.org](http://virological.org/t/epidemiological-data-from-the-ncov-2019-outbreak-early-descriptions-from-publicly-available-data/337). This data is of suspect quality but it is voluminous with approximately 45,000 individual cases, thus, the separate branch.

[This blog post published on Feb 23, 2020](https://www.dolthub.com/blog/2020-02-23-novel-coronavirus-dataset-in-dolt/) describes the dataset, how it was modeled, how it is imported, and some the features dolt provides. It's the best source of documentation on the dataset.

[This blog post from Mar 12, 2020](https://www.dolthub.com/blog/2020-03-12-coronavirus-case-details-dolt/) explains the how individual case details are sourced and collected. It also explains some of the views and sample queries in the repository that use the case details data. 

[This blog post from Mar 18, 2020](https://www.dolthub.com/blog/2020-03-18-coronavirus-case-details-using-branches/) describes the virological.org dataset, how it is imported and why it is on a separate branch.

# More Details

The source of the data has changed over time. Before Feb 7, the data was sourced from [this Google Sheet](https://docs.google.com/spreadsheets/d/1UF2pSkFTURko2OvfHWWlFpDFAr1UxCBA4JLwlSP6KFo). After Feb 7, the data was sourced from [this GitHub Repository](https://github.com/CSSEGISandData/COVID-19). The data was being updated at random timestamps before Feb. 14. That data is reflected in the `/archived_data/time_series/` directory. In Dolt, you can view that data on the `archived` branch. After Feb 14, the data was moved to `/csse_covid_19_data/csse_covid_19_time_series` and updated daily at 00:00:00 UTC. This daily data is reflected on the tip of master. 

The data is mirrored to Dolt every 12 hours by [this import script](https://github.com/liquidata-inc/liquidata-etl-jobs/blob/master/airflow_dags/corona-virus/import-data.pl).

Individual case details are [sourced from the Singapore government](https://www.wuhanvirus.sg/cases/search) by [this import script](https://github.com/liquidata-inc/liquidata-etl-jobs/blob/master/airflow_dags/corona-virus/import-case-details-singapore.pl). Individual case details are [sourced from the Hong Kong government](https://wars.vote4.hk/en/cases) by [this import script](https://github.com/liquidata-inc/liquidata-etl-jobs/blob/master/airflow_dags/corona-virus/import-case-details-hongkong.pl). Individual case details are [sourced from the South Korean government](https://github.com/jihoo-kim/Coronavirus-Dataset/) by [this import script](https://github.com/liquidata-inc/liquidata-etl-jobs/blob/master/airflow_dags/corona-virus/import-case-details-southkorea.pl). Individual case details are [sourced from the Philippines government](https://coronavirus-ph-api.now.sh/cases) by [this import script](https://github.com/liquidata-inc/liquidata-etl-jobs/blob/master/airflow_dags/corona-virus/import-case-details-philippines.pl). These scripts run every hour.

For additiional case details (~45,000) of lower quality, we maintain a separate branch called `case_details_virological_dot_org`. This is sourced from [this Google sheet](https://docs.google.com/spreadsheets/d/1itaohdPiAeniCXNlntNztZ_oRvjh0HsGuJXUJWET008/htmlview?sle=true&lsrp=2#gid=0) by [this import script](https://github.com/liquidata-inc/liquidata-etl-jobs/blob/master/airflow_dags/corona-virus/import-case-details-viro-dot-org.pl). The `case_details` table on this branch is a merge of the Singapore, Hong Kong, and Korea data with the virological.org data.

[This blog post](https://www.dolthub.com/blog/2020-02-10-introducing-sql-view-support-in-dolt/) provides a lot of context on the data through the lens of using SQL Views.

## Structure

The time series data is in two tables, `places` and `cases`. Places are identified by a `place_id`. The `place_id` is manually assigned by the import script.

In the `cases` table, each new observation receives an entry keyed by `place_id` and `observation_time`. At each timestamp, a `cases_count`, `death_count`, and `recovered_count` is added if the count changed since the last observation. There is a sample query in the query catalog that shows how to select the state of the cases table at a timestamp. 

There is `characteristics_*` tables sourced from the [China Center for Disease Control Feb. 11, 2020 report](http://weekly.chinacdc.cn/en/article/id/e53946e2-c6c4-41e9-9a9b-fea8db1a8f51). This data has a summary breakdown of cases and mortality by characteristics like age, sex, comorbid condition, etc. This data will not update automatically. It is a one time set of summary data. If anyone has raw data on patient characteristics, please email: tim@liquidata.co.

There is a `case_details` table that has individual cases with additional information like sex and age from Singapore, Hong Kong, and South Korea. This table can be used for deeper analysis. It has over 7500 individual patient entries. It is updated hourly if new data is found.

## Views

This dataset makes use of SQL Views. To see the current cases, deaths, and recoveries of Corona Virus by region, run `dolt sql -q "select * from current"`. To see the other available views, run `dolt sql -q "select * from dolt_schemas"`.
