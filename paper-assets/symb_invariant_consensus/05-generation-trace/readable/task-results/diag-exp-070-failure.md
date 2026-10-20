# diag exp 070 failure

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp-070-failure_20260519T125802_result.json`
- **Structured JSON:** [`efd0e1cddc1d106fcb2b.json`](../../sessions/ef/efd0e1cddc1d106fcb2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 失败根因
**非真正失败。** 实验完成全部 200/200 题后，managed wrapper 的 tmux session 收到 SIGHUP 信号，trap handler 将其转为 `exit 129`。Cron 系统看到非零 exit code + 无 W&B metrics，误报为失败。

### 日志路径
- 运行日志：`/root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/exp070_run.log`
- 结果文件：`/root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/exp070_results.json`
- Managed log：`~/runs/symb_invariant_consensus/exp-070-qwen7b-logiqa200.log`
- 200/200 intermediates 完整

### 实验结果
| Metric | Value |
|--------|-------|
| SICA | 71.00% (142/200) |
| SC | 68.50% (137/200) |
| Delta | **+2.50pp** |
| Wall time | 59.3 min |

### 是否可以直接重试
**无需重试**，结果完整。需要做的是：
1. 更新 registry 状态为 DONE，补录 metrics（SC=68.50, SICA=71.00, delta=+2.50）
2. 计算 McNemar p-value 补入 Table 1
3. 可以关掉 exp070_vllm tmux session 释放 GPU

### 建议修复方案
针对 cron 误报问题：managed wrapper 的 trap 应在实验正常完成（检测到 DONE 标记）后忽略后续信号，或 cron 监控应优先检查日志中的完成标记而非仅依赖 exit code。

---
