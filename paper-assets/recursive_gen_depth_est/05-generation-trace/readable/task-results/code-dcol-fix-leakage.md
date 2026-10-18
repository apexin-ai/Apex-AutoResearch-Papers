# code dcol fix leakage

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dcol_fix_leakage_20260514T162652_result.json`
- **Structured JSON:** [`e72e915e1a25ccd902c7.json`](../../sessions/e7/e72e915e1a25ccd902c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改总结：

1. `--test_size` 默认值 0.2→0.15，新增 `--val_size` 参数(默认 0.15)
2. 2-way split → 3-way split (train 70% / val 15% / test 15%)，depth-stratified
3. 新增 `val_ds`/`val_loader`
4. Training loop 中 early stopping 改用 `val_loader`（不再碰 test set）
5. Final evaluation 先报告 Val Set 指标（参考），再报告 held-out Test Set 指标
6. `results.json` 中增加 `val_accuracy_4class` 字段

---
