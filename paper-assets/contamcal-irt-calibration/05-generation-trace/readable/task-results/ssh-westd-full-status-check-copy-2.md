# ssh westd full status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-full-status-check_20260519T051655_result.json`
- **Structured JSON:** [`10e3688a682c972adb1a.json`](../../sessions/10/10e3688a682c972adb1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29999 全面状态报告

### 服务器验证
4× NVIDIA RTX PRO 6000 Blackwell, 97887 MiB each. Driver 580.82.09, CUDA 13.0. ✓

---

### GPU 实时状态

| GPU | PID | VRAM | Util | CUDA_VISIBLE_DEVICES | 任务 | 进度 | ETA |
|-----|---------|------|------|-----|------|------|-----|
| 0 | 102096 | 37.9G | 93% | 0 | OLMo-2-7B d025 s42 | 3372/3384 (99.6%) | **~30s** |
| 1 | — | 0 | 0% | — | **IDLE** | — | — |
| 2 | 106255 | 37.2G | 86% | 2 | OLMo-2-7B d005 s42 v2 | 2295/3177 (72%) | ~31min |
| 3 | 103574 | 56.7G | 94% | 3 | Phi-4 d050 s42 | 2090/3642 (57%) | ~1h15m |

所有进程 CUDA_VISIBLE_DEVICES 显式设置，与实际 GPU 匹配。✓

---

### Checkpoint .done 状态

| Model | d000 | d005 | d025 | d050 | d100 |
|-------|------|------|------|------|------|
| **Gemma-2-9B** | ✗ | ✓ | ✓ | ✓ (刚完成) | ✗ |
| **Phi-4** | ✓ | ✓ | ✓ | ⏳ 57% | ✗ |
| **OLMo-2-7B** | ✓ | ⏳ 72% (v2) | ⏳ 99.6% | ✗ | ✗ |
| **Qwen2.5-14B** | ✗ | ✗ | ✗ | ✓ | ✓ |

**完成**: 11/20  
**运行中**: 3/20 (OLMo d025 即将完成, OLMo d005 v2 ~31min, Phi-4 d050 ~1h15m)  
**未开始**: 6/20

注: OLMo d005 v1 被 kill (EXIT_CODE=143), v2 在正常训练。

---

### 未完成清单

| 待训练 | Model |
|--------|-------|
| Gemma-2-9B d000 | 未开始 |
| Gemma-2-9B d100 | 未开始 |
| Phi-4 d100 | 未开始 |
| OLMo-2-7B d050 | 未开始 |
| OLMo-2-7B d100 | 未开始 |
| Qwen2.5-14B d000 | 未开始 |
| Qwen2.5-14B d005 | 未开始 |
| Qwen2.5-14B d025 | 未开始 |

注: Qwen2.5-14B d000/d005/d025 没有 .done 文件，但 eval_results_14b 中已有这三个的 eval_results.json（可能是之前训练完成后手动删除了 checkpoint 或 .done 标记不一致）。

---

### Eval 结果

已有 eval_results.json:
- `eval_results/Qwen2.5-7B_d000_s42`
- `eval_results_14b/Qwen2.5-14B_d000_s42`
- `eval_results_14b/Qwen2.5-14B_d005_s42`
- `eval_results_14b/Qwen2.5-14B_d025_s42`
- `eval_results_14b/Qwen2.5-14B_d050_s42`
- `eval_results_14b/Qwen2.5-14B_d100_s42`

---

### 关键动态

1. **GPU 0 即将释放** — OLMo d025 剩 12 steps (~30s)，完成后 GPU 0 空闲
2. **GPU 1 空闲** — 可立即调度新任务
3. 完成后将有 **2 个 GPU 空闲**(0+1)，可安排 Gemma d000/d100 或 Qwen2.5-14B 或 OLMo d050/d100

---
