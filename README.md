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



## Rollback

Argo CD deploys what is on the `main` branch, from the `k8s/` folder.

To roll back, undo the commit that deployed the bad version, with a new commit:

```bash
git log --oneline -- k8s/
git revert <commit>
git push