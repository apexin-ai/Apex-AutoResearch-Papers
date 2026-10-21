# ops eval status check westd35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_status_check_westd35807_20260525T071936_result.json`
- **Structured JSON:** [`b6c647eb3c7e4e2c308c.json`](../../sessions/b6/b6c647eb3c7e4e2c308c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**全部 4 个 eval 正常运行中**，没有挂起或失败。GPU 利用率 0% 是 nvidia-smi 采样瞬间的假象，进程持续输出日志。

### 当前进度

| Eval ID | GPU | 进度 | TSR (interim) | CAR (interim) | Collision eps | ETA (服务器时间) |
|---------|-----|------|---------------|---------------|---------------|-----------------|
| s1_l005 | cuda:0 | **128/200** | 32.0% (41/128) | 54.7% (70/128) | 58 | ~16:25 |
| s1_l01 | cuda:1 | **120/200** | 22.5% (27/120) | 54.2% (65/120) | 55 | ~16:35 |
| s2_l005 | cuda:2 | **119/200** | 26.1% (31/119) | 57.1% (68/119) | 51 | ~16:37 |
| s2_l01 | cuda:3 | **118/200** | 20.3% (24/118) | 53.4% (63/118) | 55 | ~16:39 |

### 关键观察

- 平均 ~0.9 min/episode，全部预计 **16:40 前完成**（服务器时间，当前 15:20）
- 4 个 tmux session 均健康：`eval_s1_l005`, `eval_s1_l01`, `eval_s2_l005`, `eval_s2_l01`
- serve_policy 4 个进程（PID 12031/12034/12037/12040）已运行 ~1h55min
- **TSR 整体偏低**（20-32%），大量 episode 在 300 steps 超时（FAIL+safe）
- **碰撞率高**（~45%），moka_pot 和 wine_bottle 是最频繁的碰撞障碍物
- s1_l005（seed1 + λ=0.05）表现最好，s2_l01（seed2 + λ=0.1）最差

---
