# paper write abstract discussion

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_write-abstract-discussion_20260522T153557_result.json`
- **Structured JSON:** [`cb96fc772f31dad8ce2f.json`](../../sessions/cb/cb96fc772f31dad8ce2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入：

**Abstract** (~200 词)
- 结构：现象（跨语言冲突内部机制未知）→ 方法（残差流探针 + 跨语言迁移 + steering）→ 三个核心发现（检测 75-77%、不对称性继承通用跨语言属性、Detection ≠ Decision）→ 结论
- Steering 结果限定为 "in Llama"，未过度泛化
- 未使用 "consistently"

**Discussion** (5 段)
1. **Detection ≠ Decision** — L13 因果 vs L28 检测峰值，连接 mid-layer 跨语言对齐文献，引用 Basu 方法论警告
2. **不对称性是通用属性** — XNLI 对照数据（+6.0/+6.7 pp vs +7.2/+7.2 pp），CI 重叠，连接 Wendler & Kargaran
3. **非线性作为 observation** — MLP gains 方向对但 CI 含零，用 "directional trend" 定性
4. **Steering 的 model-specificity** — Llama 成功 Qwen 失败，框架为 "mechanistic results 跨架构迁移性本身是有意义的发现"
5. **Broader implications** — 连接 CLEAR，方法论贡献（confound pipeline），detection-decision dissociation 的实践意义

---
