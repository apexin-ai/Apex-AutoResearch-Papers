# infra gpu check all servers

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-check-all-servers_20260522T235111_result.json`
- **Structured JSON:** [`344d09a51e5d9c39e776.json`](../../sessions/34/344d09a51e5d9c39e776.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## westd-16639 (4× RTX PRO 6000 Blackwell 96GB)

| GPU | 显存占用 | GPU利用率 | 状态 | 实验 | 进度 |
|-----|---------|----------|------|------|------|
| cuda:0 | 88/98 GB | 97% | **运行中** | Qwen2.5-14B PW **seed456** (vLLM port 8001) | **219/600** (ETA ~7h) |
| cuda:1 | 88/98 GB | 96% | **运行中** | LLaMA-8B PW **seed123** (vLLM port 8006) | **173/600** (ETA ~9.3h) |
| cuda:2 | 0 GB | 0% | **空闲** | — | — |
| cuda:3 | 88/98 GB | 98% | **运行中** | Qwen2.5-14B PW **seed123** (vLLM port 8005) | **200/600** (ETA ~7.5h) |

**注意事项：**
- cuda:0 的 seed456→789 chain 中，**seed789 已完成但结果全错**（SICA=0.0%, SC=0.0%）——原因是 `max_model_len=4096` 与请求的 output tokens 冲突导致 `BadRequestError`，600个问题全部失败。当前 seed456 仍在正常跑。
- 无 tmux session

## westd-14391 (1× RTX PRO 6000 Blackwell 96GB)

| GPU | 显存占用 | GPU利用率 | 状态 | 实验 | 进度 |
|-----|---------|----------|------|------|------|
| cuda:0 | 88/98 GB | 100% | **运行中** | LLaMA-8B PW **seed42** (vLLM port 8000, `run_full_mvp.py`) | **248/600** (ETA ~5.5h) |

**注意事项：**
- 磁盘 30GB 用了 13GB（41%），之前的旧实验曾因磁盘满崩溃，当前空间暂时充足
- 无 tmux session

---

**关键问题：**
1. **seed789 实验数据作废** — vLLM `--max-model-len 8192` 但实验代码请求 4096 output tokens 导致 context 超限，需要修复后重跑
2. **westd-16639 cuda:2 空闲** — 可安排新实验

---
