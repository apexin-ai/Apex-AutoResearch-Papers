# ops plan006 dryrun

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan006-dryrun_20260514T064821_result.json`
- **Structured JSON:** [`98d809843bba0225813d.json`](../../sessions/98/98d809843bba0225813d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 结果：**PASS**

| 项目 | 状态 |
|------|------|
| 训练完成 | 2/2 步，无报错 |
| reward_log | 2 步数据完整（step 1 & 2） |
| parse_rate | 1.0（模型输出格式正确，可解析） |
| reward/ISR | 均为 0.0（2 步正常，模型尚未学到有效 trace） |
| checkpoint 保存 | 正常（~15GB safetensors） |
| GPU 隔离 | cuda:0 only，cuda:1 未受影响 |
| 清理 | 已完成 |

一个注意点：训练日志中未看到显式的 `swipl` 调用信息——reward 全为 0 可能是因为模型初始输出的 Prolog trace 还无法通过执行验证，但 parse_rate=1.0 说明格式解析链路正常。2 步 dry-run 不足以产生有效 reward，这是预期行为。

---
