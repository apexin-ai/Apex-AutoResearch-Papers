# code exp backup3 distill verifier

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_backup3_distill_verifier_20260520T174209_result.json`
- **Structured JSON:** [`0c6b58361335c8713145.json`](../../sessions/0c/0c6b58361335c8713145.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 产出报告

### 可用数据

| Dataset | Path | Instances | N | T | LP score |
|---------|------|-----------|---|---|----------|
| SciERC | `exp_026_t10_seed42/samples.jsonl` | 551 | 8 | 1.0 | ✓ sample-level `mean_logprob` + token-level `token_logprobs` |
| CoNLL | `exp_002_conll_n16/samples.jsonl` | 3,453 | 16→**subsample 8** | 1.0 | ✓ 同上 |
| FewNERD | `exp_021_inference/samples.jsonl` | 37,648 | 8 | 1.0 | ✓ 同上 |

**LP score 可用**，无需额外 forward pass。CoNLL 无 N=8 seed=42 专用文件，代码自动从 N=16 截取前 8 个 sample。

### 代码

- **本地**: `artifacts/experiments/distill_verifier/run_distill_verifier.py`
- **服务器**: `/root/autodl-tmp/struct_self_consist_ie/run_distill_verifier.py`
- 6 特征: lp_score, agreement_ratio, degeneracy_flag, span_length, type_consistency, n_samples
- 3 分类器: LogisticRegression, RandomForest(100 trees), MLP(64,32)
- Leave-one-dataset-out 3-fold CV + threshold sweep (0.3–0.7)

### 运行命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
python /root/autodl-tmp/struct_self_consist_ie/run_distill_verifier.py --seed 42
```

### Smoke test 结果（20 inst/dataset）

- Mean AUROC: LR 0.86, RF 0.84, MLP 0.85
- Mean Δ F1 vs standard MV: LR +0.016, RF +0.006, **MLP +0.031**
- agreement_ratio 是最强特征（LR coefficient ~1.4–2.0），lp_score 其次

### 预计运行时长

**5–15 分钟**，CPU-only（sklearn 不需要 GPU）。主要瓶颈是 FewNERD 37K 实例的 feature extraction 和 F1 evaluation（每 fold 重新加载一次 held-out 数据）。

### Blockers

无。所有 GPU 被占但不影响此实验（纯 CPU）。Registry 状态已设为 PENDING。

---
