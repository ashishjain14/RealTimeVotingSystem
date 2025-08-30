# RealTimeVotingSystem

A real-time voting system built with Python, PostgreSQL, and Kafka. This project simulates voter and candidate data, stores them in a database, and streams voter information to Kafka for real-time processing.

## Features
- Candidate and voter data generation using randomuser.me API
- PostgreSQL database for storing candidates, voters, and votes
- Kafka producer for streaming voter data
- Simple architecture for real-time voting simulation

## Architecture Diagram

```
+-------------------+      +-------------------+      +-------------------+
|   Data Generator  | ---> |   PostgreSQL DB   | ---> |   Kafka Producer  |
| (Candidates &     |      | (candidates,      |      | (voter data sent  |
|  Voters via API)  |      |  voters, votes)   |      |  to Kafka topic)  |
+-------------------+      +-------------------+      +-------------------+
```

- **Data Generator**: Fetches random user data for voters and candidates.
- **PostgreSQL DB**: Stores all entities and relationships.
- **Kafka Producer**: Streams voter data to the `voters_topic` for downstream consumers.

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

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Set up services using Docker Compose

This project provides a `docker-compose.yml` to easily set up all required services:

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

## Usage

1. **Run the main script:**
	```sh
	python main.py
	```
	- This will create tables, generate candidates and voters, and stream voter data to Kafka.

2. **Monitor Kafka topic:**
	- Use Kafka consumer tools to view messages on the `voters_topic`.

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