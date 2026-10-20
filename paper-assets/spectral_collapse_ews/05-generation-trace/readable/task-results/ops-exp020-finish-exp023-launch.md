# ops exp020 finish exp023 launch

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp020-finish-exp023-launch_20260524T083922_result.json`
- **Structured JSON:** [`8f8b198042d69b0cba93.json`](../../sessions/8f/8f8b198042d69b0cba93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在汇总报告。

---

## 报告

### 任务 1: exp_020 状态

**未完成，正在 Gen 10 样本生成阶段 (5760/50000)**

- PID 783957 存活，已运行 22 小时
- GPU 0: 96% 利用率，26GB VRAM 占用
- Gen 0-9 已完成，Gen 10 正在生成样本，预计还需 1.5-2 小时（含训练+评估）

Gen 0-9 数据摘要（pure_collapse, seed42, mix_ratio=0.0）：

| Gen | eff_rank | PPL | D-4 | σ₁ |
|-----|----------|-----|-----|----|
| 0 | 23.09 | 15.45 | 0.9127 | 6598.1 |
| 1 | 155.22 | 16.42 | 0.8907 | 1463.5 |
| 2 | 185.37 | 18.94 | 0.8682 | 1190.7 |
| 3 | 184.86 | 23.33 | 0.8368 | 1172.3 |
| 4 | 169.56 | 32.11 | 0.7636 | 1224.0 |
| 5 | 151.94 | 49.35 | 0.6583 | 1317.5 |
| 6 | 136.09 | 76.81 | 0.5590 | 1449.3 |
| 7 | 121.29 | 123.66 | 0.5008 | 1548.4 |
| 8 | 110.92 | 198.01 | 0.4598 | 1592.7 |
| 9 | 102.96 | 328.75 | 0.4200 | 1570.7 |

结果 JSON 中无单独的 SLV 字段，只有 top_10_singular_values 和 eff_rank/log_det。

### 任务 2: exp_022c 状态

**正常运行，处于 Gen 0 评估阶段**

- PID 868285 存活，运行 1 小时
- GPU 1: 94% 利用率，19GB VRAM
- 命令: `run_gpt2m_phase1.py --condition fixed_mix --real_ratio 0.3 --generations 3 --seed 42`
- 日志 807 行全是 padding 警告，无 Gen 完成标记——说明仍在 Gen 0 文本生成/评估阶段
- GPU 高利用率确认进程未卡住，只是生成较慢

### 任务 3: exp_023

**未启动。** cuda:0 被 exp_020 (PID 783957) 占用，需等 exp_020 完成后再启动。

---
