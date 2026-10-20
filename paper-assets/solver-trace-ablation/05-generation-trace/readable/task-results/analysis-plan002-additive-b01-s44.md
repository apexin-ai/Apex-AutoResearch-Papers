# analysis plan002 additive b01 s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan002-additive-b01-s44_20260514T093004_result.json`
- **Structured JSON:** [`d08084b380795cecf4cc.json`](../../sessions/d0/d08084b380795cecf4cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

---

## 结果摘要

### 1. 训练指标
| 指标 | 值 |
|------|-----|
| total_steps | 500 |
| duration | 40.8 min |
| loss | 0.006 |
| last100 PR | **0.9337** |
| last100 ISR | **0.9049** |

**训练曲线（windowed PR / ISR）**：
- steps 1-100: 0.165 / 0.086
- steps 101-200: 0.431 / 0.224
- steps 201-300: 0.931 / 0.584
- steps 301-400: 0.943 / 0.756
- steps 401-500: 0.934 / 0.905

### 2. Eval 指标（eval_sta.py, 100 problems）
| 指标 | 值 |
|------|-----|
| prove_rate | **0.89** |
| mean_isr | **0.803** (±0.342) |
| median_isr | 1.0 |
| proved_only_isr | **0.9022** |
| component_count_mean | **4.33** |
| component_count_2_ratio | **0.0225** |
| tautological_collapse | **false** |

### 3. Conclusion: **SUCCESS**
- tautological_collapse=false, PR=0.89>0.5, ISR=0.803>0.1 → 全部达标

### 4. 与 parent s42 对比
| 指标 | s42 | s44 | diff |
|------|-----|-----|------|
| eval_prove_rate | 0.81 | **0.89** | +0.08 |
| eval_mean_isr | 0.337 | **0.803** | **+0.466** |
| proved_only_isr | 0.415 | **0.902** | **+0.487** |
| component_count_mean | 5.58 | 4.33 | -1.25 |
| component_2_ratio | 0.037 | 0.023 | -0.015 |

s44 显著优于 s42，存在较大 seed 间方差。

### 5. 与 exec-only s44 对比
| 指标 | exec-only s44 | ISR β=0.1 s44 |
|------|---------------|---------------|
| PR | ~98% | 89% |
| tautological_collapse | **YES**（94% 样本仅 2 comp） | **NO**（2.25% 样本 2 comp） |
| ISR | ~0.5（假象） | **0.803**（真实） |

**ISR β=0.1 additive bonus 成功防止了 seed 44 的 tautological collapse。**

---
