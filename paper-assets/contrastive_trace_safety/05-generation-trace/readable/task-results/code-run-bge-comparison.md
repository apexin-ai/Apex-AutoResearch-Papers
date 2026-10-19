# code run bge comparison

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_run_bge_comparison_20260518T003108_result.json`
- **Structured JSON:** [`2f02ee52e1950ab5f17e.json`](../../sessions/2f/2f02ee52e1950ab5f17e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，无报错。结果已保存到 `artifacts/bge_large_comparison.json`。

---

## 实验结果：BGE-large (1024d) vs Hidden States

| Model | HS Precision | BGE-text Precision | Diff (HS - BGE) | 95% CI | p-value | HB-sig |
|-------|-------------|-------------------|-----------------|--------|---------|--------|
| r1_8b | 0.4971 | 0.4358 | +0.0582 | [-0.0774, 0.1939] | 0.185 | No |
| ot_7b | 0.4460 | 0.2629 | **+0.1809** | [0.0809, 0.2882] | 0.000 | **Yes** |
| r1_32b | 0.5882 | 0.4750 | +0.1171 | [-0.0015, 0.2430] | 0.027 | No |
| qwq_32b | 0.5455 | 0.4540 | +0.0944 | [-0.0654, 0.2691] | 0.132 | No |

### Holm-Bonferroni 校正结果 (α=0.05, 4 tests)

仅 **ot_7b** 通过 HB 校正（p≈0.000）。r1_32b 的 raw p=0.027 未通过校正（校正阈值 0.05/3=0.0167）。

### 与 MiniLM 384d 对比

BGE-large (1024d) 作为更强的 text baseline，缩小了差距但未消除：
- ot_7b 仍然显著（+0.18），是最稳健的模型
- r1_32b 的 CI 下界几乎触及 0（-0.0015），从之前 MiniLM 的显著变为边缘不显著
- r1_8b 和 qwq_32b 在更强 encoder 下差异不再可观测

**结论**：即使使用 3 倍维度的 BGE-large encoder，HS 在 ot_7b 上仍保持统计显著优势。对 r1_32b 优势接近边缘显著。这强化了 hidden states 提供 text surface 之外信息的 claim，但效应量确实因更强 text encoder 而收窄。

---
