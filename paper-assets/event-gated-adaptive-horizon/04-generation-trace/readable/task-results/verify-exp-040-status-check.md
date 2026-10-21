# verify exp 040 status check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp_040_status_check_20260522T065118_result.json`
- **Structured JSON:** [`e0dbb477d7cb3537db14.json`](../../sessions/e0/e0dbb477d7cb3537db14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 有 YAML 解析错误，但服务器侧信息已足够。

**exp_040 状态汇报：**

| 项目 | 结果 |
|------|------|
| PID 52397 | **ALIVE**，已运行 **3h50m26s**，CPU 1164% |
| metrics.jsonl 最近写入 | epoch timestamp `1779432674`（即刚刚在活跃写入） |
| 当前 step | **135,000** |
| FPS | 9.28 |
| gate_dt | 全部锁定在 dt=2（`gate_dt_2_frac=1.0`，empirical entropy=0） |
| registry status | 读取失败（YAML 解析错误，registry 文件约第 6465 行有格式问题，需修复） |

值得注意：gate 完全退化为常量 dt=2，没有任何自适应行为（entropy=0, autocorr=0）。actor_entropy 也极低（0.032）。如需干预请告知。

---
