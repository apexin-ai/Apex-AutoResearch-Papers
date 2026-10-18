# ops kill and extract metrics

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_and_extract_metrics_20260515T181442_result.json`
- **Structured JSON:** [`3cf199231cc31822ada3.json`](../../sessions/3c/3cf199231cc31822ada3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成，汇总如下：

---

## 1. PID 353520 — KILLED

SIGTERM 成功终止，进程已不存在。

## 2. PID 356698 — 仍在运行

```
356698 python run_yi_mistral_downstream_k2.py
```

## 3. nvidia-smi 显存

| GPU | 已用 | 总量 |
|-----|------|------|
| cuda:0 | 18,839 MiB | 97,887 MiB |
| cuda:1 | 3 MiB | 97,887 MiB |

cuda:0 从 ~36GB 降到 ~18GB，释放了约 18GB（即 353520 占用的部分）。剩余 18GB 为 356698 (Yi/Mistral eval) 占用。

## 4. llama_downstream_eval_results.json 完整 metrics

**Model**: Llama-3.1-8B | **Budget**: 0.25 | **max_2bit**: 2 | **0-shot**

| Task | FP16 Baseline | Uniform 4-bit | Constrained MCKP k=2 |
|------|:---:|:---:|:---:|
| ARC-Challenge | 0.5188 | 0.5256 | 0.5179 |
| HellaSwag | 0.6073 | 0.6024 | 0.6021 |
| PIQA | 0.7922 | 0.7873 | 0.7867 |
| WinoGrande | 0.7388 | 0.7261 | 0.7309 |

**MCKP Allocation Summary**:
- Bit distribution: 4-bit × 253 layers, 8-bit × 1, 2-bit × 2
- Actual budget: 0.25
- Total distortion: 0.7015
- Elapsed: 3387s (~56 min)

**要点**: Constrained MCKP k=2 与 Uniform 4-bit 性能基本持平（差异 < 0.5pp），在 WinoGrande 上 MCKP 略优（+0.48pp vs uniform），说明混合精度分配在同等预算下保持了竞争力。

---
