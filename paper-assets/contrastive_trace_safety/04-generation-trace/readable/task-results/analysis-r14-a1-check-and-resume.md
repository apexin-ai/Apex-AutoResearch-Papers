# analysis r14 a1 check and resume

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_a1_check_and_resume_20260518T162850_result.json`
- **Structured JSON:** [`0dc23a2c3ba0b75f1765.json`](../../sessions/0d/0dc23a2c3ba0b75f1765.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

R14-A1 实验全部完成。结果汇总：

## R14-A1 Results: BA-Optimal Layer + HS vs Text Probe

| Model | BA-opt Layer | HS Prec | Text Prec | ΔPrec | p | HS FPR | Text FPR | ΔFPR | p | HS BA | Text BA | ΔBA | p | HS AUROC | Text AUROC | ΔAUROC | p | HB |
|-------|-------------|---------|-----------|-------|------|--------|----------|------|------|-------|---------|-----|------|----------|------------|--------|------|-----|
| R1-8B | L17 | .633 | .472 | +.186 | .0001 | .114 | .205 | -.070 | .0433 | .737 | .673 | +.084 | .0062 | .857 | .736 | +.121 | .0089 | 2/3 |
| OT-7B | L2 | .377 | .254 | +.185 | .0000 | .181 | .294 | -.133 | .0001 | .657 | .580 | +.080 | .0060 | .733 | .604 | +.128 | .0031 | **3/3** |
| R1-32B | L46 | .558 | .441 | +.128 | .0143 | .306 | .382 | -.122 | .0829 | .723 | .601 | +.176 | .0000 | .788 | .637 | +.151 | .0086 | 1/3 |
| QwQ-32B | L63 | .660 | .460 | +.181 | .0008 | .134 | .202 | -.064 | .0878 | .763 | .617 | +.135 | .0000 | .840 | .689 | +.151 | .0012 | 2/3 |

**8/12 HB pass, 14/16 raw significant**

- Precision 和 BA：所有 4 个模型 HS > Text，大部分通过 HB（R1-32B precision 除外）
- FPR：仅 OT-7B 通过 HB，其余 3 个模型 FPR 改善不显著
- AUROC：全部 4 个模型 raw significant（不在 HB family 内）
- BA-optimal layer 跨模型差异大：小模型偏浅层（L2, L17），32B 模型偏深层（L46, L63）
- 注意：脚本使用 `max_iter=500`（非 spec 的 2000），存在 convergence warnings

---
