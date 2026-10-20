# fix mvp pilot v4 final

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mvp_pilot_v4_final_20260512T144919_result.json`
- **Structured JSON:** [`c00afc6f411c3b565367.json`](../../sessions/c0/c00afc6f411c3b565367.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已稳定运行，3 个 step 输出确认。

---

**产出汇总：**

**1. 修复前 tokens_per_generation grep：**
```
pilot_pipeline.py:335: default=100_000_000
config.py:18:       tokens_per_generation: int = 100_000_000
```
（代码默认 100M，无需改；launch 脚本显式覆盖为 90M）

**2. 修复后 launch_pilot_v4.sh：**
```bash
#!/bin/bash
set -euo pipefail
source /root/collapse-aware-mixing/env_init.sh
bash /root/collapse-aware-mixing/preflight.sh
cd /root/collapse-aware-mixing
python3 pilot_pipeline.py \
    --output_dir /root/autodl-tmp/output \
    --num_generations 3 \
    --tokens_per_generation 90000000 \
    --checkpoint_interval_tokens 10000000 \
    --holdout_size 5000 \
    --no_wandb \
    --seed 42
```

**3. 修复后 tokens_per_generation grep：**
```
pilot_pipeline.py:335: default=100_000_000  (代码默认)
launch_pilot_v4.sh:     --tokens_per_generation 90000000  (运行时覆盖为90M)
```

**4. data_utils.py 第 78-92 行（边界保护）：**
```python
    num_train = config.tokens_per_generation // config.max_seq_length
    available = len(ds) - config.holdout_size
    if num_train > available:
        logger.warning(
            "Requested %d train seqs but only %d available (dataset=%d, holdout=%d). Clamping.",
            num_train, available, len(ds), config.holdout_size,
        )
        num_train = available
    num_holdout = min(config.holdout_size, len(ds) - num_train)

    train_ids = ds.select(range(num_train))["input_ids"]
    holdout_ids = ds.select(range(num_train, num_train + num_holdout))["input_ids"]
```

**5. 训练启动日志（前 30 行关键信息）：**
```
=== Pre-flight PASSED ===
PILOT PIPELINE START
  Model: EleutherAI/pythia-1b
  Generations: 3 | Tokens/gen: 90M          ← 确认 90M
  Checkpoint interval: 10M tokens (152 steps)
  Device: cuda
Train: 43945 seqs (90.0M tokens) | Holdout: 5000 seqs  ← 确认 holdout 5000
GENERATION 0 / 2
=== Generation 0: training from EleutherAI/pythia-1b ===
  Train sequences: 43945 | Max steps: 1373 | Save every 152 steps
  0%|          | 1/1373 [00:04<1:51:39,  4.88s/it]
  0%|          | 2/1373 [00:06<1:13:49,  3.23s/it]
  0%|          | 3/1373 [00:09<1:01:47,  2.71s/it]   ← GPU 训练进行中
```

3 项修复已应用，训练 PID 28147 稳定运行中。预计 Generation 0 约 62 分钟完成（1373 steps × ~2.7s/step）。

---
