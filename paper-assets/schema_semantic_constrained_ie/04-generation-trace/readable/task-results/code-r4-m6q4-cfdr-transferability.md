# code r4 m6q4 cfdr transferability

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r4_m6q4_cfdr_transferability_20260517T110043_result.json`
- **Structured JSON:** [`4a6d252b37e1bbec5c50.json`](../../sessions/4a/4a6d252b37e1bbec5c50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入 `artifacts/r4_m6q4_cfdr_transferability.md` 并注册。

核心结论：

1. **6 个 ZS setting 全部展现 DR↔CF 逆相关**（Spearman ρ = −0.77）。每个 dataset 内，DR 最高的 model（Mistral）CF 最低，DR 最低的 model CF 最高，无例外。

2. **机制是架构层面的**：每个 type-bearing position 面临二选一——semantic mask 生效则可能产生 CF（registry override），grammar-first fallback 则可能产生 DR。模型校准度决定两者的相对频率，但二选一结构不依赖具体 model/dataset。

3. **SciERC/Qwen 是最佳 ablation 设置**：CF 最高（9.90%）使 trade-off 最可见；Qwen 是 primary model；ablation 修改的两个 code path 对所有配置执行逻辑相同。

4. **建议论文文本提供了三个选项**：appendix 脚注（2 句）、展开段落（适合有空间时）、rebuttal-only 回复文本。推荐 Option A（脚注）加入现有 CF-DR Trade-off Analysis 段落末尾。

---
