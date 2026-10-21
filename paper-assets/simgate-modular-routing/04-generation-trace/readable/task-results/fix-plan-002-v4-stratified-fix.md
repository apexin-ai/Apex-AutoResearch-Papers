# fix plan 002 v4 stratified fix

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan-002-v4-stratified-fix_20260514T060713_result.json`
- **Structured JSON:** [`7609403ff7dbb645e91b.json`](../../sessions/76/7609403ff7dbb645e91b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码修复确认正确。

## 修复报告

### 数据量差异原因
- **plan_c 实际数据**：2040 samples（11 tasks × labeled_steps.jsonl），这就是全部数据，没有丢失
- dryrun 和 v3 都用了相同的 2040 samples（dryrun eval_report 确认：11 tasks, 390 val samples ≈ 20% of 2040）
- 5880 的数字可能来自其他实验（plan_001b_labels/sft_triples.jsonl 有 13869 行）

### Stratified split 修复
- **修复前**：`stratified_split` 按 task_type 分组后随机抽 episode，不管 label → 7/11 task 全部 deterministic，val 中 internal 样本取决于运气
- **修复后**：用 sklearn `train_test_split(stratify=ep_labels)` 按 episode 的 label 分层
  - Val 中 internal: **30 samples**（修复前可能为 0）
  - Val 中 deterministic: **390 samples**
  - 68 episodes 总计：54 train / 14 val
- 代码修改位置：`src/router_sft_train.py:169-199`

### Oversampling 修复
- **方案**：在 `main()` 开头加互斥检查 — 两个都传时只用 `--class_weights`，自动禁用 `--upsample_minority` 并打印 WARNING
- 代码修改位置：`src/router_sft_train.py:381-384`（main 函数内）

### 验证结果
- 数据加载：2040 samples（1830 det / 210 internal）
- Stratified split：train 1620 (det:1440, int:180), val 420 (det:390, int:30)
- class_weights auto：internal=4.50, deterministic=0.5625（ratio 8:1）
- 互斥检查：`--class_weights auto --upsample_minority` → WARNING + upsample 自动禁用 ✓

### v4 启动命令

```bash
tmux new-session -d -s plan-002-formal-v4 "cd /root/autodl-tmp/simgate-modular-routing && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 WANDB_MODE=offline HF_HUB_OFFLINE=1 python src/router_sft_train.py \
  --data_dir results/plan_c \
  --model_name /root/autodl-tmp/models/Qwen/Qwen3-1.7B \
  --epochs 3 \
  --batch_size 4 \
  --gradient_accumulation_steps 8 \
  --class_weights auto \
  --lr 2e-5 \
  --output_dir checkpoints/plan-002-formal-v4 \
  --seed 42"
```

注意：**不加 `--upsample_minority`**，只用 `--class_weights auto` 单一补偿。

---
