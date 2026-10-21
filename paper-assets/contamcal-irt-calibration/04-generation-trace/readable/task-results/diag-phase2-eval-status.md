# diag phase2 eval status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_phase2_eval_status_20260519T112908_result.json`
- **Structured JSON:** [`fddccc7d24d988dd68b7.json`](../../sessions/fd/fddccc7d24d988dd68b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程仍在运行，没有 crash。** 状态总结：

**完成 11/25，进行中 4，待执行 10。** 4 个 GPU 全部活跃（89-99% 利用率）。

### 已完成结果

| Model | d000 | d005 | d025 | d050 | d100 |
|-------|------|------|------|------|------|
| **Qwen2.5-7B MMLU** | 0.661 | 0.647 | 0.630 | 0.631 | 0.643 |
| **Qwen2.5-7B ARC** | 0.879 | 0.861 | 0.840 | 0.846 | 0.850 |
| **Qwen2.5-14B MMLU** | 0.694 | 0.690 | running | - | - |
| **Qwen2.5-14B ARC** | 0.910 | 0.904 | running | - | - |
| **Phi-4 MMLU** | 0.764 | 0.764 | 0.770 | - | - |
| **Phi-4 ARC** | 0.921 | 0.918 | running | - | - |
| **Gemma-2-9B MMLU** | running | 0.634 | 0.646 | running | - |
| **Gemma-2-9B ARC** | running | 0.778 | 0.874 | running | - |
| **OLMo-2-7B** | - | - | - | - | - |

### 当前活跃进程
- GPU0: phi4_d025 ARC 阶段
- GPU1: qwen14b_d025
- GPU2: gemma2_d000 刚开始加载
- GPU3: gemma2_d050

### 预计完成时间
GPU3 是瓶颈（9 个 eval，还剩 6 个含全部 OLMo-2），预计 **~21:30 CST** 全部完成。

报告已写入 `artifacts/phase2_eval_diagnosis.md`。

---
