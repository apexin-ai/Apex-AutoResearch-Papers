# diagnose exp 005 eval failure

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-005-eval-failure_20260522T142413_result.json`
- **Structured JSON:** [`ebf2d2bd50de9b247427.json`](../../sessions/eb/ebf2d2bd50de9b247427.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，报告已写入 `artifacts/exp-005-eval/diagnosis.md`。

核心结论：实验失败于**模型下载阶段**，评估从未执行。4 次下载尝试分别因 HF 超时、xet 401、ModelScope 下载中断、CLI 语法错误而失败。唯一成功的是 GLA 模型（v3 耗时 58 分钟），DeltaNet 和 HGRN 均未完成下载。

建议直接关闭——父实验 exp-005 的 kill 理由（zoo 仅 3 种架构无法扩展）仍然成立，重试投入产出比不合理。

---
