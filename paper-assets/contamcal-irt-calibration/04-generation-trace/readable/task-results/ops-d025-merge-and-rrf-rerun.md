# ops d025 merge and rrf rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d025_merge_and_rrf_rerun_20260516T235735_result.json`
- **Structured JSON:** [`456db6d0a5a4edfd0798.json`](../../sessions/45/456db6d0a5a4edfd0798.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 结果

| 项目 | 值 |
|------|-----|
| d025 MMLU s4 状态 | ✅ 完成，14042 items |
| d025 signals_merged_mmlu | ✅ 已含 s1+s2+s4，14042 items |
| d025 RRF 产出路径 | `/root/autodl-tmp/exp003/rrf_d025/` |
| d025 RRF respondents | **8** (Llama-3.2-3B_d025_s42, Qwen 0.5B/1.5B/3B × s42+s123, 3B_v3_s42, 3B_old_alpha16) |
| d100 MMLU s4 PID (cuda:0) | **891476** |

注意：`Qwen2.5-3B_d025_s42_old_alpha16` 仅有 mmlu（无 gsm8k/arc），其他 7 个 respondent 都有完整 3 benchmarks。按 C006 约束，这个 old_alpha16 目录理论上应该被排除——RRF 脚本的 blocklist 里没有它（只 block 了 `Qwen2.5-3B_d025_s42`），可能需要后续清理。

---
