# fix d080 19828 smollm3 restart

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d080_19828_smollm3_restart_20260519T002312_result.json`
- **Structured JSON:** [`19831eeaec6d628ce16e.json`](../../sessions/19/19831eeaec6d628ce16e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D080 执行完成。

**结果：**
- v2 进程 (PID 399353) 已 kill，cuda:1 显存已释放
- 旧数据 `smollm3_3b_wiki_a100_s42_fp32/` 已删除
- Registry: v2 标记 `conclusion=killed`，v3 已创建并提交
- v3 (PID 408266) 已在 cuda:1 上启动，13835MiB 显存，94% 利用率
- 当前处于 Generation 0 baseline 合成数据阶段，无 NaN
- 显存 13.8GB 符合 fp32 预期（3B * 4B ≈ 12GB + overhead），v2 的 bfloat16 生成阶段只需约 6GB，确认 dtype 已修复

---
