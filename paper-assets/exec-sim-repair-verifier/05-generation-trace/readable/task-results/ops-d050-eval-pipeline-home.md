# ops d050 eval pipeline home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d050-eval-pipeline-home_20260513T154326_result.json`
- **Structured JSON:** [`c5a54c29ecfc4aedfe30.json`](../../sessions/c5/c5a54c29ecfc4aedfe30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
MD5:
  eval_repo_cls.py: 6612a30755f30f6d956927dfe4416949
  eval_repo_cwm.py: 27f4d4a90995aeb4823dd4c7f9b55408
  paired_bootstrap_repo.py: d9073b9399fe471c5abfaece2a438227

max_new_tokens:
  eval_repo_cls.py: 8 ✓
  eval_repo_cwm.py: 1024 (default via argparse) ✓

TOST: present ✓ (tost_equivalence函数 + TOST判定逻辑 + margin=2.0pp)
```

三项全部符合预期。

---
