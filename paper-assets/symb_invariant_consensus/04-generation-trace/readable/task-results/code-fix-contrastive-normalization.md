# code fix contrastive normalization

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-contrastive-normalization_20260519T172910_result.json`
- **Structured JSON:** [`b71e8e4d752d8e3be771.json`](../../sessions/b7/b71e8e4d752d8e3be771.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

归一化效果清晰可见：

- **folio_0 Unknown**: raw_score=5.0（旧方式因 n_pro=9 获得高原始分），归一化后 score=0.0（norm_pro=1.0 - norm_con=1.0）
- **folio_4 Unknown**: raw_score=3.0，归一化后 score=0.4286（norm_pro=1.2857 > norm_con=0.8571，pro 满足率更高）
- **folio_4 True**: raw_score=2.0（看似不错），但归一化后 score=0.0（满足率相同）

归一化确实消除了约束数量偏差。

## 汇报

### 修改位置
`/root/symb_invariant_consensus/run_contrastive.py`，两处：

1. **`contrastive_score_candidate` 函数**（~行 210-225）：评分逻辑从 `pro_sat_weight - con_sat_weight` 改为 `(pro_sat_weight / max(n_pro, 1)) - (con_sat_weight / max(n_con, 1))`。输出新增 `raw_score`, `normalized_pro`, `normalized_con`, `n_pro`, `n_con`。

2. **`details_out` 构建部分**（~行 370-383）：同步更新字段名引用，新增 `raw_score`, `normalized_pro`, `normalized_con`, `n_pro`, `n_con` 到 per_candidate_details 输出。

### Dry-run 对比（5 题真实 vLLM 推理）
| 问题 | 候选 | raw_score (旧) | normalized_score (新) | n_pro | n_con |
|------|------|---------|------|-------|-------|
| folio_0 | True | 1.0 | **1.0** | 1 | 0 |
| folio_0 | Unknown | 5.0 | **0.0** | 9 | 4 |
| folio_4 | Unknown | 3.0 | **0.4286** | 7 | 7 |
| folio_4 | True | 2.0 | **0.0** | 3 | 1 |

folio_0 Unknown 的旧 raw_score=5.0 远高于 True 的 1.0（因 n_pro=9 vs 1），归一化后 Unknown=0.0 vs True=1.0，修正了偏差。

### exp-075 影响
- **exp-075 实验已在运行**（01:31:14 启动，处理 204 题），使用的是**磁盘修改前加载到内存的旧代码**。
- 实验结果目录：`results/exp075_contrastive_mistral_folio/`，尚未产出 results.json（刚启动几分钟）。
- **需要你决定**：是否 kill 当前运行的 exp-075 并用修复后的代码重启？实验刚启动，重启代价很小。

---
