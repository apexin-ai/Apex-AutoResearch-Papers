# exp 7model preview pipeline

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_7model-preview-pipeline_20260522T150246_result.json`
- **Structured JSON:** [`8db229b5c54e495ff6d3.json`](../../sessions/8d/8db229b5c54e495ff6d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 7-model preview 结果

### Confound Diagnosis: 彻底打破
| 指标 | 6-model MVP | 7-model (+ haiku) |
|------|------------|-------------------|
| Mean r(K_eff, η_max) | (negative range) | **+0.473** |
| CONFOUND_BROKEN | — | **12/12** |
| CONFOUND_SEVERE | — | **0/12** |

加入 claude-3-haiku 后 confound **反转为正相关**。原因：haiku 来自不同模型族，与本地模型 MI 低（高 K_eff），同时 ASR 最高（mean=0.356 vs 本地最高 0.258）。含 haiku 的 panel 同时有高 K_eff 和高 η_max，彻底打破了 "diversity = low vulnerability" 的 confound。

### Regression (Step 4)
| 指标 | 6-model MVP | 7-model |
|------|------------|---------|
| K_eff sig negative | 1/12 | **2/12** |
| η_max sig | 7/12 | **10/12** |

η_max 显著性提升（7→10），K_eff 仍极少显著负。注意多个 condition 下 K_eff β 为**正数**（prompt_injection, score_manipulation），说明高多样性 panel 反而 ASR 更高——因为含 haiku 的多样性 panel 自带高 ASR 成员。

### Random-fault (Step 5)
| 指标 | 结果 |
|------|------|
| Adaptive K_eff sig neg | 2/12 |
| RF K_eff sig neg | 1/12 |
| K_eff gains sig under RF | 6/12 |
| Mean ΔR² (RF − Adaptive) | **+0.237** |

RF 模型 R² 系统性高于 adaptive（+0.237），说明实际 attack 行为偏离了独立错误假设。

### Pipeline 状态
无 bug，7 models × 12 conditions × 35 panels 全部完成。脚本：`scripts/run_7model_preview.py`，产出在 `artifacts/results/` 下。

---
