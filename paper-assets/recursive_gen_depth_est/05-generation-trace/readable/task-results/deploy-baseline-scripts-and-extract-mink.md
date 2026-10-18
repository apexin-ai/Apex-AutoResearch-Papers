# deploy baseline scripts and extract mink

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_baseline-scripts-and-extract-mink_20260519T140337_result.json`
- **Structured JSON:** [`3d9a34b898c09589b75c.json`](../../sessions/3d/3d9a34b898c09589b75c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项任务全部完成。

**任务 1 — Min-K% 结果提取**
- 9/9 cells 完成，结果保存到本地 `artifacts/mink_ordinal_baseline/mink_prob_results.json`
- Registry `mink_ordinal_baseline_002` 已更新：metrics + notes + conclusion=success
- 关键发现：methodA/C 在 chance level (~25%)，methodB 最好也仅 29-33%，确认 Min-K% 无法做 ordinal depth 分类

**任务 2 — DetectGPT 结果提取**
- 8/9 cells 完成（缺 pythia_nucleus），结果保存到本地 `artifacts/detectgpt_ordinal_baseline/detectgpt_results.json`
- Registry `detectgpt_ordinal_baseline_002` 已更新：metrics + notes
- 关键发现：mean 4class_acc=29.1%，接近 chance (25%)

**任务 3 — 脚本部署**
- `binoculars_ordinal_eval.py` → 远程 `scripts/binoculars_ordinal_eval.py` ✓
- `detectgpt_baseline.py` → 远程 `scripts/detectgpt_baseline.py` ✓
- 两个脚本 py_compile 验证通过

---
