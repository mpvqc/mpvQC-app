# Copyright 2024
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

PYTHON_DIR := invocation_directory() + '/' + if os_family() == 'windows' { 'venv/Scripts' } else { 'venv/bin' }
PYTHON := PYTHON_DIR + if os_family() == 'windows' { '/python.exe' } else { '/python3' }

# https://github.com/linuxdeepin/deepin-system-monitor/issues/22

TOOL_CLI_LUPDATE := PYTHON_DIR + '/pyside6-lupdate'
TOOL_CLI_LRELEASE := 'lrelease-qt5'
TOOL_CLI_RCC := PYTHON_DIR + '/pyrcc5'


#####       #####
##### Names #####
#####       #####
NAME_APPLICATION := 'mpvQC'

NAME_DIRECTORY_BUILD := 'build'

NAME_DIRECTORY_BUILD_HELPERS := 'build-aux'
NAME_DIRECTORY_DATA := 'data'
NAME_DIRECTORY_I18N := 'i18n'
NAME_DIRECTORY_PY_SOURCES := 'mpvqc'

NAME_FILE_MAIN_ENTRY := 'main.py'
NAME_FILE_GENERATED_RESOURCES := '_resources_rc.py'

#####                      #####
##### Existing Directories #####
#####                      #####
DIRECTORY_ROOT := invocation_directory()
DIRECTORY_BUILD_HELPERS := DIRECTORY_ROOT + '/' + NAME_DIRECTORY_BUILD_HELPERS
DIRECTORY_DATA := DIRECTORY_ROOT + '/' + NAME_DIRECTORY_DATA
DIRECTORY_I18N := DIRECTORY_ROOT + '/' + NAME_DIRECTORY_I18N
DIRECTORY_PY_SOURCES := DIRECTORY_ROOT + '/' + NAME_DIRECTORY_PY_SOURCES

#####                #####
##### Existing Files #####
#####                #####
FILE_APP_ENTRY := DIRECTORY_ROOT + '/' + NAME_FILE_MAIN_ENTRY

#####                       #####
##### Generated Directories #####
#####                       #####
DIRECTORY_BUILD := DIRECTORY_ROOT + '/' + NAME_DIRECTORY_BUILD
DIRECTORY_BUILD_QRC_DATA := DIRECTORY_BUILD + '/qrc-' + NAME_DIRECTORY_DATA
DIRECTORY_BUILD_QRC_I18N := DIRECTORY_BUILD + '/qrc-' + NAME_DIRECTORY_I18N
DIRECTORY_BUILD_TRANSLATIONS := DIRECTORY_BUILD + '/translations'
DIRECTORY_BUILD_RESOURCES := DIRECTORY_BUILD + '/resources'
DIRECTORY_BUILD_RELEASE := DIRECTORY_BUILD + '/release'
DIRECTORY_BUILD_PY := DIRECTORY_BUILD_RELEASE + '/' + NAME_DIRECTORY_PY_SOURCES

#####                 #####
##### Generated Files #####
#####                 #####
FILE_BUILD_QRC_DATA := DIRECTORY_BUILD_QRC_DATA + '/' + NAME_DIRECTORY_DATA + '.qrc'
FILE_BUILD_QRC_I18N := DIRECTORY_BUILD_QRC_I18N + '/' + NAME_DIRECTORY_I18N + '.qrc'
FILE_BUILD_QRC_I18N_JSON := DIRECTORY_BUILD_QRC_I18N + '/' + NAME_APPLICATION + '.json'
FILE_BUILD_TRANSLATIONS_JSON := DIRECTORY_BUILD_TRANSLATIONS + '/' + NAME_APPLICATION + '.json'
FILE_BUILD_RESOURCES := DIRECTORY_BUILD_RESOURCES + '/' + NAME_FILE_GENERATED_RESOURCES

FILE_PY_SOURCES_RESOURCES := DIRECTORY_PY_SOURCES + '/' + NAME_FILE_GENERATED_RESOURCES


build: _clean-build _clean-develop _compile-resources
    @rm -rf \
        {{DIRECTORY_BUILD_PY}}
    @mkdir -p \
        {{DIRECTORY_BUILD_PY}}
    @cp -r \
        {{DIRECTORY_PY_SOURCES}}/. \
        {{DIRECTORY_BUILD_PY}}
    @cp \
        {{FILE_BUILD_RESOURCES}} \
        {{DIRECTORY_BUILD_PY}}
    @cp \
        {{FILE_APP_ENTRY}} \
        {{DIRECTORY_BUILD_RELEASE}}
    @echo ''; \
        echo 'Please find the finished project in {{DIRECTORY_BUILD_RELEASE}}'

build-develop: _clean-develop _compile-resources
	@# Generates resources and copies them into the source directory
	@# This allows to develop/debug the project normally

	@cp \
		{{FILE_BUILD_RESOURCES}} {{DIRECTORY_PY_SOURCES}}

update-translations: _prepare-translation-extractions
	@# Traverses *.qml and *.py files to update translation files
	@# Requires translations in .py:   QCoreApplication.translate("context", "string")
	@# Requires translations in .qml:  qsTranslate("context", "string")
	@cd {{DIRECTORY_BUILD_TRANSLATIONS}}; \
		{{TOOL_CLI_LUPDATE}} \
		    -locations none \
			-project {{FILE_BUILD_TRANSLATIONS_JSON}}
	@cp -r \
		{{DIRECTORY_BUILD_TRANSLATIONS}}/{{NAME_DIRECTORY_I18N}}/*.ts \
		{{DIRECTORY_I18N}}

add-translation locale: _prepare-translation-extractions
    @cd {{DIRECTORY_BUILD_TRANSLATIONS}}; \
        {{TOOL_CLI_LUPDATE}} \
            -verbose \
            -source-language en_US \
            -target-language {{locale}} \
            -ts {{DIRECTORY_I18N}}/{{locale}}.ts
    @echo ''
    @just update-translations

clean: _clean-build _clean-develop

_clean-build:
	@rm -rf \
		{{DIRECTORY_BUILD}}

_clean-develop:
	@rm -rf \
		{{FILE_PY_SOURCES_RESOURCES}}

_compile-resources: _generate-qrc-data _generate-qrc-i18n
	@rm -rf \
		{{DIRECTORY_BUILD_RESOURCES}}
	@mkdir -p \
	 	{{DIRECTORY_BUILD_RESOURCES}}
	@cp -r \
	 	{{DIRECTORY_BUILD_QRC_DATA}}/. \
	 	{{DIRECTORY_BUILD_QRC_I18N}}/. \
	 	{{DIRECTORY_BUILD_RESOURCES}}
	@{{TOOL_CLI_RCC}} \
		{{DIRECTORY_BUILD_RESOURCES}}/{{NAME_DIRECTORY_DATA}}.qrc \
		{{DIRECTORY_BUILD_RESOURCES}}/{{NAME_DIRECTORY_I18N}}.qrc \
		-o {{FILE_BUILD_RESOURCES}}

_generate-qrc-data:
	@rm -rf \
		{{DIRECTORY_BUILD_QRC_DATA}}
	@mkdir -p \
		{{DIRECTORY_BUILD_QRC_DATA}}
	@cp -r \
		{{DIRECTORY_DATA}} \
		{{DIRECTORY_BUILD_QRC_DATA}}
	@{{DIRECTORY_BUILD_HELPERS}}/generate-qrc-file.py \
		--relative-to {{DIRECTORY_BUILD_QRC_DATA}} \
		--out-file {{FILE_BUILD_QRC_DATA}}

_generate-qrc-i18n:
	@rm -rf \
		{{DIRECTORY_BUILD_QRC_I18N}}
	@mkdir -p \
		{{DIRECTORY_BUILD_QRC_I18N}}
	@cp -r \
		{{DIRECTORY_I18N}} {{DIRECTORY_BUILD_QRC_I18N}}
	@{{DIRECTORY_BUILD_HELPERS}}/generate-lupdate-project-file.py \
		--relative-to {{DIRECTORY_BUILD_QRC_I18N}} \
		--out-file {{FILE_BUILD_QRC_I18N_JSON}}
	@cd \
		{{DIRECTORY_BUILD_QRC_I18N}}; \
			{{TOOL_CLI_LRELEASE}} \
				-project {{FILE_BUILD_QRC_I18N_JSON}}
	@cd \
		{{DIRECTORY_BUILD_QRC_I18N}}/{{NAME_DIRECTORY_I18N}}; \
			rm \
				{{FILE_BUILD_QRC_I18N_JSON}} \
				*.ts
	@{{DIRECTORY_BUILD_HELPERS}}/generate-qrc-file.py \
		--relative-to {{DIRECTORY_BUILD_QRC_I18N}} \
		--out-file {{FILE_BUILD_QRC_I18N}}

_prepare-translation-extractions:
	@rm -rf \
		{{DIRECTORY_BUILD_TRANSLATIONS}}
	@mkdir -p \
		{{DIRECTORY_BUILD_TRANSLATIONS}}
	@cp -r \
		{{DIRECTORY_I18N}} \
		{{DIRECTORY_PY_SOURCES}} \
		{{DIRECTORY_DATA}} \
		{{DIRECTORY_BUILD_TRANSLATIONS}}
	@{{DIRECTORY_BUILD_HELPERS}}/generate-lupdate-project-file.py \
		--relative-to {{DIRECTORY_BUILD_TRANSLATIONS}} \
		--out-file {{FILE_BUILD_TRANSLATIONS_JSON}}
