#!/bin/bash
	venv/Scripts/activate.bat
	python trampo_livre/manage.py loaddata trampo_livre/api/fixture/usuarios.json
	python trampo_livre/manage.py loaddata trampo_livre/api/fixture/setor.json
	python trampo_livre/manage.py loaddata trampo_livre/api/fixture/profissionais.json
	python trampo_livre/manage.py loaddata trampo_livre/api/fixture/atividades.json
	python trampo_livre/manage.py loaddata trampo_livre/api/fixture/avaliacoes.json