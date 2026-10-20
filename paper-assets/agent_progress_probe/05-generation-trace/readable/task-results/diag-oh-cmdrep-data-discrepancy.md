# diag oh cmdrep data discrepancy

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_oh-cmdrep-data-discrepancy_20260514T154005_result.json`
- **Structured JSON:** [`64869155eacd79ba387b.json`](../../sessions/64/64869155eacd79ba387b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

溯源完成。以下是结论：

---

## 77,763 vs 72,554 差异来源

### 77,763 — **2-LF 覆盖量**（至少一个非 cmd_rep LF 触发的窗口数）

来源：**不在脚本中**（grep 确认 `oh_cmdrep_ablation.py` 里没有 77763 这个数字）。是填 registry 时的 worker/agent 计算的：

```
143,057 (总 embeddings) - 65,294 (file_diff 和 outcome_bp 都没触发的) = 77,763
```

验证：file_diff 触发 58,224 个窗口，outcome_bp 触发 28,765 个。两者并集 = 58,224 + 28,765 - intersection = 77,763，推算 intersection = 9,226。

### 72,554 — **可用训练数据**（2-LF relabel 后 conf≥1 有效标签数）

来源：脚本 `relabel_2lf()` 的实际输出，日志明确打印：
```
--- min_conf=1 ---
Usable: 72554 (50.7% of embeddings)
Labels: {0: 42536, 1: 30018}
Stag ratio: 0.5863
```

### 5,209 差异 = **两个 LF 都触发但投票不一致的窗口**

- intersection (两个 LF 都触发) = 9,226
- 其中 agree (conf=2) = 4,017
- 其中 disagree = 9,226 - 4,017 = **5,209** ← 正好是差值

`relabel_2lf()` 对 disagree 返回 label=-1（不可用），所以这些窗口被丢弃。

### 两个 stag 比例

| 数字 | 含义 | stag 比例 |
|------|------|-----------|
| 77,763 | 有任意非 cmd_rep LF 信号的窗口 | 54.77%（包含 disagree 窗口的某种计算） |
| 72,554 | relabel_2lf conf≥1 有效标签 | 58.63%（42,536/72,554，真实训练分布） |

stag 比例升高的原因：被丢弃的 5,209 disagreement 窗口中 progress 居多（file_diff 说 progress，outcome_bp 说 stagnation，或反过来），移除后 stag 占比上升。

### Registry 应该用哪组数字

**72,554 / 58.63%** — 这是脚本实际 relabel 并用于训练的数据。77,763 只是"有信号覆盖"的窗口数，disagree 窗口从未参与训练。

Registry 的 `label_stats.new_total` 应从 77,763 改为 72,554，`new_stag_pct` 从 54.77 改为 58.63。

---
