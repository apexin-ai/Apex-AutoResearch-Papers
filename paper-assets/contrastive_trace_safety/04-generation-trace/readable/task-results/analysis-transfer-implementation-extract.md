# analysis transfer implementation extract

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_transfer_implementation_extract_20260517T044108_result.json`
- **Structured JSON:** [`ec62b10d730eff9b9f18.json`](../../sessions/ec/ec62b10d730eff9b9f18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已生成：`artifacts/exp_003_cross_transfer_details.md`

核心发现：

1. **维度对齐方法极其简单** — 不是 Procrustes/CCA/learned mapping，而是对每个模型独立做 PCA 降到相同维度（2048/1024/512），然后直接在不同模型的 PCA 空间之间迁移 probe。两个 PCA 基底之间没有任何对齐步骤。

2. **没有尝试过替代方案** — 代码中没有注释掉的其他方法，没有 config 选项，只实现了"独立 PCA + 直接迁移"和"同维度直接迁移"两种。

3. **PCA 用全量数据拟合** — 不区分 train/test，所有 traces 的所有 steps 拼接后 fit PCA。Train/test split 仅用于 LogisticRegression 的 baseline 评估。

4. **值得注意的结果** — qwq_32b→r1_32b 的 direct transfer（同为 5120 维）accuracy 0.673 甚至略超 r1_32b 自身 baseline 0.652，说明安全信号在同维模型间有较强的通用性。

---
