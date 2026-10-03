# Notes API
A small HTTP service for creating and reading notes.
## What it does

This is a small HTTP service with three endpoints: `/`, `/healthz`, and `/notes`.

## How to run

```bash
./scripts/run.sh
```

The service runs on port 8080 by default.

You can choose another port:

```bash
PORT=5000 ./scripts/run.sh
```

## How to test

```bash
./scripts/test.sh
```

The tests check the `/`, `/healthz`, and `/notes` endpoints.
