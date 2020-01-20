[![Build Status](https://travis-ci.org/USAP-Codes/usap-directory.svg?branch=master)](https://travis-ci.org/USAP-Codes/usap-directory) [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](code-of-conduct.md) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# USAP Directory

An online directory for alumni of the [United Students Achievers Program](http://www.edmattersafrica.org/united-students-achievers-program/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- Python 3.6+
- Docker(optional)

### Installing

- There are two ways to run the application. You can either run it in docker container(s) or in you virtual environment.

#### Docker

- This assumes you have docker daemon installed on your machine. Beauty of this it doesn't matter what machine you run this from, Windows, Linux, Mac.
- Check Makefile in ```./services``` folder
- Run the following command

``` makefile
make build_server # builds docker image and runs the application
```

- Check the ```./docker-compose.yml``` file. That's where the entrypoint script is specified.

## Running the tests

### Automated Tests

### Coding Style Tests

## Deployment

## Built With

* [Flask](https://palletsprojects.com/p/flask/)
* [React](https://reactjs.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)
* [ElasticSearch](https://www.elastic.co/products/elasticsearch)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) to learn how you can contribute to the project.

## Code of Conduct

Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [releases on this repository](https://github.com/USAP-Codes/usap-directory/releases).

## Authors

* Tendai Mudyiwa ([@tendaitt](https://github.com/tendaitt))
* Felix Gondwe ([@felixgondwe](https://github.com/felixgondwe))
* [Contributors](https://github.com/USAP-Codes/usap-directory/graphs/contributors)

## License

This project is licensed under the MIT License. More information can be found [here](LICENSE).
