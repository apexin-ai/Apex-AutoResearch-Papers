# ssh cqa1 eval progress v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cqa1-eval-progress-v2_20260519T083452_result.json`
- **Structured JSON:** [`25528288928aed1d499d.json`](../../sessions/25/25528288928aed1d499d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## GPU 状态
- GPU 0 (RTX 4090D 24GB): **空闲**，0MiB VRAM，无进程

## 已完成 eval（3/3 全部完成）

| Model | MMLU | ARC-Challenge |
|-------|------|---------------|
| OLMo-2-7B_d000_s42 | 58.71% (8244/14042) | 68.09% (798/1172) |
| OLMo-2-7B_d005_s42 | 58.21% (8174/14042) | 68.17% (799/1172) |
| OLMo-2-7B_d025_s42 | 59.14% (8305/14042) | 67.83% (795/1172) |

完成时间：d000 15:48-15:54, d005 16:07-16:13, d025 16:27-16:33（今天下午）。

## 模型状态
- **Gemma-2-9B**: 正在下载/传输中，已有 config.json + 8 个 safetensors 分片（合计 ~66MB，9B 模型完整约 18GB，刚开始）
- **OLMo-2-1124-7B**: 已删除

## 待跑
OLMo-2 系列 3 个 eval 已全部完成。GPU 当前空闲，Gemma-2-9B 模型文件正在传输中（才 ~66MB / ~18GB），传完后可开始 Gemma-2 跨家族 eval。

---
