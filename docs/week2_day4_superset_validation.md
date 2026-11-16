\# Week 2 Day 4 – Superset Dashboard Validation



\## Date

16 November 2026



\## Team Member

Member 4 – Superset / BI



\## Objective



Validate the AtmoSync Superset dashboard and confirm that the configured Snowflake data source is accessible and the dashboard charts display telemetry analytics correctly.



\## Superset Validation



The AtmoSync Micro-Climate Analytics dashboard was opened in Apache Superset.



Initially, the dashboard displayed a Snowflake SQL access-control error because the Superset role did not have SELECT permission on:



```text

ATMOSYNC\_DB.RAW.SENSOR\_EVENTS\_ANALYTICS

