# diagnosis exp062 progress readonly

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp062_progress_readonly_20260521T111438_result.json`
- **Structured JSON:** [`e6238a3ca6d6c8f2d331.json`](../../sessions/e6/e6238a3ca6d6c8f2d331.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_062 进度汇总

| GPU | 模型 | 阶段 | 进度 | 预计剩余 |
|-----|------|------|------|---------|
| 0 | **pythia-2.8b** | topk | 816/995 (82%) | ~45 min |
| 0 | **llama-3.2-3b** | greedy | 384/995 (39%) | ~2h40 (greedy) + ~4.4h (topk) |
| 1 | **olmo-2-1b** | topk | 949/995 (95%) | ~7 min |
| 1 | **qwen3-1.7b** | greedy | 773/996 (78%) | ~58 min (greedy) + ~4h (topk) |
| 2 | **mistral-7b-v0.3** | greedy | 365/996 (37%) | ~2h24 (greedy) + ~3.8h (topk) |
| 3 | **pythia-1b** | greedy | 989/995 (99%) | ~30s |

**GPU 利用率**: 0=91%, 1=86%, 2=87%, 3=49%（pythia-1b 小模型所以低）

**关键状态**:
- **olmo-2-1b** 和 **pythia-1b** 马上完成（两者各自 greedy+topk 中最后一段）
- **pythia-2.8b** topk 阶段也接近尾声
- 有链式启动脚本在后台等待：`extract_after_pythia.sh`、`start_mistral_after_olmo.sh`、`start_cuda3_chain.sh`
- `qwen8b` / `qwen06b` 的日志不存在，未启动
- 最晚完成的是 **llama-3.2-3b**（GPU 0），预计 ~7h 后（约凌晨 02:00）

---
