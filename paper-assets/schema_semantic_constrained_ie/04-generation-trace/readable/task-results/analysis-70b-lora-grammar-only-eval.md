# analysis 70b lora grammar only eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_70b-lora-grammar-only-eval_20260522T184233_result.json`
- **Structured JSON:** [`4948b0be56cf866e12d3.json`](../../sessions/49/4948b0be56cf866e12d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 第一部分：70B LoRA SciERC grammar_only 评估结果

| 指标 | grammar_only | unconstrained | S1 constrained |
|------|-------------|---------------|----------------|
| **DR%** | **1.5%** (17/1133) | 1.5% | 0% |
| R-F1 | 44.63 | 44.73 | 44.53 |
| E-F1 | 64.82 | — | — |
| Entity type violations | 0% | — | — |
| Relation vocab violations | 0% | — | — |
| JSON failures | 0% | — | — |

**结论：success。** Grammar layer 对 70B LoRA 零贡献——DR 与 unconstrained 完全一致（1.5%），R-F1 无显著差异。fine-tuned 模型已自行学会正确的输出语法，grammar 约束冗余。与 70B ZS pattern 一致。

### 第二部分：新实验已启动

**70B ZS SciERC unconstrained** → westd-21461 cuda:0, PID 74572

- 目的：独立验证 ZS baseline 数字（之前只有 r16_70b_scierc_zs_s1 附带的数字）
- 已注册 registry `eval_70b_zs_scierc_unconstrained`，cron 每 8 分钟轮询

### 当前实验全景

| 实验 | 服务器 | GPU | 状态 |
|------|--------|-----|------|
| 70B LoRA SciERC semantic_only | westd-16980 | cuda:0 | RUNNING |
| 70B LoRA SciERC full_s2 | westd-16980 | cuda:1 | RUNNING |
| 70B LoRA DocRED beam4 S1 | westd-21461 | cuda:1 | RUNNING |
| **70B ZS SciERC unconstrained** | **westd-21461** | **cuda:0** | **刚启动** |

---
