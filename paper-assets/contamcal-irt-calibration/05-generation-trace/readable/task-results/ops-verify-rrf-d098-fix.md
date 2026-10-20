# ops verify rrf d098 fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-rrf-d098-fix_20260516T024022_result.json`
- **Structured JSON:** [`c68e9ce0cb154153fa8b.json`](../../sessions/c6/c68e9ce0cb154153fa8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

**s3 移除状态: done** — `SIGNAL_KEYS = ["s1_embedding", "s2_minkpp", "s4_selfcritique"]`，s3_constat 已移除。`SIGNAL_NAMES` 和 `sig_name_map` 也已同步清理。

**dual format 匹配: 正常** — `sig_name_map` 映射了 `s1_embedding→embedding`, `s2_minkpp→minkpp`, `s4_selfcritique→selfcritique`，代码先尝试 `signal_{sig_key}_{bench}.json`，失败后回退 `signal_{sig_name}_{bench}.json`。

**SKIP_PATTERNS 状态: 需要补充** — 当前只有 `SKIP_PATTERNS = ["DEPRECATED"]`（第40行），在第224行做 `if any(pat in model_id for pat in SKIP_PATTERNS)` 过滤。这不会匹配 C006 要求的 alpha=16 废弃目录：
- `Qwen2.5-3B_d000_s42`
- `Qwen2.5-3B_d000_v2_s42`
- `Qwen2.5-3B_d005_s42`
- `Qwen2.5-3B_d025_s42`
- `Qwen2.5-3B_d100_s42`

除非这些目录已被重命名为包含 "DEPRECATED" 字样，否则不会被跳过。

**备份文件**: 存在，`rrf_aggregation.py.bak`，2026-05-16 09:27。

---
