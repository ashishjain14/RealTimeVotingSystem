# RealTimeVotingSystem

A real-time voting system built with Python, PostgreSQL, Kafka and Spark. This project simulates voter and candidate data, stores them in a database, and streams voter information to Kafka for real-time processing.

## Features
- Candidate and voter data generation using randomuser.me API
- PostgreSQL database for storing candidates, voters, and votes
- Kafka producer for streaming voter data
- Simple architecture for real-time voting simulation


## Updated Architecture

```
+-------------------+      +-------------------+      +-------------------+      +-------------------+      +-------------------+
|   Data Generator  | ---> |   PostgreSQL DB   | ---> |   Kafka Producer  | ---> |   Spark Streaming | ---> |   Streamlit App   |
| (Candidates &     |      | (candidates,      |      | (voter/vote data  |      | (real-time vote   |      | (live dashboard   |
|  Voters via API)  |      |  voters, votes)   |      |  sent to Kafka)   |      |  aggregation)     |      |  & analytics)     |
+-------------------+      +-------------------+      +-------------------+      +-------------------+      +-------------------+
```

- **Data Generator**: Fetches random user data for voters/candidates.
- **PostgreSQL DB**: Stores all entities and relationships.
- **Kafka Producer**: Streams voter/vote data to Kafka topics.
- **Spark Streaming**: Reads votes from Kafka, aggregates in real-time, checkpoints state for fault tolerance.
- **Streamlit App**: Connects to Kafka and PostgreSQL, displays live voting stats and analytics.

## Prerequisites
- Python 3.8+
- PostgreSQL
- Kafka (local or remote broker)
- Docker (optional, for containerized setup)

## Installation


### 1. Clone the repository
```sh
git clone https://github.com/ashishjain14/RealTimeVotingSystem.git
cd RealTimeVotingSystem
```

### 2. Create and activate a virtual environment
```sh
python3 -m venv venv
source venv/bin/activate
```

- **Zookeeper** (for Kafka coordination)
- **Kafka Broker** (for message streaming)
- **PostgreSQL** (for database)
- **Spark Master & Worker** (for distributed processing)

To start all services, run:
```sh
docker-compose up
```
This will start all containers in the background. You can check logs with:
```sh
docker-compose logs -f
```

#### Service Ports
- Zookeeper: `2181`
- Kafka Broker: `9092` (localhost)
- PostgreSQL: `5432`
- Spark Master: `8080` (web UI), `7077` (cluster)

#### PostgreSQL Credentials
- User: `postgres`
- Password: `postgres`
- Database: `voting`

#### Kafka Broker
- Accessible at `localhost:9092`

#### Spark
- Spark Master UI: [http://localhost:9090](http://localhost:9090)

### 5. (Optional) Manual setup
If you prefer to run services manually, install and configure each service as per your environment.


## Steps to Run the Streamlit App

1. **Start all services** (Kafka, PostgreSQL, Zookeeper, Spark) using Docker Compose:
   ```sh
   docker-compose up
   ```

2. **Install Python dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the main script** to generate data and stream to Kafka:
   ```sh
   python src/main.py
   ```

4. **Start Spark Streaming** to process votes:
   ```sh
   python src/spark-streaming.py
   ```

5. **Run the Streamlit dashboard**:
   ```sh
   streamlit run src/streamlit-app.py
   ```
   - This will launch a web dashboard showing live voting stats, candidate analytics, and visualizations.

## Project Structure
```
├── docker-compose.yml
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
```

## Customization
- Change the number of candidates or voters in `main.py`.
- Update database or Kafka connection settings as needed.

## License
This project is licensed under the MIT License.

# Test Coverage

To check your test coverage, use the `coverage` tool:

1. Run your tests with coverage:
   ```sh
   coverage run -m unittest discover tests
   ```
2. Generate a coverage report:
   ```sh
   coverage report -m
   ```
3. (Optional) Generate an HTML report:
   ```sh
   coverage html
   # Open htmlcov/index.html in your browser
   ```

This will show you which lines of code are covered by your tests and which are not.
