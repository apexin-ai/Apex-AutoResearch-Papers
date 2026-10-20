# diagnose 14b fewnerd final

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_14b_fewnerd_final_20260520T203444_result.json`
- **Structured JSON:** [`3a87c40cf5f3eb2d9b48.json`](../../sessions/3a/3a87c40cf5f3eb2d9b48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**exp_14b_inference_fewnerd 最终状态：DONE / failed**

- **日志**：`/tmp/14b_fewnerd.log` 不存在（实例重启清空 /tmp）
- **输出文件**：服务器上零个 14b 相关输出文件，output 目录从未创建
- **完成的 N 值**：无可用产出。之前诊断称完成了 FewNERD N=1 和 N=2 进行中（24%），但进程退出后无任何落盘数据
- **GPU 0**：当前被 PID 804665 占用（30.5GB，应为 32B 训练）
- **Cron**：已删除
- **N=16**：按之前决定不跑

Registry 已更新 status=DONE, conclusion=failed, notes 记录了完整失败原因。

---
