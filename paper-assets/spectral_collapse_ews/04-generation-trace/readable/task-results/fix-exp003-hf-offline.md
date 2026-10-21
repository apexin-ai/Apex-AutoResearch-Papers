# fix exp003 hf offline

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp003_hf_offline_20260517T040652_result.json`
- **Structured JSON:** [`86576cd029521a380519.json`](../../sessions/86/86576cd029521a380519.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**结果：**
- **缓存路径**: `/root/.cache/huggingface/hub/models--EleutherAI--pythia-410m-deduped/snapshots/c4fc8d586d62df497f1f9b69d66d3ca419992d3e/` — 包含 `model.safetensors`、`tokenizer.json` 等，完整可用
- **PID 77663**: 已 kill（force_killed）
- **GPU 1**: 已释放（3 MiB）

**结论**: 缓存完整，重新提交时加 `HF_HUB_OFFLINE=1` 环境变量即可从本地缓存加载，无需网络。请用 `submit_training_job` 重新提交，启动命令中增加该环境变量。

---
