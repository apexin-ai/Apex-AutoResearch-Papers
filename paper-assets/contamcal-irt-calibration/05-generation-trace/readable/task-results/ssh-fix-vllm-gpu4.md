# ssh fix vllm gpu4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-vllm-gpu4_20260513T184711_result.json`
- **Structured JSON:** [`6812dd90e39b6e05d09d.json`](../../sessions/68/6812dd90e39b6e05d09d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM 修复成功。

```
=== vLLM Fix Result ===
Status: FIXED
vLLM version: 0.20.2
torch version: 2.11.0+cu130
Root cause: torch._inductor.select_algorithm.py 中 TritonTemplate 和 extern kernel 的 
            duplicate 断言在 vLLM 初始化时被重复触发（PyTorch 2.11 兼容性问题）
Fix: 注释掉 select_algorithm.py 中两行 duplicate 断言（line 1775, 2264）
     备份保存在 select_algorithm.py.bak

Performance:
  - 模型加载: 17.2s
  - 单条生成: 0.87s
  - 10条批量: 1.68s (0.168s/prompt)
  - 吞吐量: ~600 tokens/s output

Recommendation: 
  - vLLM 已可用，可以用来加速 MMLU paraphrase
  - GPU 0 当前有 15GB 占用（transformers 进程），是否 kill 并用 vLLM 重跑由你决定
  - 注意：pip upgrade torch 会覆盖 patch，需要重新打
```

---
