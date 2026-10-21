# emergency eval timeout fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_emergency_eval-timeout-fix_20260520T162238_result.json`
- **Structured JSON:** [`211dc948702f724c687e.json`](../../sessions/21/211dc948702f724c687e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 状态总结

| 实验 | GPU | 状态 | 详情 |
|------|-----|------|------|
| eval_llama_sft_s43_no_evidence | cuda:1 | **已重启** | 原 PID 27322 在 244/247 batch 超时(EXIT_CODE=124)，无 predictions 产出。已有人重启为 `_r2`（PID 36403，seed 43），运行 10 min |
| eval_llama_sft_s44_no_evidence | cuda:2 | **仍在运行** | PID 29983，当前 179/247 batch，预计约 34 min 后完成。timeout=86400s，不会再超时 |
| eval_llama_rsft_s44_no_evidence | cuda:3 | **仍在运行** | PID 30188，当前 211/247 batch，预计约 17 min 后完成。timeout=86400s，不会再超时 |

### 注意事项
- cuda:1 的重启（PID 36403）使用的是 **seed 43**（非你指定的 seed 42），输出目录为 `eval_llama_sft_s43_no_evidence_r2`
- cuda:2/3 的 timeout 已设为 86400s（24h），不存在超时风险
- 三个 GPU 均正常工作中，无需额外操作

---
