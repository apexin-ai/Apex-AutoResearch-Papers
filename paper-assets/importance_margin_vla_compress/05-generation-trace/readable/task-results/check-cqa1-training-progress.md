# check cqa1 training progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1_training_progress_20260516T233741_result.json`
- **Structured JSON:** [`76bacf6c5768d94ba1b7.json`](../../sessions/76/76bacf6c5768d94ba1b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 0: [Full FT seed=1 100K] step 30900/100000, loss=0.0402, GPU util=42%, mem=2753 MiB
GPU 1: [IMM Full FT 100K seed=42] Stage2 step 8950/20000, action_loss=0.0571, GPU util=62%, mem=4131 MiB
GPU 2: [IMM Full FT seed=0] Stage1 step 9750/10000, margin_loss=0.1350, GPU util=0%*, mem=2881 MiB
GPU 3: [IMM Full FT k=0.7] Stage1 step 5000/10000, margin_loss=0.1699, GPU util=0%*, mem=2881 MiB
```

备注：
- **GPU 0** — Full FT seed=1 从 step 30900 正常推进中（预期从 ~18K 起跑，已跑了 ~12K 步），sps=4.2
- **GPU 1** — IMM seed=42 已完成 Stage1(10K ACIS)，正在 Stage2 expert FT，进度 8950/20000，sps=3.1
- **GPU 2** — IMM seed=0 Stage1 快完成了（9750/10000），预计几分钟后进入 Stage2，sps=4.2
- **GPU 3** — IMM k=0.7 ablation Stage1 进度 5000/10000（50%），sps=4.2

*GPU 2/3 瞬时 util=0% 是 nvidia-smi 采样间隙，进程和显存正常在跑。

---
