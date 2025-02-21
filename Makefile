install: 
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

re-install:
	uv build
	uv tool install --force dist/*.whl

brain-calc:
	uv run brain-calc

build:
	uv build

package-install:
	uv tool install --force dist/*.whl


make lint:
	uv run ruff check brain_game
	uv run ruff check brain_even
	uv run ruff check brain_calc