### KAFKA PRODUCER CONSUMER

## Prompt
```
Create a simple producer and consumer system using Confluent Cloud, and the kafka tools  bundled with the apache/kafka docker container.  The producers and consumers should be scalable independent of one another and should continuously produce traffic until they are stopped.
Top Selling Products Pipeline
Prompt: You will be provided a GitHub repository during the interview.  Use the files within to create a stream that takes in orders and products and uses Flink to surface top-selling products
```
## Goals
- Separate out the producer & consumer into independently scalable services
- Allow ability to scale them independently via docker-compose file
- Use flink to pull events from orders and report the top selling orders in a seperate stream

## Structure
/consumer - a flink based consumer that monitors the orders topic and find the best selling products and uploads them to a seperate topic.
/producer - a classic confluent producer that randomly produces events on the orders topic



## Issues
I did not have access to the Github repository so I made the producer randomly produce the data instead.

