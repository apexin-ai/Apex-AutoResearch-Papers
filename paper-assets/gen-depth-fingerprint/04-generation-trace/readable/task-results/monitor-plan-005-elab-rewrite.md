# monitor plan 005 elab rewrite

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_plan-005-elab-rewrite_20260515T055129_result.json`
- **Structured JSON:** [`8984e60fe3bb70f08152.json`](../../sessions/89/8984e60fe3bb70f08152.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 生成数据
| Prompt Type | Records | Skipped | Status |
|---|---|---|---|
| continuation | 4620 | — | ✅ |
| elaboration | 4946 | 14 | ✅ |
| inspired_rewriting | 4827 | 61 | ✅ |

## Features 输出路径
- `data/pythia-2.8b-continuation/features.jsonl` (4620)
- `data/pythia-2.8b-elaboration/features.jsonl` (4946)
- `data/pythia-2.8b-inspired_rewriting/features.jsonl` (4827)

## Spearman ρ (depth vs feature)

| Feature | continuation | elaboration | insp_rewrite |
|---|---|---|---|
| entropy_mean | **-0.665*** | **-0.583*** | **-0.564*** |
| entropy_std | -0.151*** | +0.001 | -0.001 |
| entropy_max | -0.023 | +0.218*** | +0.262*** |
| entropy_min | -0.462*** | -0.457*** | -0.446*** |
| tail_decay | +0.082*** | -0.059*** | -0.026 |
| ttr | **-0.629*** | **-0.666*** | **-0.659*** |
| hapax_ratio | **-0.651*** | **-0.674*** | **-0.670*** |

关键发现：
- **表面特征 (ttr, hapax_ratio)** 在三种 prompt type 中深度信号一致且最强 (|ρ| ≈ 0.63–0.67)
- **entropy_mean** 在 continuation 中最强 (-0.665)，elab/rewrite 略弱 (-0.58/-0.56)
- **entropy_std** 和 **tail_decay** 在非 continuation 中几乎无信号，提示这两个特征对 prompt type 敏感
- **entropy_max** 方向在 continuation vs elab/rewrite 间反转（负→正），值得关注

---
