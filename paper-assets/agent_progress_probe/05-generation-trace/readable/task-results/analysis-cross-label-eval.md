# analysis cross label eval

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-label-eval_20260514T140245_result.json`
- **Structured JSON:** [`be1985317023edc69dd5.json`](../../sessions/be/be1985317023edc69dd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### 结果

**关键发现：OB = coverage-valuable + vote-consistent**

1. **标签完全一致**：3-LF 和 2-LF 在所有 43,402 个有标签的 window 上 100% agreement，0 disagreement。OB 从不与另外两个 LF 矛盾。

2. **OB 提供 33.5% 额外 coverage**：
   - 3-LF conf≥2: 15,401 windows (28.1%)
   - 2-LF conf≥2: 10,243 windows (18.7%)
   - OB 贡献 5,158 个额外高置信标签

3. **0.9510 vs 0.9055 不可直接比较**：
   - 发现两个模型使用了不同的 instance split（过滤改变了 unique instance 集→shuffle 结果不同）
   - 交叉评估存在严重数据泄漏（206/297 和 203/344 instances 重叠）
   - 需要共享 split 重新训练才能公平比较

4. **without-OB 模型在完整分布上退化严重**：在原始 split 全部 8101 test windows 上仅 F1=0.7019，因为只见过 2-LF conf≥2 的"简单"样本

5. **产出**：`cross_label_eval.py` + `cross_label_eval_results.json` 已保存在服务器，registry 已更新为 DONE(success)

---
