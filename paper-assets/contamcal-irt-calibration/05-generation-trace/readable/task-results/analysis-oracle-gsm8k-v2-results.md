# analysis oracle gsm8k v2 results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oracle-gsm8k-v2-results_20260515T034506_result.json`
- **Structured JSON:** [`166623990931a0f5d06b.json`](../../sessions/16/166623990931a0f5d06b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**Memory 矛盾的根因**：v1 实验 IRT 拟合失败（Operation not permitted），只有 B0_raw baseline 成功且 C95=1.00。Memory 将 B0_raw 的指标误记为 IRT 的 → 得出"N 够了就行"的错误结论。v2 IRT 成功运行后暴露了真实的 C95=0.3125。

**Coverage 31.25% 的两个独立失败机制**：
1. **Cross-scale theta 偏差**：所有 1.5B 模型（包括 d000/无 contamination）都被低估 4-5pp。5280 个 item 参数由 16 个模型约束，严重欠定。
2. **Gamma 过校正**：gamma=3.77 捕获了真实的 item-level contamination signal，但 GSM8K accuracy 实际只变化 <2pp。IRT 校正幅度是真实变化的 21 倍。

**关键洞察**：GSM8K 的 contamination 是**再分配型**（改变哪些 items 答对）而非**加法型**（不增加总答对数）。IRT gamma 在 item 层面有效检测 contamination，但不能直接用于 aggregate score correction。

**对论文的建议**：分离 detection 和 correction——gamma 用于 contamination detection（有效），score correction 仅声称适用于 accuracy-sensitive benchmarks（如 HumanEval）。报告已保存为 `art_20260515_6a06dc`。

---
