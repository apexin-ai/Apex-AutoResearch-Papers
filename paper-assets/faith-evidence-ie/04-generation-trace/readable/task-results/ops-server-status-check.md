# ops server status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server_status_check_20260516T113437_result.json`
- **Structured JSON:** [`47d4c908dea080492d53.json`](../../sessions/47/47d4c908dea080492d53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. GPU 占用情况

| GPU | 显存占用 | 进程 | PID |
|-----|---------|------|-----|
| cuda:0 | 0 MiB / 32607 MiB | 空闲 | — |
| cuda:1 | 11415 MiB / 32607 MiB | plan_002_test_eval_s44_r2 (inference) | 319638 |
| cuda:2 | 18421 MiB / 32607 MiB | plan_006_qwen3_8b_no_evidence_eval_v2 (inference) | 335357 |
| cuda:3 | 23737 MiB / 32607 MiB | plan_016_llama_3_1_8b_no_evidence_sft (training) | 333916 |

### 2. plan_006_qwen3_8b_no_evidence_eval_v2

**PID=335357, GPU=cuda:2**

启动于服务器时间 19:17，正在运行 inference，命令含 `--no_evidence` 参数（C005 合规）。

### 3. plan_006_qwen3_1_7b_no_evidence_eval — cron 误判

**是 cron 误判，实验正常完成。** 日志末尾打印了完整 metrics，`predictions.json` 和 `metrics.json` 均存在，推理耗时 6178.8s。

但注意：config 中 `"no_evidence": false`，说明这次 eval **漏传了 `--no_evidence`**，违反 C005。结果科学上无效（训练用 no_evidence prompt，eval 用了含 evidence 的 prompt），这解释了 evi_f1=0.0007 的极低值。进程本身没有 crash。

### 4. Cron 监控实验进程状态

| 实验 | PID | 状态 |
|------|-----|------|
| plan_002_test_eval_s44_r2 | 319632 | **存活**，已运行 3h21m |
| plan_016_llama_3_1_8b_sft | 331871 | **已完成** (19:33:44 UTC)，train_loss=0.5246，模型保存于 `/root/autodl-tmp/sft_output_llama_3_1_8b` |
| plan_016_llama_3_1_8b_no_evidence_sft | 333911 | **存活**，已运行 29m |

---
