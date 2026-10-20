# ops critical path readiness

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_critical-path-readiness_20260516T050718_result.json`
- **Structured JSON:** [`05e3e5aaa1293b663da6.json`](../../sessions/05/05e3e5aaa1293b663da6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/root/autodl-tmp/critical_path_readiness.md`。

**结论**:

| 组件 | 状态 |
|------|------|
| RRF 聚合 (exp-003) | **READY** — 代码、数据均就绪，dry-run 通过 |
| Per-benchmark IRT γ_k | **READY** — 已有 4 个 benchmark 的拟合结果 |
| Joint IRT (shared γ) | 收敛失败 (Rhat=1.74, ESS=6)，非阻塞 |
| 7 Baselines | **READY** — B0–B6 全部实现并通过测试 |
| Flagged items 排除 | **缺 ~15 行代码** — 需要在 IRT 脚本中加 `--exclude-items` 参数 |

**唯一 code gap**: `run_pooled_4bench_irt.py` 没有排除 flagged items 的机制。426 个 flagged items 全是 MMLU (3.0%)，item_id 格式 `mmlu_{index}` 与 IRT 的 positional index 兼容，加一个 mask 即可。

**建议**：flagged items 应排除——它们的 aligned/para 高分歧意味着 difficulty 是 format-dependent 的，违反 IRT 单维性假设，会给 γ 估计增加噪声。

---
