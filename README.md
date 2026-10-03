# Notes API

A small HTTP service that provides a greeting, a health check, and a list of notes.

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
