# ops disk cleanup and resume

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-and-resume_20260517T001737_result.json`
- **Structured JSON:** [`9abbba2f6ac881b14f19.json`](../../sessions/9a/9abbba2f6ac881b14f19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 指标 | 值 |
|------|------|
| 清理前 | 250G / 250G (100%) |
| 清理后 | 55G / 250G (22%) |
| **释放空间** | **~195G** |

### 删除明细
- `exec_retrain_v3_s42` + `exec_retrain_v3_s43`: 全删 (30G, 失败实验)
- `plan001_exec_only_s43_1000_r2`: 删 checkpoint-100 + 顶层 model (~24G)
- `gated_warmstart_v3_t015_s43` + `gated_warmstart_v3_s43_r2`: 删 model + checkpoint-300 (~62G)
- `plan018_additive_random_b01_s44_r2` + `plan001_exec_only_s44_1000_r2`: 删 model (~32G)
- 4 个 `w2_1.7b_*` 目录: 删 model + checkpoint-500 (~52G)

### checkpoint-50 状态

- **global_step=50**, epoch=0.2, 4 shard model weights 完整 (~15G)
- **无 optimizer/scheduler/rng state** — 不能真正 resume，只能 warm-start

### 建议

checkpoint-50 缺少 optimizer 状态，按 C012 约束，不建议用它做 resume（步数语义不明确）。建议从 base model 重新训练 1000 步：

```bash
export CUDA_VISIBLE_DEVICES=0
python train_grpo.py \
  --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct \
  --data_path data/train_500_seed42.jsonl \
  --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r3 \
  --num_train_steps 1000 \
  --seed 43 \
  --save_total_limit 1 \
  ...
```

如果只需要 50 步之后的训练效果且接受 optimizer reset，也可以用 checkpoint-50 作为 `--model_path` 起点训练 950 步（但注意这与从头训练 1000 步不完全等价）。

---
