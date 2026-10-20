# code deploy and train

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deploy-and-train_20260513T015001_result.json`
- **Structured JSON:** [`4725908eb464ee3a231b.json`](../../sessions/47/4725908eb464ee3a231b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**Phase 1 - 代码同步**: 4 个文件（networks.py, models.py, tools.py, configs.yaml）已上传到服务器，行数验证通过。

**Phase 2 - 代码验证**:
- Import 测试通过
- Baseline dry-run (gate_enabled=false): 成功运行到 step 60，无错误
- Event-gated dry-run (gate_enabled=True): 成功运行到 step 60，无错误
- 注意：`--gate_enabled` 参数需要大写 `True`（非 `true`），`--logdir` 必须显式指定

**Phase 3 - 正式训练已启动**:
| 实验 | GPU | PID | Logdir |
|------|-----|-----|--------|
| exp_001_baseline | cuda:0 | 9409 | `logdir/baseline_s1` |
| exp_002_event_gated | cuda:1 | 9769 | `logdir/event_gated_s1` |

两个训练各 500K steps，当前在 prefill 阶段（baseline 已收集 4 episodes）。预计 1-2 小时完成。

---
