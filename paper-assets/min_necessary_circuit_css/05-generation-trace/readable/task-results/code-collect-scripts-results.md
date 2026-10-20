# code collect scripts results

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_collect-scripts-results_20260512T135902_result.json`
- **Structured JSON:** [`e1f3c48b11efb151c8d5.json`](../../sessions/e1/e1f3c48b11efb151c8d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part A: ACDC 状态
- **仍在运行** (PID 98594, 已运行 ~1h02m)
- 进度：**21458/32491 (66%)**，~2.57 it/s
- 预计剩余：**~71 分钟**
- 当前阶段：正在逐条移除边（Removed 21328, Left 130），正在处理 A7 层的 Q/K/V 边
- 日志输出到 `/root/min_necessary_circuit_css/mvp_output.log`

### Part B: collect_results.py
- 已部署到 `/root/structfuse-mvp/collect_results.py` (2489 bytes)
- 语法验证通过
- ACDC 完成后执行：`cd /root/structfuse-mvp && python3 collect_results.py`

### Part C: test_l0_ep.sh
- 已部署到 `/root/structfuse-mvp/test_l0_ep.sh` (1603 bytes, +x)
- 语法验证通过
- **未执行**（GPU-5 被 ACDC 占用）
- ACDC 完成后执行：`bash /root/structfuse-mvp/test_l0_ep.sh`

---
