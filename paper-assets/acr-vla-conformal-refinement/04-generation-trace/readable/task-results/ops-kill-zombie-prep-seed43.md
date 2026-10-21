# ops kill zombie prep seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-zombie-prep-seed43_20260515T115955_result.json`
- **Structured JSON:** [`7106ad57d112092e9a2e.json`](../../sessions/71/7106ad57d112092e9a2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。汇总报告：

---

## 报告

### cuda:2 清理状态
**无需操作。** PID 341878 已不存在，cuda:2 已释放（1MiB 占用，0% 利用率）。

### cuda:3 状态
**空闲。** 1MiB 占用，0% 利用率。

### 当前运行中的实验（勿动）
| GPU | PID | 命令 |
|-----|-----|------|
| cuda:0 | 325264 | `evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --K 10 --max_correction_norm 0.3` |
| cuda:1 | 311886 | `evaluate.py --mode crm_scalar --benchmark spatial --seed 42 --K 10 --max_correction_norm 0.1 --start_task 3` |

两个都是 **spatial** benchmark，跑完后 cuda:0/1 也会释放。

### Object benchmark 数据
**已就位。** `/root/autodl-tmp/libero_data/libero_object/` 下有全部 10 个 task 的 hdf5 文件。

### Python 环境
**就绪。** conda base 环境：
- Python 3.12.3, PyTorch 2.10.0+cu128
- libero 0.1.1, robosuite 1.4.0, transformers 5.8.0, accelerate 1.13.0

### CRM checkpoints
`/root/autodl-tmp/checkpoints/crm_v3_norm/` 下有三个变体：`obs_only/`, `perdof/`, `scalar_unc/`

### 推荐的 seed=43 object eval 部署方案

cuda:2 + cuda:3 现在就可用。启动命令示例（两个 GPU 各跑一个 mode）：

```bash
# cuda:2 — perdof (our method)
CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py \
  --mode crm_perdof --benchmark object --n_rollouts 20 --seed 43 --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt \
  --output_file logs/eval_object_perdof_seed43.json

# cuda:3 — vla_only baseline
CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py \
  --mode vla_only --benchmark object --n_rollouts 20 --seed 43 \
  --output_file logs/eval_object_vla_only_seed43.json
```

可以根据需要替换 mode（`crm_scalar`, `crm_obs_only`, `reconvla` 等）。不需要额外安装任何依赖或拷贝数据。

---
