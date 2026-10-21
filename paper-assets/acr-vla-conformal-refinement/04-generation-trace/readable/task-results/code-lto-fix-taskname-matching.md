# code lto fix taskname matching

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lto-fix-taskname-matching_20260519T032257_result.json`
- **Structured JSON:** [`e1f503b5a30f70cce1f0.json`](../../sessions/e1/e1f503b5a30f70cce1f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常启动，过滤逻辑正确：从 14570 总样本中筛出 7499 个样本，覆盖 5 个 train task，名称完全正确。

## 修复总结

### 修改的文件
1. **`train_crm.py`**: `--task_indices` (numeric) → `--task_names` (substring)，过滤逻辑从 numeric ID 索引改为通过 `task_mapping.json` 做 name substring 匹配（下划线自动转空格）
2. **`evaluate.py`**: `--task_indices` (numeric) → `--task_names` (substring)，过滤逻辑从 `task_envs[j]` 位置索引改为遍历 `task_name` 做 substring 匹配

### 验证清单
1. ✅ train_crm.py 用 `--task_names` 字符串匹配
2. ✅ evaluate.py 用 `--task_names` 字符串匹配
3. ✅ train 选中 5 个 task: alphabet_soup/bbq_sauce/butter/chocolate_pudding/cream_cheese (7499 samples)
4. ✅ eval 将选中 5 个 task: ketchup/milk/orange_juice/salad_dressing/tomato_sauce
5. ✅ train 和 eval 零重叠

### 训练
- **exp_id**: `crm-lto-splitA-train-fixed`
- **GPU**: cuda:2 (RTX 4090)
- **预估时长**: ~1-2h (50 epochs, 7499 samples, obs_only mode)

### 训练完成后 eval 命令
```bash
python evaluate.py --benchmark object --mode crm_obs_only \
  --checkpoint /root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt \
  --task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce' \
  --n_rollouts 20 \
  --output_file logs/eval_lto_splitA_fixed.json
```

---
