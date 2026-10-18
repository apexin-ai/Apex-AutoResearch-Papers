# diagnose gpu status 20260527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_status_20260527_20260527T005044_result.json`
- **Structured JSON:** [`dcdb3441acd203efc547.json`](../../sessions/dc/dcdb3441acd203efc547.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the summary:

## GPU 状态表

| 服务器 | GPU | Mem Used | Util% | PID | 实验 | 运行时间 | 状态 |
|--------|-----|----------|-------|-----|------|---------|------|
| westd-27271 | 0 | 15946 MiB | 72% | 609731 | OV l2norm k=0.95 Goal s42 | 35min | **正常** Task 2/10 |
| westd-27271 | 1 | 15919 MiB | 62% | 397225 | OV attn k=0.5 Long s42 | 9h08m | **正常** 接近完成 |
| westd-38929 | 0 | 1 MiB | 0% | — | — | — | **空闲** |
| westd-38929 | 1 | 1 MiB | 0% | — | — | — | **空闲** |
| westd-38929 | 2 | 15762 MiB | 75% | 732931 | OV l2norm k=0.75 Long s42 | 7h35m | **正常** Task 9/10, ~1h完成 |
| westd-38929 | 3 | 1 MiB | 0% | — | — | — | **空闲** |
| westd-41074 | 0 | 16169 MiB | 86% | 32184 | OV random k=0.95 Long s42 | 36min | **正常** Task 1/10 |
| westd-41074 | 1 | 16193 MiB | 72% | 856656 | OV random k=0.75 Long s42 | 5h44m | **正常** Task 7/10, ~2h完成 |
| westd-41074 | 2 | 15961 MiB | 68% | 934369 | OV random k=0.95 Object s42 | 3h33m | **正常** 进行中 |
| westd-41074 | 3 | 16099 MiB | 74% | 824210 | OV attn k=0.75 Long s42 | 6h36m | **正常** Task 8/10, ~1.5h完成 |
| cqa1-33015 | 0 | 15342 MiB | 76% | 834190 | OV attn k=0.5 Goal s42 | 1h12m | **⚠️ 异常** 0% SR |
| cqa1-33015 | 1 | 15357 MiB | 64% | 832020 | OV attn k=0.95 Object s42 | 1h15m | **⚠️ 异常** 0% SR |
| cqa1-33015 | 2 | 10429 MiB | 16% | 790017 | π0.5 l2norm k=0.85 Long s42 | 2h29m | **正常** |
| cqa1-33015 | 3 | 1 MiB | 0% | — | — | — | **空闲** |

## 异常实验

- **cqa1 PID 834190** (OV attn k=0.5 Goal) — transformers 5.5.3 vs 期望 4.40.1，Task 1-2 全部 0% SR。模型加载成功但推理结果完全错误，结果无效。
- **cqa1 PID 832020** (OV attn k=0.95 Object) — 同上，Task 1-2 全部 0% SR。transformers 版本不兼容导致推理退化严重。

两个 OpenVLA 实验在 cqa1 上跑了 1h+ 但全 0% 成功率，正在**浪费 2 张 GPU**。日志明确显示 transformers 版本不匹配 warning。

## 空闲 GPU

- westd-38929 GPU 0, 1, 3（3 张）
- cqa1-33015 GPU 3（1 张）
- **合计 4 张空闲**

## 即将释放

- westd-38929 GPU 2 — ~1h 后完成
- westd-41074 GPU 1 — ~2h 后完成
- westd-41074 GPU 3 — ~1.5h 后完成
- westd-27271 GPU 1 — 接近完成（9h+ 运行，10 task eval）

## 建议

1. **立即 kill cqa1 上两个 OpenVLA 实验**（PID 834190, 832020），释放 GPU 0, 1。这两个实验 0% SR，结果无意义。
2. 这两个 OpenVLA 实验（attn k=0.5 Goal、attn k=0.95 Object）应迁移到 westd-38929（有 3 张空闲 GPU，transformers 版本兼容）。
3. cqa1 释放后的 GPU 0, 1 可安排 π0.5 实验。
4. 之前任务描述中的 "19h+" 和 "20h+" 实验实际已完成，当前是同名新实验刚启动（35min / 36min）。

---
