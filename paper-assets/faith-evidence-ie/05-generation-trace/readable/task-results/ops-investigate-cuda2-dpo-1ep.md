# ops investigate cuda2 dpo 1ep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-cuda2-dpo-1ep_20260515T211913_result.json`
- **Structured JSON:** [`e2a841eab3801304e503.json`](../../sessions/e2/e2a841eab3801304e503.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查结果汇总：

## eval_plan_012_dpo_ced_1ep 状态：**正在运行**（inference 阶段）

### DPO 训练
- **已完成**，耗时 33m49s，exit code 0
- 模型保存在 `/root/autodl-tmp/dpo_output_1ep`
- 训练 loss: 0.593，rewards/accuracies: 0.821，rewards/margins: 0.859

### Dev Eval
- **正在运行**，进度 95% (59/62 batches)
- PID 251136，CPU 103%，运行在 cuda:2 上
- 启动于 04:21，已运行约 58 分钟，预计剩余 ~3 分钟
- 输出目录 `/root/autodl-tmp/eval_results/dpo_ced_1ep/`（目前只有 eval.log）

### cuda:2
- **正在使用**（89% GPU 利用率，19517/32607 MiB），被 eval_plan_012_dpo_ced_1ep 的 inference 进程占用
- resource_usage 报告空闲是误判

### 4 块 GPU 当前分配
| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 91% | 18337M | eval_plan_001_flat_nli_s43 |
| 1 | 77% | 15769M | eval_plan_011_bf16_g8_step50 |
| 2 | 89% | 19517M | **eval_plan_012_dpo_ced_1ep** (95%) |
| 3 | 72% | 16469M | eval_plan_008_rsft_topk3 |

**结论**：eval_plan_012_dpo_ced_1ep 运行正常，即将在几分钟内完成。cuda:2 当前不可用。

---
