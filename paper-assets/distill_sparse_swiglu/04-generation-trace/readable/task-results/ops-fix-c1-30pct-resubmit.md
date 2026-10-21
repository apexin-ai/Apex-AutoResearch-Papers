# ops fix c1 30pct resubmit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-c1-30pct-resubmit_20260519T000422_result.json`
- **Structured JSON:** [`c1570a18290412e938d0.json`](../../sessions/c1/c1570a18290412e938d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常启动并在运行中。

**汇报：**
- **正确脚本路径**：`src/train_bce_kl_targets.py`（仅存在于 westd-41718，已复制到 westd-34887）
- **失败原因**：脚本是在 41718 上创建的，34887 的代码目录缺少此文件
- **提交状态**：✓ 已用 nohup 提交到 westd-34887 cuda:0，PID=64486
- **exp_id**：`c1_ablation_30pct_s42_v2`
- **日志**：`~/runs/distill_sparse_swiglu/c1_ablation_30pct_s42_v2.log`
- **前几行日志确认**：
  - 模型加载成功 (llama-3.1-8b)
  - KL oracle predictor 加载成功 (75,960,320 params, frozen)
  - 训练已开始，Step 1/1000: bce=0.6905, sparsity=0.500, agree=0.549

---
