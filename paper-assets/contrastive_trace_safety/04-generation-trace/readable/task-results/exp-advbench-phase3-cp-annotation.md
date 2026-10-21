# exp advbench phase3 cp annotation

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_advbench_phase3_cp_annotation_20260520T054047_result.json`
- **Structured JSON:** [`30924017c88e181400f7.json`](../../sessions/30/30924017c88e181400f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进度正常，0.29/s 速率，ETA ~22 分钟。任务正在跑。

**当前状态总结**:
- **脚本**: `scripts/annotate_cp_llm.py` 使用 `gpt-4o-mini` 通过 OpenAI-compatible API
- **全量任务**: tmux session `advbench_llm_cp_full`，387 条 B-class traces，~22 分钟完成
- **输出**: `/root/autodl-tmp/contrastive_trace_safety/artifacts/advbench_cp_annotations/llm_cp_annotations.json`
- **模型**: 原计划 qwen3-32b（思考模型 content 字段为 None 导致不可用），回退到 gpt-4o-mini
- **Dry-run**: 10/10 成功，2 jailbreak / 8 non-jailbreak，CP 分布合理
- **Checkpoint**: 每 50 条自动保存，支持断点续传

---
