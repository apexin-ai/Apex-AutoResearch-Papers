# writing section7 pending bf16 update

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_section7_pending_bf16_update_20260514T091732_result.json`
- **Structured JSON:** [`00ab146a7bb11ba2f3e3.json`](../../sessions/00/00ab146a7bb11ba2f3e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有编辑已完成。以下是变更汇总：

---

## 替换/标注清单

### 1. 已替换：CI 数值（line 86）
| 位置 | 旧值 | 新值 | 来源 |
|------|------|------|------|
| CI lower bounds range | $0.19$ to $6.70$ | $0.20$ to $8.39$ | DeepSeek bf16 B=10000 per-problem paired: s015 lower=0.199, s030 lower=8.392 |
| s=0.30 CI example | $[6.70,\; 16.29]$ | $[8.39,\; 16.65]$ | DeepSeek s030 CI=[8.392, 16.653] |

### 2. 已标注 `[VERIFY: segment-level vs per-problem]`（3处）

| 位置 | 问题 | 详情 |
|------|------|------|
| **Line 9** (G values) | G=69–274× vs results_5_1.tex G=11.53–41.92× | ~6× 差异，可能是 segment-level vs problem-level aggregation。必须与 §5 主表对齐 |
| **Line 29** (median_diff) | 体文用 segment-level median_diff (DS: 0.39→14.59, QW: 0.039→2.943)，comment 中 Cohen's d 用 per-problem paired | per-problem paired median_diff: DS=(0.324,1.152,3.969,9.944), QW=(0.048,0.208,1.109,2.619)。两套数字混在一段中 |
| **Line 85** (mean/median ratio) | comment 中 median_diff=14.59 是 segment-level | per-problem paired median_diff=9.9436 at s030；mean/median ratio ~1.6:1 可能在 per-problem 级别不成立 |

### 3. 已确认无需改动的数值
- ρ=1.0, gradient permutation p=0.043 ✓
- Cohen's d (DS: 0.607→1.126, QW: 0.371→1.439) ✓ 已是 per-problem paired
- Qwen s015 borderline (d=0.371, CI crossing zero) ✓
- B=10,000, n=49/n=46 ✓
- C4/entropy 内容未触碰

### 需主 Agent 决策
3 处 `[VERIFY]` 标注需要统一决策：§7 Discussion 的 median_diff 和 G 值应使用 segment-level 还是 per-problem paired，取决于 §5 主表最终采用哪套数字。

---
