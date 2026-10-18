# exp mistral multi seed ppl v2

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mistral_multi_seed_ppl_v2_20260516T040001_result.json`
- **Structured JSON:** [`f3a192005569fd9fc324.json`](../../sessions/f3/f3a192005569fd9fc324.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常。日志显示：
- Device: **cuda:0**（修复生效，不再是 `cuda:1`）
- Mistral-7B-v0.3 模型加载中，checkpoint shards 已完成
- Seeds: [42, 123, 456]，Budget: 0.25，max_2bit: 2

修复总结：第 340 行新增 `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)`，第 341 行改为 `device = "cuda:0"`。`--gpu N` 现在通过环境变量选物理 GPU，脚本内部统一用逻辑 `cuda:0`，不再越界。

---
