# data compilation full sync

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_compilation-full-sync_20260515T072504_result.json`
- **Structured JSON:** [`55d88a190a8e6bca0dde.json`](../../sessions/55/55d88a190a8e6bca0dde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两份文件已同步更新。修改清单：

**Section 1 (8B val)**
- ckpt-1400: `— | — | —` → `77.15 | 91.34 | 62.95`，exp_id = cls8b-s42-ckpt1400-val8192-eval
- ckpt-1600: `— | — | —` → `78.94 | 91.76 | 66.12`，exp_id = cls8b-s42-ckpt1600-val8192-v2
- Notes 中删除 "ckpt-1400/1600 only have accuracy" 条目

**Section 2 (8B test)**
- ckpt-800: f1_pass `—` → `88.77`，exp_id = cls8b-s42-ckpt800-test8192-eval
- ckpt-1200: f1_pass `—` → `89.45`，exp_id = cls8b-s42-ckpt1200-test8192-eval
- ckpt-1400: `85.47† | — | — | —` → `**85.47** | **78.90** | **90.67** | **67.13**`（完整数据），exp_id = cls8b-s42-ckpt1400-test8192-eval
- 删除 † running_acc 脚注，更新 Notes

**Section 3 (4B val)**
- 新增 ckpt-4200 行: 89.06 | 83.07 | 93.1 | 73.0
- 新增 ckpt-4600 行: 90.07†（training-log acc，full eval QUEUED）
- gap 更新为 +14.19 pp (ckpt-4600)

**Section 5 (Summary)**
- 8B test: `ckpt-1400†` → `ckpt-1400`，f1_macro `—` → `78.90`
- 删除 "test@8192 (full) ckpt-400" 行
- 新增 4B ckpt-4600† 行 + 4B full eval ckpt-4400 行

**Section 6 (JSON)**
- 8B val: ckpt-1400/1600 的 null → 实际值
- 8B test: ckpt-800/1200 的 f1_pass null → 实际值，ckpt-1400 全部填充
- 4B: 新增 ckpt-4200 和 ckpt-4600 条目

**Majority baseline**: val=75.88%（未变，已正确）；test=72.96%（未变，已正确）。

---
