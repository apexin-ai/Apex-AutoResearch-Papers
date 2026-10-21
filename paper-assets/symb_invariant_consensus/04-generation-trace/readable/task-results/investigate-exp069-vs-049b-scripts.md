# investigate exp069 vs 049b scripts

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_exp069-vs-049b-scripts_20260519T135700_result.json`
- **Structured JSON:** [`eb6fe7d7ce2fc238254b.json`](../../sessions/eb/eb6fe7d7ce2fc238254b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM 已清理。以下是完整调查结果：

```json
{
  "exp049b_script": "run_full_mvp.py --strategyqa-data data/logiqa_200.json (但数据自带 dataset=logiqa，setdefault 不覆盖，正确路由到 multichoice+logic domain)",
  "exp069_script": "run_logiqa.py --data data/logiqa_200.json (显式设 generator.domain=multichoice, extractor.domain=logic)",
  "prompt_template_diff": "相同。两者都用 MULTICHOICE_SOLVE_PROMPT 和 LOGIC_EXTRACTION_PROMPT",
  "extraction_logic_diff": "trace_generator.py 有差异：exp-049b 新增 strip_thinking() + 双重 boxed 提取 fallback；exp-069 无。对 Mistral 无 &lt;think> 输出应无影响",
  "sica_logic_diff": "5/7 SICA 核心模块代码不同（trace_generator/constraint_extractor/pipeline/scorer/z3_maxsat），仅 self_consistency.py 和 math_equiv.py 一致。关键差异：scorer.py select_answer 的 tie-breaking 逻辑——exp-049b 用 max() 随机破平，exp-069 用 sorted() 字母序破平",
  "vllm_version_16639": "0.21.0",
  "vllm_version_25068": "0.21.0",
  "root_cause_hypothesis": "两次实验使用不同版本的 SICA 核心代码（5个模块 md5 全部不同），加上 exp-049b 设了 VLLM_USE_FLASHINFER_SAMPLER=0 而 exp-069 未设。SC 差 1.5pp 属正常采样方差；SICA delta 从 +0.50 → -3.00pp 主要由代码版本差异驱动（constraint_extractor、z3_maxsat、scorer 的演化），采样差异是次要因素",
  "vllm_cleanup": "killed PID 211125 (Mistral-7B on port 8001, cuda:1)。exp-062 (port 8003) 和 exp-065 (port 8010) 保留",
  "recommendation": "两组数据不可直接比较。如需对比 SICA 改进效果，应在同一代码版本+同一服务器上重跑。建议以 westd-25068 当前代码为准（更新版本），在 westd-25068 上用 run_logiqa.py 重跑一次作为 baseline"
}
```

**md5 对比详情：**

| 模块 | westd-16639 | westd-25068 |
|------|-------------|-------------|
| trace_generator.py | `38f914a3` | `67a7c3a1` |
| constraint_extractor.py | `8e3bea73` | `5b749002` |
| pipeline.py | `9543ea12` | `fc2cb0ad` |
| scorer.py | `6abef7f7` | `7a1262eb` |
| z3_maxsat.py | `6f7bf708` | `2cf9a195` |
| self_consistency.py | `8b4e26fc` | `8b4e26fc` |
| math_equiv.py | `a5ee55ef` | `a5ee55ef` |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exp049b_script": "run_full_mvp.py --strategyqa-data data/logiqa_200.json (但数据自带 dataset=logiqa，setdefault 不覆盖，正确路由到 multichoice+logic domain)",
    "exp069_script": "run_logiqa.py --data data/logiqa_200.json (显式设 generator.domain=multichoice, extractor.domain=logic)",
    "prompt_template_diff": "相同。两者都用 MULTICHOICE_SOLVE_PROMPT 和 LOGIC_EXTRACTION_PROMPT",
    "extraction_logic_diff": "trace_generator.py 有差异：exp-049b 新增 strip_thinking() + 双重 boxed 提取 fallback；exp-069 无。对 Mistral 无 &lt;think> 输出应无影响",
    "sica_logic_diff": "5/7 SICA 核心模块代码不同（trace_generator/constraint_extractor/pipeline/scorer/z3_maxsat），仅 self_consistency.py 和 math_equiv.py 一致。关键差异：scorer.py select_answer 的 tie-breaking 逻辑——exp-049b 用 max() 随机破平，exp-069 用 sorted() 字母序破平",
    "vllm_version_16639": "0.21.0",
    "vllm_version_25068": "0.21.0",
    "root_cause_hypothesis": "两次实验使用不同版本的 SICA 核心代码（5个模块 md5 全部不同），加上 exp-049b 设了 VLLM_USE_FLASHINFER_SAMPLER=0 而 exp-069 未设。SC 差 1.5pp 属正常采样方差；SICA delta 从 +0.50 → -3.00pp 主要由代码版本差异驱动（constraint_extractor、z3_maxsat、scorer 的演化），采样差异是次要因素",
    "vllm_cleanup": "killed PID 211125 (Mistral-7B on port 8001, cuda:1)。exp-062 (port 8003) 和 exp-065 (port 8010) 保留",
    "recommendation": "两组数据不可直接比较。如需对比 SICA 改进效果，应在同一代码版本+同一服务器上重跑。建议以 westd-25068 当前代码为准（更新版本），在 westd-25068 上用 run_logiqa.py 重跑一次作为 baseline"
  }
}
```

</details>

---
