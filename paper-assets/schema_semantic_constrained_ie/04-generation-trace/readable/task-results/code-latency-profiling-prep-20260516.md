# code latency profiling prep 20260516

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_latency_profiling_prep_20260516_20260516T123851_result.json`
- **Structured JSON:** [`85f72f54cf3e0748dd66.json`](../../sessions/85/85f72f54cf3e0748dd66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本工作正常。2 个 sample 在 GPU 0 上成功运行，平均 2.2s/sample，56.5 tok/s。

**完成：**
- `profile_latency.py` 已部署到 `/root/schema_semantic_constrained_ie/profile_latency.py`
- 支持 `--dataset {scierc,docred}`、`--mode` / `--all_modes`、`--model_path`（默认 FT，可切 base `/root/autodl-tmp/models/Qwen3-8B-ms`）、`--n_samples`、`--device`
- 输出 JSON + 终端表格（mean/median/p95/p99/overhead/throughput + paired t-test）
- Warmup、CUDA synchronize、统计检验齐全
- Dry-run 通过

**运行完整 profiling 的推荐命令**（GPU 0 空闲时）：
```bash
# SciERC 全模式，100 samples
CUDA_VISIBLE_DEVICES=0 python profile_latency.py --dataset scierc --all_modes --n_samples 100

# DocRED 全模式，100 samples
CUDA_VISIBLE_DEVICES=0 python profile_latency.py --dataset docred --all_modes --n_samples 100

# Base model (非 FT)
CUDA_VISIBLE_DEVICES=0 python profile_latency.py --dataset scierc --all_modes --n_samples 50 \
  --model_path /root/autodl-tmp/models/Qwen3-8B-ms
```

---
