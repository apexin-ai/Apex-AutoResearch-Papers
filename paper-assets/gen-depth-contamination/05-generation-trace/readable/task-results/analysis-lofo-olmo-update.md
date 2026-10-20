# analysis lofo olmo update

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lofo_olmo_update_20260521T152740_result.json`
- **Structured JSON:** [`2ff539207d072439e11c.json`](../../sessions/2f/2ff539207d072439e11c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整重算结果已写入 `artifacts/lofo_olmo_recalc.md`。

**核心结论**：Agreement 从 8/9 (89%) 暴跌至 2/9 (22%)，不宜直接更新 .tex。

**原因**：OLMo AUC_1v2=0.508 接近随机，在 4/5 个 fold 中成为 min(AUC_1v2)，将 θ̂ 从 ~0.59 拉低到 ~0.53-0.55。低 θ̂ 导致大部分模型被预测为 K*_θ̂≥3（因为两个 AUC 都超过了被压低的阈值），而 K*_0.60 仍给 K*=2 或 1，产生系统性 mismatch。

**决策选项**（详见文件）：
1. 排除 K*=1 模型出 LOFO 训练集
2. 用 median 代替 min
3. 如实报告 22%，加文字说明
4. 其他方案

需要 Director 决定处理方式。

---
