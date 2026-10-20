# fix deberta code oom

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_deberta_code_oom_20260520T050814_result.json`
- **Structured JSON:** [`9a39f1f130484e136c25.json`](../../sessions/9a/9a39f1f130484e136c25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改已完成，清理已执行。

### Diff

```
- line 97:  va_dl = DataLoader(DS(va_ids, va_masks, va_labels), batch_size=BS*2, collate_fn=collate, num_workers=2, pin_memory=True)
+ line 97:  va_dl = DataLoader(DS(va_ids, va_masks, va_labels), batch_size=BS, collate_fn=collate, num_workers=2, pin_memory=True)
```

Eval batch size: 32 → 16。训练 batch size、梯度累积等超参不变。

### 推荐重启命令

```bash
CUDA_VISIBLE_DEVICES=2 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python scripts/run_deberta_code.py
```

- `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` 作为额外保险，减少碎片化 OOM
- `CUDA_VISIBLE_DEVICES=2` 保持和之前一致（脚本内部用 `cuda:0` 是正确的，它映射到物理 GPU 2）

不自行启动，等主 Agent 通过 `submit_training_job` 提交。

---
