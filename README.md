---

# Plane Operations Simulation

This project is a Python program that simulates airplane operations. The program will allow for increasing and decreasing the speed of airplanes, seating passengers, and simulating the take-off and landing of airplanes. Additionally, operations will be tracked using log files.

## Project Structure

### `data/`
This folder stores various data:
- **passenger.py**: Functions to generate a random number of passengers and their names.
- **speed.py**: Functions to randomly increase and decrease the airplane's speed.
- **planes.txt**: Data related to airplane types and their passenger capacities.
- **random_plane_selector.py**: Functions to randomly select an airplane type.

### `logging_info/`
This folder contains log configurations:
- **logging_config.py**: The file that configures the logs.

### `plane_data/`
This folder contains the data needed to define the characteristics and operations of airplanes:
- **plane.py**: Defines the main characteristics and operations of the `Plane` class.

### `process/`
This folder contains classes that perform various operations:
- **flight.py**: A class related to take-off, landing, and other flight operations.
- **passenger.py**: A class to add, remove, and manage passengers in the airplane.
- **speed.py**: Operations to increase and decrease the airplane's speed.

### `simulation_process/`
This folder contains functions that simulate all airplane operations:
- **simulation.py**: A function that simulates airplane operations (speed increase, adding passengers, take-off, landing).

### `tests/`
This folder contains tests:
- **test_flight.py**: Tests for flight operations.
- **test_passenger.py**: Tests for passenger operations.
- **test_plane.py**: Tests for the Plane class.
- **test_random_plane_selector.py**: Tests for random plane selection.
- **test_simulation.py**: Tests for the simulation.
- **test_speed.py**: Tests for speed operations.

### `main.py`
The main file that starts the program's core functionality. This is where the airplane is created, passengers are added, and airplane operations are simulated.

## Additional Libraries
The project uses the following libraries:
- **Faker**: For generating random passenger names.
- **pytest**: For writing and running tests.

## Installation
Follow the steps below to set up the environment:

1. **Python Version**: Python 3.12 or newer is required.

2. **Dependencies**: Install the required dependencies:
   - `Faker`: For generating random data.
   - `pytest`: For running tests.

3. **Activate the virtual environment**:
   ```
   pipenv shell
   ```

4. **Install the dependencies**:
   ```
   pip install -r requirements.txt
   ```

5. Install the environment via `pipenv`:
    ```bash
    pipenv install
    ```

## Usage
1. To start the simulation, run the `main.py` file:
    ```bash
    python main.py
    ```

## Tests
To run the tests, use the following command:

    ```bash
    pipenv run pytest
    ```

---