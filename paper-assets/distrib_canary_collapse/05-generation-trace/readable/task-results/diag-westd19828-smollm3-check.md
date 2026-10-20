# diag westd19828 smollm3 check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd19828_smollm3_check_20260518T220442_result.json`
- **Structured JSON:** [`48d06f697f940a2082ff.json`](../../sessions/48/48d06f697f940a2082ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。两个实验状态汇总：

### cuda:1 — SmolLM3-3B fp32 (`smollm3_3b_wiki_a100_s42_v2`)
- **状态**: RUNNING（registry 已从 PREPARING 更新）
- **进度**: Generation 0 (baseline)，正在生成合成数据
- **GPU**: 45174 MiB / 95% 利用率
- **输出目录**: 仅有 config.json，尚无 gen 目录

### cuda:0 — Pythia-14B scale check (`scale_14b_a050_s42`)
- **状态**: RUNNING
- **进度**: Generation 8/10，刚完成 gen_7 metrics（ppl=32.04, entropy=2.2222, eff_rank=83.4, mauve=0.0261），正在生成 gen_8 合成数据
- **GPU**: 37015 MiB / 77% 利用率
- **输出目录**: gen_0 ~ gen_8 已创建

---
