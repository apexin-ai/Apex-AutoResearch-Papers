# exp d4 depth extension olmo

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_d4_depth_extension_olmo_20260518T190341_result.json`
- **Structured JSON:** [`4c6548070c09bf99ea52.json`](../../sessions/4c/4c6548070c09bf99ea52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，56.6 秒。产出文件齐全：

| 文件 | 说明 |
|------|------|
| `depth_4.jsonl` | 5000 条 d4 文本 |
| `features_d4.jsonl` | 5000 条 d4 特征 |
| `d4_extension_results.json` | 评估结果 |

**OLMo-1B 结果汇总**：

| 指标 | OLMo-1B | Pythia-1.4B | GPT-2 XL |
|------|---------|-------------|----------|
| d3v4 AUC | **0.9747** | 0.7887 | 0.7273 |
| 5-class RF acc | **0.8053** | 0.7133 | 0.7403 |
| d4 recall | **0.9014** | 0.6814 | 0.6386 |

**Pairwise AUC chain**: d0v1=0.983, d1v2=0.866, d2v3=0.801, d3v4=0.975

**Feature trends** (p90_ppl 单调递减 ✓): d0=483.7 → d1=136.1 → d2=66.5 → d3=42.7 → d4=28.2

注意 d3v4 AUC=0.9747 远高于其他模型，说明 OLMo-1B 的 d4 generation 在 Pythia ref 下与 d3 分离度很高。var_surprisal 在 d4 出现反弹（2.49→2.83），mean_ppl 非单调。

---
