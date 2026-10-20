# code d048 batch scripts

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d048_batch_scripts_20260522T102854_result.json`
- **Structured JSON:** [`83990858c48ba3cc49aa.json`](../../sessions/83/83990858c48ba3cc49aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

13 个脚本全部创建完成，已 chmod +x。所有 13 个 output 目录均不存在，无覆盖风险。

汇总：

| 条件 | 脚本数 | 文件 |
|------|--------|------|
| SS | 2 | d048_ss_s123.sh, d048_ss_s456.sh |
| PCGrad | 2 | d048_pcgrad_s123.sh, d048_pcgrad_s456.sh |
| Base | 3 | d048_base_s42.sh, d048_base_s123.sh, d048_base_s456.sh |
| TG | 2 | d048_tg_s123.sh, d048_tg_s456.sh |
| LO | 2 | d048_lo_s123.sh, d048_lo_s456.sh |
| UG | 2 | d048_ug_s123.sh, d048_ug_s456.sh |

加上已有的 d048_ss_s42.sh，共 14 个脚本覆盖 6×3=18 runs。

---
