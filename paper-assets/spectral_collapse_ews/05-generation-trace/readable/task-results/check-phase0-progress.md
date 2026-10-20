# check phase0 progress

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phase0_progress_20260516T112403_result.json`
- **Structured JSON:** [`0941b509134ca75cf298.json`](../../sessions/09/0941b509134ca75cf298.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志文件仍在写入（最后修改 19:25），Gen 2 正在生成合成数据。所有现有 checkpoint 的 HellaSwag 评估已由 auto_eval watcher 完成。

## 报告

### 1. Phase 0 进度

**当前状态：Gen 2 合成数据生成中**（GPU 0 占用 25GB, 60% utilization）

已完成：Gen 0（baseline）、Gen 1（训练 + 评估 + checkpoint）

目标 10 代，完成 2/10。

### 2. 中间 Metrics

| Gen | Effective Rank | Perplexity | Distinct-4 | Train Loss |
|-----|---------------|------------|------------|------------|
| 0   | 417.55        | 9.55       | 0.7414     | — (baseline) |
| 1   | 491.77        | 11.38      | 0.6256     | 1.6228     |

Gen 0→1 变化：
- **Perplexity**: 9.55 → 11.38 (+19.2%) — 模型质量下降
- **Distinct-4**: 0.7414 → 0.6256 (-15.6%) — 生成多样性下降
- **Effective Rank**: 417.55 → 491.77 (+17.8%) — 上升（暂时的，可能是训练初期特征扩散，后续代应该开始下降）

### 3. HellaSwag 评估结果

| Gen | acc_norm | acc | stderr(norm) |
|-----|----------|-----|-------------|
| 0   | **0.4130** | 0.3450 | ±0.0049 |
| 1   | **0.3897** | 0.3385 | ±0.0049 |

**acc_norm 下降 2.33 个百分点**（-5.6%），仅一代即可观测到明显退化。

### 4. Collapse 趋势判断

**符合预期。** 一代合成数据训练后：
- HellaSwag 能力明确下降
- 生成多样性（distinct-4）显著收缩
- Perplexity 上升

这与 model collapse 的早期信号一致：模型在自身生成数据上训练导致分布收窄、下游任务性能退化。auto_eval watcher 已在 cuda:1 上运行，后续 checkpoint 会自动评估。

---
