# diag westd25068 exp status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd25068-exp-status_20260518T180459_result.json`
- **Structured JSON:** [`ee444c7554fb2fbb2da3.json`](../../sessions/ee/ee444c7554fb2fbb2da3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是诊断结果：

---

## 实验状态

**所有 4 个实验的原始 PID 均已消失，但实验仍在 tmux 中正常运行。** PID 变化可能是因为进程被重启或由 wrapper 脚本衍生了新子进程。

| 实验 | 模型 | 数据集 | 进度 | ETA | 状态 |
|------|------|--------|------|-----|------|
| **exp-033** | Mistral-7B | FOLIO-204 | **42/204** (21%) | ~66 min | **running** (cuda:0, port 8000) |
| **exp-034** | Qwen2.5-14B | PW-600 | **16/600** (3%) | ~650 min (~10.8h) | **running** (cuda:1, port 8001) |
| **exp-035** | Qwen2.5-7B | FOLIO-204 | **43/204** (21%) | ~64 min | **running** (cuda:3, port 8003) |
| **exp-028** | Qwen3-14B thinking | FOLIO-204 | **40/204** (20%) | ~922 min (~15.4h) | **running** (cuda:2, port 8002) |

exp-028 因 thinking 模式每题 ~335s，远慢于其他实验（~24s/题）。有 WARNING: 多次 "Empty after stripping thinking" 和 "No JSON found in response"，可能影响结果质量。

## GPU 状态

**4 卡全部占满，无空闲 GPU。**

| GPU | 显存占用 | 利用率 | 占用者 |
|-----|---------|--------|--------|
| cuda:0 | 88.0/97.9 GB | 96% | exp-033 vLLM |
| cuda:1 | 88.2/97.9 GB | 97% | exp-034 vLLM |
| cuda:2 | 88.3/97.9 GB | 97% | exp-028 vLLM |
| cuda:3 | 88.3/97.9 GB | 96% | exp-035 vLLM |

## 模型下载状态

5 个下载进程中 4 个仍在运行，1 个失败：

| 模型 | 大小 | 状态 |
|------|------|------|
| deepseek-r1-0528-qwen3-8b | 8.3G | 下载中 (PID 62008) |
| DeepSeek-R1-Distill-Llama-8B | — | 下载中 (PID 62020) |
| phi-4-reasoning | 19G | 下载中，有超时重试 (PID 62033) |
| gemma-3-27b-it | 35G | 下载中 (PID 62050) |
| **llama-4-scout** | **60K** | **失败 — Access denied, requires approval** |

llama-4-scout 需要在 HuggingFace 上申请模型访问权限后才能下载。

---
