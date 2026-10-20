# code fix alpha scripts remote

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-alpha-scripts-remote_20260515T045143_result.json`
- **Structured JSON:** [`4023ebf1c10f8d9a0654.json`](../../sessions/40/4023ebf1c10f8d9a0654.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 修改报告

| 脚本 | 修改前 α（注释） | 修改后 α（注释） | 实际数组（未变） |
|------|-----------------|-----------------|----------------|
| v1 `run_alpha_ablation.sh` | `{0.0, 0.5, 1.0, 2.0, 4.0}` | `{0.0, 0.25, 0.5, 1.0, 2.0}` | `(0.0 0.25 0.5 1.0 2.0)` ✓ |
| v2 `run_alpha_ablation_v2.sh` | `{0.0, 0.25, 0.5, 0.75, 1.0}` | `{0.0, 0.25, 0.5, 1.0, 2.0}` | `(0.0 0.25 0.5 1.0 2.0)` ✓ |
| v3 `run_alpha_ablation_v3.sh` | 无需修改 | — | `(0.0 0.25 0.5 1.0 2.0)` ✓ |

三个脚本的 ALPHAS 数组、ALPHA_TAGS、内嵌 Python alphas 列表均为正确值 `{0.0, 0.25, 0.5, 1.0, 2.0}`。此次修改仅是头部注释对齐——功能代码之前已被修正。语法检查全部通过。

**md5sum 验证凭证**：
- v1: `25264725391903eb98958cf355362a4f`
- v2: `48c048617f92e2e7bf48c29195657c3d`
- v3: `0fa5349b14dac099c44d0b452c2d9668`

---
