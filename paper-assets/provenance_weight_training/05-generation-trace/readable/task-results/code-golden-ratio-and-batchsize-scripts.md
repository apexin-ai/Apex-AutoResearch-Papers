# code golden ratio and batchsize scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_golden_ratio_and_batchsize_scripts_20260515T070945_result.json`
- **Structured JSON:** [`d6902b5a02665ac9805d.json`](../../sessions/d6/d6902b5a02665ac9805d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**已完成的修改：**

1. **pretrain_weighted.py** — 添加 `golden_ratio` 方法：q>0.5 权重 1/φ≈0.618，q≤0.5 权重 1.0，归一化后加权求 loss。argparse choices 已更新，`--help` 验证通过。

2. **3 个训练脚本**（均 `chmod +x`）：
   - `run_golden_ratio_seed42.sh` — golden_ratio oracle baseline
   - `run_batchsize8_seed42.sh` — adaptive, bs=8, grad_accum=2, n_min=2
   - `run_batchsize16_seed42.sh` — adaptive, bs=16, grad_accum=1, n_min=2

3. **产出清单** → `artifacts/new_scripts_manifest.md`

所有脚本 effective batch size 保持 16，未启动任何训练。

---
