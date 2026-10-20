# analysis rsft r2ab

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rsft_r2ab_20260515T093729_result.json`
- **Structured JSON:** [`236a54f4dedafcaedae6.json`](../../sessions/23/236a54f4dedafcaedae6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RSFT r2a/r2b 实验结果

### 关键指标对比

| 指标 | SFT baseline | r1 (3ep) | r1_s43 (3ep) | r1_s44 (3ep) | **r2a** (1ep, data fix) | **r2b** (1ep, data+train fix) |
|------|:-----------:|:--------:|:-----------:|:-----------:|:--------:|:--------:|
| **rel_F1** | **0.4057** | 0.0483 | 0.0481 | 0.0509 | 0.0509 | 0.0504 |
| **Evi-F1** | **0.798** | — | 0.7368 | 0.7798 | 0.7478 | 0.7565 |
| EDCR | — | — | 0.6629 | 0.6030 | 0.6499 | 0.6046 |
| num_preds | 12234 | 848 | 861 | 771 | 800 | 754 |
| eval_loss | — | 0.756 | 0.7622 | 0.7625 | 0.7547 | 0.7545 |
| train_loss | — | — | 0.6148 | 0.6138 | 0.6624 | 0.6700 |
| steps | — | — | 510 | 510 | 160 | 160 |
| runtime | — | — | 1h56m | 1h53m | 35.5m | 33.7m |

### Training loss 趋势

**r2a** (lr=2e-5, alpha=128): 0.668 → 0.697 → 0.631 → 0.624(min@63%) → 0.681 → 0.661
**r2b** (lr=1e-5, alpha=32): 0.668 → 0.701 → 0.638 → 0.634(min@63%) → 0.689 → 0.676

两者 loss 曲线几乎一致，alpha 从 128→32、lr 从 2e-5→1e-5 对训练动态无实质影响。

### 结论：**全部 NEGATIVE**

r2a/r2b rel_F1 ≈ 0.05，与 r1 完全一致（SFT baseline 的 12%）。逐项排除：

1. **Data fix 无效** — 移除 170 个 truncated JSON 不改变结果
2. **Training dynamics fix 无效** — LoRA scaling 2.0→0.5 + lr 减半不改变结果
3. **Epoch 数无关** — 1 epoch vs 3 epochs 同样 collapse
4. **Seed 无关** — r1_s43/s44 两种子结果一致

**根因更新**：ontology collapse 不是训练超参或数据噪声问题。RSFT 训练数据本身可能就包含偏离 DocRED ontology 的 relation 名称——即使 CED 高分的样本，relation name 也可能是 open-domain 的自由文本而非 DocRED 标准名。1 epoch 就足以覆盖 SFT 学到的 ontology mapping。

### r1_s43 / r1_s44 状态

两个都已完成（EXIT_CODE=0），结果与 r1 一致，进一步确认 RSFT 路线不可行。当前无 rsft 进程在运行。

---
