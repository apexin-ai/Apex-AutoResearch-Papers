# ssh d047 fix eval cwm max tokens

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d047-fix-eval-cwm-max-tokens_20260513T075930_result.json`
- **Structured JSON:** [`d8b08908a105e62160b6.json`](../../sessions/d8/d8b08908a105e62160b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。验证结果：

**grep 确认（两台一致）：**
- `eval_repo_cwm.py:8` — `(256 vs 8)` ✓
- `eval_repo_cwm.py:260` — `default=256` ✓
- `eval_repo_level.py:165` — `max_new_tokens = 256` ✓（:161 的 `= 8` 未动）
- `eval_repo_bootstrap.py:193` — `max_new_tokens = 256` ✓（:189 的 `= 8` 未动）

**md5 对比：**

| 文件 | home-1x5090 | seetacloud-westd-4x5090 | 一致？ |
|------|------------|------------------------|--------|
| eval_repo_cwm.py | `76c571e6...` | `7753e8a7...` | ✗ |
| eval_repo_level.py | `8b7e357f...` | `8b7e357f...` | ✓ |
| eval_repo_bootstrap.py | `1e66d409...` | `1e66d409...` | ✓ |

`eval_repo_cwm.py` 的 md5 不一致——两台服务器在 max_new_tokens 之外的内容本身就有差异（修改前已存在）。max_new_tokens 相关行的修改内容两台完全一致。

---
