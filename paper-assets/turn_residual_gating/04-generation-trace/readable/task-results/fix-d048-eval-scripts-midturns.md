# fix d048 eval scripts midturns

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d048_eval_scripts_midturns_20260522T135128_result.json`
- **Structured JSON:** [`a2b80b4a0280180e7bc4.json`](../../sessions/a2/a2b80b4a0280180e7bc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

1. **`d048_eval_ss_s42.sh`** — `curve[1:]` → `curve[2:]`，`len(curve) > 1` → `len(curve) > 2`
2. **`d048_eval_existing_s42_ar_n50.sh`** — 同样的 `[1:]` → `[2:]` 修正 + 移除了 Base eval 段（原 section 1/5），重编号为 1/4 ~ 4/4，只保留 TG/UG/LO/PCGrad
3. 两个脚本 `bash -n` 语法检查通过
4. grep 确认两个文件中无残留 `[1:]`

---
