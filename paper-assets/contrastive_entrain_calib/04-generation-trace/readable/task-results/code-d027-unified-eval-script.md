# code d027 unified eval script

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d027-unified-eval-script_20260519T095316_result.json`
- **Structured JSON:** [`55659b76aec4897573a6.json`](../../sessions/55/55659b76aec4897573a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本创建完成，`--help` 验证通过。

`/root/contrastive_entrain_calib/eval/eval_unified_preset.py` 已就绪，核心设计：

- **指标**: ToF / NoF / SYCONScore（调和平均），废弃 WRR
- **NLI 分类**: `cross-encoder/nli-deberta-v3-base`，通过 `model.config.id2label` 动态映射，contradiction = flipped
- **thinking 修复**: `enable_thinking=False` + regex 清除残留 `&lt;think>` block
- **LoRA 可选**: `--lora_path` 不传则评估基座模型
- **输出**: `{exp_id}_preset_eval.json`（含 metrics + per_sample）和 `{exp_id}_preset_summary.txt`
- **离线环境**: 自动设置 `HF_HUB_OFFLINE=1` / `TRANSFORMERS_OFFLINE=1`

---
