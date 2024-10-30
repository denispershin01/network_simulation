.PHONY: flood, 1, leach, 2
flood or 1:
	@python3.13 network_protocols/main.py flood

leach or 2:
	@python3.13 network_protocols/main.py leach

.PHONY: test
test:
	@pytest
