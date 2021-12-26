# html2csv

*Developed in virtual environment using python 3.10.0*

Command line tool to download HTML tables from webpages to local csvs.

### Usage
There is only a single positional argument `url`: From the root of the repo run `python html2csv.py <your webpage url>`. E.g.,
```
> python html2csv.py https://www.halhigdon.com/training-programs/half-marathon-training/novice-1-half-marathon/
Deleting the directory ./html2csv_output ...
Done.

Creating output directory at ./html2csv_output ...
Done.

Wrote table to csv: ./html2csv_output/html2csv_pandas_0.csv
Wrote table to csv: ./html2csv_output/html2csv_pandas_1.csv
Done.
```