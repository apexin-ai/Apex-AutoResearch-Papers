# paper writing abstract

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_abstract_20260515T044821_result.json`
- **Structured JSON:** [`3c0644029c2cfc9b20ea.json`](../../sessions/3c/3c0644029c2cfc9b20ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Abstract 已写入 `artifacts/_project/paper/abstract.tex` 并注册。

结构遵循 Farquhar 五句法：
1. **问题**：web 语料中递归生成文本的深度未知
2. **难点**：现有检测器仅提供二分类，跨生成器方差大（CI 0.41–0.82）
3. **方法**：differential depth response — 中心趋势/多样性特征漂移 + 形状特征稳态 → 7 特征互补集成
4. **证据**：6-gen LOGO F1=0.79 [0.786, 0.799]，p<0.001；per-generator 0.68–0.86
5. **负面结果**：depth-aware curation 不优于随机抽样，depth fingerprinting 是诊断工具而非治疗工具

所有数字均从 registry 核实：plan-014（6-gen LOGO 0.7893）、plan-015-v2（CI/p值）、plan-004-v2（downstream ppl）、plan-002-eval（ablation 0.80/0.75/0.75）。

---
