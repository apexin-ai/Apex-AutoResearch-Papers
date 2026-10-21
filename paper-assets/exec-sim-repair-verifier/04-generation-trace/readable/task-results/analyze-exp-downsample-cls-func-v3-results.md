# analyze exp downsample cls func v3 results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp-downsample-cls-func-v3-results_20260519T051056_result.json`
- **Structured JSON:** [`398b1bb7065cebb1efe1.json`](../../sessions/39/398b1bb7065cebb1efe1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已注册。汇总如下：

---

## exp-downsample-cls-func-v3：训练成功 ✓

| Metric | Value |
|---|---|
| train_loss | 0.2869 |
| eval_loss (epoch 1) | 0.1061 |
| eval_loss (epoch 2) | **0.0907** (best) |
| eval_loss (epoch 3) | 0.1156 |
| training time | 44.4 min |
| checkpoint | `/root/autodl-tmp/checkpoints_cls_downsample_qwen3_4b/best` (epoch 2) |

Epoch 3 eval_loss 回升，best model 正确保存在 epoch 2。

**Eval 命令**（CLS repo-level eval，使用 `eval_repo_cls.py`）：

```bash
cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_repo_cls.py \
  --model_name_or_path /root/autodl-tmp/models/Qwen/Qwen3-4B \
  --adapter_path /root/autodl-tmp/checkpoints_cls_downsample_qwen3_4b/best \
  --data_dir data/swebench_full \
  --split test \
  --max_seq_length 2048 \
  --device cuda:0 \
  --output_dir artifacts/eval_cls_downsample_qwen3_4b
```

（需确认 `eval_repo_cls.py` 的具体参数再提交）

---

## exp-e-qwen3-3shot-baseline：Eval 成功 ✓

| Metric | Qwen3-8B | DeepSeek (ref) |
|---|---|---|
| per-test accuracy | **71.61%** | 46.28% |
| variant accuracy | **45.83%** (22/48) | 45.83% (22/48) |
| majority baseline | 73.0% | 73.0% |
| gap vs majority | -1.35pp | -26.7pp |
| F1 (macro) | 69.48% | — |
| unparseable | 0 | 0 |
| runtime | 24.6 min | — |

Qwen3-8B 3-shot per-test accuracy (71.61%) 远高于 DeepSeek (46.28%)，但仍低于 majority baseline 1.35pp。Variant accuracy 两者完全相同 (45.83%)。Qwen3 per-test 高是因为它更倾向于预测 pass（precision_pass=91.68%, recall_fail=83.56%），接近 majority voting 行为但略有区分能力。

---
