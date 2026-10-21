# analysis d037 figure data audit

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d037_figure_data_audit_20260516T040010_result.json`
- **Structured JSON:** [`acb459f8176da765966a.json`](../../sessions/ac/acb459f8176da765966a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计结果：

### Task 1: Figure 1a 用的是 micro recall (pooled)
- 数据**硬编码**在 `gen_fig_count_curves.py` 里，不读任何外部文件
- count_22=0.527, count_44=0.551，与 round2 JSON 的 `pooled_recall`（0.5268, 0.5512）吻合
- 排除 macro recall（batch mean 是 0.5222, 0.5491）

### Task 2: round2_statistical_analyses.json 已获取
- 路径：`/root/schema-dag-extraction/artifacts/round2_statistical_analyses.json`
- Cluster bootstrap CI 均显著：FewNERD r=0.137 CI [0.069, 0.219], MAVEN r=0.129 CI [0.081, 0.185]
- W4 count_22/44 的 pooled CI 重叠，delta=0.024 不显著

### Task 3: Practical Magnitude 差异根源
存在**两个不同的数据源**，slope 相同（-0.401）但 BCS 分布不同：

| 来源 | BCS IQR | Gap (pp) | Q1 → Q3 |
|------|---------|----------|----------|
| 本地 W2 JSON (100 batches) | 0.0539 | 2.16 | 0.528 → 0.582 |
| 服务器 round2 JSON `80pool_16sub` | 0.0655 | 2.63 | 0.504 → 0.569 |
| 论文当前文字 | ~0.054 | ~2.2 | (rounded from 本地 W2) |

**根因**：两次运行产生了不同的 100-batch BCS 分布（不同随机种子或采样策略），导致 IQR 差异 0.012、gap 差异 0.47pp。论文当前数字是本地 W2 的四舍五入。需确认哪个运行是权威版本。

输出已写入 `figure_data_audit.json`。

---
