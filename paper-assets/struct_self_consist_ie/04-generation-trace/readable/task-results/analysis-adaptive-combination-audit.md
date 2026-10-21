# analysis adaptive combination audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_adaptive_combination_audit_20260519T022017_result.json`
- **Structured JSON:** [`ad4b490bfa03b309cee7.json`](../../sessions/ad/ad4b490bfa03b309cee7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**确认存在 gold label 泄漏。** 以下是逐行分析。

---

## 泄漏核心：`compute_lp_alignment` (line 357-383)

```python
def compute_lp_alignment(inst):
    gold = entity_set(inst["gold"]["entities"])          # line 358: 读取 gold labels
    samples = inst["samples"]
    logprobs = inst.get("logprobs", None)

    lps = []
    f1s = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        ...
        lps.append(lp)
        pred = entity_set(s.get("entities", []))
        _, _, f = compute_prf(pred, gold)                # line 372: 每个 sample 对 gold 算 F1
        f1s.append(f)

    ...
    from scipy.stats import spearmanr
    rho, _ = spearmanr(lps, f1s)                         # line 380: LP 与 gold-F1 的 Spearman 相关
    return rho
```

**这个函数的语义**：计算某个实例内，各 sample 的 log-probability 与其 gold F1 的 Spearman 相关系数。**这个信号本身就是 gold label 的函数**——没有 gold label 无法计算。

---

## 泄漏传播路径：`adaptive_combination_cv` (line 385-443)

```python
def adaptive_combination_cv(data, n_splits=5, seed=42, variant="uniform"):
    ...
    alignments = np.array([compute_lp_alignment(inst) for inst in data])  # line 389: 对 ALL 实例算 alignment（含 gold）
    lp_f1s = compute_per_instance_f1s(data, make_lp_selection_fn())       # line 390

    ...
    for fold_idx, (train_idx, test_idx) in enumerate(kf.split(indices)):
        ...
        for gate_t in gating_thresholds:
            for constr_t in THRESHOLDS:
                ...
                for i in train_idx:
                    if alignments[i] > gate_t:           # line 407: 用 gold-derived alignment 做门控决策
                        train_f1_sum += lp_f1s[i]
                    else:
                        ...
                        gold = entity_set(data[i]["gold"]["entities"])  # line 411
                        ...
                        train_f1_sum += f

        # Test phase
        for i in test_idx:
            if alignments[i] > best_gate_t:              # line 423: TEST 实例也用自己的 gold-derived alignment
                f = lp_f1s[i]
            else:
                ...
                gold = entity_set(data[i]["gold"]["entities"])  # line 427
                ...
```

---

## 泄漏机制总结

两层泄漏：

1. **`compute_lp_alignment` 本身是 gold 的函数**（line 358, 372）：alignment score = spearman(logprobs, gold_F1)。没有 gold label 就不可能算出这个值。这是一个 **fundamentally supervised signal**，不是 unsupervised 的 LP 信号。

2. **alignment 在 CV split 之前对全部数据计算**（line 389）：`alignments` 数组包含所有实例（包括每个 fold 的 test 实例）。当 line 423 用 `alignments[i] > best_gate_t` 对 test 实例做门控决策时，这个决策使用了 **该实例自身的 gold label 信息**。CV 只保护了 `gate_t` 和 `constr_t` 两个超参的选择，但门控信号本身已经泄漏了。

**泄漏程度**：这不是边缘泄漏，而是核心机制性泄漏。adaptive combination 的整个决策逻辑建立在"LP 与 gold F1 的相关性"之上。在真实部署场景中，没有 gold label，`compute_lp_alignment` 无法运行，这个方法不可用。

**结论：adaptive combination 的结果不能写入论文。**

---

如果要做 clean 版本的 adaptive gating，决策信号应该只使用 unsupervised 的 LP 统计量，例如：
- within-instance LP 方差（高方差 → 模型不确定 → 用 construction）
- LP range（max LP - min LP）
- 平均 LP 绝对值（高 LP → 模型自信 → 用 LP selection）

这些信号不依赖 gold label，可以在 inference 时计算。

---
