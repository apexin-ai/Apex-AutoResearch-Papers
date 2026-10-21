# code r18 base vs instruct dif

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r18_base_vs_instruct_dif_20260522T174522_result.json`
- **Structured JSON:** [`fed763012071b8ef280c.json`](../../sessions/fe/fed763012071b8ef280c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。三个产出文件均已生成。

**核心发现：**

| 指标 | Base | Instruct |
|------|------|----------|
| 样本量 | 861+548=1409 | 219+259=478 |
| C% | 32.1% | 36.5% |
| ρ(difficulty, Δ_MH) | **−0.570** | −0.079 |
| DIF 方向 | 60.1% ref-favoring | 65.6% focal-favoring |

关键解读：
1. **C% 差异不显著**（−4.4 pp, 95% CI [−13.4, 4.3] 包含 0），instruct 稍高但 bootstrap CI 宽
2. **Difficulty gradient 差异极大**：base 组 ρ=−0.57（容易题 DIF 大），instruct 组几乎无梯度（ρ=−0.08）——说明 base 和 instruct 的 DIF 机制不同
3. **方向完全相反**：base 组以 ref-favoring（2023↑）为主，instruct 组以 focal-favoring（2024↑）为主，χ²=562.7, p<10⁻¹²⁴
4. **Overlap 中等** (Jaccard=0.314, 1.5× 独立基线)：约一半 DIF items 是 group-specific 的

---
