# verify generative router code

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_generative-router-code_20260514T074032_result.json`
- **Structured JSON:** [`00d850784a7d85ca6077.json`](../../sessions/00/00d850784a7d85ca6077.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。报告如下：

---

## 验证报告

### 1. 脚本选择

用 **`generative_router_sft.py`**（24KB，May 14 15:23 更新）。它是 `implicit_router_sft.py` 的专用进化版：
- 移除 `class_weights` 路径（只保留 upsample）
- upsample 默认开启
- 训练中计算 `internal_recall` / `det_recall`（非退化检测关键指标）
- 显式设置 `pad_token_id`

### 2. Upsample 机制：**sample 级，双重平衡**

**第一层（数据级）**：`load_data()` 中先按 episode (task_type, variation) 做 stratified split，然后对 **train set 内的少数类 sample 直接复制** 至目标比例。`upsample_ratio=1.0` → 补到 1:1。这是 sample 级，不是 episode 级。

**第二层（采样器级）**：`WeightedRandomSampler` 按 inverse-frequency 权重再做 epoch 内均衡采样。

### 3. CLI 参数（`generative_router_sft.py train`）

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--data_dir` | **必填** | 数据路径 |
| `--output_dir` | `checkpoints/plan-002-generative` | 输出目录 |
| `--batch_size` | **4** | micro batch |
| `--gradient_accumulation_steps` | **8** | 梯度累积 |
| `--upsample_minority` | **True** | 默认开启，`--no_upsample_minority` 关闭 |
| `--upsample_ratio` | **1.0** | 少数类:多数类目标比 |
| `--max_steps` | 0 | >0 用于 dry-run |
| `--epochs` | 3 | |
| `--lr` | 2e-5 | |
| `--lora_r` / `--lora_alpha` | 16 / 32 | |

### 4. 数据确认

- **2040 条** 总量（与 ablation-b 一致）
- 分布：~1830 deterministic / ~210 internal（≈90:10）
- route_label 样例：`"deterministic"` 对应 `[SIMULATE]` 前缀，`"internal"` 对应直接输出 action

### 5. Eval 指标

训练中自动计算 `routing_acc`、`internal_recall`、`det_recall`、`internal_n`、`det_n`。`internal_recall` 是非退化关键指标。

### 6. ⚠️ 关键注意：effective batch size 差异

| 实验 | batch_size | grad_accum | **effective batch** |
|------|-----------|------------|-------------------|
| generative-v1-ga8 | 4 | 8 | **32** |
| generative-v1-ga1 | 4 | 1 | **4** |
| ablation-b (对照) | 32 | 1 | **32** |

**ga1 的 effective batch 只有 4，不是 32。** 如果 Director 的意图是在相同 effective batch (32) 下对比 grad_accum 机制，则 ga1 应设 `--batch_size 32 --gradient_accumulation_steps 1`。如果意图是对比不同 effective batch（32 vs 4）对训练的影响，则当前默认参数即可。

### 7. 提交命令

```bash
# generative-v1-ga8 (effective batch=32)
python src/training/generative_router_sft.py train \
  --data_dir data/plan-004-implicit/implicit_sft.jsonl \
  --output_dir checkpoints/generative-v1-ga8 \
  --gradient_accumulation_steps 8

# generative-v1-ga1 (effective batch=4, 除非改 batch_size)
python src/training/generative_router_sft.py train \
  --data_dir data/plan-004-implicit/implicit_sft.jsonl \
  --output_dir checkpoints/generative-v1-ga1 \
  --gradient_accumulation_steps 1
```

**代码无需额外修改即可提交。** 唯一需确认的是 ga1 的 effective batch size 是否符合 Director 预期。

---
