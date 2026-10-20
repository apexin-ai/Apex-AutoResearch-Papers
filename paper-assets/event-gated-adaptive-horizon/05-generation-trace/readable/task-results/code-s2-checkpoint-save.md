# code s2 checkpoint save

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_s2-checkpoint-save_20260516T133641_result.json`
- **Structured JSON:** [`e7fe261c65fffa3a46c6.json`](../../sessions/e7/e7fe261c65fffa3a46c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修改总结：

**configs.yaml**: 添加 `checkpoint_every: 0`（默认禁用）

**dreamer.py** (line 349-350): 在 `latest.pt` 保存后新增 2 行：
```python
if config.checkpoint_every > 0 and logger.step % config.checkpoint_every < config.eval_every:
    torch.save(items_to_save, logdir / f"checkpoint_{logger.step}.pt")
```

**脚本修改**:
- `exp_008d_civo_trigger_s2.sh`: 加 `--checkpoint_every 25000`
- `exp_018_full_sgs_s2.sh`: 加 `--checkpoint_every 25000`
- `exp_001_baseline_s2.sh`: 加 `--checkpoint_every 100000`

逻辑说明：由于 `eval_every=10000`，checkpoint 会在首次越过目标步数边界时保存。对于 25000 间隔，实际保存点在 30k, 50k, 80k, 100k（最近的 10k 倍数）。`latest.pt` 保存逻辑不受影响。

---
