# code wikievents mistral investigate

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_mistral_investigate_20260517T190323_result.json`
- **Structured JSON:** [`a3cdf4bf85811d4101d9.json`](../../sessions/a3/a3cdf4bf85811d4101d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进度日志没在 tmux 可见区域（可能被 transformers 警告覆盖了 buffer），但文件行数在稳定增长。

**总结：**

- 原始 Mistral unconstrained 进程 (PID 28658) 已 crash，crash 原因无法追溯（tmux buffer 被覆盖）
- 输出停在 93/246 docs
- 已用正确 CLI 参数重启：`--mode unconstrained --resume`，tmux session = `mistral_restart`
- GPU 0 正常运行：16.5GB VRAM / 90% 利用率 / 53°C
- 文件已从 93 增长到 96 行，confirmed 稳定推理中
- 剩余 150 docs，每 doc 约 15-60s，预计 **1.5-3 小时**完成

---
