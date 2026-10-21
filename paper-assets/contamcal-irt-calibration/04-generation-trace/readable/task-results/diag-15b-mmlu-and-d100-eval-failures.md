# diag 15B mmlu and d100 eval failures

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_15B_mmlu_and_d100_eval_failures_20260516T213219_result.json`
- **Structured JSON:** [`62505d0777ef2aee044c.json`](../../sessions/62/62505d0777ef2aee044c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## MMLU_v2 诊断
**原因**: 模型路径解析失败。设置了 `HF_HUB_OFFLINE=1` 但 tokenizer 加载时仍尝试访问 HuggingFace Hub。错误显示路径被解析为 repo_id `Qwen2.5-1.5B-Instruct` 而非本地路径 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct`。

根因：`exp002/signals/s2_minkpp.py` 的 `load_model_and_tokenizer` 中 tokenizer 加载使用的路径不是传入的完整本地路径，而是被截断/解析为 hub identifier。需要检查 `exp002/utils.py:39` 的 `from_pretrained` 调用是否正确传递了本地路径。

**GPU 0 状态**: 空闲 (0MiB, 0%)

## d100 eval 诊断
**原因**: 已正常完成（`.done` 标记文件存在，所有 benchmark 结果齐全）

结果文件: 有，各 benchmark 分数：
| Benchmark | Score |
|-----------|-------|
| MMLU | 34.08% (4786/14042) |
| GSM8K | 26.00% (343/1319) |
| ARC-Challenge | 59.81% (701/1172) |
| HumanEval | 1.22% pass@1 (2/164) |

**注意**: MMLU 所有预测几乎都是 "A"，HumanEval pass@1 极低。这个 d100 contaminated 模型在 aligned format 下表现严重退化，可能是 chat template 不匹配导致模型坍缩到固定输出。

**GPU 5 状态**: 空闲 (0MiB, 0%)

## nvidia-smi 汇总
| GPU | 状态 | 显存 | 进程 |
|-----|------|------|------|
| cuda:0 | 空闲 | 0MiB | - |
| cuda:1 | 占用 | 7141MiB | PID 863173 (python) |
| cuda:2 | 占用 | 6787MiB | PID 853489 (python) |
| cuda:3 | 空闲 | 3MiB | - |
| cuda:4 | 占用 | 6859MiB | PID 842929 (python) |
| cuda:5 | 空闲 | 0MiB | - |

**可用 GPU**: cuda:0, cuda:3, cuda:5

---
