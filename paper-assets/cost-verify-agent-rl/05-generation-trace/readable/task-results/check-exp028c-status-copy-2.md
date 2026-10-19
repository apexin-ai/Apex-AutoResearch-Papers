# check exp028c status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp028c_status_20260515T232755_result.json`
- **Structured JSON:** [`165f30ca865d8b472e6b.json`](../../sessions/16/165f30ca865d8b472e6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp028c_selfguide_recipe 状态

### 进程
| PID | 角色 | 运行时间 |
|-----|------|---------|
| 824675 | 主进程 (bash) | 2h10m |
| 828110 | Ray Worker | 2h10m |
| 828111 | Ray Worker | 2h10m |

所有进程存活，无 OOM。

### GPU
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 48,379 / 97,887 MiB |
| 1 | 0% | 48,379 / 97,887 MiB |

利用率 0% 但各占 ~48GB VRAM — 正处于 step 3 的 rollout/环境交互阶段（非 GPU 密集），正常。

### 训练进度
**Step 2/100 (2%)** — 已运行 1h46m，预计剩余 ~86h（~3.6 天），每 step ~53 分钟。

### 关键指标对比

| 指标 | Step 1 | Step 2 | 趋势 |
|------|--------|--------|------|
| **success_rate** | 13.3% | 6.25% | ↓ 下降 |
| **pass@8** | 37.5% | 25.0% | ↓ 下降 |
| action_is_valid | 76.4% | 83.2% | ↑ 改善 |
| action_is_effective | 96.4% | 97.9% | ↑ 改善 |
| entropy | 0.263 | 0.247 | ↓ 略降 |
| **kl_loss** | 0.013 | **0.171** | ↑↑ 跃升 13x |
| pg_loss | 0.008 | 0.007 | → 稳定 |
| grad_norm | 16.9 | 17.3 | → 稳定 |
| num_actions | 45.6 | 47.2 | → 稳定 |
| response_length (mean) | 700.6 | 651.5 | ↓ 略降 |

### 注意事项
1. **success_rate 下降**：13.3% → 6.25%，仅 2 步数据，方差大，暂不报警
2. **kl_loss 跃升 13 倍**（0.013 → 0.171）：策略偏移显著，需持续观察。kl_coef 仍为 0.01，若 KL 继续攀升可能需要干预
3. 日志中大量 `Skipping non-numeric metric 'anchor_obs'` 警告，无害，不影响训练
4. 无报错、无 OOM、无进程崩溃

---
