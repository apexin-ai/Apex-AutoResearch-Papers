# diagnose factorial h2 episodeadv seed1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_factorial_h2_episodeadv_seed1_20260517T192458_result.json`
- **Structured JSON:** [`65fa448679594f535c79.json`](../../sessions/65/65fa448679594f535c79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已保存到 `artifacts/diagnose_factorial_h2_episodeadv.md`。

**根因**: westd-47453 上 `model_path` 是断裂符号链接。`qwen3_exp021_ragen_sft_v4` -> `exp021_ragen_sft_v4/final`，但目标目录不存在（模型 ~3.4GB 仅在 bjb1-17606 上）。`from_pretrained()` 因 `os.path.isdir()` 返回 `False` 回退到 HuggingFace Hub 解析，触发 `HFValidationError`。

**修复**: 需要从 bjb1-17606 传输模型到 westd-47453，或直接用 scp 同步 `exp021_ragen_sft_v4/final` 目录。这属于 C002 pre-flight checklist 第4项应拦截的问题。

---
