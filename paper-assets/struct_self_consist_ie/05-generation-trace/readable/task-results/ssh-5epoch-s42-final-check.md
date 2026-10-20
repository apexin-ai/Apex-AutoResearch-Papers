# ssh 5epoch s42 final check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5epoch_s42_final_check_20260521T180612_result.json`
- **Structured JSON:** [`d3aabce747d2b62d9ea3.json`](../../sessions/d3/d3aabce747d2b62d9ea3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个实验都仍在运行中，cron 报的进程退出是误报。**

| 实验 | 进度 | 已处理/总计 | 速度 | 预计剩余 |
|------|------|-------------|------|----------|
| s42 | 5.6% | 16,960 / 301,184 | ~6,124 toks/s in, ~3,261 toks/s out | ~2h |
| s123 | 5.4% | 16,192 / 301,184 | ~5,894 toks/s in, ~3,143 toks/s out | ~2h |

GPU 状态：4 卡全在用（87%/74%/72%/67% 利用率，各占 ~30GB/32GB VRAM），两个推理进程分别占 2 卡。

输出目录已创建但 `samples.jsonl` 尚未生成（vLLM 推理完成后才会写出）。301,184 = 37,648 × 8 samples，符合预期。

**不做 registry 更新和 cron 删除**——等推理完成后再操作。预计约 2 小时后完成。

---
