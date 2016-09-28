GYM_RUNTIME := ./src/kieser/stat/runtime.py

export PYTHONPATH := ./src:$(PYTHONPATH)

PYTHON_BIN := python
PYTHON_FLAGS := -tt
PYTHON_SHELL := ipython
PYTHON_SCRIPTS := $(GYM_RUNTIME)
PYTHON := $(PYTHON_BIN) $(PYTHON_FLAGS)

SETUP = $(PYTHON) setup.py

DB := mysql
ifeq ($(DB),mysql)
DB_CLIENT := mysql
DB_VERSION := $(shell $(DB_CLIENT) -V | cut -d ' ' -f 6 | cut -d . -f 1,2 )
endif
DB_SCHEMA := dbgym
DB_TABLE_PREFIX :=

SQL_BUILD := sql/build-$(DB)-$(DB_VERSION).sql
SQL_CLEAN := sql/clean.sql
SQL_DROP := sql/drop.sql
SQL_HOUSEKEEP := sql/housekeep-$(DB)-$(DB_VERSION).sql
SQL_ALL := $(SQL_BUILD) $(SQL_CLEAN) $(SQL_DROP) $(SQL_HOUSEKEEP)

KID_TEMPLATES := $(shell find src -type f -name '*.kid')
KID_PYTHON := $(patsubst %.kid,%.py,$(KID_TEMPLATES) )
KID_COMPILED := $(patsubst %.kid,%.pyc,$(KID_TEMPLATES) )
KID_OUT := $(patsubst %.kid,%.html,$(patsubst src/%,out/%,$(KID_TEMPLATES) ) )

TESTS := $(wildcard test/*.py)

.PHONY: \
	help install sdist bdist dist clean tests sql kid kidout load db console \
	database-build database-clean database-drop database-rebuild FORCE

help:
	@echo "Targets for $(MAKE):"
	@echo
	@echo "	install			Install this package"
	@echo "	sdist			Create a source distribution"
	@echo
ifdef TESTS
	@echo "	tests			Run all tests"
	@echo "	test/*.py		Run a test with that log"
	@echo
endif
	@echo "	database-build		Build the database"
	@echo "	database-clean		Clean the database of all data"
	@echo "	database-drop		Drop the tables from the database"
	@echo "	database-rebuild	Drop and build the database"
	@echo
	@echo "	kid			Build kid templates"
	@echo
	@echo "Environment variables:"
	@echo
	@echo "	DB_TABLE_PREFIX		Tables will be have this prefixed to their names"
	@echo "	DB_SCHEMA		Name of the schema to use"
	@echo

install: $(KID_PYTHON)
	$(SETUP) install -O1

sdist: $(KID_PYTHON)
	$(SETUP) sdist

bdist: $(KID_PYTHON)
	$(SETUP) bdist

dist: sdist bdist

clean:
	rm -rvf dist build MANIFEST out
	rm -rvf $(SQL_ALL)
	rm -rvf $(KID_PYTHON) $(KID_COMPILED)
	find src -type f \( -name '*.pyc' -o -name '*.pyo' \) -exec rm -vf {} \;
	find . -type f \( -name '*~' \) -exec rm -vf {} \;

tests: $(TESTS)

test/*.py: FORCE
	$(PYTHON) $@

database-build: $(SQL_BUILD)
	$(DB_CLIENT) $(DB_SCHEMA) < $<

database-clean: $(SQL_CLEAN)
	$(DB_CLIENT) $(DB_SCHEMA) < $<

database-drop: $(SQL_DROP)
	$(DB_CLIENT) $(DB_SCHEMA) < $<

database-housekeep: $(SQL_HOUSEKEEP)
	$(DB_CLIENT) $(DB_SCHEMA) < $<

database-rebuild: database-drop database-build

sql: $(SQL_ALL)

kid: $(KID_PYTHON) $(KID_COMPILED)

kidout: kid $(KID_OUT)

load:
	$(PYTHON) -m kieser/stat/load -

# Convenience targets

db:
	$(DB_CLIENT) $(DB_SCHEMA)

console:
	$(PYTHON_SHELL) $(PYTHON_SCRIPTS)

# Pattern targets

%.xhtml: %.html
	# The test at the end ignores warnings
	tidy -wrap 78 -i -asxhtml -utf8 -o $@ $< || test $$? -eq 1

%.sql: %.in.sql
	sed 's/PREFIX/$(DB_TABLE_PREFIX)/g' $< > $@

%.py %.pyc: %.kid
	kidc -fs $<

# For testing
out/%.html: src/%.kid
	@mkdir -p $(dir $@)
	kid -o $@ $<

# Misc

FORCE:

# End
