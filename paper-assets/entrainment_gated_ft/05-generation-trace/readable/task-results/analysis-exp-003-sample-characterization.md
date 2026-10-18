# analysis exp 003 sample characterization

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_003_sample_characterization_20260519T131141_result.json`
- **Structured JSON:** [`127bbab14cd881d19f40.json`](../../sessions/12/127bbab14cd881d19f40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Helped/Hurt 统计（h3-1 hybrid vs pure）：**

| 架构 | Helped | Hurt | Both Correct | Both Wrong |
|------|--------|------|-------------|------------|
| GDN | 462 | 615 | 2183 | 1893 |
| HGRN2 | 548 | 395 | 2100 | 2110 |
| RetNet | 426 | 495 | 2167 | 2065 |

HGRN2 是唯一 helped > hurt 的架构（净正效果）；GDN 和 RetNet 的 attention 层反而 hurt 更多。

**统计检验关键发现：**
- **GDN、HGRN2**：helped vs hurt 在所有特征上均无显著差异（p > 0.2）
- **RetNet**：helped 样本的 context_length 显著更长（p=0.012, r=-0.096）且 context_unique_tokens 显著更多（p=0.009, r=-0.099）——attention 更倾向帮助长上下文、高词汇多样性的样本
- **跨架构比较**：三个架构的 helped 样本特征分布之间无显著差异

**输出文件（westb-48145）：**
- `analysis/sample_characterization.py`（脚本）
- `analysis/sample_characterization_results.csv`（统计表）
- `analysis/sample_characterization.pdf` + `.png`（6-panel violin plot）

---
