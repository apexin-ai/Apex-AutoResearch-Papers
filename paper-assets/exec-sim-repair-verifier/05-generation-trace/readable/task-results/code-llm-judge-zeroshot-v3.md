# code llm judge zeroshot v3

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llm-judge-zeroshot-v3_20260512T080619_result.json`
- **Structured JSON:** [`dc2178b9f89e15f7f143.json`](../../sessions/dc/dc2178b9f89e15f7f143.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已提交。汇总：

### 1. Qwen3-32B 模型检查
- 路径：`/root/autodl-tmp/models/Qwen/Qwen3-32B/`
- 大小：62GB（full precision，17 个 safetensors shard）
- 状态：**完整**，需 4-bit 量化加载到单卡 32GB

### 2. 数据格式（test.jsonl）
字段：`code`, `test`, `label`（1=PASS, 0=FAIL）, `source`, `problem_id`, `mutation_type`

### 3. Dry-run
`--help` 解析正常通过

### 4. 实验状态

| 实验 | GPU | PID | 日志 |
|------|-----|-----|------|
| llm-judge-8b-zeroshot | cuda:2 | 13295 | `~/runs/exec-sim-repair-verifier/llm-judge-8b-zeroshot.log` |
| llm-judge-32b-zeroshot | cuda:3 | 13452 | `~/runs/exec-sim-repair-verifier/llm-judge-32b-zeroshot.log` |

8B 为 full precision（bfloat16），32B 为 NF4 4-bit 量化。两个实验并行运行在 cuda:2 和 cuda:3。

---
