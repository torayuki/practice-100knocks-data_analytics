#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
IMAGE_NAME="${IMAGE_NAME:-100knocks-marimo}"
CONTAINER_NAME="${CONTAINER_NAME:-100knocks-marimo}"
MARIMO_PORT="${MARIMO_PORT:-2718}"
UV_HTTP_TIMEOUT="${UV_HTTP_TIMEOUT:-600}"
NOTEBOOK_PATH="${1:-}"

if [[ -n "${NOTEBOOK_PATH}" ]]; then
  NOTEBOOK_ABS="$(cd "${PROJECT_ROOT}" && realpath "${NOTEBOOK_PATH}")"
  if [[ ! -f "${NOTEBOOK_ABS}" ]]; then
    echo "Notebook not found: ${NOTEBOOK_PATH}" >&2
    exit 1
  fi

  NOTEBOOK_DIR="$(dirname "${NOTEBOOK_ABS}")"
  NOTEBOOK_FILE="$(basename "${NOTEBOOK_ABS}")"
  CONTAINER_CMD="cd \"${NOTEBOOK_DIR/${PROJECT_ROOT}/\/workspace}\" && marimo edit --host 0.0.0.0 --port ${MARIMO_PORT} \"${NOTEBOOK_FILE}\""
else
  CONTAINER_CMD="cd /workspace && marimo edit --host 0.0.0.0 --port ${MARIMO_PORT}"
fi

docker run --rm -it \
  --name "${CONTAINER_NAME}" \
  -e UV_HTTP_TIMEOUT="${UV_HTTP_TIMEOUT}" \
  -p "${MARIMO_PORT}:${MARIMO_PORT}" \
  -v "${PROJECT_ROOT}:/workspace" \
  -w /workspace \
  "${IMAGE_NAME}" \
  bash -lc "${CONTAINER_CMD}"
