# ssh westd phase2 final collect

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-phase2-final-collect_20260519T112617_result.json`
- **Structured JSON:** [`8025adb32b9e498f5ff9.json`](../../sessions/80/8025adb32b9e498f5ff9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据已收集。以下是报告。

---

## Phase 2 状态报告

### 1. GPU Log 最终状态

| GPU | 当前任务 | 已完成 | 剩余队列 |
|-----|---------|--------|---------|
| GPU 0 | phi4_d025 MMLU (running) | phi4_d000, phi4_d005 | d050, d100 |
| GPU 1 | qwen14b_d025 MMLU (running) | qwen14b_d000, qwen14b_d005 | d050, d100 |
| GPU 2 | qwen7b_d100 MMLU (running) | qwen7b d000~d050 (4个) | **gemma2_d000** |
| GPU 3 | gemma2_d050 MMLU (running) | gemma2_d005, gemma2_d025 | d100, **olmo2 全部5个** |

所有 4 个 GPU 正常运行，无报错。

### 2. 完成进度：10/25

有 `.done` 标记的（MMLU + ARC 均完成）：
- phi4_d000, phi4_d005
- qwen14b_d000, qwen14b_d005
- qwen7b_d000, qwen7b_d005, qwen7b_d025, qwen7b_d050
- gemma2_d005, gemma2_d025

### 3. 完整结果表（已完成的 10 个）

| Model | Dosage | MMLU | ARC |
|-------|--------|------|-----|
| **Phi-4** | d000 | 0.7644 | 0.9206 |
| | d005 | 0.7636 | 0.9181 |
| | d025 | 🔄 running | |
| | d050 | queued | |
| | d100 | queued | |
| **Qwen2.5-14B** | d000 | 0.6944 | 0.9104 |
| | d005 | 0.6901 | 0.9036 |
| | d025 | 🔄 running | |
| | d050 | queued | |
| | d100 | queued | |
| **Qwen2.5-7B** | d000 | 0.6611 | 0.8788 |
| | d005 | 0.6474 | 0.8609 |
| | d025 | 0.6298 | 0.8404 |
| | d050 | 0.6307 | 0.8456 |
| | d100 | 🔄 running | |
| **Gemma-2-9B** | d000 | queued (GPU2) | |
| | d005 | 0.6342 | 0.7782 |
| | d025 | 0.6456 | 0.8737 |
| | d050 | 🔄 running | |
| | d100 | queued | |
| **OLMo-2-7B** | d000 | queued (GPU3) | |
| | d005 | queued | |
| | d025 | queued | |
| | d050 | queued | |
| | d100 | queued | |

### 4. Director 特别关注项

- **Gemma-2 d000**: 尚未评估。排在 GPU 2 队列末尾（qwen7b_d100 之后），预计 ~30min 后开始。
- **OLMo-2 全部 5 个**: 均未开始。全部排在 GPU 3 队列末尾（gemma2_d100 之后），GPU 3 当前还有 gemma2_d050 + d100 要跑完，OLMo-2 预计 1.5~2h 后才开始，全部完成需 ~3-4h。
- **Phi-4 d100**: 未开始。GPU 0 还需跑完 d025 + d050，预计 ~1.5h 后到 d100。

### 5. 负载分配不均

GPU 3 队列最重（9 个任务：gemma2×4 + olmo2×5），GPU 0/1 各 5 个，GPU 2 是 6 个。GPU 0/1/2 会比 GPU 3 早完成 1-2 小时处于空闲状态。如需加速可考虑将部分 OLMo-2 任务迁移到先完成的 GPU。

---
