# analysis error analysis s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error-analysis-s42_20260519T192541_result.json`
- **Structured JSON:** [`a81fb154b561061c8eaf.json`](../../sessions/a8/a81fb154b561061c8eaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。输出文件：

| 文件 | 大小 |
|------|------|
| `error_analysis.py` | 30,629 B |
| `error_analysis_results.json` | 25,720 B |
| `forgetting_by_domain.csv` | 1,563 B |
| `knowledge_gain_by_domain.csv` | 1,541 B |
| `persistent_errors.csv` | 46,437 B |
| `error_analysis_figures.pdf` | 37,579 B |

**关键发现**（§4 Analysis 素材）：

**Forgetting (d000→d100)**:
- **Qwen2.5-0.5B 崩溃最严重**: MMLU forgot=3542 (25.2%), gained=1232, net=−2310。ARC 也是 net=−205。整体严重退化。
- **Qwen2.5-1.5B 基本平衡**: MMLU forgot=637, gained=749, net=+112。但 GSM8K 和 ARC 略负。
- **Qwen2.5-3B 分化**: MMLU net=+81（轻微增益），但 GSM8K net=+742（巨大增益，从 24→766 gained，可能因 SFT 数据含 math 相关内容）。
- **Qwen2.5-7B / Llama-3.2-3B**: d000 缺 MMLU 数据，只有 ARC 可比（均 net≈−3，几乎免疫）。

**Persistent Errors** (所有 family × 所有 dosage 都错):
- MMLU: 1097 items（7.8%），genuinely hard items
- HumanEval: 72/164（43.9%），代码题天花板
- GSM8K: 107/1319（8.1%）
- ARC: 23/1172（2.0%）

**Cross-model Agreement (d100)**:
- MMLU unanimous forgetting 仅 21 items — 绝大多数 forgetting 是 model-specific（unique_forgot=4083）
- 这说明 contamination 的 forgetting 效应高度依赖模型架构/容量，不是 item-level difficulty 变化

**MMLU 领域分布**: 0.5B 的 forgetting 集中在 Humanities（1075）> Social Sciences（1015）> Other（869）> STEM（583），与 domain 大小大致成比例。top subjects: professional_law (305), miscellaneous (261), high_school_psychology (241)。

**注意**: Qwen2.5-7B d000 和 Llama-3.2-3B d000 的 MMLU eval 缺失，导致这两个 family 的 MMLU forgetting/gain 分析不可用。如需完整分析，需补跑这两个 d000 的 MMLU eval。

---
