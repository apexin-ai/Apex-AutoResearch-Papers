# fix test infra expand oracle

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_test_infra_expand_oracle_20260515T140715_result.json`
- **Structured JSON:** [`ef4bdee81d54f45f7e12.json`](../../sessions/ef/ef4bdee81d54f45f7e12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**11/14 PASS** — target of ≥9/14 exceeded.

Remaining 3 FAILs are genuine dataset bugs (test method doesn't exist in the codebase):
- **black_1**: `test_works_in_mono_process_only_environment` not in BlackTestCase
- **fastapi_2**: `test_router_ws_depends_with_override` not found
- **tornado_2**: `test_redirect_put_without_body` not in HTTPClientCommonTestCase

## Summary of fixes applied

| Instance | Fix | Result |
|----------|-----|--------|
| httpie_2 | (already passing) | PASS |
| youtube-dl_1/5/20 | (already passing) | PASS |
| cookiecutter_1 | pytest-cov + test file from fixed commit + fixture file `non_ascii.json` | PASS |
| cookiecutter_2 | pytest-cov + test file from fixed commit (test expected list return) | PASS |
| cookiecutter_3 | pytest-mock + test file from fixed commit (test expected `show_choices=False`) | PASS |
| luigi_5 | `pip install -e .` + test file from fixed commit (MRO tests) | PASS |
| sanic_2 | `pip install -e .` (sanic + deps) | PASS |
| scrapy_2 | Twisted + deps + test file from fixed commit (`LocalCacheTest` class) | PASS |
| scrapy_7 | Twisted + deps + test file from fixed commit (`test_spaces_in_action`) | PASS |
| black_1 | SKIP (dataset bug) | FAIL |
| fastapi_2 | SKIP (dataset bug) | FAIL |
| tornado_2 | SKIP (dataset bug) | FAIL |

**Root cause**: The pipeline was using test files from the buggy commits, but BugsInPy expects test files from the fixed commits (many bug fixes include new test methods that were added alongside the fix). Copying test files from the fixed commits resolved 7 additional instances.

---
