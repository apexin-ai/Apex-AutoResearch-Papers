# monitoring exec only s45s46 check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitoring_exec-only-s45s46-check_20260516T081650_result.json`
- **Structured JSON:** [`fc210c139ce39e464780.json`](../../sessions/fc/fc210c139ce39e464780.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

注意：PID 728319 实际跑的是 **s46**（不是 s45），命令行显示 `--seed 46 --output_dir sweep_exec_only_s46`。PID 728245 已死。

## 状态汇总

| 实验 | PID | 状态 | 当前 step | 备注 |
|------|-----|------|-----------|------|
| **s45** (cuda:1) | 728245→已结束 | **完成** | 500/500 | checkpoint-500 已保存，日志 "Done."，EXIT_CODE=0 |
| **s46** (cuda:0) | 728319 | **训练中** | 403/500 | 已运行 1h12m，~15s/step，剩余 ~97 steps ≈ 24 min |

**GPU 利用率：**
- GPU 0: 95%, 80285/97887 MiB — s46 训练中
- **GPU 1: 0%, 0 MiB — 空闲可用**

**磁盘：** 167G/250G used (67%), 84G 可用

**s45 最终指标：** prove_rate=0.740, mean_isr=0.360, parse_rate=1.0

---
