# verify kill after n8

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_kill_after_n8_20260520T205629_result.json`
- **Structured JSON:** [`157f7fbea8d4b096193c.json`](../../sessions/15/157f7fbea8d4b096193c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。

## 结论

**PID 230885（VLLM::EngineCore）**：存活，状态 Rl（运行中）。

**kill_after_n8 监控（PID 224789）**：存活，正在运行。脚本 `/root/autodl-tmp/kill_after_n8.sh` 每 15 秒检查日志中是否出现 `=== FewNERD N=8 finished`，触发后会：
- kill 编排脚本 PID 200995（`bash run_14b_fewnerd.sh`，仍存活）
- pkill 所有 `run_mvp_pilot.py.*fewnerd` 和 `VLLM::EngineCore` 进程

监控逻辑正确，目标 PID 200995 也仍存活，无需重新部署。

**当前推理进度**：
| 数据集 | N=1 | N=2 | N=4 | N=8 | N=16 |
|--------|-----|-----|-----|-----|------|
| SciERC | done | done | done | done | done |
| CoNLL2003 | done | done | done | done | done |
| FewNERD | done | done | **39% 进行中** | 未开始 | 将被 kill |

FewNERD N=4 于 04:09 开始，当前处理 14543/37648（39%），速度约 8-12 it/s，预计还需约 40 分钟完成 N=4。N=8 完成后监控脚本将自动终止进程，阻止 N=16 运行。

---
