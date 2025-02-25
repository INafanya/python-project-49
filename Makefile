install: 
	uv sync

brain-games:
	uv run brain-game

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime

reinstall:
	uv build
	uv tool install --force dist/*.whl

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

make lint:
	uv run ruff check brain_game
	uv run ruff check brain_even
	uv run ruff check brain_calc
	uv run ruff check brain_gcd
	uv run ruff check brain_progression
	uv run ruff check brain_prime