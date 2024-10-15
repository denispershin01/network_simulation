# Network Protocols

Work in which you need to implement 3 algorithms for data communication in the network.

At the moment the implementation of the algorithm “Flood” is in progress.

## Requirements

- [GNU Make](https://www.gnu.org/software/make/)

## How to Use

1. **Clone the repository:**

```bash
git clone https://github.com/infast1k/network_protocols.git
cd network_protocols
```

2. Install all required packages in `Requirements` section.

3. Install all dependencies using `poetry install`

4. Run `make app`


### Implemented Commands

* `make app` - up application

* `make test` - run tests


## Todo
* create class for logging network state after each round
    * information can be stored into dictionary with next fields: node_oid, buffer_length, sending_count, getting count
* implement gateways
