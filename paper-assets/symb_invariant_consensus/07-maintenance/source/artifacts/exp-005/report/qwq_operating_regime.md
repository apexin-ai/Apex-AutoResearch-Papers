## QwQ-32B Operating Regime Analysis

**Experiment**: exp-005 | **Date**: 2026-05-16 | **Model**: QwQ-32B (reasoning model)

### Summary Table

| Dataset | Domain | N | K | T | C0 (nominal) | C0 (effective†) | SICA acc | SC acc | Δ (pp) | Verdict |
|---------|--------|---|---|---|---------------|-----------------|----------|--------|--------|---------|
| AIME 2024 | Math | 22/30‡ | 12 | 0.7 | 0.0% (0/22) | 0.0% | 72.7% | 72.7% | 0.0 | SICA≡SC |
| ProofWriter D5 | Logic | 17/30‡ | 12 | 0.7 | 23.5% (4/17) | 5.9% (1/17) | 82.4% | 88.2% | **−5.9** | **SICA<SC** |
| FOLIO (live test) | Logic | 2/30‡ | 4 | 0.7 | 0.0% (0/2) | 0.0% | 100% | 100% | 0.0 | SICA≡SC§ |
| MATH L4-5 (temp) | Math | 5 | 12 | 0.7/0.9/1.0 | 0.0% (0/5) | 0.0% | — | — | — | No divergence |
| **Combined (main)** | | **39** | **12** | **0.7** | **10.3% (4/39)** | **2.6% (1/39)** | | | | **C0 ≪ 20%** |

†Effective C0 = problems with both multiple candidates AND successful constraint extraction
‡Experiments killed before completion (see notes)
§N=2, K=4: insufficient for meaningful analysis

### ProofWriter Multi-Candidate Detail

| Problem | Ground Truth | SC Vote Distribution | Constraints | SICA | SC | SICA✓ | SC✓ |
|---------|-------------|---------------------|-------------|------|-----|-------|-----|
| 616_Q7 | True | False:7, True:5 | **0** extracted | False | False | ✗ | ✗ |
| 498_Q8 | False | False:11, True:1 | 41 (4 traces) | **True** | False | **✗** | **✓** |
| 251_Q10 | False | Unknown:3, False:7, True:2 | **0** extracted | False | False | ✓ | ✓ |
| 31_Q12 | False | False:4, Unknown:8 | **0** extracted | Unknown | Unknown | ✗ | ✗ |

**Critical finding on 498_Q8**: SICA scored minority answer True=38 > majority False=27, flipping SC's correct answer to wrong. Root cause: QwQ-32B re-reasons during constraint extraction instead of outputting structured JSON, producing biased constraints from 4/12 traces only.

### Temperature Diversity Analysis

| Problem | Level | T=0.7 | T=0.9 | T=1.0 | Divergence |
|---------|-------|-------|-------|-------|------------|
| algebra/2277 | 5 | 10/12→"0" | 9/12→"0" | 9/12→"0" | 0% |
| int_algebra/582 | 5 | 0/12 (truncated) | 0/12 (truncated) | 0/12 (truncated) | N/A |
| number_theory/427 | 5 | 12/12→"25" | 12/12→"25" | 12/12→"25" | 0% |
| precalculus/1199 | 4 | 2/12→"π" | 2/12→"π" | 3/12→"π" | 0% |
| precalculus/659 | 4 | 11/12→same | 10/12→same | 11/12→same | 0% |

Even at T=1.0, QwQ-32B produces zero answer divergence. Truncation (max_tokens=4096) affected 2 problems but did not introduce diversity—just failures.

### Key Finding

QwQ-32B 作为 reasoning model，其 chain-of-thought 的确定性极高：

1. **数学域 C0=0%**：K=12 条 trace 在 AIME 2024 的全部 22 题上产生完全一致的最终答案，即使 T 从 0.7 提升至 1.0 也无分歧
2. **逻辑域名义 C0=23.5%，但有效 C0=5.9%**：ProofWriter 4/17 题有多候选，但 3/4 约束提取完全失败（0 constraints），唯一有约束的题 SICA 反而选错
3. **综合有效 C0=2.6%**，远低于 SICA 有效阈值（≥20%）

**结论**：SICA 的效用与模型的 trace diversity (C0) 正相关。Reasoning model 的自一致性使 SICA 退化为 SC（数学域），甚至劣于 SC（逻辑域，因约束提取偏差）。这验证了论文的 Operating Regime 预测，并支持了从 QwQ-32B pivot 到 Qwen2.5-14B-Instruct（C0=46%）的决策。

### Data Sources

| Experiment | Registry ID | Result File | Status |
|-----------|-------------|-------------|--------|
| AIME 2024 | sica_aime30_v3 | results/aime30_v2.json | killed at 22/30 |
| ProofWriter D5 | sica_proofwriter30_v2 | results/proofwriter_30_v2.json | killed at 17/30 |
| FOLIO live test | sica_folio30 | results/folio_livetest.json | 2-problem test only |
| Temp diversity | sica_temp_diversity | results/diversity_diagnosis.json | completed (negative) |