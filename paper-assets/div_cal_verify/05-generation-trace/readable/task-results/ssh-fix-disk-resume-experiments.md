# ssh fix disk resume experiments

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-disk-resume-experiments_20260512T143912_result.json`
- **Structured JSON:** [`519661d5b69c01f6626e.json`](../../sessions/51/519661d5b69c01f6626e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

**磁盘清理**：释放约 9GB（gen_0/gen_1 checkpoint 各 3.3G + gen_3 不完整数据），根分区从 100% → 68%（9.8G 可用）

**软链接**：`/root/div_cal_verify/results` → `/root/autodl-tmp/div_cal_verify/results/`，正常工作。gen_0-2 的 metrics.json 均保留完整。

**串行脚本 PID**：
- 外层 bash: 42073
- Python run_mvp.py (rgds): 42079（CPU 136%, RAM 3.3GB，正在加载模型）

**磁盘当前状态**：
| 分区 | 大小 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30G | 21G | 9.8G | 68% |
| 数据盘 `/root/autodl-tmp/` | 250G | 3.3G | 247G | 2% |

**实验状态**：RGDS 已启动，模型加载中（输出缓冲未 flush，日志暂只有 "Starting RGDS"，无报错）。后续 checkpoint 和结果会写入数据盘，不会再撑爆根分区。三个方法（rgds → external_only → uncurated）会串行执行。

---
