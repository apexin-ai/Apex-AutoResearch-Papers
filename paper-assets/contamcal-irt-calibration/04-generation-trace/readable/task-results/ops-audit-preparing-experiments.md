# ops audit preparing experiments

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_preparing_experiments_20260516T233623_result.json`
- **Structured JSON:** [`1f56c1f29167fed98893.json`](../../sessions/1f/1f56c1f29167fed98893.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have enough data to compile the full matrix. Here's the complete audit:

## Signal 完整性矩阵 (exp002)

路径: `/root/autodl-tmp/exp002/signals/`

### Qwen2.5-0.5B (全完整 ✓)

| Model | Dosage | Seed | MMLU | ARC | GSM8K |
|-------|--------|------|------|-----|-------|
| Qwen2.5-0.5B | d000 | s42 | ✓ 2.7MB | ✓ 239KB | ✓ 259KB |
| Qwen2.5-0.5B | d005 | s42 | ✓ 2.7MB | ✓ 240KB | ✓ 259KB |
| Qwen2.5-0.5B | d025 | s42 | ✓ 2.7MB | ✓ 239KB | ✓ 259KB |
| Qwen2.5-0.5B | d100 | s42 | ✓ 2.7MB | ✓ 240KB | ✓ 259KB |
| Qwen2.5-0.5B | d000 | s123 | ✓ 2.5MB | ✓ 235KB | ✓ 243KB |
| Qwen2.5-0.5B | d005 | s123 | ✓ 2.5MB | ✓ 234KB | ✓ 242KB |
| Qwen2.5-0.5B | d025 | s123 | ✓ 2.5MB | ✓ 235KB | ✓ 243KB |
| Qwen2.5-0.5B | d100 | s123 | ✓ 2.5MB | ✓ 235KB | ✓ 243KB |
| Qwen2.5-0.5B-Instruct | — | — | ✓ 2.2MB | ✓ 204KB | ✓ 208KB |

### Qwen2.5-1.5B (全完整 ✓)

| Model | Dosage | Seed | MMLU | ARC | GSM8K |
|-------|--------|------|------|-----|-------|
| Qwen2.5-1.5B | d000 | s42 | ✓ 2.7MB | ✓ 239KB | ✓ 257KB |
| Qwen2.5-1.5B | d005 | s42 | ✓ (truncated) | ✓ | ✓ |
| Qwen2.5-1.5B | d025 | s42 | ✓ | ✓ | ✓ |
| Qwen2.5-1.5B | d100 | s42 | ✓ 2.7MB | ✓ 239KB | ✓ 258KB |
| Qwen2.5-1.5B | d000 | s123 | ✓ 2.5MB | ✓ 234KB | ✓ 242KB |
| Qwen2.5-1.5B | d005 | s123 | ✓ 2.5MB | ✓ 234KB | ✓ 243KB |
| Qwen2.5-1.5B | d025 | s123 | ✓ 2.5MB | ✓ 234KB | ✓ 242KB |
| Qwen2.5-1.5B | d100 | s123 | ✓ 2.5MB | ✓ 234KB | ✓ 241KB |
| Qwen2.5-1.5B-Instruct | — | — | ✓ 2.5MB | ✓ 235KB | ✓ 243KB |

### Qwen2.5-3B (alpha=32 有效版本)

| Model | Dosage | Seed | MMLU | ARC | GSM8K |
|-------|--------|------|------|-----|-------|
| Qwen2.5-3B_d000_a32 | d000 | s42 | ✓ 2.5MB | ✓ 235KB | ✓ 244KB |
| Qwen2.5-3B_d005_a32 | d005 | s42 | ✓ 2.5MB | ✓ 235KB | ✓ 243KB |
| Qwen2.5-3B_d025_v3 | d025 | s42 | ✓ 2.5MB | ✓ 235KB | ✓ 243KB |
| Qwen2.5-3B_d100_a32 | d100 | s42 | ✓ 2.5MB | ✓ 235KB | ✓ 243KB |
| Qwen2.5-3B_d000_s123_a32 | d000 | s123 | ✓ 2.2MB | ✓ 235KB | ✓ 243KB |
| Qwen2.5-3B_d005 | d005 | s123 | ✓ 2.5MB | ✓ 235KB | ✓ 243KB |
| Qwen2.5-3B_d025 | d025 | s123 | ✓ 2.5MB | ✓ 235KB | ✓ 243KB |
| Qwen2.5-3B_d100_a32 | d100 | s123 | ✓ 2.5MB | ✓ 235KB | ✓ 243KB |

### Qwen2.5-3B (DEPRECATED alpha=16, 忽略)

| Dir | Status |
|-----|--------|
| Qwen2.5-3B_d005_s42 | ⚠️ 仅有 arc merged |
| Qwen2.5-3B_d100_s42 | ⚠️ arc+gsm8k merged, 缺 mmlu |
| Qwen2.5-3B_d025_s42_DEPRECATED_alpha16 | ⚠️ arc+gsm8k, 缺 mmlu |
| Qwen2.5-3B_d025_s42_old_alpha16 | ⚠️ 仅 mmlu merged |
| Qwen2.5-3B_d000_v2_s42 | ⚠️ 无 merged (仅 s1+s2+s3 个体信号) |

### Llama-3.2-3B

| Model | Dosage | MMLU | ARC | GSM8K |
|-------|--------|------|-----|-------|
| Llama-3.2-3B | d000 | ✓ 2.5MB | ✓ 236KB | ✓ 244KB |
| Llama-3.2-3B | d005 | ✓ 2.5MB | ✓ 236KB | ✓ 244KB |
| Llama-3.2-3B | d025 | **✗ 缺失** | ✓ 236KB | ✓ 244KB |
| Llama-3.2-3B | d100 | **✗ 缺失** | ✓ 235KB | ✓ 243KB |

Llama d025 有 12 个 s4 chunks (0-12K), d100 只有 6 个 chunks (0-6K) — s4_selfcritique_mmlu 未完成。

### RRF 产出
- `/root/autodl-tmp/exp002/signals/rrf/exposure_aggregated.json` — ✓ 418KB
- `/root/autodl-tmp/exp002/signals/rrf/exposure_scores.json` — ✓ 15.9MB
- `/root/autodl-tmp/exp002/signals/rrf/exposure_scores_qwen_only.json` — ✓ 14.5MB

### Eval (exp001) 产出
大量完整 eval 结果已存在，覆盖 Qwen 0.5B/1.5B/3B 所有 dosage+seed 组合（aligned 和 para_aligned）。

### IRT (exp006) 产出
大量结果已存在：pooled IRT (n16/n20/n24/n25)、cross-family、domain-gamma、2PL/4PL 变体均有产出。

---

## 结论：真正缺失需要 GPU 的实验

| 缺失项 | 需要做什么 |
|--------|-----------|
| **Llama-3.2-3B_d025_s42 MMLU merged** | s4_selfcritique_mmlu 的 12 个 chunks 已全部完成但未 merge — 检查是否只需跑 merge 脚本（无需 GPU） |
| **Llama-3.2-3B_d100_s42 MMLU merged** | s4 chunks 只到 6K（MMLU 共 ~14K），还需继续跑 s4 约 8K 条 — **需要 GPU** |

**真正需要 GPU 的：仅 1 个任务** — Llama-3.2-3B d100 s42 的 s4_selfcritique_mmlu (约 8000 条剩余)。

Llama d025 的 s4 chunks 可能已全部完成（12 chunks × 1000 = 12K，接近 MMLU 总量），可能只需要跑 merge 脚本（纯 CPU）。需要确认 MMLU 总条目数是否为 ~12K。

---
