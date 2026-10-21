# deploy cqa1 gpu2 next gap

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_gpu2_next_gap_20260527T055520_result.json`
- **Structured JSON:** [`6ce4109b3bf8702a1c3d.json`](../../sessions/6c/6ce4109b3bf8702a1c3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU2 状态：仍在跑，不可用。**

**实验**: π0.5 Attn k=0.95 Long strict (PID 938642)
**进度**: 4.8/10 tasks 完成 (T0-T3 done, T4 at ep 40/50)

| Task | SR | 状态 |
|------|-----|------|
| T0 | 88% | done |
| T1 | 98% | done |
| T2 | 72% | done |
| T3 | 100% | done |
| T4 | 85% (40ep) | running |
| T5-T9 | — | pending |

**累计**: 213/240 = 88.8%, 每 task 约 25 min。
**预估剩余**: ~10 min (T4) + 5 tasks × 25 min ≈ **2.5 小时**完成。

注意: 第一次启动 (`eval_pi05_attn_k095_long_seed42_strict.log`) 因 `ModuleNotFoundError: transformers.models.qwen2_5_vl` 崩溃，当前是重启的版本在正常运行。

GPU2 不空闲，无法部署新实验。cqa1 四卡全满。

---
