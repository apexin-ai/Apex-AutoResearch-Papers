# diag perlayer kl k16 eval v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_perlayer_kl_k16_eval_v2_20260523T051305_result.json`
- **Structured JSON:** [`12ce70be3e870fc06bcb.json`](../../sessions/12/12ce70be3e870fc06bcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：`nohup` 不 source `.bashrc`，导致 `HF_HOME=/root/autodl-tmp/.hf_cache` 未设置。lm-eval 的 `datasets.load_dataset` 去默认路径 `/root/.cache/huggingface/datasets/` 找缓存——该目录不存在。数据集实际缓存在 `/root/autodl-tmp/.hf_cache/datasets/`，但 eval 进程不知道。

两次失败是同一根因的不同表现：
- Parent：缺 HF_HOME → 找不到缓存 → 联网 → 网络不可达
- v2：加了 `HF_DATASETS_OFFLINE=1` → 缺 HF_HOME → 找不到缓存 → "离线模式无缓存"

**修复**：在 nohup 命令里显式加 `HF_HOME=/root/autodl-tmp/.hf_cache`。报告已写入 `artifacts/diag_k16_eval_v2.md`，含完整重试命令。

---
