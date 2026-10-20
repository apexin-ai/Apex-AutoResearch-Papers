# eval llama phase1 launch and n50 check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama_phase1_launch_and_n50_check_20260520T195028_result.json`
- **Structured JSON:** [`f2f24dfc13e6b267698d.json`](../../sessions/f2/f2f24dfc13e6b267698d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Llama 正在正常运行：GPU 18.3GB / 89% 利用率，正在生成对话。

---

## 总结

### Part 1: N=50 Attention Steering — 已完成 ✓

| Beta | Mid-GAR | PPL |
|------|---------|-----|
| 0.0 | 0.1011 | 1.43 |
| 2.0 | 0.2068 | 1.48 |
| **3.0** | **0.6662** | **1.56** |
| 4.0 | 0.7579 | 1.67 |
| 5.0 | 0.8315 | 1.77 |
| 10.0 | 0.9806 | 3.45 |

Phase transition 在 β∈[2,3]（GAR 从 0.21 跳到 0.67），与 N=5 一致但更 sharp。β=5 是最佳操作点（GAR=0.83, PPL=1.77 可接受）。Registry 已标记 DONE/success。

### Part 2: Llama Phase 1 GAR 诊断 — 已提交运行

- **PID**: 198817
- **tmux session**: `llama_phase1`
- **GPU**: 18.3GB / 89% util
- **Log**: `/root/turn_residual_gating/logs/llama_phase1_gar_diag.log`
- **Registry**: `llama_phase1_gar_diag` → RUNNING
- **预估运行时间**: ~30 min（5 conversations × 10 turns 生成 + GAR 测量）

---
