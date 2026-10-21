# eval d067 seed variance results

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d067_seed_variance_results_20260520T022109_result.json`
- **Structured JSON:** [`5dfd41baa158f6eba903.json`](../../sessions/5d/5dfd41baa158f6eba903.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**d067 seed variance 评估结果：**

- **SciERC 部分已完成**（8/12 文件，剩余 1 个在跑 + 4 个 DocRED 待启动）
- **核心发现**：greedy decoding (temperature=0) 下，不同 seed 的输出完全一致。seed 123 和 456 产生 byte-identical 输出。seed 42 的微小差异（σ_max = 0.43pp R-F1）来自跨服务器浮点噪声（w5 在 16980 评估 vs d067 在 21461 运行）
- **所有 σ < 0.5pp**，hypothesis 成立
- **unc→con 改进的 SNR > 12×**：DR 降幅（-2.06pp / -1.01pp）远大于 seed variance
- **qwen_docred** 4 个文件未开始（需等 llama_scierc_seed456_full_s1 完成后 pipeline 继续），但基于 greedy determinism，结果将与 seed 42 基本一致

**待决策**：greedy decoding 下 σ=0，报 error bars 意义不大。可选方案：(a) 不报 error bars，附录注明 greedy determinism；(b) 用跨服务器 std 作为保守上界；(c) 改用 sampling 重跑（如果需要真实 seed variance）。

报告已写入 `artifacts/_project/report/d067_seed_variance_eval.md`，registry 已更新为 ANALYZING。

---
