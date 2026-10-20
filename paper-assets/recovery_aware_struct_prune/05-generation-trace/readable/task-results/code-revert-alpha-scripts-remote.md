# code revert alpha scripts remote

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_revert-alpha-scripts-remote_20260515T061709_result.json`
- **Structured JSON:** [`f32fe4744075ea70cc42.json`](../../sessions/f3/f32fe4744075ea70cc42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 文件 | 修改前 | 修改后 | 语法 | md5sum |
|------|--------|--------|------|--------|
| `scripts/run_alpha_ablation.sh` | `(0.0 0.25 0.5 1.0 2.0)` + tags `alpha025` | `(0.0 0.5 1.0 2.0 4.0)` + tags `alpha40` | OK | `c1761ca3` |
| `scripts/run_alpha_ablation_v2.sh` | `(0.0 0.25 0.5 1.0 2.0)` + Python `[0.0, 0.25, ...]` | `(0.0 0.5 1.0 2.0 4.0)` + Python `[0.0, 0.5, ...]` | OK | `cb3a6f80` |
| `scripts/run_alpha_ablation_v3.sh` | `(0.0 0.25 0.5 1.0 2.0)` + Python `[0.0, 0.25, ...]` | `(0.0 0.5 1.0 2.0 4.0)` + Python `[0.0, 0.5, ...]` | OK | `4d9efaca` |
| `src/run_alpha_ablation.sh` | 已经是 `(0.0 0.5 1.0 2.0 4.0)` | 无需修改 | — | `a40a4669` |

修改内容：注释头、bash `ALPHAS` 数组、`ALPHA_TAGS` 数组（v1）、内嵌 Python `alphas` 列表（v2/v3）均已统一为 `{0.0, 0.5, 1.0, 2.0, 4.0}`。

---
