# harvest s47 final check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_s47_final_check_20260529T021513_result.json`
- **Structured JSON:** [`4e6c40018cb4f037b1d4.json`](../../sessions/4e/4e6c40018cb4f037b1d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验仍在运行，GPU 0-3 均有显存占用。当前进度：

| # | 实验 | GPU | 当前任务 | 累计 SR | 预计剩余 |
|---|------|-----|---------|---------|---------|
| 1 | eval_pi05_l2norm_k07_long_seed47_w41 | 0 | T9 ep30 (80%) | 269/450=59.8% (T1-T8) | ~30min |
| 2 | eval_pi05_attn_k07_long_seed47_cqa1 | 1 | T8 ep30 (13%) | 223/400=55.8% (T1-T7) | ~1h |
| 3 | eval_pi05_attn_k075_long_seed47_cqa1 | 2 | T8 ep20 (10%) | 206/400=51.5% (T1-T7) | ~1.2h |
| 4 | eval_pi05_l2norm_k05_long_seed47_cqa1 | 3 | T8 ep30 (7%) | 205/400=51.2% (T1-T7) | ~1h |

GPU 状态：4 卡均 ~10GB 显存占用，利用率正常。

实验 1（L2Norm k=0.7）进度最快，已到 T9；其余 3 个在 T8。全部预计 1-1.5h 内完成。待完成后再提取最终 SR 并更新 registry。

---
