FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_HTTP_TIMEOUT=600 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    PATH="/opt/venv/bin:${PATH}"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        g++ \
        git \
        libgl1 \
        libglib2.0-0 \
        libgomp1 \
        libmecab-dev \
        libsm6 \
        libxext6 \
        libxrender1 \
        mecab \
        mecab-ipadic-utf8 \
        pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp/project

COPY pyproject.toml uv.lock README.md ./

RUN uv sync --frozen --no-dev

WORKDIR /workspace

EXPOSE 2718

CMD ["bash"]
