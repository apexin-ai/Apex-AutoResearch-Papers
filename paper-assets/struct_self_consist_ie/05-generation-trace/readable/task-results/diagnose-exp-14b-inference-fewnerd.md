# diagnose exp 14b inference fewnerd

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_14b_inference_fewnerd_20260520T171838_result.json`
- **Structured JSON:** [`8e857521dbe683ebd7e3.json`](../../sessions/8e/8e857521dbe683ebd7e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志持续增长（6116340 → 6121644），进程确认在运行。

## 诊断结论

**进程未退出。** `exp_14b_inference_fewnerd` 仍在 GPU 0 上运行：

- **已完成**: scierc (n1-n16), conll2003 (n1-n16), fewnerd_n1 — 全部有 `report.json` + `samples.jsonl`
- **进行中**: fewnerd_n2 — 截至日志末尾处理到 16% (12118/75296)，速度 ~10 it/s
- **待跑**: fewnerd_n4, n8, n16
- **PID**: 217960 (VLLM::EngineCore)，31088 MiB on GPU 0
- **日志**: `/tmp/14b_fewnerd.log`，持续写入

**预计 fewnerd_n2 剩余 ~105 分钟**（63K samples ÷ ~10 it/s），之后还有 n4/n8/n16 需要数小时。

**GPU 状态**:
- GPU 0: 98% 占用 (本实验)
- GPU 1: 94% 占用 (另一进程)
- GPU 2/3: 空闲

不更新 registry，不删除 cron — 进程仍在运行，cron 监控应继续保留。

---
