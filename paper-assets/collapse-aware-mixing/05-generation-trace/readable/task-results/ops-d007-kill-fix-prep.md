# ops d007 kill fix prep

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d007_kill_fix_prep_20260513T022050_result.json`
- **Structured JSON:** [`098e2a07bda20f99b95e.json`](../../sessions/09/098e2a07bda20f99b95e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 全部完成，汇总：

### 1. v5 Kill 确认
- 已终止 PID 32492 (python3 训练) + 32153/32154/32158/32159 (tmux/bash/timeout)
- GPU 0: **0 MiB / 97887 MiB, 0% 利用率**

### 2. padding_side 修复 diff
`generate.py` 两处修改（line 27, 91），在 `generate_synthetic_data` 和 `generate_sample_tokens` 的 `model.eval()` 后各加：
```python
tokenizer.padding_side = "left"
```
修复在 generate 层，pilot_pipeline.py / v6 自动受益，训练侧 tokenizer 不受影响。语法验证 OK。

### 3. G0 复用评估
**不能复用。** G0/final_model 完整存在，但 pipeline 无 `--start-generation` 参数，且 v7 checkpoint_interval 和 output_dir 均不同。v7 从头跑，G0 真实数据训练约几分钟。

### 4. launch_pilot_v7.sh
```bash
#!/bin/bash
set -euo pipefail
source /root/collapse-aware-mixing/env_init.sh
bash /root/collapse-aware-mixing/preflight.sh
cd /root/collapse-aware-mixing
python3 pilot_pipeline.py \
    --output_dir /root/autodl-tmp/output_v7 \
    --num_generations 3 \
    --tokens_per_generation 20000000 \
    --checkpoint_interval_tokens 5000000 \
    --holdout_size 5000 \
    --learning_rate 0.000002 \
    --no_wandb \
    --seed 42
```
vs v5 变化：tokens 90M→20M, checkpoint 10M→5M, output 隔离到 output_v7/

### 5. 环境就绪
- GPU: 0% / 0MiB（空闲）
- 无遗留 Python 进程（仅 jupyter-lab）
- 磁盘: 99GB 可用 (61% used)

### 6. v7 启动命令
```bash
cd /root/collapse-aware-mixing && bash launch_pilot_v7.sh
```

---
