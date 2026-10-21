# code cka figure prep v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cka-figure-prep-v2_20260515T052834_result.json`
- **Structured JSON:** [`89384404032f45f9531c.json`](../../sessions/89/89384404032f45f9531c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出汇总：

**CKA 数据结构**（`cka_scores.pt`，122KB）：
- `attn_overlap`: 28 层 × 4 heads 的 overlap 值
- `mlp_overlap`: 28 层 × 28 neurons 的 overlap 值
- `attn_cka_matrix`: 28 层，每层 4×4 head 间 CKA 相似度矩阵
- `mlp_cka_matrix`: 28 层，每层 28×28 neuron 间 CKA 矩阵

**关键统计**：
| 指标 | Attn overlap | MLP overlap |
|------|-------------|-------------|
| Mean | 0.7817 | 0.9223 |
| Std | 0.0909 | 0.0332 |
| Range | [0.31, 0.88] | [0.88, 1.00] |
| 最低层 | 0, 27, 1 | 25, 15, 26 |
| 最高层 | 9, 13, 18 | 0, 2, 1 |

**生成文件**：
- `results/cka_per_layer.json`（30KB）— 每层 attn/mlp overlap 值 + 全局统计
- `results/cka_heatmap.json`（629KB）— 每层完整 CKA 矩阵 + cross-layer off-diagonal 均值
- `src/extract_cka_for_figures.py` — 提取脚本

MLP overlap 普遍很高（>0.88），说明 MLP neuron 间冗余大；Attn 头间差异更显著，layer 0 和 27（首尾层）overlap 最低，中间层（9, 13, 18）最高。

---
