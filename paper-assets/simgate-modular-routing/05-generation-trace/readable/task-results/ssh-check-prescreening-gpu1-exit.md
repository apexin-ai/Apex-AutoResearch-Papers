# ssh check prescreening gpu1 exit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-prescreening-gpu1-exit_20260513T220635_result.json`
- **Structured JSON:** [`9481cd2e8c68d8b2d5d3.json`](../../sessions/94/9481cd2e8c68d8b2d5d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**research-prescreening-gpu1 完成。** Registry 已更新为 DONE/success，cron 已清除。

结果汇总：8/8 tasks 全部 POSITIVE，全部 **death-dominated** 信号：

| Task | int_mean | det_mean | delta |
|------|----------|----------|-------|
| measure-melting-point-unknown-substance | -58.6 | -32.0 | +26.6 |
| mendelian-genetics-known-plant | -60.0 | -20.0 | +40.0 |
| mendelian-genetics-unknown-plant | -60.0 | -40.0 | +20.0 |
| power-component | -60.0 | -20.0 | +40.0 |
| power-component-renewable-vs-nonrenewable | -60.0 | 0.0 | +60.0 |
| test-conductivity | -60.0 | -20.0 | +40.0 |
| test-conductivity-of-unknown-substances | -60.0 | -20.0 | +40.0 |
| use-thermometer | -59.4 | -19.4 | +40.0 |

模式一致：internal mode 在 3/5 episodes 触发 -100（致死动作），deterministic mode 大幅避免死亡（det scores 多为 0），但正向任务进展极少。Delta 完全由死亡规避驱动。

---
