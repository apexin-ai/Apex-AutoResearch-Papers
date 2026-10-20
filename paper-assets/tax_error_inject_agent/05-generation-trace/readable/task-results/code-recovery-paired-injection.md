# code recovery paired injection

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_recovery-paired-injection_20260515T130059_result.json`
- **Structured JSON:** [`66c31b1917143be184b4.json`](../../sessions/66/66c31b1917143be184b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**脚本路径**: `/root/autodl-tmp/tax_error_inject_agent/scripts/gen_recovery_paired.py`

**数据统计**:
- 总 injected variants: 760
- 可处理: 711（49 条因 source trajectory 不在 successful_trajectories.jsonl 中被跳过）
- 按 operator 分布: P1=170, P2=184, C1=182, C4=175（均匀）

**Recovery 规模**:
- 平均每条需生成 7.6 步 recovery continuation
- 最少 1 步，最多 46 步
- 总 API 调用数: **5,408 次**

**预估 API 成本**:
- Input tokens: ~2.88M → $7.20
- Output tokens: ~811K → $8.11
- **总计: ~$15.31**

脚本支持 `--dry-run`、`--limit N`、`--estimate-cost`，API 调用用 openai 库 + retry 逻辑。等待审批后可加 `--api-key` 运行实际生成。

---
