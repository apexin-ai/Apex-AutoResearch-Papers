# diagnose eval pi05 random k085 long seed42 strict w27

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k085_long_seed42_strict_w27_20260527T134757_result.json`
- **Structured JSON:** [`62026b6ec077ca3714ea.json`](../../sessions/62/62026b6ec077ca3714ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验实际已完成，cron 误报。**

- **原因**：日志写到了 `~/autodl-tmp/importance_margin_vla_compress/` 项目根目录下，而 cron 监控在 `~/runs/importance_margin_vla_compress/` 找不到文件，判定为失败。
- **结果**：π0.5 Random k=0.85 LIBERO Long seed42 → **SR=44.0%** (220/500)，耗时 170 min，结果 JSON 已保存。
- **无需重启。**

另外注意：westd-27271 上 tmux 里的 `pi05_attn_k075_long` 和 `pi05_attn_k07_long_rerun` 两个 session 的日志都只有 637 bytes，可能已经 stall 了，值得检查。`pi05_l2norm_k07_long_rerun` 在正常运行中（T0=72%，正在跑 T1）。

---
