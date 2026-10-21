# submit llama3b westd41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_llama3b_westd41312_20260516T112517_result.json`
- **Structured JSON:** [`c6d03227136c0188ca63.json`](../../sessions/c6/c6d03227136c0188ca63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已成功启动并正在训练。

## 汇报

| 实验 | PID | GPU | 显存 | GPU利用率 | 速度 | 预计完成 |
|------|-----|-----|------|-----------|------|----------|
| llama3b_uniform_seed42 | 3112 (python) | cuda:0 | 47.3GB/97.9GB | 100% | ~5.2s/it | ~8.8h |
| llama3b_adaptive_seed42 | 4005 (python) | cuda:1 | 47.3GB/97.9GB | 100% | ~5.5s/it | ~9.3h |

- 总步数：6103 steps（200M tokens / batch4 / grad_accum4 / seq2048）
- 两个实验均已进入正常训练循环，loss ~1.7-2.2 范围正常
- GPU 2/3 上还有其他进程在运行（46.5GB 占用）
- 预计完成时间：约 5月17日凌晨 4:00-5:00 (UTC+8)

---
