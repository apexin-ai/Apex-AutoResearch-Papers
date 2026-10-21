# code plan 010 check and analyze

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_010_check_and_analyze_20260516T062453_result.json`
- **Structured JSON:** [`549faf90a0da8c3875fb.json`](../../sessions/54/549faf90a0da8c3875fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程都在运行。

**状态报告：**

| 项目 | 状态 |
|------|------|
| **Extraction** | 完成 — trained 10/10 (24GB), untrained 10/10 (25GB), 两个 EXIT_CODE=0 |
| **RSA 分析** | 已启动 — PID 708431, tmux `plan010_rsa_spatial`, cuda:0 (实际 CPU-only), timeout 4h |
| **Action probe** | 已启动 — PID 708576, tmux `plan010_action_probe_spatial`, cuda:0+1 (双 GPU 并行 trained/untrained), timeout 6h |
| **GPU** | 2x H800 97GB, 当前 0% 利用率（数据加载阶段） |

**日志路径：**
- RSA: `/root/autodl-tmp/vla-ssd/logs/rsa_spatial.log`
- Probe: `/root/autodl-tmp/vla-ssd/logs/action_probe_spatial.log`

**结果输出：**
- RSA: `/root/autodl-tmp/vla-ssd/results/rsa/rsa_libero_spatial.json`
- Probe: `/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_libero_spatial.json`

---
