# ssh d048 eval cwm maxtoken 1024

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d048-eval-cwm-maxtoken-1024_20260513T092716_result.json`
- **Structured JSON:** [`559bebcebc97e4ed8daf.json`](../../sessions/55/559bebcebc97e4ed8daf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 修改前后 grep 对比

| 文件 | 行 | 修改前 | 修改后 |
|------|----|--------|--------|
| `eval_repo_cwm.py:8` | 注释 | `(256 vs 8)` | `(1024 vs 8)` |
| `eval_repo_cwm.py:260` | argparse default | `default=256` | `default=1024` |
| `eval_repo_level.py:165` | CWM 分支 | `max_new_tokens = 256` | `max_new_tokens = 1024` |
| `eval_repo_bootstrap.py:193` | CWM 分支 | `max_new_tokens = 256` | `max_new_tokens = 1024` |

CLS 行（`= 8`）未动，两台服务器均已确认。

### 2. eval_repo_level.py 和 eval_repo_bootstrap.py

都改了，256 → 1024。

### 3. md5 对比

| 文件 | home-1x5090 | seetacloud-westd-4x5090 |
|------|-------------|------------------------|
| `eval_repo_cwm.py` | `27f4d4a9...` | `5f1c80d0...` ❌ |
| `eval_repo_level.py` | `bc258513...` | `bc258513...` ✅ |
| `eval_repo_bootstrap.py` | `2d14784c...` | `2d14784c...` ✅ |

`eval_repo_cwm.py` 两台 md5 不一致。之前 grep 就显示 home 版本行号 290/330 vs westd 296/336，说明两台服务器的 `eval_repo_cwm.py` 本身就有其他差异（非 max_new_tokens 部分）。max_new_tokens 相关行的修改内容一致。

---
