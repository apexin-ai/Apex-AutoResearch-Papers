# deploy exp 084 085 logiqa seed123

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp-084-085-logiqa-seed123_20260519T223240_result.json`
- **Structured JSON:** [`20bf1d3f97f70a61cf71.json`](../../sessions/20/20bf1d3f97f70a61cf71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功部署。

## 汇总

| 实验 | exp_id | GPU | PID | vLLM Port | 状态 |
|------|--------|-----|-----|-----------|------|
| exp-084 | `exp-084-debate-mistral-logiqa-seed123` | cuda:1 | 295372 | 8001 | RUNNING，[1/200] 进行中 |
| exp-085 | `exp-085-contrastive-mistral-logiqa-seed123` | cuda:2 | 295533 | 8002 | RUNNING，[1/200] 进行中 |

- 两个 dry-run 均验证通过（前 2-3 题无报错）
- vLLM 复用已有实例（port 8001/8002 均 READY，模型 Mistral-7B-Instruct-v0.3）
- 预计每个实验 ~2-3 小时（exp-085 contrastive ETA ~100-187 min）

---
