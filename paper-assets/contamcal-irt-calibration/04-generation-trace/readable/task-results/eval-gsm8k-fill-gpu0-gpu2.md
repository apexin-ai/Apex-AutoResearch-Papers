# eval gsm8k fill gpu0 gpu2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gsm8k-fill-gpu0-gpu2_20260521T085956_result.json`
- **Structured JSON:** [`cf606a48fce2e68327f8.json`](../../sessions/cf/cf606a48fce2e68327f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4/4 GPU 全部在用。

**已完成 GSM8K eval 结果：**

| Model | Dosage | Accuracy | Correct/Total |
|-------|--------|----------|---------------|
| Gemma-2-9b | d000_s0 | **17.82%** | 235/1319 |
| Qwen2.5-14B | d000_s0 | **79.30%** | 1046/1319 |
| Qwen2.5-14B | d005_s0 | **71.19%** | 939/1319 |
| Qwen2.5-14B | d025_s0 | **74.98%** | 989/1319 |
| Qwen2.5-14B | d050_s0 | **81.05%** | 1069/1319 |
| Qwen2.5-14B | d100_s0 | **82.41%** | 1087/1319 |
| Phi-4 | d000_s0 | **84.46%** | 1114/1319 |

**新启动的 eval：**

| GPU | Model | Dosage | PID | Status |
|-----|-------|--------|-----|--------|
| 0 | OLMo-2-7B d100_s0 | gsm8k | 502703 | 模型已加载，正在推理 (16705 MiB) |
| 2 | Gemma-2-9b d100_s0 | gsm8k | 503544 | 模型已加载，正在推理 (19351 MiB) |

**GPU 利用率确认：** 4/4 GPU 全部在工作（GPU 0: 16.7GB, GPU 1: 16.7GB, GPU 2: 19.4GB, GPU 3: 31.7GB）。

**注意：** evaluate.py 当前 37775 bytes (md5: 17673bf3...)，与 C009 reference（37591 bytes）不一致。但 westd 上所有现有结果均使用同一版本，新 eval 也用同一文件，C010 一致性满足。Gemma-2 d000_s0 accuracy 17.82% 异常低，可能值得复查。

---
