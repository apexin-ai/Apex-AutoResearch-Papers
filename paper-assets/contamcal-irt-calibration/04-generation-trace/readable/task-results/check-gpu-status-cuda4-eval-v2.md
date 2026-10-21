# check gpu status cuda4 eval v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_cuda4_eval_v2_20260515T193245_result.json`
- **Structured JSON:** [`af2dcec177facc99ef9e.json`](../../sessions/af/af2dcec177facc99ef9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总报告如下：

---

## GPU 状态总览

| GPU | 显存占用 | GPU利用率 | PID | 状态 |
|-----|---------|-----------|-----|------|
| cuda:0 | 17975/24564 MiB | 40% | 594494 (python) | **占用** |
| cuda:1 | 13341/24564 MiB | 33% | 593745 (python) | **占用** |
| cuda:2 | 0/24564 MiB | 0% | — | **空闲** |
| cuda:3 | 7535/24564 MiB | 62% | 617202 (python) | **占用** |
| cuda:4 | 0/24564 MiB | 0% | — | **空闲** |
| cuda:5 | 17651/24564 MiB | 44% | 589763 (python) | **占用** |

- **cuda:4**: 完全空闲，d000_v3 SFT 和 signals 进程均已结束
- **cuda:2**: 完全空闲，PID 614412 不在 — eval_v2 **已跑完**（EXIT_CODE=0）

## eval_v2 (exp_001_eval_3B_d100_s123_para_aligned_v2) 运行状态

**已完成**，EXIT_CODE=0。结果已保存到 `Qwen2.5-3B_d100_s123_para_aligned/`。日志末尾显示的最后几个 benchmark 结果：
- arc_challenge (paraphrased): **0.8164**
- humaneval (paraphrased) pass@1: **0.0769** (2/26)

## d005_s123 aligned eval 结果

全部 5 个配置的结果均已存在（`.done` sentinel 已写入）：

| 模型 | 类型 | MMLU | GSM8K | ARC-C | HumanEval |
|------|------|------|-------|-------|-----------|
| 0.5B d005_s123 | original | 0.3002 | 0.3677 | 0.2978 | 0.0976 |
| 0.5B d005_s123 | para | 0.3166 | 0.2939 | 0.2912 | 0.0000 |
| 1.5B d005_s123 | original | 0.5869 | 0.6482 | 0.7568 | 0.2500 |
| 3B d005_s123 | original | 0.6324 | 0.6308 | 0.8242 | 0.1037 |
| 3B d005_s123 | para | 0.6461 | 0.5000 | 0.8192 | 0.0769 |

**注意**：1.5B d005_s123_para_aligned 结果目录也存在（May 16 00:31），但未在本次查询范围。

---
