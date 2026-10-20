# code phase1 1b adapt

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1_1b_adapt_20260517T052614_result.json`
- **Structured JSON:** [`a53b4f9dc5b0baab3d10.json`](../../sessions/a5/a53b4f9dc5b0baab3d10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`run_phase1.py` 已参数化支持 1B：

- `--model pythia-1b` 使用 `EleutherAI/pythia-1b-deduped`
- 默认 `--model pythia-410m`（向后兼容）
- 1B checkpoint 写到 `checkpoints_phase1_1b/{condition}_seed{seed}/`
- 1B results 写到 `phase1_1b_{condition}_seed{seed}_results.json`
- 训练参数沿用现有 Config 默认值（lr=5e-5, batch_size=8, grad_accum=4），1B 在 98GB 卡上无需降低 batch_size
- 模型已缓存在 `/root/.cache/huggingface/hub/models--EleutherAI--pythia-1b-deduped`，离线可用

---
