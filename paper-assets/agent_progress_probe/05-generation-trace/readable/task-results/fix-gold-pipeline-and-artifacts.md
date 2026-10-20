# fix gold pipeline and artifacts

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gold-pipeline-and-artifacts_20260514T192745_result.json`
- **Structured JSON:** [`703859e7810fb28095cb.json`](../../sessions/70/703859e7810fb28095cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个任务完成。汇总：

---

### Task 1: Gold pipeline 泄漏修复 ✓
**问题**：`evaluate_structural` 用 `split_info["train_indices"]` 训练，dry-run gold 全部 15401 conf>=2 窗口中有 10634 在训练集中（69% 泄漏）。

**修复**：排除 gold 窗口出训练集；若训练集清空（dry-run 场景），fallback 到原始 train split 训练 + 仅评估 held-out gold。

**验证**：full 15401 dry run RF 0.9994→**0.9983**（4767 held-out），GB 0.9991→**0.9972**。

### Task 2: 650 规模 dry run ✓
3 seeds (42/123/456) 结果（macro_f1 mean±std）:
| Model | Mean | Std |
|-------|------|-----|
| Probe | 0.9544 | ±0.0064 |
| RF | 0.9961 | ±0.0034 |
| GB | 0.9961 | ±0.0034 |
| TWV | 0.9508 | ±0.0099 |
| TWV Probe | 0.9481 | ±0.0077 |

方差可控（Probe <1pp, TWV ~1pp）。

### Task 3: --device 默认值 ✓
改为 `"cuda:0"`，简化 device 选择逻辑。

### Task 4: Registry ✓
- `gold_dryrun_v1`, `gold_dryrun_v2` → killed
- `gold_dryrun_v3` → conclusion=success + 写入修复后 metrics（含 full 和 650x3 seeds）

### Task 5: FP/FN 命名统一 ✓
`analysis_f1_stag_conf_stratified.json` 和 `.md` 统一为 **stagnation-positive**：TP=pred stag+actual stag, FP=pred stag+actual prog, FN=pred prog+actual stag, TN=pred prog+actual prog。

---
