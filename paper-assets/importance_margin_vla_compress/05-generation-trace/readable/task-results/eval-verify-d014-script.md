# eval verify d014 script

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_verify-d014-script_20260515T200610_result.json`
- **Structured JSON:** [`4a9670e26f2b1fad94d9.json`](../../sessions/4a/4a9670e26f2b1fad94d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审阅完成，以下是逐项检查结果：

---

### a) v7 checkpoint 路径
**PASS** — `CKPT_V7="checkpoints/imm_anchor"`，正确（非 `imm_anchor_v7/`）。脚本优先找 `latest/checkpoint.pt`，不存在则取最高 step 的 `checkpoint.pt`。当前训练到 `step_028000`，完成后无论产生 `latest/` 还是 `step_029999/` 都能正确匹配。

### b) baseline final checkpoint 路径
**PASS** — `checkpoints/baseline/step_029999/checkpoint.pt`，磁盘上确认存在。

### c) baseline mid-checkpoint 路径
**PASS** — `step_005000` 和 `step_010000` 均存在于 `checkpoints/baseline/` 下，文件名是 `checkpoint.pt`，与脚本一致。

### d) batch 数量
**PASS** — Phase 1/2 (final) = 500 batches，Phase 3a/3b (mid) = 50 batches。

### e) config 文件
**PASS** — v7 用 `configs/imm_anchor.yaml`，baseline 用 `configs/baseline.yaml`，两个文件均存在于 configs 目录。

### f) GPU 参数
**PASS** — `GPU=${1:-0}` 接受位置参数，evaluate.py 的 `--gpu` 是 `type=int`。执行时传 `bash run_d014_eval.sh 1` 即可用 cuda:1。

### g) 输出路径
**PASS** — 四个输出文件名各不相同，均含 exp 标识 + checkpoint 标识：
- `eval_imm_v7_final.json`
- `eval_baseline_v5_final.json`
- `eval_baseline_v5_step005000.json`
- `eval_baseline_v5_step010000.json`

### lipschitz_samples 参数
**PASS（注意）** — 脚本未显式设置 `--lipschitz_samples`，将使用 evaluate.py 的默认值 **100**。D014 无硬性要求，默认值合理。

---

### 结论

**脚本可以直接执行，无需修改。** 所有硬约束全部通过。v7 训练完成后运行 `bash run_d014_eval.sh 1` 即可。

---
