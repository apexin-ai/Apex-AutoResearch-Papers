# ssh traj collect resume

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_traj-collect-resume_20260514T141730_result.json`
- **Structured JSON:** [`9e694572e918ed0c8053.json`](../../sessions/9e/9e694572e918ed0c8053.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收集已成功启动并在运行：

- **已有状态**: 400 成功 / 175 失败，已 resume
- **新采样**: 575 个 game，过滤已完成后剩 474 个新 episode
- **Workers**: 4 个并发
- **PID**: 61438
- **日志**: `/root/runs/tax_error_inject_agent/collect_traj_r2.log`

474 个新尝试按 ~70% 成功率可产出 ~330 条成功轨迹，远超所需的 100 条。脚本会在达到 500 条成功后自动停止。

**预计完成时间**: 之前 575 次尝试的耗时可参考，100 条成功约需 143 次尝试。按每条轨迹平均 ~30-60 秒 API 交互、4 并发，预计 **30-60 分钟**完成。

---
