# ops disk cleanup and sft fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-and-sft-fix_20260514T113942_result.json`
- **Structured JSON:** [`3cd9bc1e5fbe67f575a2.json`](../../sessions/3c/3cd9bc1e5fbe67f575a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 总结

### Part 1: 磁盘清理
- 删除 4 个目录共 ~112G
- **可用空间**: 250G → 109G available (57%)
- plan018-s44 (PID 564900) 正常运行，不受影响

### Part 2: train_sft.py
- **无需修改**。脚本已有正确配置：
  - `device_map={"": 0}` (单卡加载)
  - `save_total_limit=1`
  - GPU 隔离逻辑 (C002/C005 合规)
- **Dry-run 通过**: 1 step, 1.82s/it, train_loss=2.44, 最终模型 ~8GB 保存成功

### Part 3: plan009 提交命令建议

```bash
export CUDA_VISIBLE_DEVICES=1 && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/solver-trace-ablation && \
python3 scripts/train_sft.py \
  --model_path /root/autodl-tmp/models/Qwen3-4B \
  --data_path data/train_500_seed42.jsonl \
  --output_dir /root/autodl-tmp/outputs/plan009_sft_s42 \
  --num_steps 500 \
  --seed 42 \
  --gpu 1 \
  --wandb_project solver-trace-ablation \
  --wandb_run plan009-sft-s42
```

注意：必须用 `CUDA_VISIBLE_DEVICES=1`，cuda:0 被 plan018-s44 占用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "": 0
  }
}
```

</details>

---
