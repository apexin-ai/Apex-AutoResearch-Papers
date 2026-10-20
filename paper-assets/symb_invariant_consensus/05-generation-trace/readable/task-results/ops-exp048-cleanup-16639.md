# ops exp048 cleanup 16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp048-cleanup-16639_20260519T162234_result.json`
- **Structured JSON:** [`ba799e6a140336157261.json`](../../sessions/ba/ba799e6a140336157261.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有检查完成，无需清理。汇报如下：

### exp-048 日志确认

`FULL_MVP_DONE` 标记已确认。最终结果：
- **SICA accuracy: 64.8%** (389/600)
- **SC accuracy: 70.0%** (420/600)
- Extraction rate: 88.0%, Contradiction rate: 4.5%
- Wall time: 786.9 min
- 数据集: ProofWriter OWA-D5, n=600

### 清理状态

**无需清理** — exp-048 相关进程和 tmux sessions 已经不存在。

### GPU 最终状态 (westd-16639)

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 88246/97887 MiB | 96% | exp-064 vLLM 运行中 ✓ |
| 1 | 90200/97887 MiB | 100% | exp-072 vLLM 运行中 ✓ |
| 2 | 0 MiB | 0% | 空闲 ✓ |
| 3 | 0 MiB | 0% | 空闲 ✓ |

### tmux sessions

仅剩 `exp064_run`, `exp064_vllm`, `exp072_run`, `exp072_vllm` — 均为活跃实验，保持不动。

---
