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
- Use flink to pull events from orders and report the top-selling orders in a separate stream

## Structure
The repository is laid out in a monorepo, each directory can run as a stand-alone directory; these stand-alone instances are coordinated via docker-compose

* /consumer - a flink based consumer that monitors the orders topic and find the best-selling products and uploads them to a separate topic.
* /producer - a classic confluent producer that randomly produces events on the orders topic



## Issues
I did not have access to the GitHub repository, so I made the producer randomly produce the data instead.


## Future Vision
In today's landscape, compliance is something that is met for a moment in time, not something that is  consistently validated - that changes today.

By monitoring specific event streams with custom-built connectors, Confluent gives your organization the ability to know you are compliant today, yesterday , & tomorrow.

Welcome to the world's first self monitoring auditing system. Simply enumerate your relevant datastream topics, ensure the correct connectors are set up, and watch risk disappear before your eyes for all applicable services.

Our connectors take compliance a step further with all relevant compliance datastreams being automatically setup and presented to you in real time via our process so risk is understood and managed at a glance. 

Don't risk hefty fines or embarrassing security leaks, stop issues before they start with real time compliance dashboards with Confluent Connect & Process.


### TODO:

- update docker-compose to kubernetes
- remove keys/secrets from code, pipe them into services via environment variables 


### Resources:
- If I needed to create a flink event creation from file I would use [this tutorial](https://medium.com/@priyankbhandia_24919/apache-flink-for-data-enrichment-6118d48de04).

