# code exp d constrained decoding prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-d-constrained-decoding-prep_20260519T030047_result.json`
- **Structured JSON:** [`ab8aaa1b4aadb3fbf1ef.json`](../../sessions/ab/ab8aaa1b4aadb3fbf1ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All scripts are ready. Here's the summary:

---

## EXP-D Results

### 方案 1: Regex Forced-Parse (已完成, 无需 GPU)

脚本: `cwm_forced_parse.py` (已部署并运行)

7 级 parse 策略: original → pytest_summary → unittest_summary → pytest_dots → test_ok_fail → error_signals → last_line → majority_fallback

**结果:**

| 模型 | 原 unparseable | 挽救率 | 原 parseable acc | Forced-parseable acc | Delta |
|------|---------|--------|---------|---------|-------|
| Qwen3-8B CWM (n=9784) | 73.8% | 90.6% | 38.5% | 49.4% | +10.8pp |
| Qwen3-4B CWM (n=500) | 75.2% | 77.9% | 42.7% | 55.9% | +13.2pp |
| DeepSeek CWM (n=9784) | 51.0% | 20.3% | 38.7% | 51.8% | +13.1pp |

**假设被拒绝**: forced-parse accuracy 显著高于 original parseable-only accuracy (delta 10-13pp), 说明 unparseable outputs 的信号质量反而更好。最有效策略是 `test_ok_fail` (unittest "... ok" pattern, acc 67-71%)。

### 方案 2: vLLM Constrained Decoding (代码就绪, 需 GPU)

- vLLM 0.18.1 可用, 支持 `StructuredOutputsParams(choice=["PASS", "FAIL"])`
- `outlines` 未安装

**运行步骤 (需 GPU):**
```bash
# 1. Merge LoRA (约 5 min, 1 GPU)
python merge_lora.py \
  --base /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ \
  --adapter /root/autodl-tmp/checkpoints_backup_cwm_8b/checkpoint-400/ \
  --output /root/autodl-tmp/merged_cwm_8b_ckpt400/

# 2. Constrained decoding (需要 swebench_full 测试数据)
python eval_cwm_constrained.py \
  --model_path /root/autodl-tmp/merged_cwm_8b_ckpt400/ \
  --data_path data/swebench_full/swebench_test.jsonl \
  --mode choice \
  --output_dir /root/autodl-tmp/eval_results/cwm_8b_constrained/
```

**Blocker**: `data/swebench_full/swebench_test.jsonl` 不在当前服务器上 (原始 89K 样本数据集)。需要从生成源重新构建或从备份恢复。

**预估 GPU 时间**: merge ~5 min + inference ~15-20 min (9784 samples, choice mode 只生成 1 token/sample)

---
