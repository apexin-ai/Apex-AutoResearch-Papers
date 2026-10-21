# diagnose scale 14b t10 a050 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scale_14b_t10_a050_s42_fp32_20260522T065302_result.json`
- **Structured JSON:** [`6f562c1ec1d41d17a2d7.json`](../../sessions/6f/6f562c1ec1d41d17a2d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/diag_scale_14b_t10_a050_s42_fp32.md`。

**根因**：HF cache 中 `EleutherAI/pythia-1.4b-deduped` 的 safetensors shard 1/2 缺失（仅有 shard 2/2，643MB / 预期 ~2.8GB），模型加载阶段直接报 `OSError` 退出。Generation 0 未开始，无 GPU/磁盘/内存问题。

**修复**：`source /etc/network_turbo` 后用 `hf_hub_download` 补下缺失的 `model-00001-of-00002.safetensors`，然后重跑实验。

---
