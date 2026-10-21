# diagnose eval math500 timeout

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_timeout_20260517T143922_result.json`
- **Structured JSON:** [`01d5dcb496ad942e4973.json`](../../sessions/01/01d5dcb496ad942e4973.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `artifacts/diag_eval_math500_grpo_timeout.md`。核心结论：

### 实验状态

| 实验 | 状态 | 进度 | 耗时 |
|------|------|------|------|
| grpo_rasp_20_v2 | **FAILED** (timeout EXIT_CODE=124) | 193/500 | 5h55m |
| grpo_standard_20 (pid 14556) | **仍在运行** | 123/500 | 5h13m+ |

### 根因

`max_new_tokens=4096` + GRPO 模型生成极长 `&lt;think>` 推理链。GRPO 模型频繁命中 4096 token 上限，单题最慢达 **350s**，平均 110-153s/题。对比 SFT 模型平均仅 21s/题（7x 差距）。脚本无 per-sample timeout。

### 修复建议

1. **GRPO eval 使用 `--max_new_tokens 2048`**：2048 tokens 足够覆盖正确推理，预估总时间从 15-21h 降至 **8-10h**
2. 当前 standard_20 进程（pid 14556，acc@100=36%）建议让它跑完（预计明天 ~09:00），结果有价值
3. rasp_20_v2 用 `--max_new_tokens 2048` 重跑

---
