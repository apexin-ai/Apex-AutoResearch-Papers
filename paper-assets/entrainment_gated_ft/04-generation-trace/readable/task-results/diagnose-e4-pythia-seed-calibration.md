# diagnose e4 pythia seed calibration

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_e4-pythia-seed-calibration_20260522T111122_result.json`
- **Structured JSON:** [`19464432ff934eb5dc2b.json`](../../sessions/19/19464432ff934eb5dc2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，报告已写入 `artifacts/report_e4_diagnosis.md`。

**根因**：aria2 并行下载 9 个 Pythia 410M seed 权重（各 869MB）时，仅下载 1-5% 即触发 Emergency shutdown 中断。seed1-5 权重文件损坏（缺 `model_type`），seed6-9 完全没下载。Eval 阶段在损坏文件上运行全部失败。0/9 seed 完成。

**修复**：弃用 aria2 直接下载方式，改用已有的 `run_eval.sh`（通过 HF transformers 自动下载，已配置 `HF_HUB_DISABLE_XET=1`）。重跑前需：
1. 确认 `EleutherAI/pythia-410m-seed{1..9}` 在 HuggingFace 上的实际 repo 名称
2. 清理残留的空 seed 目录
3. 用 `nohup` 运行避免 SSH 断连

---
