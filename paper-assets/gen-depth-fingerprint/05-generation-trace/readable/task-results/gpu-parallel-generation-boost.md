# gpu parallel generation boost

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_parallel_generation_boost_20260521T081901_result.json`
- **Structured JSON:** [`ae589f4d3ff418d78572.json`](../../sessions/ae/ae589f4d3ff418d78572.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。最终状态：

| GPU | PID | 模型 | 策略 | VRAM | GPU-Util |
|-----|-----|------|------|------|----------|
| **cuda:0** | 283041 | Pythia-2.8b | greedy → topk (自动) | 6.2GB | 68% |
| **cuda:1** | 283607 | OLMo-2-1b | greedy → topk (自动) | 3.6GB | 87% (共) |
| **cuda:1** | 344399 | **Qwen3-1.7B** (新) | greedy → topk | 4.0GB | |
| cuda:2 | — | 空闲 | — | 0 | 0% |
| cuda:3 | — | 空闲 | — | 0 | 0% |

**cuda:1 合计 7.6GB/32GB，利用率从 45% 提升到 87%。**

操作总结：
- **已 kill** `start_qwen_after_olmo.sh` watcher（PID 340310/340315），避免 OLMo 结束后重复启动 Qwen
- **已启动** Qwen3-1.7B (PID 344399) 在 cuda:1 并行运行，从 81 seeds 处 resume，~5.17 it/s
- **未启动** Pythia topk / OLMo topk — 两个现有进程的 `--strategies greedy topk` 参数已包含 topk，greedy 完成后自动执行。单独启动会写同一个输出文件造成数据损坏
- **不需要 watcher 脚本** — 三个进程各自按 greedy → topk 顺序执行，无需外部调度

---
