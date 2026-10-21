# check nlp control urgent

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_nlp_control_urgent_20260522T115218_result.json`
- **Structured JSON:** [`0e84fdf01a5d9976539c.json`](../../sessions/0e/0e84fdf01a5d9976539c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 项目 | 状态 |
|------|------|
| **模型下载** | **进行中 ~90%** — shard 2/2 已完成 (3.3G)，shard 1/2 正在下载 8.34G/9.29G，速度 ~340 KB/s |
| **预计完成** | 剩余 ~0.95 GB，按当前速度约 **45-50 分钟**（~20:10 左右） |
| **wait_and_run** | 已启动（PID 613207），正在 sleep 60 循环等待下载完成 |
| **Probing** | **未启动** — results 目录只有初始 run.log（仅一行 "Waiting for model download"） |
| **GPU** | 2× GPU 完全空闲（0% util, 0 MiB used, 各 ~96 GB — 应为 H800/A800） |
| **R² 数据** | 不存在，probing 尚未执行 |

**结论**：下载被 HuggingFace 代理限速（~340 KB/s），已跑了 6.5 小时。shard 1 完成后 wait_and_run 会自动触发 probing。预计还需约 50 分钟。

---
