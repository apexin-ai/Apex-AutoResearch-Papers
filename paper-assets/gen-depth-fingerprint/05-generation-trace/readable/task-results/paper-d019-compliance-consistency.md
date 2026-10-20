# paper d019 compliance consistency

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d019-compliance-consistency_20260515T165650_result.json`
- **Structured JSON:** [`9d3580dc2526af5f181a.json`](../../sessions/9d/9d3580dc2526af5f181a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete. Here's the full report:

---

## 任务 A: D019 合规检查

**结果: 全部通过 ✓**

检查了 7 个论文文件中所有涉及 instruct 的段落（共 5 处）：

| 文件 | 行 | 内容 | 合规 |
|------|-----|------|------|
| introduction.tex | 20 | "base (pretrained) models; instruction-tuned and RLHF models...remain untested (Limitations)" | ✓ scope 限定 |
| limitations.tex | 5-6 | "All six generators are base (pretrained) models...instruction tuning is a critical direction for future work" | ✓ limitation |
| limitations.tex | 13 | "instruction following" 作为未测试的 prompt type | ✓ limitation |
| limitations.tex | 23 | "instruction following" 作为未测试的下游任务 | ✓ limitation |
| conclusion.tex | 9 | "extend evaluation to instruction-tuned and RLHF models" | ✓ future work |

- "inverted DDR" / "方向反转" 相关表述：**零残留** ✓
- 主要 claims（abstract/intro/results/conclusion）均限定为 base model ✓

---

## 任务 B: 全文数字一致性验证

| 数字 | Registry | 论文 | 状态 |
|------|----------|------|------|
| Binary LOGO F1 | 0.723 | 0.723 | ✓ |
| Binary CI | [0.717, 0.729] | [0.717, 0.729] | ✓ |
| 3-class LOGO F1 | 0.789 | 0.789 | ✓ |
| 6 generators, 3 families, 0.6B–8.2B | — | — | ✓ |
| Per-gen: Pythia-1B | 0.8562 → 0.856 | 0.856 | ✓ |
| Per-gen: Pythia-2.8B | 0.8041 → 0.804 | 0.804 | ✓ |
| Per-gen: OLMo-2-1B | 0.7635 → 0.764 | 0.764 | ✓ |
| Per-gen: Qwen3-0.6B | 0.8243 → 0.824 | 0.824 | ✓ |
| **Per-gen: Qwen3-1.7B** | **0.8064 → 0.806** | **0.805 → 已修复为 0.806** | **已修复** |
| Per-gen: Qwen3-8B | 0.6832 → 0.683 | 0.683 | ✓ |
| Per-gen std | 0.051 | 0.051 | ✓ |
| 4-baseline ensemble (3-class) | 0.796 | 0.796 | ✓ |
| 4-baseline ensemble (binary) | 0.712 | 0.712 | ✓ |
| 4-baseline+surface | 0.805 | 0.805 | ✓ |
| 7-feature unified (3-class) | 0.789 | 0.789 | ✓ |
| CORAL (3-class) | 0.771 | 0.771 | ✓ |
| Frank-Hall (3-class) | 0.793 | 0.793 | ✓ |
| Concordance: XGBoost | 0.821 | 0.821 | ✓ |
| Concordance: CORAL | 0.810 | 0.810 | ✓ |
| Concordance: Frank-Hall | 0.825 | 0.825 | ✓ |
| Volume-matched diversity | 94% | 94% | ✓ |
| LOPTO avg F1 | 0.7525 → 0.753 | 0.753 | ✓ |
| Prompt type CV (continuation) | 0.781 → 0.78 | 0.78 | ✓ (2dp) |
| Prompt type CV (rewriting) | 0.737 → 0.74 | 0.74 | ✓ (2dp) |
| Prompt type CV (elaboration) | 0.730 → 0.73 | 0.73 | ✓ (2dp) |
| Baseline diffs (+1.1/+2.2/+10.7/+19.9pp) | — | — | ✓ (算术验证) |

### 修改的文件

| 文件 | 变更 |
|------|------|
| `artifacts/_project/paper/results.tex` | Table 1: Qwen3-1.7B 0.805 → 0.806 |
| `artifacts/_project/paper/appendix_classifier.tex` | XGBoost 行: Qw-1.7B 0.805 → 0.806 |
| `docs/paper/results.tex` | 同步: Qwen3-1.7B 0.805 → 0.806 |
| `docs/paper/table1.tex` | 同步: Qwen3-1.7B 0.805 → 0.806 |
| `docs/paper/appendix_classifier.tex` | 同步: XGBoost 行 0.805 → 0.806 |

唯一的数字不一致是 Qwen3-1.7B held-out F1（registry 0.8064 应四舍五入为 0.806，论文误写为 0.805），已在全部 5 个文件中修正。

---
