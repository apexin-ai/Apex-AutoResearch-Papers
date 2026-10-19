# check training progress loop5

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training_progress_loop5_20260514T080030_result.json`
- **Structured JSON:** [`c3c37931e1f456f4d9f5.json`](../../sessions/c3/c3c37931e1f456f4d9f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

### Qwen m2_full_qwen (cuda:0) — 运行中，日志不可读
- PID 73558 已运行 14h21m，GPU 100%/51.6GB VRAM
- **日志仅 3 行**：`tee log` 和外层 `> log 2>&1` 写同一文件导致冲突，输出丢失
- Checkpoint 在 05:50 保存过 best model，估算当前约 2700 steps / 4242 (64%)
- 预计 ~00:00 May 15 完成 s42

### StarCoder m2_full_starcoder (cuda:1) — step 2500/4242 (59%)
- PID 76627 运行 13h30m，GPU 100%/55.2GB VRAM
- **过拟合明显**：best checkpoint 在 step 1000 (val_loss=0.6134, R@1=0.4537)，之后持续恶化 (step 2000: val_loss=0.6698, R@1=0.4456)
- 速度 ~185 steps/hr，预计 ~01:30 May 15 完成 s42

### m1_reextract_v2 (CPU) — 42/82 groups (51%)
- all.jsonl 已有 44,173 行，活跃运行中
- 当前处理 click/dvc/line_profiler/python-pinyin，预计 ~04:00 May 15 完成

### 磁盘 — 充裕
- /root/autodl-tmp: 90GB 剩余 (65%)，/root: 21GB 剩余 (31%)

### 需关注
1. **Qwen 日志修复** — 后续 seed (s43 等) 前必须修脚本，否则全程盲跑
2. **StarCoder 过拟合** — 不影响结果（取 best checkpoint），但浪费了 epoch 2-3 的 GPU 时间
3. **s42→s43 切换** — 两个模型完成 s42 后需确认自动启动下一个 seed

---
