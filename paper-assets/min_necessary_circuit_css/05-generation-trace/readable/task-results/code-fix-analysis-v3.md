# code fix analysis v3

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-analysis-v3_20260512T231917_result.json`
- **Structured JSON:** [`4bbe9f3c61b8949a094d.json`](../../sessions/4b/4bbe9f3c61b8949a094d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 修复脚本

**路径**: `/root/min_necessary_circuit_css/analysis_fix_v3.py`

**使用**: `python3 analysis_fix_v3.py` (ACDC 完成后自动读取 cache_acdc.json)

### 五项修复

| # | 问题 | 修复 |
|---|------|------|
| 1 | EP `score > 0.5` 对 mask_gradient 无意义 | top-N=100（与 EAP-IG 对齐） |
| 2 | CIRCUS 在 32491 边操作 vs CSS 在 ~150 边 | CIRCUS 限制到二值化并集 |
| 3 | 作用域不匹配导致 off-diagonal ~98% | 统一 universe 后重算 |
| 4 | `KILL` 直接判死 | `KILL_CANDIDATE`（D003 需 2 tasks 确认） |
| 5 | 无 pairwise 比较 | Jaccard + 3-way ratio |

### K=2 预览结果（ACDC 未完成）

- Off-diagonal: **7.1%**（原 ~98% 是 artifact）
- Verdict: **PASS_FINDINGS**（原 KILL 是 artifact）
- Jaccard(EAP-IG, EP): 0.3072
- EP old(>0.5) vs new(top-100) overlap: 65/100

ACDC 完成后运行 `python3 analysis_fix_v3.py` 获取 K=3 完整结果。

---
