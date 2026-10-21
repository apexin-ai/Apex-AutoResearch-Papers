# ssh 5090b 7b inference status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090b-7b-inference-status-check_20260520T030447_result.json`
- **Structured JSON:** [`eee1c31d839ae26cf575.json`](../../sessions/ee/eee1c31d839ae26cf575.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个推理进程均正常运行：

| | Seed 123 (GPU0) | Seed 456 (GPU1) |
|---|---|---|
| PID | 164579 | 165186 |
| 启动时间 | 10:49 | 10:49 |
| 显存占用 | 30054 MiB / 32607 MiB (92%) | 30262 MiB / 32607 MiB (93%) |
| GPU 利用率 | 87% | 87% |
| 进度 | 45912 / 301184 (~15.2%) | 45696 / 301184 (~15.2%) |
| 运行时间 | ~14 分钟 | ~14 分钟 |
| 吞吐 | ~9780 tok/s input, ~4810 tok/s output | ~9755 tok/s input, ~4797 tok/s output |

按当前速度估算，每个 seed 总计约 301184 条 prompt，已处理 ~15%，预计还需 **约 1.5 小时**完成。GPU2 和 GPU3 空闲。输出目录 `output/fewnerd_7b/` 下已创建 `qwen25_7b_n8_seed123` 和 `qwen25_7b_n8_seed456` 两个子目录（目前为空，推理完成后写入）。

---
