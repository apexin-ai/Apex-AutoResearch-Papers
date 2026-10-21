# ops d050 eval pipeline westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d050-eval-pipeline-westd_20260513T154335_result.json`
- **Structured JSON:** [`252bde2915538c206f44.json`](../../sessions/25/252bde2915538c206f44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
MD5:
  eval_repo_cls.py:           2e3867d83f0566cd6c8978570354304c
  eval_repo_cwm.py:           5f1c80d01445bc0474a420c9353a1104
  paired_bootstrap_repo.py:   d9073b9399fe471c5abfaece2a438227

max_new_tokens:
  eval_repo_cls.py:  8        ✓
  eval_repo_cwm.py:  1024     ✓ (default via argparse)

TOST: present ✓ (tost_equivalence function + full TOST pipeline)

CWM v11 Status:
  PID 145692: running ✓ (uptime 4h21m, RSS 5.4GB, resumed from checkpoint-500)
  Current step: 1477/6633 (22%)
  Speed: ~8.9s/step ✓
  GPU memory:
    cuda:0  24923/32607 MiB  (99%)
    cuda:1  16335/32607 MiB  (92%)
    cuda:2  16297/32607 MiB  (77%)  ← CWM training
    cuda:3  25751/32607 MiB  (71%)
  Any errors: no
```

全部符合预期。训练从 step 501 恢复，当前 step 1477，速度稳定 ~8.9s/step，预计还需约 12.8 小时完成。

---
