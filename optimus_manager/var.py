import os
from pathlib import Path
import json
import optimus_manager.envs as envs


class VarError(Exception):
    pass


def read_startup_mode():

    try:
        with open(envs.STARTUP_MODE_VAR_PATH, 'r') as f:
            content = f.read().strip()

            if content in ["intel", "nvidia", "hybrid", "ac_auto"]:
                mode = content
            else:
                raise VarError("Invalid value : %s" % content)
    except IOError:
        raise VarError("Cannot open or read %s" % envs.STARTUP_MODE_VAR_PATH)

    return mode


def write_startup_mode(mode):

    assert mode in ["intel", "nvidia", "hybrid", "ac_auto"]

    filepath = Path(envs.STARTUP_MODE_VAR_PATH)

    os.makedirs(filepath.parent, exist_ok=True)

    try:
        with open(filepath, 'w') as f:
            f.write(mode)
    except IOError:
        raise VarError("Cannot open or write to %s" % str(filepath))


def remove_startup_mode_var():

    try:
        os.remove(envs.STARTUP_MODE_VAR_PATH)
    except FileNotFoundError:
        pass

def read_temp_conf_path_var():

    filepath = Path(envs.TEMP_CONFIG_PATH_VAR_PATH)

    try:
        with open(filepath, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise VarError("File %s not found." % str(filepath))
    except IOError:
        raise VarError("Cannot open or read %s" % str(filepath))

def write_temp_conf_path_var(path):

    filepath = Path(envs.TEMP_CONFIG_PATH_VAR_PATH)

    os.makedirs(filepath.parent, exist_ok=True)

    try:
        with open(envs.TEMP_CONFIG_PATH_VAR_PATH, 'w') as f:
            f.write(path)
    except IOError:
        raise VarError("Cannot open or write to %s" % envs.TEMP_CONFIG_PATH_VAR_PATH)

def remove_temp_conf_path_var():

    try:
        os.remove(envs.TEMP_CONFIG_PATH_VAR_PATH)
    except FileNotFoundError:
        pass

def write_acpi_call_strings(call_strings_list):

    filepath = Path(envs.ACPI_CALL_STRING_VAR_PATH)

    os.makedirs(filepath.parent, exist_ok=True)

    try:
        with open(filepath, 'w') as f:
            json.dump(call_strings_list, f)
    except IOError:
        raise VarError("Cannot open or write to %s" % str(filepath))

def read_acpi_call_strings():

    filepath = Path(envs.ACPI_CALL_STRING_VAR_PATH)

    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise VarError("File %s not found." % str(filepath))
    except (IOError, json.decoder.JSONDecodeError):
        raise VarError("Cannot open or read %s" % str(filepath))

def write_last_acpi_call_state(state):

    filepath = Path(envs.LAST_ACPI_CALL_STATE_VAR)

    os.makedirs(filepath.parent, exist_ok=True)

    try:
        with open(filepath, 'w') as f:
            f.write(state)
    except IOError:
        raise VarError("Cannot open or write to %s" % str(filepath))

def read_last_acpi_call_state():

    filepath = Path(envs.LAST_ACPI_CALL_STATE_VAR)

    try:
        with open(filepath, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise VarError("File %s not found." % str(filepath))
    except IOError:
        raise VarError("Cannot open or read %s" % str(filepath))

def remove_last_acpi_call_state():

    try:
        os.remove(envs.LAST_ACPI_CALL_STATE_VAR)
    except FileNotFoundError:
        pass
