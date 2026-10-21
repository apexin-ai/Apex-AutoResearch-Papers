# diagnosis gpu process check v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_gpu_process_check_v2_20260521T064356_result.json`
- **Structured JSON:** [`e49556c3871d4dfb5be3.json`](../../sessions/e4/e49556c3871d4dfb5be3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有进程正常运行，无错误。**

| 进程 | GPU | 进度 | 速度 | 预计完成 |
|------|-----|------|------|----------|
| pythia-2.8b | cuda:0 (66%) | 72/995 greedy (还有 topk) | 9.07s/it | ~19:35 |
| olmo-2-1b | cuda:1 (46%) | 97/995 greedy (还有 topk) | 8.65s/it | ~19:18 |
| qwen chain | — | 等 OLMo 完成 | — | OLMo 后启动 |
| pythia feature extract | — | 等 Pythia 完成 | — | Pythia 后启动 |

GPU 2/3 空闲。有一个旧的 zombie 进程 (PID 27228, temp_qwen06) 无影响。

---
