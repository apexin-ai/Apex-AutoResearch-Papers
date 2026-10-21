# ops plan006 readiness check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan006-readiness-check_20260514T055701_result.json`
- **Structured JSON:** [`5cd42a1277b2021011e4.json`](../../sessions/5c/5cd42a1277b2021011e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan006 Prolog GRPO 就绪性报告

**所有 6 项检查全部 ✅，无阻塞项。**

| 项目 | 状态 |
|------|------|
| Prolog STA 代码 (`prolog_reward.py`, `prolog.py`, factory) | ✅ |
| swipl (`/usr/bin/swipl`, 在 PATH) | ✅ |
| 训练数据 (`train_500_seed42.jsonl`, 500条, C001合规) | ✅ |
| 训练脚本 (`--logic_type prolog` 完整支持) | ✅ |
| Eval 脚本 (`eval_sta.py --logic_type prolog` 完整支持) | ✅ |
| 磁盘 (142G free, 单次~15G) | ✅ |

**vs 旧报告变化**: 此前标记的 4 个 ❌（config data_path、eval_sta Prolog 支持、multi-seed、WandB）已全部修复。configs 已指向 `train_500_seed42.jsonl`，`eval_sta.py` 已有完整 Prolog 支持。

**磁盘建议**: `grpo_exec_only` + `grpo_exec_sta`（各 15G）为早期试跑，可安全删除回收 30G。

**启动命令模板**已写入报告，遵守 C001-C005 全部约束。等 GPU 释放即可跑。

报告已更新至 `artifacts/plan006_readiness.md`。

---
