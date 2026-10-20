# eval mvp 004 repair collect

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mvp_004_repair_collect_20260515T032756_result.json`
- **Structured JSON:** [`a17cdcae29b333575ba6.json`](../../sessions/a1/a17cdcae29b333575ba6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**repair_only.py 状态**：进行中

- 进度：47/86（54.7%）
- 已运行：2h42m（08:46 启动）
- 速率：~3.4 min/条
- 剩余：39 条，预计 ~2h13m 后完成（约 13:40）
- 输出文件：repair_fixed.json 尚未生成（完成后才写）

---

**表 1：去重后原始评估（对照组，mvp_v4_full.jsonl，204 条）**

| Gate | All-mode 结果 | 阈值 | 状态 | Excl-Unknown 结果 | 状态 |
|------|--------------|------|------|-------------------|------|
| C1 disagree_rate | 39.6% (76/192) | ≥10% | **PASS** | 35.7% (45/126) | **PASS** |
| C2 diagnostic_rate | 86.8% (66/76) | ≥40% | **PASS** | 84.4% (38/45) | **PASS** |
| C3 error_types | 3 types | ≥2 | **PASS** | 2 types | **PASS** |
| C4 targeted_vs_blind | +6.2pp (T:60/96 B:54/96) | >5pp | **PASS** | -1.7pp (T:34/59 B:35/59) | **FAIL** |
| C5 localization | 85.4% (35/41) | ≥60% | **PASS** | 89.3% (25/28) | **PASS** |

**All-mode MVP RESULT: 5/5 PASS → PROCEED**

---

**表 2：repair_only 修复后评估** — 待 repair 完成（预计 ~13:40）

---

**对照组要点**：
- All-mode 已全部通过，C4 = +6.2pp 刚过 5pp 阈值
- Excl-Unknown 的 C4 为 -1.7pp FAIL（targeted 反而不如 blind），但 All-mode 通过即可
- C1 disagreement 率 39.6%，远超 10% 阈值
- C2 诊断率 86.8%，表现强劲

**下一步**：repair 完成后（约 2h 后），运行 `python3 src/evaluate_mvp.py results/mvp_v4_repair_fixed.json` 对比 C4 是否进一步改善。当前 All-mode 5/5 PASS 已满足 MVP 判定标准。

---
