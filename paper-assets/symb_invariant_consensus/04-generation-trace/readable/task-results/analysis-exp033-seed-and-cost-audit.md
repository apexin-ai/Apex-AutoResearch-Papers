# analysis exp033 seed and cost audit

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp033-seed-and-cost-audit_20260520T111429_result.json`
- **Structured JSON:** [`cda2be79f6b8eef44bf3.json`](../../sessions/cd/cda2be79f6b8eef44bf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，以下是结果。

---

## 任务 1: exp033 seed 验证

### 确认：exp033 运行时 seed=None

证据：
- `run_full_mvp.py:213` — `--seed` 参数 `default=None`
- exp033 日志首行：`SICA Full MVP | mode=vllm k=12 resume=False temperature=0.70 max_tokens=4096` — **未记录 seed**
- `grep -i "seed"` 在 exp033.log 中**零匹配**
- exp033_results.json summary 中**无 seed 字段**
- 代码逻辑 (L219-221)：仅当 `args.seed is not None` 时才调用 `random.seed()`，且**只影响 Python random 模块，不影响 vLLM 采样**

### SC=54.41% 的 seed 匹配

| 实验 | Seed | SC Acc | 匹配 exp033? |
|------|------|--------|-------------|
| exp033 (SICA) | **None** | **54.41%** (111/204) | — |
| exp067 (SICA, seed=789) | 789 | **54.41%** (111/204) | **精确匹配** |
| exp074 (ICG, seed=42) | 42 | 53.92% | ✗ |
| exp074c (ICG, seed=123) | 123 | 57.35% | ✗ |
| exp074d (ICG, seed=456) | 456 | 55.88% | ✗ |
| exp075b (contrastive, seed=42) | 42 | 56.86% | ✗ |

**结论**：exp033 的 SC=54.41% 仅与 **seed=789** (exp067) 精确匹配。Reviewer 提到的 "seed=123" 对应 SC=57.35%（不匹配），"seed=42 的 55.88%" 实际是 seed=456 的结果。

注意：`random.seed()` 仅控制 Python 内部随机数（如问题排序），vLLM 在 temperature=0.7 下始终非确定性采样。exp033 与 exp067 的匹配（同为 111/204 正确）可能是巧合。

---

## 任务 2: 计算成本数据

### exp033 SICA vs SC Wall-Time (Mistral-7B, FOLIO-204, k=12)

| 指标 | SC (trace only) | SICA (full pipeline) |
|------|-----------------|---------------------|
| Total wall time | ~17.7 min | 81.4 min |
| Per-question avg | 5.2s | 23.6s |
| Per-question range | 1.7–10.8s | 2.4–40.9s |
| **SICA / SC ratio** | — | **4.5x** |

### 分阶段耗时 (per-question avg, 171/204 samples)

| Stage | Time | % of Total | 归属 |
|-------|------|-----------|------|
| 1. Trace generation | 5.2s | 22% | SC + SICA 共享 |
| 2. Constraint extraction | 17.8s | 76% | SICA 独有 |
| 3. Dedup | ~0.5s | ~2% | SICA 独有 |
| 4. MaxSAT solving | ~3ms | <0.1% | SICA 独有 |

### 方法间总 wall-time 对比 (Mistral-7B, FOLIO-204)

| 方法 | Seed | Wall Time | 相对 SC |
|------|------|-----------|--------|
| SC baseline (估算) | — | ~17.7 min | 1.0x |
| **SICA** (exp033) | None | 81.4 min | 4.5x |
| ICG (exp074) | 42 | 56.1 min | 3.2x |
| Debate (exp076) | 42 | 186.4 min | 10.5x |
| Contrastive (exp075b) | 42 | 193.6 min | 10.9x |

**核心结论**：SICA 的额外成本主要来自 constraint extraction (LLM 调用)，占 SICA 独有开销的 ~96%。MaxSAT 求解可忽略不计 (~3ms)。与 Debate/Contrastive 相比，SICA 的计算开销显著更低。

---
