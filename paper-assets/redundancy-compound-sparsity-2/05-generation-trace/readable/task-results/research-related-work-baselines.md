# research related work baselines

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_baselines_20260512T124638_result.json`
- **Structured JSON:** [`7eaeb39b20738947aea3.json`](../../sessions/7e/7eaeb39b20738947aea3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成，已写入并注册 `related_work_survey.md`（artifact ID: `art_20260512_d34086`）。

**核心发现：**

**Part 1 — 13 个方法已分类记录**，覆盖 4 大 signal type 家族：
- Attention-score 类（H2O, Scissorhands, FastGen, R-KV, SkipKV, LazyEviction, LongFlow）
- Positional 类（StreamingLLM）
- Similarity/Geometric 类（KeyDiff, TriAttention, **CARC**）
- Learned 类（EvolKV）

**CARC 定位**：O(1) EMA centroid similarity 在 signal taxonomy 中是独特的——唯一同时满足 O(1) 复杂度 + 内容感知 + 冗余检测的方法。

**Part 2 — Baseline 代码可用性：**

| Baseline | 可用性 | Qwen2 支持 | 集成难度 | 优先级 |
|---|---|---|---|---|
| **R-KV** | 有 repo，直接支持 DeepSeek-R1-Distill | Yes | Easy | CRITICAL |
| **H2O** | 有 repo + kvpress 集成 | 需适配 GQA | Medium | HIGH |
| **StreamingLLM** | 有 repo，7.2k stars | 应该兼容 | Easy | HIGH |
| **kvpress** | pip install，NVIDIA 维护 | 显式支持 Qwen2 | Easy | HIGH（含 KeyDiff/SnapKV/TOVA 等多个 baseline） |
| **TriAttention** | 有 repo + vLLM 插件 | 需确认 | Medium | Nice-to-have |

**建议**：优先通过 R-KV 官方 repo + kvpress 框架覆盖大部分 baseline 对比。考虑将 CARC 实现为 kvpress press 以便统一评测。

---
