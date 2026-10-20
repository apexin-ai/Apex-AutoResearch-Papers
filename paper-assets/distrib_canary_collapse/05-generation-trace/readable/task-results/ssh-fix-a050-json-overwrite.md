# ssh fix a050 json overwrite

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_a050_json_overwrite_20260517T070755_result.json`
- **Structured JSON:** [`4fc0e297ac1f6ff8ac80.json`](../../sessions/4f/4fc0e297ac1f6ff8ac80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Step 1: 当前数据已正确，无需重跑

磁盘上三个 `5method_leadlag.json` 的 PermG FDR forward sig：
- **s42: 0/8** (文件时间 May 17 04:37)
- **s43: 6/8** (文件时间 May 17 03:57)
- **s44: 3/8** (文件时间 May 17 14:37)

全部匹配预期值。

### Step 2: `analyze_alpha_sweep.py` 不是覆写源

- 它输出到 `alpha_sweep_analysis.json`（line 552），**不写 `5method_leadlag.json`**
- 三个 seed 目录下均不存在 `alpha_sweep_analysis.json`，说明该脚本最近没有对这些目录执行过
- 其 BH family_size = per-alpha per-method 跨所有 seed（3 seeds × 8 pairs = 24），与 `run_5method_analysis.py` 的 family_size=8 不同
- 服务器上无 crontab

### Step 3: 无需防覆写措施

`analyze_alpha_sweep.py` 的输出路径与 `run_5method_analysis.py` 不冲突，不存在覆写风险。

### 结论

任务描述中的"4/8, 7/8, 4/8 错误数据"不是当前状态。数据已经是正确的 0/8, 6/8, 3/8。根因排查显示 `analyze_alpha_sweep.py` 不会写入 `5method_leadlag.json`，两个脚本输出路径独立，无需修复。

---
