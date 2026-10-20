# check westd gpu and shortgpt results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_gpu_and_shortgpt_results_20260520T022150_result.json`
- **Structured JSON:** [`4888ec8af3c3e31a6f70.json`](../../sessions/48/4888ec8af3c3e31a6f70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部补录完成。汇报如下：

## GPU 状态

| 服务器 | GPU | 显存占用 | 利用率 |
|--------|-----|----------|--------|
| westd-29022 | cuda:0-3 | 全部 0 MiB | 0% |
| westb-23072 | cuda:0-1 | 全部 0 MiB | 0% |

**6 GPU 全空，0 RUNNING 实验，无残留进程。**

## ShortGPT MBPP 结果（已确认，文件含 `.done` 标记）

| 模型 | pass@1 | n_correct | n_total | stderr |
|------|--------|-----------|---------|--------|
| ShortGPT SFT 20% | **10.43%** | 39 | 374 | ±1.58% |
| ShortGPT GRPO 20% | **14.44%** | 54 | 374 | ±1.82% |

Reviewer 上轮报告的数字 (SFT 10.43%, GRPO 14.44%) **完全一致**，结果可信。

## Registry 补录

- `eval_mbpp_sft_shortgpt_20_v2`: QUEUED → **DONE/success**，metrics 已写入
- `eval_mbpp_grpo_shortgpt_20_v2`: DONE/failed → **DONE/success**，metrics 已写入

注：ShortGPT GRPO 在 MBPP 上反而比 SFT 提升 +4.01pp，与 GSM8K 上 GRPO 退化 (44.73→43.37%) 的趋势相反。

---
