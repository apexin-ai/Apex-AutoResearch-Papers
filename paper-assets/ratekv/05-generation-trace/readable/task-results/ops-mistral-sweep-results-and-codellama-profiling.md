# ops mistral sweep results and codellama profiling

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mistral_sweep_results_and_codellama_profiling_20260515T185143_result.json`
- **Structured JSON:** [`1437544101384226d9d9.json`](../../sessions/14/1437544101384226d9d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两件事都完成了。

---

### Part A: Mistral Compounding Sweep V2 — DONE ✓

```
Model: Mistral-7B-v0.3 | Budget: 0.25 | 256 heads (bf16_2bitonly profiles)

    k      PPL    2bit  16bit    mem
    0   7.0352      0    256   1.00
    2   7.0366      2    254   0.99
    4   7.0453      4    252   0.99
    8   7.0636      8    248   0.97
   16   7.1139     16    240   0.95
   32   7.2378     32    224   0.89
   64   7.7747     64    192   0.78
  128  10.4730    128    128   0.56
  256  45.2766    220     36   0.25
```

Registry → `DONE`, conclusion = `success`. Wall clock: ~855s, 0.24 GPU-hours.

### Part B: CodeLlama-7B Profiling — RUNNING

- 脚本已存在于服务器，直接提交
- cuda:0 空闲，已启动 tmux session `codellama_hires_profiling`
- PID: 362945, timeout: 8h
- Registry → `RUNNING`
- 预计耗时较长：32 layers × 32 KV heads = 1024 heads (MHA，是 Llama-8B 的 4 倍)

---
