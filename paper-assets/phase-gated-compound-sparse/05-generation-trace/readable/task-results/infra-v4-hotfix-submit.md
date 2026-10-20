# infra v4 hotfix submit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_v4-hotfix-submit_20260513T232341_result.json`
- **Structured JSON:** [`87bac50090b07ee92e7b.json`](../../sessions/87/87bac50090b07ee92e7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 报告

**代码同步验证**：`PARSE OK` — `--masking_method` 和 `--sparsity_levels` CLI 参数正常解析。4 个目标路径 md5 一致。

**4 个实验已 RUNNING**：

| exp_id | GPU | PID | GPU Util | VRAM |
|--------|-----|-----|----------|------|
| mvp_v4a_r2 | cuda:0 | 31119 | 96% | 79 GB / 98 GB |
| mvp_v4b_r2 | cuda:1 | 31481 | 95% | 50 GB / 98 GB |
| mvp_v4c_r2 | cuda:2 | 31839 | 97% | 50 GB / 98 GB |
| mvp_v4_random_r2 | cuda:3 | 32187 | 99% | 44 GB / 98 GB |

日志：`/tmp/mvp_v4{a,b,c,_random}_r2.log`

---
