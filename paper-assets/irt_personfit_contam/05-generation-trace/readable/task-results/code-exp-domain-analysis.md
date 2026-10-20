# code exp domain analysis

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-domain-analysis_20260520T130459_result.json`
- **Structured JSON:** [`c79873744f8fd27dabed.json`](../../sessions/c7/c79873744f8fd27dabed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

## 关键结果

**Gemini-1.5**: MMLU **100% accuracy (14042/14042)**，覆盖全部57个subjects，异常是**全面性的而非domain-concentrated**。所有subject的lz*均为正值（50/57 > 1.96），最高的是miscellaneous (12.4)、elementary_mathematics (11.8)、high_school_psychology (10.1)。Category-level lz*: STEM=21.2, Humanities=17.9, Social Sciences=15.9, Other=15.3。

**Hypothesis 被否定**: Gemini-1.5的异常均匀分布在所有domain，不存在domain集中现象。这更像是完整的MMLU测试集泄露，而非特定domain的训练数据污染。

**其他模型的domain-specific patterns**:
- **Yi-Lightning** (lz*=48.2) 和 **Qwen-Plus** (lz*=44.9) 是MMLU上lz*最高的两个模型，在Social Sciences (28.5/27.1) 和 STEM (26.8/24.4) 尤为显著
- **Doubao-pro** 是唯一整体lz*为负的模型 (−14.6)，在Humanities (−13.0) 和 Social Sciences (−14.8) 表现远低于IRT预期，但在Other (+4.4) 和部分STEM科目正常——呈现反向的domain-specific pattern
- **Hunyuan-Turbo** 显示不均匀pattern: STEM仅1.8但Social Sciences高达13.9，暗示特定domain的contamination
- **Mistral-7B** (θ=−1.37, acc=53.3%) lz*高达32.9，55/57 subjects被flag，说明即使低能力模型也在MMLU上表现出系统性超预期

所有产出已保存至 `artifacts/domain_analysis/`。

---
