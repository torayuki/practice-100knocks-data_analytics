#!/usr/bin/env bash

_activate_python_fail() {
    echo "activate_python.bash: $*" >&2
}

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    _activate_python_fail "source this file instead: source ${BASH_SOURCE[0]}"
    exit 1
fi

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$project_dir" || {
    _activate_python_fail "failed to enter project directory: $project_dir"
    return 1
}

if ! command -v uv >/dev/null 2>&1; then
    _activate_python_fail "uv command not found"
    return 1
fi

sync_check="$(uv sync --locked --dry-run 2>&1)"
sync_status=$?
if [[ $sync_status -ne 0 ]]; then
    echo "$sync_check" >&2
    _activate_python_fail "uv sync dry-run failed"
    return 1
fi

if [[ "$sync_check" != *"Would make no changes"* ]]; then
    uv sync --locked || {
        _activate_python_fail "uv sync failed"
        return 1
    }
fi

source "$project_dir/.venv/bin/activate"
