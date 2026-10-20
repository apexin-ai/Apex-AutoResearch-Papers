# gpu expand cuda23

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_expand_cuda23_20260521T095138_result.json`
- **Structured JSON:** [`ca98e524bc5f1088829f.json`](../../sessions/ca/ca98e524bc5f1088829f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张卡全部在跑，全部确认正常。

## 最终状态

| GPU | 模型 | PID | 日志 | 状态 |
|-----|------|-----|------|------|
| cuda:0 | pythia-2.8b | 283041 | /tmp/gen_pythia.log | 运行中 |
| cuda:0 | llama-3.2-3b | 347968 | /tmp/gen_llama_decoding.log | 运行中 |
| cuda:1 | olmo-2-1b | 283607 | /tmp/gen_olmo.log | 运行中 |
| cuda:1 | qwen3-1.7b | 344399 | /tmp/gen_qwen_greedy.log | 运行中 |
| **cuda:2** | **mistral-7b-v0.3** | **349080** | /tmp/gen_mistral_decoding.log | **~13.7s/it, ETA ~3.8h** |
| **cuda:3** | **pythia-1b** | **349387** | /tmp/gen_pythia1b_decoding.log | **~5.2s/it, ETA ~1.4h** |

### cuda:3 串行链 (watcher PID 349616)

1. **pythia-1b** (当前) → 完成后自动
2. **qwen3-0.6b** → /tmp/gen_qwen06b_decoding.log → 完成后自动
3. **qwen3-8b** → /tmp/gen_qwen8b_decoding.log

Watcher 日志: `/tmp/start_cuda3_chain_watcher.log`

新增 MODEL_PATHS: `pythia-1b`, `qwen3-0.6b`, `qwen3-8b`。8/8 generator 全覆盖已启动。

---
