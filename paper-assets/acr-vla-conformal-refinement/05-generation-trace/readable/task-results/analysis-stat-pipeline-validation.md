# analysis stat pipeline validation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_stat-pipeline-validation_20260515T185718_result.json`
- **Structured JSON:** [`cb2704a25ca696cb2543.json`](../../sessions/cb/cb2704a25ca696cb2543.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 验证结果汇总

### 通过

| 验证项 | 结果 |
|--------|------|
| **端到端运行** (`--log-dir logs/`) | 成功，发现 7 个文件（6 methods × 2 seeds），输出比较表、pooled summary、per-task breakdown |
| **extract_method_seed** | 7/7 case 通过：norm003/norm005/norm0p3/norm02 后缀、seed 提取、.log 格式均正确 |
| **SR normalization** | 代码仅使用 `successes/total` 整数计数，不依赖 `overall_success_rate` 或 `success_rate` 字段。0-1 和 0-100 格式的 JSON 均得到正确结果 |
| **Fisher exact test** | obs_only vs vla_only: odds_ratio=1.7202, p=0.1168 (n.s.)，逻辑正确 |
| **Bootstrap SR CI** | 19/100 → [12.0%, 27.0%]，合理 |
| **Bootstrap diff CI** | 19/100 vs 12/100 → [-3.0pp, +17.0pp]，合理 |
| **Log 文件解析** | 完整 log（4 个）正确解析 mode/seed/norm/per_task；中断 log（seed43, 1 task）正确标记 partial |
| **norm_sensitivity.py** | obs_only norm=0.1→19.0%, norm=0.2→22.0%，baseline 输出正确 |
| **Explicit --methods 模式** | `--methods obs_only:... obs_only_norm02:... --test-pair obs_only obs_only_norm02` 正确执行 |
| **Output JSON** | `analysis/results/comparison.json` 格式完整，包含 comparison_table / pooled_summary / fisher_test / per_task |

### 无 bug 发现

3 个修复点均验证通过，端到端无报错，输出格式正确。唯一值得注意的是 `eval_object_obs_only_norm02_seed43.log` 是一个中断的评估（1/10 tasks），被正确标记为 partial 并合入 pooled summary（22/110 而非 22/100），这是预期行为但会稀释该 method 的 pooled SR。

---
