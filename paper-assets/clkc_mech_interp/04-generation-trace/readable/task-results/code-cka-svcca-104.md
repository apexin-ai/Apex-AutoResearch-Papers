# code cka svcca 104

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cka-svcca-104_20260522T074849_result.json`
- **Structured JSON:** [`3962f4b96750f59a7fbd.json`](../../sessions/39/3962f4b96750f59a7fbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

输出和图表都已保存。以下是结果汇报：

---

## 结果摘要

### 重要发现：XNLI CKA 不可直接对比

验证发现 **conflict 数据的 EN/ZH 是 sample-aligned（paired translations），但 XNLI 数据 EN/ZH 样本未对齐**（不同样本顺序，labels 不匹配）。CKA 要求逐样本配对，因此 XNLI 的 CKA≈0 主要是数据对齐问题，不代表表征差异。label-based alignment 只能按类别分组，无法恢复 sample-level pairing。

**SVCCA 受此影响较小**——它度量的是子空间重合度而非逐样本对应关系。

### Conflict 任务 CKA（有效结果）

| 指标 | Qwen3 (36层) | Llama3.1 (32层) |
|------|-------------|----------------|
| CKA 均值 | 0.696 | 0.786 |
| CKA 峰值 | 0.881 (L24) | 0.906 (L15) |
| CKA 最低 | 0.206 (L35) | 0.512 (L31) |

**层分布模式**：
- **Qwen3**: CKA 从 L0=0.39 逐层上升至 L24=0.88（EN/ZH 表征高度收敛），然后急剧下降至 L35=0.21（最后一层 EN/ZH 严重分离）
- **Llama3.1**: CKA 从 L0=0.59 快速上升至 L15=0.91（更早的峰值），然后平缓下降至 L31=0.51（分离程度不如 Qwen3 极端）
- 两个模型都呈现 **倒 U 型** CKA 曲线——中间层 EN/ZH 最相似，首尾层分离

### SVCCA 对比（可参考）

| 指标 | Qwen3 Conflict | Qwen3 XNLI | Llama Conflict | Llama XNLI |
|------|---------------|-------------|----------------|------------|
| 均值 | 0.830 | 0.817 | 0.807 | 0.854 |
| SVCCA diff 均值 | +0.013 | — | -0.047 | — |

- Qwen3: conflict 和 XNLI 的 SVCCA 差异很小（~1.3%），子空间结构相似
- Llama3.1: XNLI 的 SVCCA 反而略高于 conflict（~4.7%），说明 XNLI 的 EN/ZH 子空间更重合

### 输出文件
- `data/cka_svcca_results.json` — 完整逐层数值
- `data/cka_svcca_plot.png` — 可视化图表
- `logs/cka_svcca_v2.log` — 运行日志

### 后续建议
XNLI 要做有效的 CKA 对比，需要**使用真正的平行翻译数据**（XNLI validation set 本身是 parallel corpus），在 activation 提取阶段保证 EN/ZH 按相同样本顺序处理。

---
