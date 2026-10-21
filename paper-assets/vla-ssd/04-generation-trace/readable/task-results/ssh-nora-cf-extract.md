# ssh nora cf extract

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_nora_cf_extract_20260522T023605_result.json`
- **Structured JSON:** [`a3c081084af504f92cf6.json`](../../sessions/a3/a3c081084af504f92cf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程仍在运行（17:29 elapsed），当前 2800/5000 of "wrong" condition。

**状态总结**：
- 进程 PID 597691 活跃（CPU 1100%+, GPU 7922 MiB）
- 当前：`wrong` condition 2800/5000
- 速率变化：task 0-4 快（34s/200样本），task 5+ 慢（~5min/200样本）
- 估计 "wrong" condition 剩余：~55 分钟
- 还有 3 个 condition（empty, shuffled, paraphrased），每个 ~70 分钟
- **预计总完成时间：约 4-5 小时**（非原估计的 15 分钟）

这个慢速可能是因为 task 5+ 的 instruction 更长，导致 tokenization 和 attention 计算量增大。

后台等待脚本已在 `/tmp/cf_wait_done.txt` 监控。进程完成后该文件会写入最终结果。要继续等待还是做其他处理？

---
