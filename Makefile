.PHONY: flood, 1, leach, 2, aco, 3
flood or 1:
	@python3.13 network_protocols/main.py flood

leach or 2:
	@python3.13 network_protocols/main.py leach

aco or 3:
	@python3.13 network_protocols/main.py aco


