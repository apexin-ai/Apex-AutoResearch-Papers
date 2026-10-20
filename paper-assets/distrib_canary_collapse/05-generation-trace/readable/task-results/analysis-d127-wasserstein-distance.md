# analysis d127 wasserstein distance

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d127_wasserstein_distance_20260520T095447_result.json`
- **Structured JSON:** [`4469a403a7714eeda38e.json`](../../sessions/44/4469a403a7714eeda38e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已在远程服务器。汇总结果。

## D127 Track F 结果

**脚本**: `/root/autodl-tmp/distrib_canary_collapse/scripts/d127_wasserstein.py`
**JSON**: `/root/autodl-tmp/distrib_canary_collapse/artifacts/d127_wasserstein/d127_wasserstein.json`
**PNG**: `/root/autodl-tmp/distrib_canary_collapse/artifacts/d127_wasserstein/wasserstein_canary.png`

### Blind Zone 检测汇总 (FDR-significant pairs)

| Canary | α=0.10 | α=0.25 | α=0.30 | α=0.35 | α=0.40 | α=0.45 | α=0.50 | α=0.75 |
|---|---|---|---|---|---|---|---|---|
| **W-1** | 2/4 | 2/4 | 2/4 | 2/4 | 2/4 | 2/4 | 2/4 | 2/4 |
| **entropy** | 1/4 | 2/4 | 0/4 | 0/4 | 0/4 | 0/4 | 3/4 | 3/4 |
| **eff_rank** | 3/4 | 3/4 | 3/4 | 3/4 | 1/4 | 3/4 | 3/4 | 3/4 |

**Blind Zone (α≤0.45) 总计**:
- W-1: **12/24**
- entropy: **3/24**
- eff_rank: **16/24**

### 关键发现

1. **W-1 无 blind zone** — 在所有 α 下一致检测 2/4 对（distinct_1 + distinct_2），包括 entropy 完全失败的 α=0.30–0.45 区间
2. **W-1 比 entropy 好 4×**（blind zone 内 12/24 vs 3/24）
3. **eff_rank 仍是最强 canary**（16/24），但在 α=0.40 有凹陷（1/4）；W-1 更稳定，无凹陷
4. **W-1 选择性检测 distinct_1 和 distinct_2**，对 distinct_3 和 mauve 不敏感 — 与 eff_rank 互补
5. **Entropy blind zone 确认**: [0.30, 0.45]，该区间内 0/16 pairs detected

### Blind zone 缩小对比
- Entropy: blind zone = [0, 0.45]（完全失败于 α=0.30–0.45）
- Effective_rank (D126): blind zone ≈ [0, 0.25)
- **W-1: 无 blind zone** — 从 α=0.10 起一致有信号，但检测深度有限（2/4 而非 3-4/4）

---
