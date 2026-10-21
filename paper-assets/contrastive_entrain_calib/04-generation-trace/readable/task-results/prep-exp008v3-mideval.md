# prep exp008v3 mideval

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp008v3-mideval_20260519T184445_result.json`
- **Structured JSON:** [`7c390b345661e739318f.json`](../../sessions/7c/7c390b345661e739318f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。

```
=== 1. exp-008v3 checkpoint 配置 (westd-28034) ===
save_steps: 500
当前已有 checkpoint: checkpoint-500, checkpoint-1000, checkpoint-1500, checkpoint-2000
当前步数: 2145/8000 (27%)
step 4000 是否会保存: 是（500 是 4000 的因数，step 4000 会保存）
预计到达 step 4000 时间: 当前 ~37.7s/step，还需 ~1855 步，约 19.4 小时（≈5月20日 22:00 UTC+8）

=== 2. eval_unified_preset.py (westd-29046) ===
存在: 是（10837 bytes, 2026-05-19 18:20）
D027 NLI 分类: 已应用（cross-encoder/nli-deberta-v3-base, NLIChecker, SYCONScore）
CUDA 设置 bug: 无（使用 CUDA_VISIBLE_DEVICES 环境变量前缀，未在 import 前硬编码）
版本判断: 可用

=== 3. 数据和模型 (westd-29046) ===
calibration_v2_1_expanded.jsonl: 存在（路径: /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl，362 行）
  备用路径 /root/contrastive_entrain_calib/data/ 下: 缺失
base model cache: 存在（路径: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B）
```

---
