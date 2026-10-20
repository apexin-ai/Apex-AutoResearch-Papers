# code fix alpha ablation script

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-alpha-ablation-script_20260515T044743_result.json`
- **Structured JSON:** [`7e6a1ad15b9963a34ad7.json`](../../sessions/7e/7e6a1ad15b9963a34ad7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本全部验证通过，α值均为 `{0.0, 0.25, 0.5, 1.0, 2.0}`。

修改前后对比：

| 脚本 | 修改前 | 修改后 |
|------|--------|--------|
| `run_alpha_ablation.sh` (v1) | `0.0 0.5 1.0 2.0 4.0` | `0.0 0.25 0.5 1.0 2.0` |
| `run_alpha_ablation_v2.sh` | `0.0 0.25 0.5 0.75 1.0` | `0.0 0.25 0.5 1.0 2.0` |
| `run_alpha_ablation_v3.sh` | `0.0 0.25 0.5 1.0 2.0` | 无需修改（已正确） |

v1同步更新了 `ALPHA_TAGS`：`alpha00 alpha05 alpha10 alpha20 alpha40` → `alpha00 alpha025 alpha05 alpha10 alpha20`。v2的内嵌Python汇总脚本中的 `alphas` 列表也已同步修正。

---
