# ops check 14b gpu6000pro2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_14b_gpu6000pro2_20260517T211449_result.json`
- **Structured JSON:** [`dffe014432619590acda.json`](../../sessions/df/dffe014432619590acda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## gpu-6000pro-2 — qwen25_14b_scale_002 状态报告

| 项目 | 状态 |
|------|------|
| **PID 806751** | 存活，正在运行 |
| **GPU 0** | 94% 利用率，32.3G / 97.9G 显存 |
| **阶段** | Phase 2: 生成 d0（5000 unconditional samples） |
| **d0 进度** | 4696 / 5000 samples（~94%） |
| **总体进度** | depth 0-3 共 4 轮，当前第 1 轮接近完成 |
| **错误** | 无。早前有模型下载 SSL 错误，已重试成功，所有 8 个 safetensors 文件完整下载 |

d0 即将生成完毕（还差 ~300 条），之后进入 d1、d2、d3 的递归生成。按当前速度估计整体还需数小时完成全部 4 个 depth。

---
