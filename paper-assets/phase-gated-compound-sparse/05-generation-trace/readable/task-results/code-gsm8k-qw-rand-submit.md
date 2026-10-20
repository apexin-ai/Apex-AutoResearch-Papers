# code gsm8k qw rand submit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k_qw_rand_submit_20260515T215748_result.json`
- **Structured JSON:** [`63edd9facbd49c499ce6.json`](../../sessions/63/63edd9facbd49c499ce6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已提交并在运行：

| 实验 | GPU | tmux session | 状态 |
|------|-----|-------------|------|
| `gsm8k_qw_rand_s025` | cuda:0 | gsm8k_qw_rand_s025 | RUNNING，已开始处理 1/50 |
| `gsm8k_qw_rand_s030` | cuda:1 | gsm8k_qw_rand_s030 | RUNNING，模型加载中 |

注意：s030 首次提交因 `--device cuda:1` 在 `CUDA_VISIBLE_DEVICES=1` 下找不到设备而失败，已改为 `--device cuda:0` 重新提交成功（框架自动映射物理 GPU）。Registry 已更新。

---
