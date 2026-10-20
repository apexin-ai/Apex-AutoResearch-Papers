# code plan 002 router sft

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-002-router-sft_20260514T004238_result.json`
- **Structured JSON:** [`61044382c1896204ad8d.json`](../../sessions/61/61044382c1896204ad8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结：

### 发现并修复的问题

**Critical Bug — `death_aware_labeling.py` 不递归子目录**
- 原版 `process_dir` 只在传入目录直接找 `episodes.jsonl`，但数据结构是 `results/prescreening/{task}/episodes.jsonl`
- `launch_plan002.sh` 传入 `results/prescreening` 等父目录，会全部 skip，产出 0 条数据
- **修复**：新增 `expand_input_dirs()` 函数，自动扫描一级子目录

**缺失 — `--dry_run` 支持**
- 原版 `death_aware_labeling.py` 没有 dry_run 参数
- **修复**：添加 `--dry_run` flag，只扫描和打印分布，不写文件

**缺失 — 独立 eval 脚本**
- 训练后只有 `router_sft_train.py` 内建的 val 评估，无独立 eval
- **新建** `src/router_sft_eval.py`：加载 LoRA adapter，eval 同 split 的 held-out 数据，输出 accuracy/F1/confusion matrix，对比 majority-class 和 always-det baselines

**缺失 — `launch_plan002.sh` 无 Step 3**
- **修复**：添加 Step 3 调用 `router_sft_eval.py`

### 已有代码验证结论

| 检查项 | 状态 |
|--------|------|
| 三标签逻辑 (death asymmetry → score comparison) | OK |
| 输出路径 `results/plan_001b_labels/sft_triples.jsonl` | OK |
| `router_sft_train.py` 2-way 分类 (drops no-preference) | OK, 符合设计 |
| SFT 参数 lr=2e-5, batch=32, epochs=3 | OK |
| Episode-level stratified split (防 leakage) | OK |
| `--class_weights auto` (inverse-frequency) | OK, 已有 |
| `--upsample_minority` (WeightedRandomSampler) | OK, 已有 |
| 输出 checkpoint 到 `results/plan_002_router/` | OK |

### Dry-run 结果 (prescreening + research, 145 episodes)
- det-preferred: 68 (46.9%), internal-preferred: 1 (0.7%), no-preference: 76 (52.4%)
- 4386 SFT steps, 其中 training 实际只用 det-preferred + internal-preferred = 2190 steps (no-preference 被 router_sft_train.py 丢弃)
- 极端不平衡（2160 det vs 30 internal）确认——`--class_weights auto --upsample_minority` 是必要的

---
