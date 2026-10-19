# code classify rulebased v2 d025b

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_classify-rulebased-v2-d025b_20260512T225335_result.json`
- **Structured JSON:** [`236c2c48b3541d85545b.json`](../../sessions/23/236c2c48b3541d85545b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 产出

**文件**：`/root/autodl-tmp/error_diag_dpo_recovery/src/classify_errors_rulebased.py`

### 规则设计

| 优先级 | 规则 | 触发条件 | → error_type |
|---|---|---|---|
| 1 | `rule_pcb` | csf_details 存在 或 detect_csf 检测到终止循环 | verification |
| 2 | `rule_wrong_object` | divergence point 处同 verb、不同 object type | action |
| 3 | `rule_wrong_instance` | 同 verb + 同 object type、不同 instance 编号 | action |
| 4 | `rule_wrong_receptacle` | take/put 同 verb + 同 object、不同 receptacle | action |
| 5 | `rule_wrong_verb` | model 用 "go to" 而 expert 用 take/put/clean 等 | action |
| 6 | `rule_ignored_failure` | "Nothing happens" 后重复同一动作，或全程 ≥3 次 | verification |
| 7 | `rule_repeated_action` | 连续 ≥3 次相同非终止动作 | verification |
| 8 | `rule_missing_subtask` | task_type 要求 clean/heat/cool/use 但轨迹中缺失 | planning |
| 9 | `rule_inefficient_search` | >8 个不同目的地 + 导航比 >60% | planning |
| 10 | `rule_default` | 以上均未命中 | planning |

### 分类分布（v6 ICL 合并，25 条失败轨迹）

```
action          20 (80.0%)   — 17 wrong_object, 2 wrong_instance, 1 wrong_verb_nav
verification     5 (20.0%)   — 4 ignored_failure, 1 PCB
planning         0 ( 0.0%)
```

**关键对比**：LLM 分类器把 98% 判为 planning，rule-based 把 80% 判为 action。差异来自方法论——rule-based 看 divergence point 处的动作结构（同 verb 不同 target → action），LLM 看全局语义（错误导航 → 策略问题 → planning）。这验证了需要多种分类方法作为 sanity check。

---
