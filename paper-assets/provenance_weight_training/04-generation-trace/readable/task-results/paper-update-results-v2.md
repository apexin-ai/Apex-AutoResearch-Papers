# paper update results v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_update-results-v2_20260516T002349_result.json`
- **Structured JSON:** [`ff38982f4539a3082bda.json`](../../sessions/ff/ff38982f4539a3082bda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改摘要：

**ESS-only 段落（Claim 1）**：补充 per-seed 一致性论证——ESS-only 在所有 3 个 seed 上均劣于 uniform，adaptive 在所有 3 个 seed 上均优于 uniform（差值 0.041/0.043/0.045），排除 seed-specific artifact。

**n_min 段落**：从 2 句话扩展为完整 ablation 分析：
- 新增 Table 3（`tab:nmin`）：4 点数据（n_min=1/2/3/4），含 PPL 和 b* mean
- n_min=4 → b*=0 恒成立，退化为 uniform（17.695 vs 17.694）
- n_min=3 标注 `‡` 脚注说明来自早期配置，非独立 ablation
- 新增 bs8_nmin2 分析：B=8 + n_min=2 → ESS range [2,8] 过宽 → PPL 17.73，与 ESS-only 相当
- 提出 scaling rule：n_min = max(2, ⌊B/2⌋)

**Table 1**：无变化（ESS-only 3 seeds 和 Golden Ratio 已是最新数据）。

**tau 段落**：无变化。

---
