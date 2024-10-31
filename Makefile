.PHONY: flood, 1, leach, 2, aco, 3
flood  1:
	@python3.13 network_protocols/main.py flood

leach  2:
	@python3.13 network_protocols/main.py leach

aco  3:
	@python3.13 network_protocols/main.py aco


