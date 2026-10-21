# analysis eval humaneval unpruned 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_humaneval_unpruned_2048_20260517T135316_result.json`
- **Structured JSON:** [`f3b0cdfd03d4a0ec2905.json`](../../sessions/f3/f3b0cdfd03d4a0ec2905.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

## eval_humaneval_unpruned_2048 结果

| 指标 | 值 |
|------|-----|
| **pass@1** | **0.4512 ± 0.0389** |
| correct / total | 74 / 164 |
| max_new_tokens | 2048 |
| avg_response_length | 1771 tokens |
| median_response_length | 2048 (仍在截断) |
| wall_time | 67.6 min |

## 关键发现

1. **Dense ceiling 确立**: unpruned 模型在 2048 tokens 下 pass@1 = 0.4512，远高于 512-token 版本的 0.0183 (24.7x 提升)。证实 512 tokens 严重截断了 R1 的 chain-of-thought。

2. **仍有截断**: median_response_length = 2048 表示超过一半的问题仍在 2048 被截断。失败案例中大量是 R1 的思维链 (chain-of-thought) 耗尽 token budget 后产生 SyntaxError (思考文本被当作代码执行)。真实 ceiling 可能更高 (需要 4096+ tokens)。

3. **与 pruned 模型对比**:
   - SFT RASP 20% (2048): 0.1037 → 保留了 dense 的 23% 能力
   - GRPO RASP 20% (512): 0.1037 → 在 512 tokens 下已接近 SFT@2048
   - Dense unpruned (2048): 0.4512 → 这是 ceiling

---
