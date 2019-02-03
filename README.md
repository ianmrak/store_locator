Store finder
================================
This is a simple program to find the closest store within a list using a provided address

Project Structure
-----------------
This project has two packages:
* `com.store_finder` contains program files.
* `com.tests` contains `unittest` test cases.

Running the Program
-------------------
* Requires a Google Geocoding API key assigned to `API_KEY` env variable
    * https://developers.google.com/maps/documentation/geocoding/get-api-key
* From the terminal you are running the program: 
    * `export API_KEY=<your_key>`
* From the project base in the terminal run:
    * `python com/store_finder/main.py **args**`
    
Arguments
---------
**Required**:

Address (can provide full address or zip in either of the following arguments, but NOT both)
* `--address=<address here>`
* `--zip=<address here>`

**Optional** 

Units
* Accepted inputs: `imperial, metric, miles, km` (default is imperial)
* `--units=<input>`

Output
* Accepted inputs: `json, text` (default is text)
* `--output=<input>`

Running Tests
-------------

To run tests from the example project root directory, run one of the following commands:

* `python -m unittest discover` to discover all unit tests in a project
* `python -m unittest com.tests.**module**` to run the test module by name