# ops pytest f1gate verify

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pytest-f1gate-verify_20260514T161447_result.json`
- **Structured JSON:** [`4f262723f78be7291c29.json`](../../sessions/4f/4f262723f78be7291c29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完毕，汇总结果：

---

### 1. F1 Gate 代码 — 已确认存在

`CEDRewardWrapper.__call__`（`grpo_trainer.py:220` 附近）包含 F1 gating 逻辑：
- 将 predicted triples 和 gold triples 都规范化为 `(head, relation, tail)` 小写 key
- 遍历 predicted triples，检查是否至少有一个匹配 gold_map
- **`if not has_gold_match: rewards.append(0.0); continue`** — 无匹配则 CED reward 直接归零，跳过 NLI 计算

### 2. Pytest — 3/3 PASSED

```
test_empty_output_returns_zero     PASSED
test_correct_triple_returns_positive PASSED
test_nonsense_output_returns_zero  PASSED
```

测试文件位于 `/root/autodl-tmp/freige/tests/test_ced_gate.py`，全部通过。

### 3. ced_kl001_r4 — 使用了正确代码

日志确认：
- 加载了 NLI 模型 `cross-encoder/nli-deberta-v3-base`
- **`Stage 3: using ced reward, tau 0.30→0.50 over 190 steps`** — CED reward 已启用，包含 F1 gate
- 训练正在进行中，当前约 33/100 steps

---
