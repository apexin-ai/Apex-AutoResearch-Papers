# ops j16 results extraction

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_j16_results_extraction_20260517T122319_result.json`
- **Structured JSON:** [`06af9ce636132d477f16.json`](../../sessions/06/06af9ce636132d477f16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## MCMC 状态: 进行中（2/9 完成）

**时间线:**
| 阶段 | 时间 (UTC) | 耗时 |
|------|-----------|------|
| 启动 | 20:07:25 | - |
| STEM_Math 完成 | 20:15:41 | 8.3 min |
| STEM_Science 采样完成 | 20:22:18 | 6.6 min (结果待写入) |
| 剩余 6 domains + pooled | - | 预计 ~70 min |
| **预计全部完成** | **~21:35 UTC** | - |

---

## 已完成结果: STEM_Math

| 指标 | 值 |
|------|---|
| γ mean | **-0.3855** |
| γ 95% CI | [-0.999, 0.200] |
| γ 90% CI | [-0.890, 0.119] |
| Significant? | **No** (CI includes 0) |
| PPP | **0.998** (excellent fit) |
| n_items | 1190 |
| n_models | 16 |
| mean_acc | 0.412 |
| rhat | 1.009 (ok) |
| ESS | 1448 (ok) |
| Divergences | 0 |

γ 为负值趋势（contamination 在 math domain 可能反而降低表现），但 CI 太宽，无法下结论。

---

## GPU 状态

| GPU | Util% | Memory | Process |
|-----|-------|--------|---------|
| 0 | 36% | 1475/24564 MiB | PID 983741: exp008 eval Qwen2.5-0.5B base — GSM8K **87%** (1147/1319), ~14 min 剩余 |
| 1 | 0% | 0 MiB | **idle** |
| 2 | 0% | 0 MiB | **idle** |
| 3 | 0% | 0 MiB | **idle** |
| 4 | 0% | 0 MiB | **idle** |
| 5 | 0% | 0 MiB | **idle** |

IRT MCMC (PID 990725) 是 CPU-only 任务，不占 GPU。

**tmux sessions:**
- `exp008_eval`: Qwen2.5-0.5B base pretrained → GSM8K 87% 完成，之后跑 ARC_challenge
- `exp009_3b_instruct`, `exp009_deepseek`: 自 12:18 UTC 起运行（可能已完成或 idle）

---

MCMC 预计 ~21:35 UTC 全部完成，届时再查看完整 8 domains + pooled 结果。GPU 1-5 当前全部空闲。

---
