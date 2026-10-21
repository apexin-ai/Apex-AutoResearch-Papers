# code tail decay audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tail-decay-audit_20260517T102130_result.json`
- **Structured JSON:** [`2f7027faf71b23221dc4.json`](../../sessions/2f/2f7027faf71b23221dc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### tail_decay 完整代码

所有三个实现文件（`extract_features.py`、`extract_features_multi.py`、`fix_tail_decay_and_eval.py`）逻辑完全一致。以 `extract_features.py:79-141` 为准：

```python
def compute_reference_features(texts: list[str], tokenizer, model, device: str, batch_size: int) -> list[dict]:
    results = []
    for start in range(0, len(texts), batch_size):
        batch_texts = texts[start : start + batch_size]
        encodings = tokenizer(
            batch_texts, return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        ).to(device)

        with torch.no_grad():
            outputs = model(**encodings)
            logits = outputs.logits  # (B, seq_len, vocab)

        for i in range(len(batch_texts)):
            mask = encodings["attention_mask"][i].bool()
            seq_len = mask.sum().item()
            if seq_len < 2:
                results.append({
                    "entropy_mean": 0.0, "entropy_std": 0.0,
                    "entropy_min": 0.0, "entropy_max": 0.0,
                    "tail_decay": 0.0,
                })
                continue

            # Token-level entropy: logits[0..T-2] predict tokens[1..T-1]
            token_logits = logits[i, :seq_len - 1, :]  # (T-1, V)
            log_probs = torch.log_softmax(token_logits, dim=-1)
            probs = torch.exp(log_probs)
            entropy = -(probs * log_probs).sum(dim=-1)  # (T-1,)
            entropy_np = entropy.float().cpu().numpy()

            # Tail decay: average log-prob distribution, fit slope on ranks 100-1000
            avg_log_probs = log_probs.float().mean(dim=0)  # (V,)
            sorted_lp, _ = torch.sort(avg_log_probs, descending=True)
            sorted_lp_np = sorted_lp.cpu().numpy()

            vocab_size = sorted_lp_np.shape[0]
            hi = min(1000, vocab_size)
            lo = min(100, hi)
            if hi - lo >= 2:
                x = np.arange(lo, hi, dtype=np.float64)
                y = sorted_lp_np[lo:hi].astype(np.float64)
                coeffs = np.polyfit(x, y, 1)
                tail_decay = float(coeffs[0])
            else:
                tail_decay = 0.0

            results.append({
                "entropy_mean": float(np.mean(entropy_np)),
                "entropy_std": float(np.std(entropy_np)),
                "entropy_min": float(np.min(entropy_np)),
                "entropy_max": float(np.max(entropy_np)),
                "tail_decay": tail_decay,
            })
    return results
```

**文件路径和行号**：`/root/gen-depth-fingerprint/extract_features.py:79-141`

---

### 论文描述（`method.tex:49`）

> **tail\_decay**: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.

---

### 结论：论文与代码描述的是完全不同的计算

| | 论文描述 | 代码实现 |
|---|---|---|
| **输入** | token-level NLL 序列 | 每个 token 位置的 log-softmax → 跨位置取均值得到 vocabulary-level 的 avg log-prob |
| **操作** | 统计超过全局 90th percentile 阈值（基于 $\mathcal{C}_0$）的 token 比例 | 对 vocab 维度排序后取 rank 100–1000 区间，做线性回归 |
| **返回值** | 一个比例值（proportion, ∈[0,1]） | 一个斜率值（slope, 负数） |
| **语义** | token-level NLL 的尾部权重 | vocabulary-level log-prob 分布的衰减速率 |

代码实际计算的是：**将每篇文本在参考模型下的词表级平均 log-probability 按降序排列，取第 100–1000 名区间拟合线性回归，返回斜率**——衡量的是词表概率分布尾部的衰减速度，与论文描述的"超过 90th 百分位的 token 比例"完全不同。

---
