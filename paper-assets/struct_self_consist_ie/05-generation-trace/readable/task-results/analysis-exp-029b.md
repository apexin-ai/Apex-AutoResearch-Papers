# analysis exp 029b

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_029b_20260518T015955_result.json`
- **Structured JSON:** [`08326ea0cca15fe993be.json`](../../sessions/08/08326ea0cca15fe993be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正在进行中（step 540/1170, 46%, ~31 min remaining）。已准备好全部后处理脚本：

- `scripts/exp_029b_postprocess/01_merge_lora.sh` — LoRA 合并
- `scripts/exp_029b_postprocess/02_inference.sh` — N=8 采样推理
- `scripts/exp_029b_postprocess/03_analyze.py` — degeneracy + QE signals 分析
- `export_config_scierc_10epoch.yaml` — 导出配置

等待训练完成后自动继续执行分析流程。

---
