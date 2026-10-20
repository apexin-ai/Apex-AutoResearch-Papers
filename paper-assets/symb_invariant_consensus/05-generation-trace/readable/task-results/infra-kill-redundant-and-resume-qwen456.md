# infra kill redundant and resume qwen456

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill-redundant-and-resume-qwen456_20260523T123946_result.json`
- **Structured JSON:** [`de1136298ec4a93b9fab.json`](../../sessions/de/de1136298ec4a93b9fab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 最终状态汇报

### Kill 结果
| 服务器 | GPU | 实验 | 状态 |
|--------|-----|------|------|
| westd-14391 | cuda:0 | LLaMA seed123 | ✓ 已释放，GPU 空闲 |
| westd-30973 | cuda:0 | Qwen seed789-v3 | ✓ 已释放，GPU 空闲 |
| westd-30973 | cuda:1 | LLaMA seed789-v2 | ✓ 已释放，GPU 空闲 |
| westd-16639 | cuda:1 | LLaMA seed456 | ✓ 已释放，GPU 空闲 |

### Resume 结果
Qwen seed456 resume 成功：跳过 478 条已完成，从第 479/600 开始运行，剩余 122 条。tmux session: `qwen_seed456_resume`。

### 最终 GPU 布局

| 服务器 | cuda:0 | cuda:1 | cuda:2 | cuda:3 |
|--------|--------|--------|--------|--------|
| westd-14391 | 空闲 | — | — | — |
| westd-30973 | 空闲 | 空闲 | LLaMA seed456-v2 (326/600) | — |
| westd-16639 | LLaMA seed789 (383/600) | 空闲 | Qwen seed789 (441/600) | **Qwen seed456 resume (478→600)** |

---
