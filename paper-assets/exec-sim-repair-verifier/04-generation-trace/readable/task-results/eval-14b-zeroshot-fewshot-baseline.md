# eval 14b zeroshot fewshot baseline

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_14b-zeroshot-fewshot-baseline_20260522T175229_result.json`
- **Structured JSON:** [`31a20bd913aa3a50f5b2.json`](../../sessions/31/31a20bd913aa3a50f5b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

后台进程已启动，会在模型下载完成后自动运行 0-shot 和 3-shot 评估。

当前状态：
- 脚本 `eval_14b_baseline.py` 已上传到服务器
- Qwen3-14B 通过 ModelScope 下载到 `/dev/shm/Qwen3-14B`（约 1.8G/29G 已下载）
- 后台监控脚本 (PID 201294) 会自动等待下载完成后依次运行两次评估
- 结果会写入 `results_14b_0shot.json` 和 `results_14b_3shot.json`
- 4.5 分钟后自动检查进度

---
