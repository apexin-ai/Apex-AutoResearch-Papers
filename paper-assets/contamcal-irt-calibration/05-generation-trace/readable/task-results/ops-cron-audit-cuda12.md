# ops cron audit cuda12

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cron-audit-cuda12_20260515T033757_result.json`
- **Structured JSON:** [`819d8f7134f95aba6f50.json`](../../sessions/81/819d8f7134f95aba6f50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

| GPU | 实验 | PID | 状态 | 运行时间 | GPU Util |
|-----|------|-----|------|---------|----------|
| cuda:1 | exp_001_eval_3B_d000_v2_s123_aligned | 492660 | RUNNING | ~17min | 0% (可能在数据加载/切换 benchmark) |
| cuda:2 | exp_001_eval_3B_d000_v2_s123_para_aligned | 492733 | RUNNING | ~17min | 55% |

**已完成修复：**
- Registry 补录了两个实验的 PID（之前缺失）
- 注册了 2 个 cron 监控（每 8 分钟轮询）：
  - `6f576060` → cuda:1 aligned eval
  - `fe6c35b6` → cuda:2 para_aligned eval
- 进程结束后 cron 会自动读取结果、更新 registry、自删除

---
