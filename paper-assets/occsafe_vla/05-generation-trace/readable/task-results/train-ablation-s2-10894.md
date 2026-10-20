# train ablation s2 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_ablation-s2-10894_20260522T061007_result.json`
- **Structured JSON:** [`0257ac430421d9527206.json`](../../sessions/02/0257ac430421d9527206.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 ablation seed-2 训练已成功启动并注册监控。

**汇总：**

| 实验 | GPU | PID | tmux session | 速度 | 预计耗时 |
|------|-----|-----|-------------|------|---------|
| ablation_random_occ_s2 | cuda:0 | 932619 | `ablation_random_occ_s2` | ~1.65s/it | ~23h |
| ablation_occ_detach_s2 | cuda:1 | 932767 | `ablation_occ_detach_s2` | ~1.63s/it | ~23h |

**参数配置：**
- seed=44, max_steps=50005, save_freq=10000, occ_loss_weight=0.01 (default)
- random_occ_s2: `--random_occ True --use_occ_head True`
- occ_detach_s2: `--occ_detach true --use_occ_head True`
- 日志：`/root/runs/occsafe_vla/ablation_{random_occ,occ_detach}_s2.log`
- Checkpoint 输出：`/root/autodl-tmp/checkpoints/ablation_{random_occ,occ_detach}_s2/`
- Cron 监控已注册（300s 间隔）

---
