# fix plan 002 004 classweight scripts

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan-002-004-classweight-scripts_20260514T052102_result.json`
- **Structured JSON:** [`4583659cca5845ba2306.json`](../../sessions/45/4583659cca5845ba2306.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All validations pass. Here's the summary:

## 修复清单

### launch_plan002.sh
- `--batch_size 32` → `--batch_size 4`
- 新增 `--gradient_accumulation_steps 8`（有效 batch size = 4×8 = 32）
- eval 步骤保持 `--batch_size 32`（无梯度计算，不会 OOM）
- 参数确认：`--class_weights auto` ✓ / `--upsample_minority` ✓ / `--batch_size 4` ✓ / `--gradient_accumulation_steps 8` ✓ / `--epochs 3` ✓

### router_sft_train.py
- **class_weights 传入 loss**: YES，`WeightedCETrainer.compute_loss()` 已正确将 `class_weights` 传入 `CrossEntropyLoss(weight=...)`，无需修复
- **WeightedRandomSampler**: YES，已在 `get_train_dataloader()` 中实现
- **gradient_accumulation_steps**: 新增 CLI 参数，已连接到 `TrainingArguments`
- **sentinel 机制**: 新增 — 训练+eval 完成后写 `TRAINING_COMPLETE` 文件（含 `completed_at`, `output_dir`, `eval_accuracy`）
- **启动确认日志**: 已有 — class_weights 值 ✓ / sampler 类型 ✓ / 数据分布 ✓

### implicit_router_sft.py (plan-004)
- **class_weights 支持**: N/A — 这是 causal LM（生成式），不是分类器，CrossEntropyLoss weight 作用在 token 级而非路由级，不适用
- **oversampling 支持**: 新增 `--upsample_minority` — 基于 `route_label` 字段用 `WeightedRandomSampler` 过采样少数路由类
- **sentinel 机制**: 新增 `TRAINING_COMPLETE`
- **UpsamplingTrainer**: 新增自定义 Trainer 子类，覆盖 `get_train_dataloader()`

### 验证结果
- plan-002 `--help` 解析: **PASS** — `--gradient_accumulation_steps` / `--class_weights` / `--upsample_minority` 均识别
- plan-002 `--dry_run`: **PASS** — 数据分布 det 95.4% / internal 4.6%，auto weights 将大幅提升 internal 权重
- plan-004 `train --help` 解析: **PASS** — `--upsample_minority` 已识别

---
