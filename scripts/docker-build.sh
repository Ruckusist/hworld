#!/bin/bash
# scripts/docker-build.sh
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

set -e

VERSION=${1:-latest}

echo "Building hworld-server:${VERSION}..."

docker build -t hworld-server:${VERSION} .

if [ "$VERSION" != "latest" ]; then
    docker tag hworld-server:${VERSION} hworld-server:latest
fi

echo "Build complete: hworld-server:${VERSION}"
