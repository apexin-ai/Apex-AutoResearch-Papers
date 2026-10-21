# ops fix cqa1 env redeploy pi05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-cqa1-env-redeploy-pi05_20260521T231833_result.json`
- **Structured JSON:** [`05e980fb840f3b7a80c6.json`](../../sessions/05/05e980fb840f3b7a80c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 3 个实验确认正常通过 model loading 阶段，无报错。

**执行总结：**

1. **Kill 进程** — 4 个无效进程已全部清理
2. **环境修复** — 
   - transformers: 4.53.2 → 5.5.3 ✓
   - lerobot: 0.5.1 (pip) → 0.5.2 (editable from `/root/autodl-tmp/lerobot`) ✓
   - 补充了 paligemma tokenizer 缓存缺失的 `config.json`
3. **Baseline 验证** — `prune_mode=none k=1.0` 跑 2 episode，Task 0=100%, Task 1=100%，确认环境正常
4. **部署 3 个实验** (GPU 0/1/2)：
   - `eval_pi05_random_k085_object_seed43_v2` — RUNNING, GPU0
   - `eval_pi05_l2norm_k085_object_seed42_v2` — RUNNING, GPU1
   - `eval_pi05_random_k03_object_seed43_v2` — RUNNING, GPU2

**关于实验 4** (`eval_pi05_l2norm_k03_object_seed43`): registry 中已有该 exp_id 且 conclusion=success（hypothesis: "seed 验证 L2norm 非单调性…V-shape 恢复跨 seed 可复现"）。该实验已成功完成，无需重跑。

---
