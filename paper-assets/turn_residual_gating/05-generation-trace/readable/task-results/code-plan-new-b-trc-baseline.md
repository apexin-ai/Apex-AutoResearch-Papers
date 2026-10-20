# code plan new b trc baseline

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_new_b_trc_baseline_20260520T070905_result.json`
- **Structured JSON:** [`f7ed3d0262a665e46612.json`](../../sessions/f7/f7ed3d0262a665e46612.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。全部代码准备完毕，验证结果：

**创建的文件：**
- `src/trc_measure.py` — TRC/TBP 测量模块（`compute_trc`, `compute_tbp`, `measure_trc_and_tbp`）
- `src/eval_trc_baseline.py` — eval 脚本，支持 TF/gen/both 三种模式，三种 checkpoint 类型
- `scripts/launch_trc_baseline.sh` — 批量跑 v7 TG / LoRA-only / base 三组

**Dry-run 结果（base model, 1 conv, TF）：**
- TRC = 0.189（9 个 turn pair，range 0.006–0.723）
- TBP CE = 0.553, PPL = 1.74
- hidden states 提取 + cos_sim 计算 + JSON 输出全部正常
- 耗时 ~24s（含模型加载），GPU 占用约 15GB

**未启动完整 eval。** 跑 `bash scripts/launch_trc_baseline.sh` 即可启动全量评测。

---
