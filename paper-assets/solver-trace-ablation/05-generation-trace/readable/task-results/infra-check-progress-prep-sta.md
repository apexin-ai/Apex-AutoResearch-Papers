# infra check progress prep sta

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-progress-prep-sta_20260514T160414_result.json`
- **Structured JSON:** [`204a1604cc0971e1c756.json`](../../sessions/20/204a1604cc0971e1c756.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`save_total_limit=1` is hardcoded in train_grpo.py line 425. Good, C003 is satisfied.

Here's the report:

---

## plan018-additive-random-b01-s43-r2

| 指标 | 值 |
|------|-----|
| PID | 858386 (wrapper) / 858391 (python3) |
| 进度 | **250/500 (50%)** |
| 已运行 | 40 分钟 |
| step 速度 | ~7-9s/step |
| 预计剩余 | **~33 分钟**（日志估计 35:50） |
| GPU | cuda:0, 86031 MiB / 97887 MiB |
| 最新 metrics (step 250) | reward=1.052, prove_rate=1.000, isr=0.359, parse_rate=1.000 |

训练正常，prove_rate 已到 1.0，reward ~1.0 附近，趋势健康。

## plan006-prolog-sta-s43

**GPU 1 当前被占用** — PID 881804 正在运行 eval_sta.py（plan006_prolog_exec_s43_r3 评估，已跑 5 分钟，预计还需 ~10-15 分钟）。需等评估完成后再提交。

`/root/autodl-tmp/outputs/plan006_prolog_sta_s43/` 已存在但为空目录（之前失败的 run），可直接覆盖写入。

**完整提交命令：**

```bash
export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_sta.yaml \
  --data_path data/train_500_seed42.jsonl \
  --num_steps 500 \
  --seed 43 \
  --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s43
```

约束检查：
- C001 ✓ 使用 train_500_seed42.jsonl
- C002 ✓ export CUDA_VISIBLE_DEVICES（非 inline）
- C003 ✓ save_total_limit=1 已在 train_grpo.py:425 硬编码
- C005 ✓ 显式设置 CUDA_VISIBLE_DEVICES=1

## 磁盘

```
/dev/md0  250G  168G  83G  68%  /root/autodl-tmp
```

83G 可用，足够一次训练（单 checkpoint ~16GB + reward_log）。

---
