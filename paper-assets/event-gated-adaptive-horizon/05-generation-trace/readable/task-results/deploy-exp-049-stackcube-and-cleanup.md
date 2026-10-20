# deploy exp 049 stackcube and cleanup

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp_049_stackcube_and_cleanup_20260522T165111_result.json`
- **Structured JSON:** [`4d246819969ba272886a.json`](../../sessions/4d/4d246819969ba272886a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇报：

**Zombie 清理**：PID 87614 已不存在（ALREADY_DEAD），无需 kill。

**exp_049 部署成功**：
- **PID**: 91395
- StackCube-v1 环境创建成功，Action Space `Box(-1.0, 1.0, (8,), float32)`
- Prefill 完成（2500 steps, 12 episodes），已进入 training 阶段
- ManiSkill 正确 resolve 到 cuda:1：`CVD='1', requested=cuda:0, resolved=cuda:1`

**GPU 分布**：
| GPU | PID | 实验 | 显存 |
|-----|-----|------|------|
| GPU 0 | 88654 | exp_048 Cheetah CIVO extension | 3361 MiB |
| GPU 1 | 91395 | exp_049 StackCube CIVO trigger s0 | 794 MiB (正在增长) |

注：PID 91395 在 GPU 0 有 643 MiB 小额分配，来自 `fork_rng` 初始化所有 CUDA 设备，不影响 Cheetah 实验。

---
