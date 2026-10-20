# ssh fix gpu1 d050 conflict

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-gpu1-d050-conflict_20260519T124619_result.json`
- **Structured JSON:** [`47b3de94c5a54756418b.json`](../../sessions/47/47b3de94c5a54756418b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：问题已自行解决，无需干预。**

实际情况与预期不同：

| GPU | 状态 | 说明 |
|-----|------|------|
| GPU 0 | PID 173479 跑 d005 eval | 正常 |
| GPU 1 | 空闲 | **从未启动过 OLMo-2 eval 脚本**（gpu1.log 显示跑的是之前的 qwen14b 批次，20:14 已结束）|
| GPU 2 | 空闲 | d100 已完成 |
| GPU 3 | 空闲 | d025→d050 已完成（20:38，日志确认 "ALL olmo2 GPU3 DONE"）|

**为什么没有 race condition**：`olmo2_eval_gpu1.sh` 和 `olmo2_eval_gpu3.sh` 虽然都包含 d025→d050 序列，但只有 GPU3 的脚本被实际执行了（有 `olmo2_gpu3.log` 和对应 tmux session）。GPU1 没有对应的 OLMo-2 tmux session 或日志文件。

**数据完整性**：d025 和 d050 结果完整（JSON 有效、item 数量正确、剂量-响应趋势合理）。无需修复。

---
