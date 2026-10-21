# analysis d150 dose response csv v2 fdr fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d150_dose_response_csv_v2_fdr_fix_20260520T140303_result.json`
- **Structured JSON:** [`e5e185210d15602758cc.json`](../../sessions/e5/e5e185210d15602758cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总**:
- CSV 49 行（与 v1 同），覆盖 7 个 category
- 12 个实验的 `permg_count` 因 FDR 校正发生变化，其中 11 个降至 0/8
- 只有 `diff_xcorr` 和 `perm_granger` 有 `significant_fdr` 字段，其余 3 个方法 JSON 中无 FDR 字段，沿用 `significant`

**验证全部通过**:
- α=0.45 s42: 3→0 ✓
- α=0.55 s42: 5→0 ✓
- α=0.50 s42: 6（不变）✓
- α=0.00 all seeds: 0 ✓

**核心发现**: FDR 校正后，α≤0.45 的 PermG 全部归零，dose-response 阈值更清晰地落在 α=0.45–0.50 之间。

---
