# infra s456 eval collect and s123 launch

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_s456_eval_collect_and_s123_launch_20260517T204520_result.json`
- **Structured JSON:** [`e6e081b2c8e8686b1df9.json`](../../sessions/e6/e6e081b2c8e8686b1df9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. bce_isocompute_v3_s456_eval 完整指标

| 指标 | 值 |
|---|---|
| WikiText-2 PPL | **28.35** |
| ARC-Challenge (acc_norm) | **28.07%** |
| WinoGrande (acc) | **52.41%** |
| MMLU (acc) | **25.67%** |
| GSM8K (exact_match) | **2.20%** |

配置：BCE loss, 50% global_topk sparsity, teal_global mode, seed=456

### 2. bce_isocompute_v3_s123 训练状态

- **PID**: 72392
- **启动方式**: nohup（符合 C002 约束）
- **日志**: `/root/runs/distill_sparse_swiglu/bce_isocompute_v3_s123.log`
- **GPU**: westd-34887 cuda:1
- **状态**: 模型已加载完成，正在训练（Trainable: 75.96M / 8.03B = 0.946%）
- 无 tmux session（nohup 直接后台）

### 3. 预估训练时间

参考 s456 约 49 min，s123 配置完全相同，预计 **~49 min** 完成。

---
