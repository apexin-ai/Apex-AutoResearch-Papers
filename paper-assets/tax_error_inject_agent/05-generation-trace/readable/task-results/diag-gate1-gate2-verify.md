# diag gate1 gate2 verify

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gate1-gate2-verify_20260514T121457_result.json`
- **Structured JSON:** [`0fd0e97965c8a9315831.json`](../../sessions/0f/0fd0e97965c8a9315831.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### Gate 1: 注入算子合法率 — **PASS (100.0%)**

| 算子 | 合法/总数 | 合法率 |
|------|-----------|--------|
| C1_context_truncation | 191/191 | 100.0% |
| C4_observation_masking | 189/189 | 100.0% |
| P1_step_order_swap | 188/188 | 100.0% |
| P2_sub_goal_deletion | 192/192 | 100.0% |
| **Overall** | **760/760** | **100.0%** |

全部 760 条注入记录 `success=True`，阈值 80%，通过。

### Gate 2: Recovery demo 质量 — **PASS (89.5%)**

评估方法：检查每条记录最后一步 `think` 字段的 recovery reasoning 质量，分三档：
- **Strong**：明确提到 inconsistency/swap/mismatch/error 等异常
- **Moderate**：展示正确的任务推理（引用 history/current state/goal），能正确判断下一步
- **Weak**：无明显错误感知或任务推理

| 算子 | Strong | Moderate | Weak | 质量率 |
|------|--------|----------|------|--------|
| P1_step_order_swap | 68.6% | 27.7% | 3.7% | **96.3%** |
| P2_sub_goal_deletion | 27.6% | 62.0% | 10.4% | **89.6%** |
| C4_observation_masking | 9.5% | 76.7% | 13.8% | **86.2%** |
| C1_context_truncation | 10.5% | 75.4% | 14.1% | **85.9%** |
| **Overall** | | | | **89.5%** |

阈值 75%，通过。P1_step_order_swap 质量最高（96.3%），模型对步骤顺序错乱的感知最显著。抽样验证确认 recovery 推理内容合理——模型在收到注入后的 corrupted context 后能正确识别当前状态并选择正确的下一步动作。

---
