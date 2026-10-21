# eval exp8 macro f1 and leakage audit

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp8-macro-f1-and-leakage-audit_20260518T171248_result.json`
- **Structured JSON:** [`382a926cbf996a0f231b.json`](../../sessions/38/382a926cbf996a0f231b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Here's the summary:

---

## 问题 1: F1 指标修正结果

所有 exp8 评估已用 `macro F1` 和 `binary F1` 重算。Macro F1 普遍低于 binary F1（因为 binary F1 只看 positive class，忽略 benign class 表现差的问题）。

**ToxicChat (204 jb + 204 bn):**

| Variant | Macro F1 | Binary F1 (旧) |
|---------|----------|----------------|
| vanilla | 0.413±0.021 | 0.221±0.055 |
| 9class | 0.596±0.087 | 0.654±0.087 |
| binary | 0.705±0.072 | 0.766±0.038 |
| scrambled | 0.616±0.056 | 0.691±0.041 |
| **jb_mlm** | **0.837±0.013** | 0.842±0.009 |
| wiki_mlm | 0.791±0.093 | 0.764±0.132 |
| topic | 0.496±0.042 | 0.558±0.067 |

**Verazuo (666 jb + 213 bn):**

| Variant | Macro F1 | Binary F1 (旧) |
|---------|----------|----------------|
| vanilla | 0.267±0.018 | 0.132±0.033 |
| 9class | 0.767±0.153 | 0.812±0.135 |
| binary | 0.883±0.054 | 0.929±0.037 |
| scrambled | 0.822±0.046 | 0.884±0.037 |
| **jb_mlm** | **0.937±0.020** | 0.968±0.010 |
| wiki_mlm | 0.845±0.109 | 0.897±0.093 |
| topic | 0.669±0.087 | 0.758±0.082 |

---

## 问题 2: Verazuo benign 数据泄露确认

**泄露已确认**：213 条 benign 中，**167 条来自 train.jsonl（78%），仅 46 条来自 test.jsonl**。

去除泄露数据后的 verazuo 评估 (666 jb + 46 bn, test-only benign)：

| Variant | Macro F1 (no leak) | Macro F1 (all) | 差值 |
|---------|-------------------|----------------|------|
| vanilla | 0.129 | 0.267 | -0.138 |
| 9class | 0.627 | 0.767 | -0.139 |
| binary | 0.738 | 0.883 | -0.145 |
| scrambled | 0.649 | 0.822 | -0.173 |
| jb_mlm | 0.852 | 0.937 | -0.085 |
| wiki_mlm | 0.742 | 0.845 | -0.103 |
| topic | 0.503 | 0.669 | -0.166 |

macro F1 在去除泄露后普遍下降 0.08-0.17，但 test-only benign 只有 46 条 vs 666 jailbreak（极度不平衡），所以这个数字受 benign 样本不足影响。论文中建议使用外部 benign 数据源。

---

**输出文件：**
- `results/exp8_macro_f1_corrected.json` — 所有 metrics（不含 raw predictions）
- `results/exp8_raw_predictions.json` — 每个 variant×seed×dataset 的 y_true/y_pred/y_prob
- `results/exp8_recalc_run.log` — 完整运行日志
- 脚本：`scripts/exp8_recalc_macro_f1.py`

---
