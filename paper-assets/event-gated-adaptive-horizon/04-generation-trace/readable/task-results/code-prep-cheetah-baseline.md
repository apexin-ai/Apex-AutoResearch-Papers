# code prep cheetah baseline

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_cheetah_baseline_20260515T145154_result.json`
- **Structured JSON:** [`c2da35d4a016821ecec8.json`](../../sessions/c2/c2da35d4a016821ecec8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### 1. Cheetah Run 环境验证：✅ 通过

已有 `dryrun_cheetah_baseline` 完整验证：
- 环境创建正常，Action Space `Box(-1.0, 1.0, (6,), float32)`
- 训练 12K 步 train_return 从 ~5 涨到 ~65，loss 正常下降
- `dmc_proprio` 通用配置 + `--task dmc_cheetah_run` 方式可用

### 2. 完整启动命令

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s1 --steps 500000 --seed 1 --compile False --device cuda:0"
```

### 3. 预估训练时间

Walker Walk baseline 在同款 RTX PRO 6000 上稳定 FPS ≈ **7.5**（warmup 后）。Cheetah Run 同为 DMC proprio 任务，obs/act 维度相近，FPS 应相当。

- **500K steps / 7.5 FPS ≈ 18.5 小时**

### GPU 状态

| GPU | 占用 | 利用率 | 当前任务 |
|-----|------|--------|---------|
| cuda:0 | 4.2GB / 98GB | 0% | 009d（可能已结束） |
| cuda:1 | 2.8GB / 98GB | 18% | 015b |

cuda:0 利用率 0% 且显存很低，009d 可能已完成。如果确认 009d 结束，可立即在 cuda:0 启动 010a。

---
