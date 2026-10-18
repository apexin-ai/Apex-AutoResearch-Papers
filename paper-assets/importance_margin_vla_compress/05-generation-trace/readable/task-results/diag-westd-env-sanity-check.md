# diag westd env sanity check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd_env_sanity_check_20260518T194645_result.json`
- **Structured JSON:** [`088c2c7bdb3dd8686f30.json`](../../sessions/08/088c2c7bdb3dd8686f30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Sanity Check 结果

**GPU 状态**: 2x NVIDIA RTX PRO 6000 Black (98GB each)，均空闲，0% 利用率

**eval 脚本运行**: 全部正常，无报错
- 模型加载: 7.2s，从本地 `/root/autodl-tmp/.hf_cache/smolvla_libero_official` 加载成功
- 10 个 task 各 1 episode，总耗时约 65 秒
- Overall SR: **3/10 (30.0%)** — 3 个 SUCCESS (tomato sauce/milk/chocolate pudding)，7 个 FAIL (均跑满 280 步)
- JSON 输出正常，结构完整

**环境就绪确认**: westd-27271 的 eval 环境完全可用，可以直接跑 Smart Compress 实验。

---
