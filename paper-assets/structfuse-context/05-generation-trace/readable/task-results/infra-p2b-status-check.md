# infra p2b status check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_p2b_status_check_20260512T143123_result.json`
- **Structured JSON:** [`a880a768832e458b286e.json`](../../sessions/a8/a880a768832e458b286e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 4 100% 利用率，8025 MiB 已用。Run 2 (p2b_random_s123) 已进入 Epoch 1 训练。

---

**汇总：**

| 项目 | 状态 |
|------|------|
| PID 117618 | **DEAD** — run 2 在 evaluate 阶段崩溃 |
| 死因 | 空 tokens 导致 0 长度 tensor reshape 失败 (`contrastive_model.py:165`) |
| Bug 修复 | 已打补丁：(1) 空 tokens fallback 为 `"[empty]"`；(2) `_pad_2d` 保证 `max_len >= 1` |
| Run 1 eval | **recall@1=94.49%, recall@5=98.43%, recall@10=98.43%** (127 samples, 25 candidates) |
| GPU 4 | 100% 利用率，run 2 已重启训练 (PID 132149) |
| 剩余 | Runs 2-9 将依次自动执行（`run_p2b_all.sh`） |

---
