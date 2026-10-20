# analysis table3 deberta verification

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table3-deberta-verification_20260520T203356_result.json`
- **Structured JSON:** [`d7eba0d7a63ae05ad0f1.json`](../../sessions/d7/d7eba0d7a63ae05ad0f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕。以下是调查结果：

```
Mistral-7B combo experiment (Dir J3 / Direction R):
  - Script: westd-16639:/root/symb_invariant_consensus/ 下的 dir_j3 系列
    (本地: artifacts/dir_j3_nli_multi_verifier.py, artifacts/direction_r_deberta_proofwriter.py)
  - DeBERTa model ID: /root/models/deberta-large-mnli (= microsoft/deberta-large-mnli)
  - Standalone accuracy on PW600: 55.00%

Qwen3-14B combo experiment (Dir K):
  - Script: westd-16639:/root/symb_invariant_consensus/dir_k_nli_qwen3_pw600.py
  - DeBERTa model ID: /root/autodl-tmp/models/deberta-base-mnli (= microsoft/deberta-base-mnli)
  - Standalone accuracy on PW600: 36.17%

Push B experiment:
  - Script: artifacts/push_b_stronger_nli.py
  - DeBERTa model ID: /root/autodl-tmp/models/deberta-v3-large-mnli-fever-anli-ling-wanli
    (= MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli)
  - Standalone accuracy on PW600: 45.17%

结论: 两个实验用了不同的 DeBERTa 模型。
  - Mistral-7B combo 用的是 deberta-LARGE-mnli（55.00%）
  - Qwen3-14B combo 用的是 deberta-BASE-mnli（36.17%）
  论文 Table 3 将 Mistral-7B combo 的 NLI verifier 标注为 "DeBERTa-base" 是错误的，
  实际应为 "DeBERTa-large"。
```

Worker 日志也明确记录了这一点（`worker_experiment_dir-k-nli-qwen3-proofwriter_20260520T180214_result.json`）：

> "used `deberta-base-mnli` (not `deberta-large-mnli` from the Mistral experiment). The large model had 55% standalone on this data vs 36.17% for base"

**需要修正**：Table 3 中 Mistral-7B combo 行的 NLI verifier 应改为 "DeBERTa-large" 而非 "DeBERTa-base"，或者统一用同一个模型重新跑实验。

---
