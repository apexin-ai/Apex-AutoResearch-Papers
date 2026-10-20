# ops gpu status check label only

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_label_only_20260520T191717_result.json`
- **Structured JSON:** [`3eebb77f2e89663da845.json`](../../sessions/3e/3eebb77f2e89663da845.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### qwen15b_label_only_seed42_v2
- **PID 642828**: **已结束**（进程不存在）
- **训练**: 已完成，3 个 checkpoint（148/296/444）+ final
- **Eval**: **已完成** ✓
  - **Accuracy = 78.9%**（majority baseline 71.5%，lift +7.4%）
  - Pass: P=0.82 R=0.91 F1=0.86
  - Fail: P=0.68 R=0.50 F1=0.57
  - Accuracy 95% CI: [76.6%, 81.2%]

### codellama13b_label_only_seed42_v2
- **PID 642747**: **存活**，已运行 1h53m
- **训练**: 进行中，**231/444 steps（52%）**，~28s/step，ETA ~1h39m
- **Checkpoint**: 已保存 checkpoint-148
- **Eval**: 未开始（训练未完成）

### GPU 利用率
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 100% | 85.5 / 97.9 GB |
| cuda:1 | 0% | 0 / 97.9 GB |

**注意**: cuda:1 完全空闲——qwen15b 已跑完释放了 GPU，codellama13b 只用 cuda:0。

---
