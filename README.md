# Personal Stock/Investment Analysis Application

## Goal

Track a select few stocks and news/finacial reports. Take in the data from these stocks and perform various analyses on these stocks for trends and future predictions. 

## Architecture 

```
 ┌───────────────┐
 │ Stock API     │
 │ (AlphaVantage │
 │  /Yahoo/IEX)  │
 └───────┬───────┘
         │ Pull stock ticks (every few sec)
         ▼
 ┌───────────────┐
 │ Python Producer│
 │ (Docker)       │
 └───────┬───────┘
         │ Publish messages
         ▼
 ┌───────────────┐
 │ Kafka Broker  │
 │ (Docker)      │
 └───────┬───────┘
         │ Stream messages
         ▼
 ┌────────────────────────┐
 │ Spark Structured       │
 │ Streaming (Docker)     │
 │ - Moving averages      │
 │ - Anomalies            │
 │ - Feature engineering  │
 └─────────┬──────────────┘
           │ Write analytics
           ▼
 ┌────────────────────────┐
 │ Postgres (Docker)      │
 │ - raw stock data       │
 │ - processed metrics    │
 │ - news/sentiment       │
 └─────────┬──────────────┘
           │ Query data
           ▼
 ┌───────────────┐
 │ Grafana       │
 │ (Docker)      │
 │ - Dashboard:  │
 │   stock charts│
 │   analytics   │
 │   sentiment   │
 └───────────────┘
 
 (SCRAPY)
 ┌───────────────┐
 │ Scrapy Crawler│
 │ (Docker)      │
 └───────┬───────┘
         │ Push scraped news/reports
         ▼
     Kafka / Postgres
```
