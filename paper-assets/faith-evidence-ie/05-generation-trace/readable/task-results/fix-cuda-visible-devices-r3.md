# fix cuda visible devices r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cuda_visible_devices_r3_20260516T002708_result.json`
- **Structured JSON:** [`152b291188bd938aaedb.json`](../../sessions/15/152b291188bd938aaedb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s45 训练已正常启动，正在训练中（2/510 steps）。

## 汇报

**1. 诊断结果**
- s43 (PID 277315) **只在 GPU 1**，占 28332MiB，99% 利用率 — 正常
- GPU 2 上的 PID 276148（崩溃的 s45）已退出，GPU 内存已自动释放

**2. 决策：情况 A**
- s43 未跨 GPU，不需要 kill，继续运行

**3. 重提交 PID**
- s45 新 PID: **278776**（nvidia-smi 可见），从 nohup 启动的 wrapper PID 是 278771

**4. 验证结果 — 无跨 GPU 泄漏**

| GPU | PID | 进程 | 显存占用 | 利用率 |
|-----|-----|------|---------|--------|
| 0 | 270467 | eval_flat_nli_s44 | 10846 MiB / 32607 MiB | 44% |
| 1 | 277315 | rsft_ced_s43_train_r3 | 28332 MiB / 32607 MiB | 99% |
| 2 | 278776 | rsft_ced_s45_train_r3 | 27562 MiB / 32607 MiB | 99% |
| 3 | 272169 | eval_flat_nli_s45 | 10850 MiB / 32607 MiB | 43% |

每个进程各占一张卡，所有命令均带 `CUDA_VISIBLE_DEVICES` 前缀，符合 C002 约束。s45 训练日志确认 510 steps 已开始（~4.6s/step）。

---
