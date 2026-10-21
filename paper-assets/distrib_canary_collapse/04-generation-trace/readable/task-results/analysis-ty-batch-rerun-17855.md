# analysis ty batch rerun 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ty_batch_rerun_17855_20260520T194739_result.json`
- **Structured JSON:** [`aa61c2abd80585de0873.json`](../../sessions/aa/aa61c2abd80585de0873.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**TY Granger 方向修复批量重跑 — westd-17855**

- **修复确认**: `causing=0, caused=1` (canary→downstream forward)
- **总计**: 35/35 实验全部成功重跑，0 失败
- **备份**: 每个实验的旧结果已保存为 `5method_leadlag_pre_tyfix_batch.json`
- **Spot-check (7 experiments)**:
  - TY fwd 计数有变化（方向修复生效）：a010_s43 3→1, a040_s42 4→2, a075_s42 3→2, pythia69b_s42 1→0
  - 部分实验 TY 不变（对称情况）：a050_s42, c4_a050_s42, gpt2m_s43
  - PermG/DiffXcorr 全部 unchanged（7/7 spot-checked）
  - K≥3 基本稳定（仅 c4_a050 从 6→5，因 TY 票数变化）
- **全局校验**: 31/35 格式匹配的实验 PermG/DiffXcorr 完全不变。4 个旧格式实验（无 summary 块）是格式差异非数据差异
- **汇总文件**: `results/ty_batch_rerun_17855_summary.json`

---
