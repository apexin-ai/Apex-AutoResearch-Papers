# code plan 004 launch

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-004-launch_20260515T002637_result.json`
- **Structured JSON:** [`2329a4353f3b5cc7b42d.json`](../../sessions/23/2329a4353f3b5cc7b42d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 都在正常训练：

**GPU 3** (PID 143197) — depth0_only_seed42 正在评估阶段，73/785 步
**GPU 1** (PID 143765) — size_matched_seed42 训练中，43/741 步，~1.73 it/s

## 状态汇总

| GPU | Bash PID | Python PID | Variants | 日志路径 |
|-----|----------|------------|----------|----------|
| cuda:3 | 143189 | 143197 | depth0_only, depth01, all (9 runs) | /tmp/plan004_gpu3.log |
| cuda:1 | 143757 | 143765 | size_matched, binary_filtered (6 runs) | /tmp/plan004_gpu1.log |

## 修改记录
- 删除旧 worker 遗留的 `outputs/plan-004/`（22GB 检查点），释放磁盘至 20GB 可用
- 修改 `finetune_downstream.py`：`save_strategy="no"`, `load_best_model_at_end=False`，避免写大检查点
- 修改 `run_downstream.sh`：VARIANTS 支持环境变量覆盖

## 预估完成时间
- **GPU 1**（6 runs）：每 run ~12 min → ~74 min → **约 09:55 CST**
- **GPU 3**（9 runs）：depth0_only ~10 min + depth01 ~37 min + all ~111 min → ~158 min → **约 11:20 CST**

## 初始训练指标
- GPU 1 size_matched_seed42：Training at 1.73 it/s
- GPU 3 depth0_only_seed42 参考（旧 worker 结果）：eval_loss=0.986, eval_ppl=2.68

---
