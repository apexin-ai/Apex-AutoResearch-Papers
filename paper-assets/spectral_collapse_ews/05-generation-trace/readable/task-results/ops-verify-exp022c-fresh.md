# ops verify exp022c fresh

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-exp022c-fresh_20260524T074403_result.json`
- **Structured JSON:** [`f11c423dd07b6c0bb9fc.json`](../../sessions/f1/f11c423dd07b6c0bb9fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

| | GPU 0 | GPU 1 |
|---|---|---|
| **实验** | exp_020 | exp_022c |
| **PID** | 783957 | 868285 (wrapper: 868280) |
| **命令** | `pure_collapse, seed=42, 10 gens, k=0` | `fixed_mix, r=0.3, 3 gens, seed=42` |
| **显存** | 26,431 / 97,887 MiB (27%) | 19,349 / 97,887 MiB (20%) |
| **GPU 利用率** | 95% | 95% |
| **功耗** | 340W / 600W | 352W / 600W |

### exp_020 (GPU 0)
- **Generation 9/10**，正在生成合成样本：**43,840 / 50,000** (~88%)
- 上一次 fine-tuning 完成到 Gen 8，当前 Gen 9 处于数据生成阶段
- 日志持续写入（15:45:22 最新修改），无 error

### exp_022c (GPU 1)
- 刚启动约 **6 分钟**（15:38 启动），处于 **Gen 0 baseline 评估**阶段
- 日志仅 51 行 warning（right-padding），尚未出现 Generation 进度标记
- PID 868280 (bash wrapper) + 868285 (python) 均存活，无异常

### 残留进程
- exp_022.log (85B) 和 exp_022b.log (54B) 均为早期终止的小文件，**无对应 GPU 进程**，已清理干净

---
