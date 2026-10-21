# code fix thinking mode eval

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-thinking-mode-eval_20260514T085609_result.json`
- **Structured JSON:** [`3b59950d09b4cca97b65.json`](../../sessions/3b/3b59950d09b4cca97b65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在我有完整的 diff 了。以下是完整产出。

---

## 产出 1：eval_end_to_end.py 修改清单

| 行号 | 改动 |
|------|------|
| 334 (原 333-334) | `apply_chat_template()` 增加 `enable_thinking=False` 参数 |

**已有防御**：line 352 已有 `re.sub(r"&lt;think>.*?&lt;/think>", "", raw_output, flags=re.DOTALL).strip()`——这次修复从源头禁用 thinking，regex 作为兜底保留。

## 产出 2：generative_router_sft.py 修改清单

| 行号 | 改动 |
|------|------|
| 519 | `apply_chat_template()` 增加 `enable_thinking=False` |
| 530 | 新增 `re.sub(r"&lt;think>.*?&lt;/think>", "", raw_output, flags=re.DOTALL).strip()` 兜底清理 |
| 40 | 新增 `import re` |

## 产出 3：implicit_router_sft.py 修改清单

| 行号 | 改动 |
|------|------|
| 440 | `apply_chat_template()` 增加 `enable_thinking=False` |
| 451 | 新增 `re.sub(r"&lt;think>.*?&lt;/think>", "", raw_output, flags=re.DOTALL).strip()` 兜底清理 |
| 30 | 新增 `import re` |

## 产出 4：implicit_router_sft.py vs generative_router_sft.py 代码变更分析

项目没有 git 历史。通过 diff 两文件（`generative_router_sft.py` 文件头注释明确说 "Based on ablation-b's implicit_router_sft.py"），以下是 **ablation-b → v5 的全部实质性改动**：

### 训练逻辑改动（影响模型质量，可能导致 accuracy 差异）

| 改动 | ablation-b (implicit) | v5 (generative) | 影响 |
|------|----------------------|-----------------|------|
| **数据加载+上采样** | `load_implicit_sft_data()` 无上采样 | `load_data()` 内置 `upsample_ratio` 参数，训练前复制少数类样本 | **高**：直接改变训练数据分布 |
| **上采样默认值** | `--upsample_minority` 默认关 | `--upsample_minority` 默认开 (`default=True`)，`--upsample_ratio=1.0`（完全平衡） | **高**：v5 默认双重上采样（数据复制+WeightedRandomSampler） |
| **class_weights 路径** | 支持 `--class_weights auto` 或手动权重，自定义 `WeightedTrainer.compute_loss` 实现 per-sample 加权 loss | **完全移除**，只用上采样 | **中**：loss 计算方式不同 |
| **Loss 计算** | 自定义 `WeightedTrainer.compute_loss`：手动 shift logits + per-sample 加权 | 标准 HuggingFace `Trainer` loss（`SamplerTrainer` 只覆写 dataloader） | **中**：ablation-b 可能有 per-token loss mask 更精细 |
| **Batch size** | 默认 `batch_size=32`, `grad_accum=1`（effective 32） | 默认 `batch_size=4`, `grad_accum=8`（effective 32） | **低**：effective 相同但梯度噪声分布不同 |
| **Eval metrics** | 只有 eval_loss | 新增 `compute_metrics_fn`：routing_acc, internal_recall, det_recall | **无**：不影响训练 |
| **model.config.pad_token_id** | 未设置 | 显式设置 `= tokenizer.pad_token_id` | **低** |
| **bf16/fp16** | 硬编码 `bf16=True` | 动态检测 GPU capability >= 8 → bf16，否则 fp16 | **低** |
| **wandb** | `report_to="none"` | `report_to="wandb"` (unless WANDB_MODE=offline) | **无** |

### 推理路径改动

| 改动 | ablation-b | v5 |
|------|-----------|-----|
| **parse 函数** | `parse_implicit_output` | `parse_output`（同逻辑） |
| **think-tag 清理** | 无 | 无（本次修复前） |
| **Router 类名** | `Implicit1_7BRouter` | `GenerativeRouter` |
| **pad_token_id** | 未设置 | 显式设置 |

### 结论

**v5 vs ablation-b 的 accuracy 差异（74.5% vs 65.4%）最可能来源于数据上采样策略的改变**：
1. v5 默认开启 `upsample_minority=True` + `upsample_ratio=1.0`，在 `load_data` 中先复制少数类，再用 `WeightedRandomSampler`——双重平衡
2. ablation-b 的 `upsample_minority` 默认关闭，依赖 `class_weights` 做 loss 加权
3. v5 移除了自定义 `compute_loss` 中的 per-sample 加权逻辑，改用标准 Trainer loss

如果 ablation-b 实际运行时 `--upsample_minority` 和 `--class_weights` 都没传，则训练在 90:10 不平衡数据上跑，模型倾向全部预测多数类（deterministic），导致 internal recall 低、overall accuracy 低。

---
