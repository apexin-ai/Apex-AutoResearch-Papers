# ssh final collect launch v73

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_final-collect-launch-v73_20260517T191556_result.json`
- **Structured JSON:** [`269851d11ae046df212d.json`](../../sessions/26/269851d11ae046df212d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Config validation passed. Here's the current status:

## v7.2 Eval 结果（3/4 suites 完成，libero_10 进行中）

| Suite | α=0.0 | α=1.0 | Baseline |
|-------|-------|-------|----------|
| libero_spatial | 59.4% | 61.0% | 66.0% |
| libero_object | 65.6% | 66.2% | 67.8% |
| libero_goal | **78.6%** | **78.0%** | 76.4% |
| libero_10 | IN PROGRESS | IN PROGRESS | 54.2% |
| avg (3 done) | 67.9% | 68.4% | 70.1% |

## v7.3 启动前验证
- test_v73_t2.py: TIMEOUT（需加载模型，SSH 30s 限制）
- Config validation: **PASS** (`connector_lora`, rank=8, scale=1.0, drift=0.0)
- 训练脚本: `run_v73_connector_lora.sh` ✓, `run_connector_only.sh` ✓

## 阻塞：无法启动 v7.3 训练

**两张 GPU 都被 v7.2 eval 占用：**
- GPU 0: PID 40598, α=0.0 eval, libero_10 进度 ~10/500 episodes
- GPU 1: PID 44022, α=1.0 eval, libero_10 进度 ~10/500 episodes

每个 suite 约 1.5-2h，libero_10 刚开始 ~15min，预计还需 **~1.5h** 完成。

Per **C004**: 禁止在有活跃进程的 GPU 上启动新任务。需等 eval 完成后再启动 v7.3 训练。

**下一步选项：**
1. 等 eval 完成后手动启动训练
2. 我定期轮询，eval 完成后自动启动
3. 先 kill eval（丢失 libero_10 数据），立即启动训练

选哪个？

---
