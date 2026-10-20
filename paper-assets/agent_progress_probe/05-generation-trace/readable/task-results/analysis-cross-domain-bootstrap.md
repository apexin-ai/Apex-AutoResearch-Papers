# analysis cross domain bootstrap

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-domain-bootstrap_20260514T220201_result.json`
- **Structured JSON:** [`b8feaf4ab60e74064e2e.json`](../../sessions/b8/b8feaf4ab60e74064e2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已注册 (`art_20260514_c0a8f2`)。

---

## Cross-domain Bootstrap 结果

**测试集**: OH test split, 20,807 windows, 512 instances

### 发现了标签管线不一致问题

embeddings.pt 中存储的 `majority_label` 与当前 `windows_labeled.jsonl` 的标签有 **14.9% 不一致**（3,110 / 20,807 windows）。原因是 embeddings.pt 生成后，labeling function 管线做过更新并重新生成了 `windows_labeled.jsonl`。

两个标签源的 stagnation 比例差异巨大：
- **emb labels**（Probe 训练用的）: stag 6.8% (1,417/20,807)
- **WL labels**（当前 3-LF MV）: stag 21.4% (4,449/20,807)

### 结果取决于用哪个标签作 ground truth

| Ground Truth | GB macro_f1 | Probe macro_f1 | Δ | 95% CI | p-value |
|---|---|---|---|---|---|
| WL labels (当前 3-LF MV) | **0.9021** | 0.6443 | +25.78pp | [+24.8, +26.8] | <0.001 |
| Emb labels (Probe 训练标签) | 0.6212 | **0.7512** | −13.00pp | [−14.1, −11.9] | <0.001 |

### 解读

你的任务指定用 **3-LF majority vote silver labels** 作 ground truth，对应 WL labels。按这个标准：

**GB 以 25.78pp 的显著优势胜过 Probe (p<0.001)**，GB=0.9021 vs Probe=0.6443。

但需注意：这个比较对 Probe **不公平**——Probe 是在 stale 的 emb labels 上训练的（stag 仅 6.8%），而当前 WL labels 的 stag 比例是 21.4%。Probe 从未见过当前标准下的正确标签。要做公平比较，需要用当前 WL labels 重新生成 embeddings 并重新训练 Probe。

---
