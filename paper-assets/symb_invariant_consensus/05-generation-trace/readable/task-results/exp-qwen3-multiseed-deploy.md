# exp qwen3 multiseed deploy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen3-multiseed-deploy_20260523T180238_result.json`
- **Structured JSON:** [`9538f8ea48f78c379c40.json`](../../sessions/95/9538f8ea48f78c379c40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个种子都在正常运行且产生正确结果。

## 部署完成总结

| Seed | GPU | Port | vLLM PID | 实验 PID | 状态 |
|------|-----|------|----------|---------|------|
| 123 | cuda:0 | 8020 | 801558 | 804112 | 运行中 |
| 456 | cuda:2 | 8021 | 801559 | 804114 | 运行中 |
| 789 | cuda:3 | 8022 | 801560 | 804116 | 运行中 |

**配置**（完全匹配 exp033）：
- 模型：`/root/autodl-tmp/models/Qwen3-14B`
- 非思考模式：`--default-chat-template-kwargs '{"enable_thinking": false}'`
- K=12, T=0.7, max_tokens=4096, max_model_len=8192
- 数据：`data/proofwriter_full.json` (600 problems)
- Tiebreaking：alphabetical（代码内置）

**输出路径**：
- `results/multi_seed/qwen3_pw_seed{123,456,789}/results.json`

**预计完成时间**：~90s/problem × 600 = ~15 小时（约今晚 17:00 CST）

**监控命令**：
```
tail -f /tmp/qwen3_pw_seed123.log
tail -f /tmp/qwen3_pw_seed456.log
tail -f /tmp/qwen3_pw_seed789.log
```

---
