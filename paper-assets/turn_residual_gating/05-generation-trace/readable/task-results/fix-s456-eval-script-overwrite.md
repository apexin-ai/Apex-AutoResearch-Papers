# fix s456 eval script overwrite

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_s456_eval_script_overwrite_20260523T180957_result.json`
- **Structured JSON:** [`9ae6689fd3c39e184d64.json`](../../sessions/9a/9ae6689fd3c39e184d64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处都已修复：

- **L93**: `--output-name "base_ar_n50"` → `"base_s456_ar_n50"` — 避免覆写 s123 的 base 结果
- **L115**: bootstrap CI 的 glob 同步更新为 `base_s456_ar_n50.json`

`gpu_chain_next.sh` L29 已正确引用 `scripts/d048_eval_ss_s456.sh`，无需修改。TF Phase 1 的 base eval（步骤 1/4 和 2/4）输出到 `tf_base_ours`/`tf_base_dongre`，是无 checkpoint 的确定性 eval，重复运行结果相同，不存在覆写问题。

---
