# ops verify aligned eval start

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-aligned-eval-start_20260514T084609_result.json`
- **Structured JSON:** [`3949bcaee7d18e5683c5.json`](../../sessions/39/3949bcaee7d18e5683c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切正常：

- **进程**: PID 332207 存活，已运行 7m35s，状态 `Ss+`（前台 session leader）
- **当前 benchmark**: MMLU 已完成（accuracy 0.3979, 5587/14042），正在跑 GSM8K（43/1319, ~3%，约 5.3s/it，预计还需约 1h53m）
- **GPU 2**: 3695 MiB 显存占用，34% 利用率 — 符合 0.5B 模型 eval 的预期
- **输出目录**: `Qwen2.5-0.5B_d000_s42_aligned` 已创建
- **bitsandbytes 警告**: `libnvJitLink.so.13` 加载失败，但这只是 bnb 的非关键警告，不影响 eval 运行

第一个 eval 配置 `d000_s42_aligned` 正常推进中。

---
