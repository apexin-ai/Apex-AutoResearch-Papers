# infra full status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_full-status-check_20260521T142134_result.json`
- **Structured JSON:** [`6a84926e49ab678d2ad2.json`](../../sessions/6a/6a84926e49ab678d2ad2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收齐。汇总如下：

## GPU 状态

| GPU | VRAM 占用 | 利用率 | 用途 |
|-----|----------|--------|------|
| 0 | 84/98 GB | 0% | Mistral-7B vLLM (cross-model) |
| 1 | 84/98 GB | 100% | Qwen3-14B vLLM (cross-model) |
| 2 | 88/98 GB | 100% | Qwen2.5-72B-AWQ vLLM (70B SICA) |
| 3 | 83/98 GB | 100% | R1-Distill-8B vLLM |

## 实验状态

| 实验 | 状态 | 进度 | 关键指标 | ETA/备注 |
|------|------|------|----------|----------|
| **D135 Frontier gpt-4.1** | running | 33/204 | SC acc=0.733 | ~63min（2.8q/min） |
| **D135 Frontier gpt-5.5** | running | 5/204 | 5/5 correct so far | 慢，~70-140s/q，偶发 502；ETA ~5-6h |
| **D135 Frontier o3** | running | 5/204 | 3/5 correct，大量 HTTP 500 | 不稳定，频繁 500 错误，部分回答为空 |
| **R1-Distill-8B SICA** | running | 45/204 | SC=0.689, SICA=0.689 | extraction_rate=0.0（约束提取全失败，context length 400 错误）；运行 42min |
| **Cross-Model SICA** | running | ~90/204 (phase1) | checkpoint: 90 problems done | 运行 5h42m，当前在 phase2 extraction 阶段 |
| **70B SICA** | running | 5/204 | SC=1.0, SICA=1.0 (n=5) | extraction_rate=1.0；运行 1h42m，极慢 ~19min/q |
| **E6 GPT4O FOLIO** | running | 157/204 | — | 运行 4h48m |

## 关键问题

1. **R1-Distill-8B**: `extraction_rate=0.0` — 约束提取阶段全部因 context length 超限失败（prompt 4097 tokens + 请求 4096 output = 8193 > max 8192）。SC 正常跑，但 SICA 等于 SC（无约束增强效果）。
2. **o3**: 大量 HTTP 500 server error，部分回答丢失（dist={}），准确率受影响。
3. **70B**: 每题 ~19 分钟，按此速度 204 题需 ~63 小时。
4. **Cross-Model**: 已跑 5.7h 完成 phase1 的 90/204，phase2 extraction 进行中，无 intermediates 目录（结构不同，用 extraction_* 子目录）。

---
