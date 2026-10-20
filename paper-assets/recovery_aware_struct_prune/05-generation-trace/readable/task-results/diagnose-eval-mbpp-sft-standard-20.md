# diagnose eval mbpp sft standard 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_mbpp_sft_standard_20_20260519T203136_result.json`
- **Structured JSON:** [`cf126b8ba11dbcb5d2d8.json`](../../sessions/cf/cf126b8ba11dbcb5d2d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

- **进度**：完成 189/374（50.5%），最后 checkpoint 180/374 时 Pass@1=0.1278
- **SIGTERM 来源**：外部 kill（直接 `kill &lt;pid>`）。排除 OOM（OOM 发 SIGKILL=137）和 timeout wrapper（timeout 返回 124）。最可能是其他 Worker 在 ~04:00 启动新 MBPP eval 时杀掉了此进程以释放 GPU
- **Partial results**：无。结果文件不存在，脚本只在全部完成后才写文件
- **速度问题**：~40s/it，比同服务器的 sft_rasp_20（~10s/it）慢 4 倍，完成全部 374 题预计需 ~4.5h
- **建议**：需要重提交。可考虑降低 `--max_new_tokens`（如 1024）或加 per-task timeout 来加速，防止个别长生成拖慢整体进度

---
