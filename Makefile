.PHONY: test generate lint doctor

doctor:
	python3 tools/doctor.py

generate:
	python3 tools/series_generator.py examples/series/series_ai_augmentation_atlas.json

lint:
	python3 tools/blueprint_linter.py examples/blueprints/example_academic_writing_vs.blueprint.md
