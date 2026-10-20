# code classify h8 upgrade

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_classify-h8-upgrade_20260515T115437_result.json`
- **Structured JSON:** [`2df11d749c754bd7638e.json`](../../sessions/2d/2df11d749c754bd7638e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 分类器升级

`scripts/classify_h7.py` 新增两个检测规则：
- **H8 conjunction-collapse**: 结论是前提的顶层合取（如 `P1 ∧ P2`），通过括号感知的分割器实现
- **Content-independent predicates**: 所有谓词为单字母（P, Q, R...）的标记

genuine 定义更新为 `proved - |H7 ∪ H1 ∪ H8|`（集合去重）。

## 回溯审计结果（24 个 eval 文件）

**Genuine 下调的实验：**

| exp_id | 旧 genuine | 新 genuine | H8 count | 
|--------|-----------|-----------|----------|
| plan001-exec-only-s42-r2 | 12 (12.9%) | **7 (7.5%)** | 6 |
| plan002-additive-b01-s42-1000 | 3 (3.0%) | **2 (2.2%)** | 1 |
| plan002-additive-b03-s42 | 4 (22.2%) | **1 (5.6%)** | 3 |

**H8 检出但 genuine 不变（已为 0）：**
- exp1-isr-b03-s42-1000-r2: H8=41（95 个 proved 全是 H1 或 H8）
- plan004-o1-ablation-s42: H8=2

**无 H8 的实验：** plan006-prolog-exec-s42 (genuine=86, 100%), plan009-sft (genuine 93-94%), plan017-random, plan013-r4 等均 H8=0。

## 无法验证

**plan002-additive-b01-s42**（genuine=25，任务最高优先级）checkpoint 和 eval 文件已被删除，无法重新分类。需要从 base model 重训以验证 H8 影响。

## Registry 已更新

5 个实验的 metrics 已写入 h8_conjunction_collapse_count/rate 和更正后的 genuine 值。审计报告位于 `/root/autodl-tmp/outputs/h8_retroactive_audit.json`。

---
