# ops scp backup tarballs

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scp_backup_tarballs_20260523T201149_result.json`
- **Structured JSON:** [`b903f8e576f61151b210.json`](../../sessions/b9/b903f8e576f61151b210.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 下载验证结果

### 文件清单与 MD5

| 文件 | 大小 | 服务器 MD5 | 本地 MD5 | 一致 |
|------|------|-----------|---------|------|
| `nlp_vg_full_backup.tar.gz` | 476M | `48f92bfe44a3b56c48c908eb0c8100ab` | `48f92bfe44a3b56c48c908eb0c8100ab` | **Yes** |
| `backup_jsons.tar.gz` | 194K | `ec2bdd7d881b54b2232786fec165ae73` | `ec2bdd7d881b54b2232786fec165ae73` | **Yes** |

### tar 包内容概要

**nlp_vg_full_backup.tar.gz**（563 个条目）：
- `data/` — 实验数据（MMLU/GSM8K/ARC/HellaSwag/MATH items, few-shot examples, exp_llama70b 设计矩阵）
- `results/` — 全部实验结果（exp001 各模型 shards, exp002-004, analysis JSON, figures）
- `scripts/` — 实验脚本
- `src/` — 源代码
- `tests/` — 测试代码
- `artifacts/` — 分析产出
- `figures/` — 图表

**backup_jsons.tar.gz**（77 个条目）：
- `results/` — 分析 JSON 文件（G-study, D-study, bootstrap, IRT, simulation 等关键分析结果）

### 结论

- 下载成功，MD5 完全一致
- 两个 tar 包涵盖了完整的实验数据、代码、分析结果和论文图表
- **westd-32570 可以标记为 C 类释放**——所有关键产出已备份到本地

---
