# infra fix processor rerun std

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-processor-rerun-std_20260515T180832_result.json`
- **Structured JSON:** [`f53f6b2c733e324b1239.json`](../../sessions/f5/f53f6b2c733e324b1239.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪，eval 已成功启动。

**产出汇总：**

1. **Processor 修复** — 成功。`SmolVLMProcessor` 已下载并缓存到 `/root/autodl-tmp/.hf_cache/models--HuggingFaceTB--SmolVLM2-500M-Video-Instruct/`。修复关键：eval 脚本必须同时设置 `HF_HUB_CACHE=/root/autodl-tmp/.hf_cache`（之前的脚本已有此设置，所以 v2 脚本保持一致即可）。
2. **Eval 已启动** — PID 89136，GPU 1 占用 4340 MiB / 8% 利用率，正在跑 `libero_spatial`（第一个 suite）。
3. **Registry 已更新** — `mvp1_baseline_std` 状态 RUNNING，含修复说明。
4. **日志路径** — `/root/acib/outputs/baseline_std_v2/main.log`

注意：GPU 0 的 PID 10910（原 baseline_plus）VRAM 已释放（从 5407→1 MiB），可能已结束或崩溃，需要后续确认。

---
