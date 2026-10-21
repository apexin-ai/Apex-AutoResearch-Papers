# prep exp 011 llama8b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp-011-llama8b_20260516T204635_result.json`
- **Structured JSON:** [`efc205c18946c51af4ae.json`](../../sessions/ef/efc205c18946c51af4ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-011 准备完成。

**总结：**

| 项目 | 状态 |
|------|------|
| LLaMA-3.1-8B-Instruct 模型 | ✓ 14GB, 4 shards 完整 |
| D012 数据集 (30 PW + 30 FOLIO) | ✓ 60 题已确认 |
| 启动脚本 | ✓ `scripts/run_exp011_llama8b.sh` 已创建 |
| GPU (RTX PRO 6000 98GB) | exp-002 占用中，exp-011 预计仅需 ~25-30GB |

**一键启动命令**（exp-002 结束后）：
```bash
nohup bash /root/symb_invariant_consensus/scripts/run_exp011_llama8b.sh > /tmp/exp011.log 2>&1 &
```

预估运行时间 ~1-1.5 小时。无缺失项。

---
