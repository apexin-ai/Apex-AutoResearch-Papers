# eval check mmlu acc norm and teal

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check_mmlu_acc_norm_and_teal_20260516T002408_result.json`
- **Structured JSON:** [`c846f131272b9e6a7a29.json`](../../sessions/c8/c846f131272b9e6a7a29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the summary:

---

## 1. MMLU acc_norm

**MMLU 不产生 acc_norm。** lm-eval-harness 0.4.12 中 MMLU 子任务的 `metric_list` 只配置了 `acc`，未配置 `acc_norm`（与 ARC-Challenge 不同，后者明确配置了两者）。

Dense (Llama) 的 MMLU 完整结果只有：
- `acc,none`: 0.6532
- 无 `acc_norm`

**如需 MMLU acc_norm**，须修改 lm-eval 的 MMLU task YAML 在 `metric_list` 中添加 `acc_norm`，然后重跑。

ARC-Challenge 已有 acc_norm：
- Dense: acc=0.5478, **acc_norm=0.5819**

## 2. PID 179918 状态（注意：是 KL sparse，不是 TEAL）

PID 179918 运行的是 `lm_eval_sparse.py` + **KL predictor**（predictor_kl_normalized.pt），不是 TEAL。
- 当前进度：GSM8K generate_until **453/1319 (34%)**，ETA ~30 min
- 输出目录 `results/lm_eval_kl_s42/` 会在完成时写入

**TEAL downstream 未运行过**，只有 PPL 结果（corrected: 23.31）。

## 3. 其他进程状态

| Job | GPU | Progress | ETA |
|-----|-----|----------|-----|
| KL sparse lm_eval (PID 179918) | cuda:0 | GSM8K 34% (453/1319) | ~30 min |
| Mistral KL downstream | cuda:1 | GSM8K 52% (685/1319) | ~25 min |
| Mistral Dense downstream | cuda:0 | GSM8K 15% (197/1319) | ~25 min |
| Dense (Llama) lm_eval | — | **COMPLETE** | — |

## 4. 完整对比表

| Condition | ARC-c acc | ARC-c acc_norm | WinoGrande acc | MMLU acc | GSM8K exact_match |
|-----------|-----------|----------------|----------------|----------|-------------------|
| Dense (Llama) | 0.5478 | **0.5819** | 0.7814 | 0.6532 | 0.5004 |
| KL sparse 50% (Llama) | pending | pending | pending | pending | pending |
| TEAL sparse 50% (Llama) | **not run** | **not run** | **not run** | **not run** | **not run** |
| Dense (Mistral) | pending | pending | pending | pending | pending |
| KL sparse 50% (Mistral) | pending | pending | pending | pending | pending |

**说明：**
- "MMLU acc_norm" 列已移除——lm-eval-harness 对 MMLU 不输出此指标
- WinoGrande 也只有 acc，无 acc_norm
- KL sparse (Llama) 结果 ~30 min 后可用
- Mistral 两条 ~25-30 min 后可用
- TEAL downstream 从未启动，需要另行安排

## 5. 如需重跑 MMLU 以获取 acc_norm

需要自定义 task config 覆盖默认 MMLU 配置：

```bash
# 创建自定义 MMLU config（添加 acc_norm metric）
cat > /root/distill_sparse_swiglu/configs/mmlu_with_acc_norm.yaml << 'EOF'
group: mmlu
task:
  - mmlu_abstract_algebra
  # ... 所有 MMLU 子任务
metadata:
  version: 1.0
aggregate_metric_list:
  - metric: acc_norm
    aggregation: mean
    higher_is_better: true
EOF
```

但考虑到 MMLU 是 multiple choice（选项长度差异不大），acc 和 acc_norm 通常非常接近，重跑的性价比可能不高。

---
