# analyze check and d102 19828 loop17

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_check-and-d102-19828-loop17_20260522T004805_result.json`
- **Structured JSON:** [`2dfcf985dec02fe6a178.json`](../../sessions/2d/2dfcf985dec02fe6a178.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 实验状态

| 实验 | T | α | seed | 进度 | 状态 |
|------|---|---|------|------|------|
| t15_a045_s42_fp32 | 15 | 0.45 | 42 | 16/16 gen | **DONE** |
| t25_a075_s42_fp32 | 25 | 0.75 | 42 | 26/26 gen | **DONE** |
| t20_a045_s43_fp32 | 20 | 0.45 | 43 | gen 19/19 training (step ~2014/5000, ~40%) | RUNNING, ~7min 训练完 |
| t25_a075_s43_fp32 | 25 | 0.75 | 43 | gen 1/24 training (step ~3690/5000, 74%) | RUNNING, 刚开始，预计还需 ~10h |

### D102 5-method 分析结果（已完成实验）

**t15_a045_s42_fp32** (T=15, α=0.45, s42):
- PermG fwd: **6/8**, rev: **0/8**
- Robust pairs (K≥3): **5/8**
- mauve pairs 全不显著 (token_entropy→mauve 0/5, ece→mauve 1/5)

**t25_a075_s42_fp32** (T=25, α=0.75, s42):
- PermG fwd: **6/8**, rev: **0/8**
- Robust pairs (K≥3): **6/8**
- 4 个方法在 distinct 上一致 (4-5/5)，mauve 仍弱 (0-1/5)

D102 分析文件已复制到：
- `artifacts/phase_diagram_t15_a045_s42_fp32/data/5method_leadlag.json`
- `artifacts/phase_diagram_t25_a075_s42_fp32/data/5method_leadlag.json`

t20_a045_s43 预计 ~15min 内完成（训练 + gen + metrics），届时可执行 D102 分析。

---
