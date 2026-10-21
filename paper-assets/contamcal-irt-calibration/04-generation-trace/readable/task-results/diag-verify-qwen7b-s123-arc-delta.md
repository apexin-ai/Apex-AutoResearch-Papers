# diag verify qwen7b s123 arc delta

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_verify-qwen7b-s123-arc-delta_20260521T010428_result.json`
- **Structured JSON:** [`d2ef87325bb4b44e84b7.json`](../../sessions/d2/d2ef87325bb4b44e84b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 核实结果

### 差异根因：两台服务器的 eval 结果差 1 题

| 来源 | 服务器 | d000 accuracy | correct/total | d100 accuracy |
|------|--------|--------------|---------------|--------------|
| `eval_qwen7b_s123_cqa1_v2` | cqa1-21977 | **0.87201365** (87.20%) | **1022**/1172 | 0.84726962 (84.73%) |
| `eval_arc_s123_batch` | westd-29999 | **0.87116041** (87.12%) | **1021**/1172 | 0.84726962 (84.73%) |

- **d100 完全一致**：两台服务器都是 993/1172 = 84.73%
- **d000 差 1 题**：cqa1 得 1022 correct，westd 得 1021 correct

### Bootstrap CI 用了哪个

Bootstrap CI 用的是 **cqa1 的数据**（registry `eval_qwen7b_s123_cqa1_v2`，d000=0.872）：
- delta = 0.8473 - 0.8720 = **-0.0247** (-2.47pp)

### Reviewer 用了哪个

Reviewer 独立验证用的是 **westd 的数据**（registry `eval_arc_s123_batch`，d000=87.12%）：
- delta = 84.73 - 87.12 = **-2.39pp**

### 差异来源

不是四舍五入，是**两次不同 eval run 之间的真实差异**——d000 差 1 个 item (1022 vs 1021)。可能原因：
1. **evaluate.py 版本差异**（C009/C010 约束正是针对此问题）——mc_suffix 位置等细节差异可导致个别 item 判定不同
2. **推理非确定性**（虽然 greedy decoding 通常确定，但跨服务器 GPU 差异偶尔导致 borderline case 翻转）

### 对结论的影响

0.08pp 差异（-2.47 vs -2.39）不影响 CI 方向和显著性判断。但按 C009/C010 原则，应统一使用同一版本 evaluate.py 的产出。需要确认 bootstrap CI 应该用 cqa1 还是 westd 的数据作为权威来源。

---
