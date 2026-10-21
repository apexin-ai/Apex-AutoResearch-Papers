# ssh mmlu speed check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mmlu-speed-check_20260513T192735_result.json`
- **Structured JSON:** [`4c5a7c348fcc60fd9984.json`](../../sessions/4c/4c5a7c348fcc60fd9984.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

```
MMLU paraphrase:
- PID: 204472 (vLLM engine: 204758)
- GPU 0 utilization: 100%
- GPU 0 memory: 22541/24564 MiB (91.8%)
- batch_size: 16
- 当前进度: 168/878 batches (19%)
- 运行时间: ~13 min
- ETA: ~53 min (平均 4.5s/batch，但波动大，2.7-6.9s/batch)
- vLLM 配置: LLM(model=..., trust_remote_code=True, max_model_len=4096)
  - gpu_memory_utilization: 未设置（默认 0.9）
  - tensor_parallel_size: 未设置（默认 1）
- 吞吐: input 144-1258 toks/s, output 138-636 toks/s（不稳定）

GSM8K (GPU 1):
- PID: 189375
- GPU 1: 96% util, 15133/24564 MiB
- ⚠️ vLLM 初始化失败，回退到 transformers（慢 ~10x）
- 错误: "Free memory on device cuda:0 (8.48/23.52 GiB) < desired 0.92"
- 当前: retry 第 2 轮, 14/38 batches, ~42s/batch
- ETA: ~17 min

ARC (GPU 2):
- PID: 190717
- GPU 2: 95% util, 15201/24564 MiB
- ⚠️ vLLM 初始化失败，同样回退到 transformers
- 当前: retry 第 2 轮, 10/22 batches, ~49s/batch
- ETA: ~10 min

HumanEval: ✅ 已完成 (vLLM 成功), 26/164 passed QC (15.9%)

全部 6 GPU:
GPU 0: 100% 303W  22541MiB  MMLU (vLLM)
GPU 1:  96% 283W  15133MiB  GSM8K (transformers fallback)
GPU 2:  95% 322W  15201MiB  ARC (transformers fallback)
GPU 3:   0%  22W      0MiB  idle
GPU 4:   0%  11W      0MiB  idle
GPU 5:   0%  15W      0MiB  idle
```

**关键问题**：

1. **GSM8K 和 ARC 的 vLLM 全部失败**，回退到逐条 transformers 生成，速度只有 vLLM 的 ~1/10。原因是启动时 GPU 显存不足（可能与同时启动多个进程或之前的 MMLU v1/v2 残留进程有关）。它们快完成了所以不值得重启。

2. **MMLU 速度波动大**（2.7s-6.9s/batch），某些 batch 的 output throughput 突降到 138 toks/s。这是因为某些 MMLU 题目的 paraphrase 输出特别长（长 generation 占用 KV cache 阻塞其他请求）。batch_size=16 对 4090D 24GB 来说偏保守。

3. **建议优化**：
   - MMLU 正在运行中，不建议中断。当前 ETA ~53 min 可接受。
   - 如果 GSM8K/ARC 完成后需要更多 retry，可以 kill 后用 vLLM 重跑（此时 GPU 1/2 会是干净的）。
   - `paraphrase_gen.py` 第 219 行的 vLLM 初始化可加 `gpu_memory_utilization=0.95` 提高 KV cache 容量。
   - HumanEval QC 通过率只有 15.9%，后续需要关注。

---
