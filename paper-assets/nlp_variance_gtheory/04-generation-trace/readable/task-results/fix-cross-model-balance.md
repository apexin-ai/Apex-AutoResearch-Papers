# fix cross model balance

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cross_model_balance_20260521T045353_result.json`
- **Structured JSON:** [`82f9c313c0f2ba177823.json`](../../sessions/82/82f9c313c0f2ba177823.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 fully crossed 数据集全部生成成功。验证通过，每个 cell 都是 200 items。

## 汇报

### 1. Llama FP32 缺失原因
- 缺失 **100 个 conditions**，全部集中在 **temp=0.0**（44/144 存在，100/144 缺失）
- temp=0.3 和 0.7 完整（各 144/144）
- 原因：FP32 推理在 temp=0.0 时某些 shard 未跑完（可能是实验中途中断）

### 2. 各模型 seed 分布
所有模型使用 **相同 seed 集** {42, 123, 456, 789, 1024, 2048}，无需重编码。

| 模型 | BF16 | FP16 | FP32 |
|------|------|------|------|
| Llama | 86,400 ✓ | 86,400 ✓ | **66,400** (缺 temp=0.0 的 100 conds) |
| Gemma | 86,400 ✓ | — | 86,400 ✓ |
| Mistral | 86,400 ✓ | 86,400 ✓ | **56,000** (三个温度均缺，散布各因子) |

### 3. 生成的平衡数据集

| 数据集 | 用途 | 记录数 | Cells | 设计 |
|--------|------|--------|-------|------|
| `cross_model_3way_bf16.csv` | 跨模型方差分解 | 259,200 | 1,296 | 3 model × 3 temp × 6 prompt × 6 seed × 4 order |
| `cross_model_2way_precision.csv` | 精度效应分析 | 230,400 | 1,152 | 2 model × 2 prec × 2 temp × 6 prompt × 6 seed × 4 order |
| `llama_precision_balanced.csv` | Llama 单模型精度 | 115,200 | 576 | 2 prec × 2 temp × 6 prompt × 6 seed × 4 order |

全部 fully crossed，每 cell 200 items，Henderson Method I 可直接使用。

### 4. 平衡前后对比
- **旧** `cross_model_llama_gemma.jsonl`：325,600 条，设计不平衡（Llama fp32 缺 100 条件），Henderson Method I 估计有偏
- **新 Dataset B**：230,400 条，fully crossed，代价是丢弃 temp=0.0（因 Llama fp32 在该温度大量缺失）和 Mistral（fp32 全面不完整）
- **新 Dataset A**：259,200 条，3 模型 bf16-only，保留全部温度，丢弃精度因子

脚本：`scripts/balance_cross_model.py`，输出目录：`results/analysis/`。

---
