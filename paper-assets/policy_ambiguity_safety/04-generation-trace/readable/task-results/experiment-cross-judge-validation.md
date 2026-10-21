# experiment cross judge validation

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_cross_judge_validation_20260522T221725_result.json`
- **Structured JSON:** [`123ee146b1eee3d524a2.json`](../../sessions/12/123ee146b1eee3d524a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OpenRouter 余额不足（402 Insufficient balance）。所有调用都失败了。

需要充值 OpenRouter 账户后重新运行。脚本支持 resume，重跑时会跳过已判的 episode（但当前所有判定都是错误占位，需要先清理）。

清理错误数据并重跑的命令：

```bash
# 清理错误判定
rm -f artifacts/cross_judge_validation/judgments_claude/judgments.jsonl

# 充值后重跑
cd artifacts && source .venv/bin/activate
python cross_judge_validation/run_cross_judge.py --judge both --concurrency 5
```

需要你充值 OpenRouter 后我再继续？还是有其他 API key 可用？

---
