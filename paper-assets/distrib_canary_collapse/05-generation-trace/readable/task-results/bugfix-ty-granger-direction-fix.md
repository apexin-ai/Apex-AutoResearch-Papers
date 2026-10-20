# bugfix ty granger direction fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_ty_granger_direction_fix_20260520T182806_result.json`
- **Structured JSON:** [`bbfba9bb75fd61798185.json`](../../sessions/bb/bbfba9bb75fd61798185.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**修复内容**: `run_5method_analysis_d102.py` 第 223 行 `causing=1, caused=0` → `causing=0, caused=1`

**合成数据验证**: Forward p≈0 (显著)，Reverse p=0.80 (不显著) — 确认修复正确

**三个 T=20 实验重跑结果**:

| 实验 | TY fwd | TY rev | K≥3 | 非 TY 方法 |
|---|---|---|---|---|
| a050 | 4→2 | 2→4 | 6→6 | 不变 |
| a060 | 3→5 | 5→3 | 3→**4** | 不变 |
| a100 | 1→2 | 2→1 | 6→6 | 不变 |

TY forward/reverse 精确互换，非 TY 方法零变化，确认 bug 是纯方向反转。a060 的 K≥3 从 3 提升到 4（token_entropy→distinct_{1,2,3} 三个 pair 通过 TY 后达到 3/5 consensus）。

**产出**:
- 修复脚本: `westd-17855:run_5method_analysis_d102.py`
- 对比报告: `artifacts/ty_direction_fix_results.md`
- 修复后 JSON: `artifacts/t20_tyfix_v2/{exp}/5method_summary_tyfix.json`
- 服务器备份: `5method_leadlag_pre_tyfix.json`（三个实验均有）

---
