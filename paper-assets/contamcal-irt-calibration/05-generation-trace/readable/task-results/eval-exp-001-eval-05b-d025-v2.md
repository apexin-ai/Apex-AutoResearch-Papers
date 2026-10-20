# eval exp 001 eval 05B d025 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp_001_eval_05B_d025_v2_20260514T161441_result.json`
- **Structured JSON:** [`011222c24f0649df6f15.json`](../../sessions/01/011222c24f0649df6f15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

总结：

| 项目 | 状态 |
|------|------|
| **诊断** | Original aligned eval (`Qwen2.5-0.5B_d025_s42_aligned/`) 已完成（4 个 benchmark 全部有结果），缺失的是 **paraphrase aligned eval** |
| **提交** | `exp_001_eval_05B_d025_aligned_v2` — paraphrase aligned eval，PID 406027，cuda:5 |
| **参数** | `--mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --benchmarks mmlu gsm8k arc_challenge humaneval` |
| **输出** | `/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_para_aligned/` |
| **GPU 共存** | GPU 5 同时跑 3B 训练（18.6GB）+ 0.5B eval（1.5GB），总 20.1/24.6GB，headroom 充足 |
| **Registry** | RUNNING，parent=`exp_001_sft_d025_05B_v3` |

---
