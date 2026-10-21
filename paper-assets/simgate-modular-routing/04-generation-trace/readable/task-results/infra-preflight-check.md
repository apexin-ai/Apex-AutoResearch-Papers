# infra preflight check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_preflight-check_20260513T061826_result.json`
- **Structured JSON:** [`f10db6e64c04aa5093a5.json`](../../sessions/f1/f10db6e64c04aa5093a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 飞行检查报告

| 检查项 | 状态 | 详情 |
|--------|------|------|
| **SSH** | ✓ | `westb-13313` 连通 |
| **GPU** | ✓ | 2× RTX 5090 (32GB each)，显存空闲 |
| **模型** | ✓ | Qwen2.5-7B-Instruct 存在，Tokenizer 正常 (vocab=151643) |
| **SCORE_FIX** | ✓ | `_last_score` 已修复 |
| **VARIATION_FIX** | ✓ | `ep_idx % max_var` 已修复 |
| **SEED_FIX** | ✓ | `random.seed(42)` 已修复 |
| **CI_FIX** | ✓ | `oracle_minus_det_ci90` 已修复 |
| **残留进程** | ✓ | 无 phase1 进程在跑 |
| **已有产出** | ℹ | `results/mvp/` 下有 phase0 验证文件、`phase1_gpu0.log` (17KB)、`boil/` 目录 |

全部通过，可以启动 Phase 1。

---
