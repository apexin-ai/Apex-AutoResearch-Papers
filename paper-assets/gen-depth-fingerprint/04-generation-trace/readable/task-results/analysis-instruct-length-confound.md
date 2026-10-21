# analysis instruct length confound

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_instruct-length-confound_20260515T160303_result.json`
- **Structured JSON:** [`0d07a7121a40d8059939.json`](../../sessions/0d/0d07a7121a40d8059939.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果在 `results/instruct_length_confound.json`。

## 核心发现

### Part 1: 长度分布
| Model | depth-0 | depth-1 | depth-2 | depth-3 | depth-4 | length-depth ρ |
|-------|---------|---------|---------|---------|---------|---------------|
| **0.6B-Instruct** | 252 tok | **35 tok** | 27 tok | 24 tok | 23 tok | **-0.583** |
| **1.7B-Instruct** | 252 tok | 79 tok | 74 tok | 72 tok | 68 tok | **-0.520** |

**长度混淆确认：** 两个模型 |ρ| > 0.5，远超 0.3 阈值。0.6B 的 depth-1 仅原文的 1/7 长度。

### Part 2: 长度控制后

**0.6B-Instruct (length-matched 16-31 tok, gen-1+ only):**
| Feature | 原始 ρ | Length-matched ρ | Partial ρ | 缩减 |
|---------|--------|-----------------|-----------|------|
| TTR | +0.529 | **-0.007** | 0.139 | 74-99% |
| hapax_ratio | +0.509 | **-0.003** | 0.125 | 75-99% |
| entropy_mean | +0.518 | **-0.012** | 0.103 | 80-98% |

**1.7B-Instruct (length-matched 39-97 tok):**
| Feature | 原始 ρ | Length-matched ρ | Partial ρ | 缩减 |
|---------|--------|-----------------|-----------|------|
| TTR | +0.480 | +0.190 | 0.130 | 60-73% |
| hapax_ratio | +0.477 | +0.224 | 0.166 | 53-65% |
| entropy_mean | +0.478 | **+0.042** | 0.161 | 66-91% |

### Part 3: 短文本可靠性
- 0.6B: **73.1%** 样本 <50 tokens。TTR/hapax 的 bootstrap SE 很小（CV < 0.3%），说明即使短文本上指标的 **点估计** 是稳定的，但 TTR 在短文本上被机械抬高（TTR_mean=0.91 vs depth-0 的 0.64）。
- 1.7B: 25.7% 样本 <50 tokens。

### Part 4: Binary gen-1 vs gen-2+ LOGO F1
| Model | Instruct held-out F1 | Base models avg F1 |
|-------|---------------------|-------------------|
| 0.6B-Instruct | **0.552** | 0.693 avg |
| 1.7B-Instruct | **0.506** | 0.687 avg |

Instruct 模型的 gen-1 vs gen-2+ 分类接近随机（0.5），说明 depth fingerprint 在 instruct 生成链上几乎不存在。

### 结论
1. **长度混淆确认：** Reviewer 说得对。instruct 模型输出极短，造成严重长度混淆。
2. **Surface reversal 大部分是伪影：** 0.6B length-matched 后 ρ ≈ 0（完全消失），1.7B 缩减 53-91%。Partial correlation 残留 0.10-0.17——方向上仍"反转"，但效应量从 ~0.5 骤降到 ~0.13，不再有实际意义。
3. **Entropy reversal 同理：** 0.6B length-matched ρ = -0.01，1.7B = 0.04。控制长度后 entropy 信号消失。
4. **gen-1 vs gen-2+ 无法区分：** F1 ≈ 0.5，instruct 生成链不产生可检测的 depth 信号递进。

---
