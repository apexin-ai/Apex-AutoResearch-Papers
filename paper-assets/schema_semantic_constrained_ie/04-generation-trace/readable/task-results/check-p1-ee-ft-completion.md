# check p1 ee ft completion

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_p1_ee_ft_completion_20260518T194115_result.json`
- **Structured JSON:** [`b84ce807a58a26d6ddea.json`](../../sessions/b8/b84ce807a58a26d6ddea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态机不允许 PREPARING→DONE 直接跳转，但 conclusion=failed 和 notes 已记录。无 cron 需要删除。

```
Pipeline 状态：完全未启动（卡在 PREPARING，从未进入 RUNNING）
训练：未执行（无日志、无 checkpoint）
推理 unconstrained：未执行
推理 constrained：未执行
评估 F1：无
Violation rates：无

诊断：
  - westd-21461 上无任何 p1_ee_ft 相关文件（日志/输出/checkpoint/完成标记均不存在）
  - /root/schema_semantic_constrained_ie/checkpoints/ 目录为空
  - 仅存在旧 checkpoint: qwen_lora_docred_merged, qwen3_8b_lora_scierc_merged
  - 训练脚本 train_lora_wikievents.py 存在，但 pipeline 未被调用
  - 进程在启动脚本生成或环境准备阶段就退出了

Registry：PREPARING (conclusion=failed, notes 已更新)
  注：PREPARING→DONE 跳转被状态机拒绝，需先经过 RUNNING
Cron：当前 session 无 cron 任务
```

需要手动重新启动整个 pipeline。

---
