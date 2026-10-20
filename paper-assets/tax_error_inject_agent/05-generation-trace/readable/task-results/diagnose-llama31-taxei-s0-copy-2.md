# diagnose llama31 taxei s0

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama31-taxei-s0_20260516T102134_result.json`
- **Structured JSON:** [`f182a43f0fad1dd039b7.json`](../../sessions/f1/f182a43f0fad1dd039b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**失败原因：tmux session 被 AutoDL 平台中断（SIGHUP）**

证据：

| 检查项 | 结果 |
|--------|------|
| **训练日志** | v0 正常运行到 step 1120/3387（epoch 0.99），无任何错误/traceback，突然中断 |
| **显存** | 全程稳定 30.73 GiB，**非 OOM** |
| **GPU 状态** | 同服务器其他任务（vanilla cuda:0, random cuda:2）仍在运行，排除系统级故障 |
| **磁盘** | 58% (145G/250G)，充足 |
| **checkpoint** | v0 成功保存了 checkpoint-1129（epoch 1 完整 checkpoint，~500MB），保存完成后被杀 |
| **dmesg** | AutoDL 容器无权限读取，无法确认 OOM killer |
| **tmux** | 原 session 已不存在，新 session 于 18:18 创建 |

**判断**：进程在完成 epoch 1 checkpoint 保存（step 1129）后不久收到 SIGHUP。训练指标完全正常（loss ~0.41-0.48 稳步下降，grad_norm 稳定），排除代码/配置问题。最大可能是 AutoDL 平台侧的网络/调度抖动导致 tmux 控制终端丢失。

## 当前状态

**v1 已自动重启**，目前在 step 97/3387 正常训练中。但这是从头开始的，没有 resume v0 的 checkpoint。

## 建议

- v1 正在运行，让它继续即可，无需改配置
- v0 的 `checkpoint-1129`（epoch 1）完好保存在 `output/llama31-taxei-s0/v0-20260516-171606/checkpoint-1129/`，如果 v1 再次失败可以从此 checkpoint resume，避免浪费 epoch 1 的训练时间
- 这是 AutoDL 平台的偶发问题，非可复现 bug

---
