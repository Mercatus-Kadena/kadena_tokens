# Kadena Fungible Tokens Database

## What is it ?
This repository serves as a centralized token Database. It aims to reference all existing fungible tokens in the Eco-System, and gives information to users regarding meta-data and artworks (logos).


This database is mainly used by Mercatus: https://www.mercatus.works.

Other projects, or wallets, are welcome to access and use this list.

## Listing policy

This database is "inclusive". Tokens can be listed as soon they are not obvious scam tokens.
Such "bad" behavior will include (but is not limited to):
  - Presence of functions in the contract, that allow for illegitimately changing the user's balances or guards.
  - History of unjustified manipulations (illegitimate mint, ...)

## How to add a new token or update information

Submit a Pull Request:
  - Add or update an item in `tokens.yaml`
  - Add or update the corresponding logo in `img`. The logo size must be less than 100 kB.

In the body of the PR, please include some information and rationale about the changes you're requesting.

A Github workflow exists to help to verify the integrity of the database, fields and artworks. Don't forget to check the green ticks in your PR, and do the required changes when some checks don't pass.

## No disclaimer

This database must not be considered as a "trusted database".

Maintainers only do some basic checks on token contracts. Users are encouraged to do their own research before investing.

Maintainers cannot be held liable for any resulting losses that you experience while accessing or using any of the listed tokens. Accordingly, you understand and agree to assume full responsibility for all the risks of using or buying listed tokens.
