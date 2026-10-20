# research read p2 result

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_read_p2_result_20260516T102422_result.json`
- **Structured JSON:** [`81fed1b54f28266779b2.json`](../../sessions/81/81fed1b54f28266779b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**状态：仍在运行中**（进程 PID 720674，CPU 205%，已用内存 ~5.2GB，启动于 18:17）

**已产出的结果文件** (`demo_sensitivity_25.json`)：

| 指标 | 50 demos | 25 demos |
|------|----------|----------|
| RSA (layer 0) | 0.0484 | 0.0198 |
| Probe R² (layer 0) | 0.6448 | 0.5709 |

- 只有 layer 0 的单点结果，`rsa_profile_correlation` 和 `probe_profile_correlation` 均为 `null`（需要多层数据才能算 profile 相关）
- 条件：`trained_image_mean`，subsample seed=42，10 tasks
- 耗时 50.7 秒完成了这部分

**日志文件**为空（stdout 重定向到日志但尚无新输出），exit 文件不存在 → 进程尚未退出。

脚本当前仍在 GPU 1 上运行，可能正在处理更多层或其他条件的计算。

---
