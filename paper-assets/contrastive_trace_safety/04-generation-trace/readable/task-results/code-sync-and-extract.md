# code sync and extract

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sync_and_extract_20260516T191140_result.json`
- **Structured JSON:** [`44eaecd487189bbbef93.json`](../../sessions/44/44eaecd487189bbbef93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

**Extraction 结果：**
- 提取了 **268** 个 traces 的 hidden states（209 jailbreak + 59 safe）
- 总大小：**1.2 GB**
- ���文件大小：3.0–5.4 MB（取决于 trace 长度，每个 trace 形状 `[num_sentences, 13, 4096]` fp16）
- 耗时：~79 秒（3.38 it/s 平均）
- 无错误
- 磁盘剩余：33 GB（充裕）

可以进入下一步 `--step train` 训练 probes。

---
