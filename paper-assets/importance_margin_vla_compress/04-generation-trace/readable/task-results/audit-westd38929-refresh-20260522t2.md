# audit westd38929 refresh 20260522T2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd38929_refresh_20260522T2_20260522T203123_result.json`
- **Structured JSON:** [`da6db0ae2e4b20fcebfd.json`](../../sessions/da/da6db0ae2e4b20fcebfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计完成汇报

### 四卡状态

| GPU | 显存占用 | 利用率 | 实验 | PID | 状态 |
|-----|---------|--------|------|-----|------|
| cuda:0 | 10.9/97.9 GB | 30% | Random k=0.9 Long seed42 | 989045 | 运行中 (1h25m) |
| cuda:1 | ~0 → 加载中 | 0% | **新部署** Random k=0.3 Long seed42 | 84327 | 刚启动 |
| cuda:2 | ~0 → 加载中 | 0% | **新部署** L2norm k=0.5 Long seed42 | 84491 | 刚启动 |
| cuda:3 | 10.7/97.9 GB | 19% | Random k=0.5 Long seed42 | 59244 | 运行中 (28m) |

### 收割结果 (4个实验 RUNNING → DONE)

| 实验 | Suite | Mode | k | SR | vs Baseline |
|------|-------|------|---|-----|-------------|
| L2norm k=0.85 Long | libero_10 | l2norm | 0.85 | **78.0%** | 91.6% → -13.6pp |
| Random k=0.95 Long | libero_10 | random | 0.95 | **61.2%** | 91.6% → -30.4pp |
| L2norm k=0.7 Long | libero_10 | l2norm | 0.70 | **60.0%** | 91.6% → -31.6pp |
| Random k=0.85 Goal | libero_goal | random | 0.85 | **52.4%** | vs k=0.9 (62.6%) → -10.2pp |

### 关键发现

- **Long suite 对 pruning 极度敏感**：Random k=0.95 仅去掉 5% 就从 91.6% 暴跌到 61.2%（-30pp），远超其他 suite
- **L2norm 在 Long 上仍显著优于 Random**：k=0.85 时 L2norm 78.0% vs Random k=0.95 61.2%，L2norm 去掉 15% 仍优于 Random 去掉 5%
- **Goal Random cliff 在 k=0.85-0.9**：从 62.6% → 52.4%，每下降 5% keep_ratio 掉 ~10pp

### 新部署 (2个)

| 实验 | GPU | tmux session |
|------|-----|-------------|
| Random k=0.3 Long seed42 | cuda:1 | eval_random_k03_long |
| L2norm k=0.5 Long seed42 | cuda:2 | eval_l2norm_k05_long |

### 过期 RUNNING 条目

`eval_pi05_l2norm_k095_spatial_seed42`、`eval_pi05_random_k085_spatial_seed42`、`eval_pi05_random_k0925_object_seed43` — 均已在 registry 中标记 DONE，无需处理。

---
