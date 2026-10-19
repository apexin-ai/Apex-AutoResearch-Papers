# eval fix and launch 14b 4task uniform

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_fix_and_launch_14b_4task_uniform_20260518T005341_result.json`
- **Structured JSON:** [`ca24f6bc425c6d2631dc.json`](../../sessions/ca/ca24f6bc425c6d2631dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断与状态报告

### 原始失败原因

| 实验 | 失败原因 |
|------|----------|
| KL uniform eval | 模型路径大小写错误：命令用了 `Qwen2.5-14B`，实际目录是 `qwen2.5-14b` → HuggingFace 把路径当 repo ID 解析 → `OSError` |
| TEAL uniform eval | 未失败，但卡在 GSM8K `generate_until`（1319 items，15s/it，需要 ~5.5h），实质上是 GSM8K 太慢导致超时或被认为失败 |

### 当前状态：4-task eval 已在运行

有人已经修复路径并启动了 4-task 版本，两个 GPU 都在跑：

| 实验 | PID | GPU | exp_id | WikiText-2 PPL | 当前阶段 |
|------|-----|-----|--------|-----------------|---------|
| KL uniform | 87149 | cuda:0 | `qwen14b_kl30_uniform_4task` | **7.6318** | MMLU loglikelihood 296/4687 (~6%) |
| TEAL uniform | 87288 | cuda:1 | `qwen14b_teal30_uniform_4task` | **8.0054** | MMLU loglikelihood 312/4687 (~7%) |

KL 用了 `--sparsity_mode teal_global --checkpoint ...predictor_kl_normalized.pt`，TEAL 用了 `--baseline_mode teal_vanilla`。`--allocation uniform` 参数正确（代码 L111-113 确认支持 `global_topk` 和 `uniform` 两个选项）。

Uniform allocation 每层约 0.30 sparsity，两者均已完成 WikiText-2 和 ARC Challenge，正在跑 MMLU。按当前速度 (~9.4 it/s)，MMLU 约需 8 分钟完成。整体预计 **10-15 分钟内** 两个 eval 都会跑完。

**无需重新提交，等结果即可。**

---
