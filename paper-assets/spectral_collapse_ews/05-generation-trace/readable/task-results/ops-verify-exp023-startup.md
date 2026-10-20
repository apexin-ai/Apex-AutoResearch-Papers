# ops verify exp023 startup

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-exp023-startup_20260524T111156_result.json`
- **Structured JSON:** [`eb8e9d9c3f2029bbb887.json`](../../sessions/eb/eb8e9d9c3f2029bbb887.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### exp_023 — 已成功启动
- **PID** 881066，运行 1 分 10 秒
- **命令**: `run_gpt2m_phase1.py --condition fixed_mix --real_ratio 0.25 --generations 3 --seed 42 --gpu 0`
- **GPU 0**: 19,282 MiB / 97% 利用率
- **日志**: 仅 3 行（初始化警告），刚进入 Generation 0 评估阶段，正常

### exp_022c — 正在跑 Generation 2/3
- **PID** 868285，已运行 3 小时 32 分钟
- **命令**: `run_gpt2m_phase1.py --condition fixed_mix --real_ratio 0.3 --generations 3 --seed 42`
- **GPU 1**: 26,431 MiB / 97% 利用率
- **进度**: Gen 0 (baseline eval) ✓ → Gen 1 ✓ → **Gen 2/3 进行中**（最后一代）
- **日志**: 2,493 行
- **预计剩余**: Gen 1 大约耗时 ~1.5h，Gen 2 类似，估计还需 **~1–1.5 小时**完成

### GPU 状态
| GPU | 实验 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 | exp_023 (r=0.25) | 19.3 GB / 95.6 GB | 97% |
| 1 | exp_022c (r=0.3) | 26.4 GB / 95.6 GB | 97% |

两张卡都满载运行，一切正常。

---
