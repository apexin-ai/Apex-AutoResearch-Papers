# analysis lambda curve verify

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lambda-curve-verify_20260516T210834_result.json`
- **Structured JSON:** [`594999bb6d1237cd6cc2.json`](../../sessions/59/594999bb6d1237cd6cc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证报告

### 1. 文件状态
- **存在**: `/root/distill_sparse_swiglu/artifacts/lambda_sparsity_curves.json`
- **大小**: 42,037 bytes, 2,734 lines
- **格式**: 合法 JSON，无 NaN / null / Infinity / 空数组

### 2. 包含 4 个 run

| Run | 数据点 | Step范围 | total_steps | target_sparsity | lambda_max |
|-----|--------|---------|-------------|-----------------|------------|
| kl_30pct_s42 | 109 | 1–1000 | 1000 | 0.3 | 5000 |
| kl_40pct_s42 | 109 | 1–1000 | 1000 | 0.4 | 5000 |
| kl_50pct_s42 | 48 | 1–200 | 200 | 0.5 | 1000 |
| kl_70pct_s42 | 109 | 1–1000 | 1000 | 0.7 | 1000 |

### 3. 每个 run 的字段
7 个数据序列 + 1 个 config dict：
`steps`, `loss`, `kl_raw`, `lambda`, `sparsity`, `tau`, `constraint_loss`, `config`

### 4. 采样模式
- 30/40/70% runs: steps 1-10 逐步，之后每 10 步采样到 1000
- 50% run: steps 1-10 逐步，之后每 5 步采样到 200（较短实验）

### 5. 关键数据范围

**kl_30pct_s42**:
- loss: 1.188 → 0.165
- lambda: 0.5 → 5000 (step ~260 后饱和到 lambda_max)
- sparsity: 0.406 → 0.285 (收敛到 target 0.3 附近)
- tau: 0.999 → 0.1 (线性退火)
- constraint_loss: 0.0075 → ~0

**kl_70pct_s42**:
- loss: step 20 处 spike 到 74（早期 lambda 冲击），之后恢复到 0.5–0.6
- constraint_loss: 0.075 起，step 40 后基本为 0
- tau: 0.999 → 0.1

**kl_40pct_s42**:
- constraint_loss 几乎全程为 0（约束满足良好）

### 6. 异常检查
- **无缺失**: 所有 run 的 7 个数据序列长度一致（与 steps 数量匹配）
- **无 NaN/null/Infinity**
- **无空数组**
- **注意**: kl_50pct_s42 仅 200 步/48 点，与其他 run（1000 步/109 点）不对称，但 config 中 `total_steps=200` 明确标注，属预期行为

数据完整，可直接用于绘图。

---
