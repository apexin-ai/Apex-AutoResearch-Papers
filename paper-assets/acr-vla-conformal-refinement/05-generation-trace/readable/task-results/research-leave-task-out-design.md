# research leave task out design

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_leave-task-out-design_20260519T022146_result.json`
- **Structured JSON:** [`1fb0b69d341e31e34b2d.json`](../../sessions/1f/1fb0b69d341e31e34b2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the information needed. Let me compile the complete design.

---

## 汇报：Leave-Task-Out 泛化实验设计

### 1. Precomputed Features 结构

**位置**: `/root/autodl-tmp/crm_cache/{benchmark}/`

**文件格式**: 3 个 flat tensor + 1 个 manifest
- `obs_features.pt` — `(N, 960)` VLM hidden features
- `k_samples.pt` — `(N, K=10, H_eff=5, D=6)` K 次采样的 pose actions
- `expert_actions.pt` — `(N, H_eff=5, D=6)` expert demo actions
- `manifest.json` — `{benchmark, n_samples, K, obs_dim, action_dim, h_eff}`

**关键问题**: 当前缓存**没有 per-task 索引**，所有 task 的 samples 混在一起。且 **object 缓存为空**（只有 spatial 有 2402 samples）。

**数据来源**: `load_libero_demos()` 按 hdf5 文件名排序加载 → `build_training_samples()` 按 trajectory 顺序展开为 timestep samples，每个 sample 含 `task_name` 字段，但 precompute 存储时**丢弃了 task_name**。

**现有 CRM 训练情况**: crm_v3_norm 模型仅在 spatial 10 tasks 的缓存上训练（2402 samples, max_demos_per_task=10），但在 object benchmark 上也做了 eval（live SmolVLA inference）。

---

### 2. LIBERO-Object 10 Tasks

**LIBERO Benchmark API 顺序**（evaluate.py 使用此顺序）:

| Idx | Task Name |
|-----|-----------|
| 0 | pick_up_the_alphabet_soup_and_place_it_in_the_basket |
| 1 | pick_up_the_cream_cheese_and_place_it_in_the_basket |
| 2 | pick_up_the_salad_dressing_and_place_it_in_the_basket |
| 3 | pick_up_the_bbq_sauce_and_place_it_in_the_basket |
| 4 | pick_up_the_ketchup_and_place_it_in_the_basket |
| 5 | pick_up_the_tomato_sauce_and_place_it_in_the_basket |
| 6 | pick_up_the_butter_and_place_it_in_the_basket |
| 7 | pick_up_the_milk_and_place_it_in_the_basket |
| 8 | pick_up_the_chocolate_pudding_and_place_it_in_the_basket |
| 9 | pick_up_the_orange_juice_and_place_it_in_the_basket |

**注意**: HDF5 文件是按字母序排列的（alphabet_soup, bbq_sauce, butter, ...），与 benchmark API 顺序**不同**。代码修改时必须用 task name 匹配，不能用 index。

每个 task 50 demos，avg ~150 steps/demo。

---

### 3. Split 定义

| | Split A (train) | Split A (eval) |
|---|---|---|
| Benchmark idx | 0-4 | 5-9 |
| Tasks | alphabet_soup, cream_cheese, salad_dressing, bbq_sauce, ketchup | tomato_sauce, butter, milk, chocolate_pudding, orange_juice |

Split B 反过来。

---

### 4. 需要的代码修改

#### 4.1 train_crm.py — 3 处修改

**(a) 新增 `--task_names` 参数**

```python
p.add_argument("--task_names", type=str, default=None,
               help="Comma-separated task name substrings to include (e.g., 'alphabet_soup,cream_cheese')")
```

**(b) precompute 时保存 task_names**

在 `precompute_features()` 中，`build_training_samples()` 返回的 samples 都有 `task_name`。在保存 partial cache 和 merge 时，同步保存 `task_names` list:

```python
# 在 precompute 循环中，与 exp_buf 并列：
name_buf.append([s["task_name"] for s in batch_samples])

# 在 _try_merge() 最后：
torch.save(task_names_list, cache_dir / "task_names.json")
# 或者存为 json
```

**(c) train 时按 task_names 过滤**

在 `train()` 中加载缓存后，如果 `--task_names` 不为 None：

```python
if args.task_names:
    allowed = set(args.task_names.split(","))
    task_names = json.loads((cache_dir / "task_names.json").read_text())
    mask = [any(a in tn for a in allowed) for tn in task_names]
    indices = [i for i, m in enumerate(mask) if m]
    obs_features = obs_features[indices]
    k_samples = k_samples[indices]
    expert_actions = expert_actions[indices]
```

**替代方案（更简单，不修改 precompute）**: 在 `load_libero_demos()` 中按 task name 过滤 trajectory，然后直接用 `--auto` 让每个 split 分别 precompute。将不同 split 的 cache 存到不同目录。

```python
# utils.py load_libero_demos() 修改：
def load_libero_demos(benchmark_name, data_dir=..., max_demos_per_task=50,
                      task_name_filter=None):
    ...
    for hdf5_file in hdf5_files:
        task_name = hdf5_file.stem.replace("_demo", "").replace("_", " ")
        if task_name_filter and not any(f in task_name for f in task_name_filter):
            continue
        ...
```

#### 4.2 evaluate.py — 1 处修改

新增 `--task_indices` 参数，过滤 eval tasks：

```python
p.add_argument("--task_indices", type=str, default=None,
               help="Comma-separated task indices to evaluate (e.g., '5,6,7,8,9')")

# 在 evaluate() 函数的 rollout 循环中：
eval_task_indices = None
if args.task_indices:
    eval_task_indices = set(int(x) for x in args.task_indices.split(","))

for idx, task_info in enumerate(task_envs):
    if eval_task_indices is not None and idx not in eval_task_indices:
        task_info["env"].close()
        continue
    ...
```

---

### 5. 具体训练命令

使用替代方案（不修改 precompute，用过滤后的 demo 分别 precompute + train）：

```bash
cd /root/acr-vla-conformal-refinement/src

# Split A: train on tasks 0-4
python train_crm.py --benchmark object \
  --task_names "alphabet_soup,cream_cheese,salad_dressing,bbq_sauce,ketchup" \
  --cache_dir /root/autodl-tmp/crm_cache_lto/splitA \
  --output_dir /root/autodl-tmp/checkpoints/crm_lto/splitA \
  --input_mode obs_only --epochs 50 --batch_size 32 --lr 1e-3 \
  --max_demos_per_task 50 --seed 42 --auto

# Split B: train on tasks 5-9
python train_crm.py --benchmark object \
  --task_names "tomato_sauce,butter,milk,chocolate_pudding,orange_juice" \
  --cache_dir /root/autodl-tmp/crm_cache_lto/splitB \
  --output_dir /root/autodl-tmp/checkpoints/crm_lto/splitB \
  --input_mode obs_only --epochs 50 --batch_size 32 --lr 1e-3 \
  --max_demos_per_task 50 --seed 42 --auto
```

---

### 6. 具体 Eval 命令

```bash
# Split A: trained on 0-4, eval on 5-9 (held-out)
python evaluate.py --benchmark object \
  --mode crm_obs_only \
  --checkpoint /root/autodl-tmp/checkpoints/crm_lto/splitA/crm_best.pt \
  --task_indices 5,6,7,8,9 \
  --K 10 --n_rollouts 20 --seed 42 \
  --output_file logs/lto_splitA_heldout_eval.json

# Split B: trained on 5-9, eval on 0-4 (held-out)
python evaluate.py --benchmark object \
  --mode crm_obs_only \
  --checkpoint /root/autodl-tmp/checkpoints/crm_lto/splitB/crm_best.pt \
  --task_indices 0,1,2,3,4 \
  --K 10 --n_rollouts 20 --seed 42 \
  --output_file logs/lto_splitB_heldout_eval.json

# 同时跑 in-distribution eval 作为对照
python evaluate.py --benchmark object \
  --mode crm_obs_only \
  --checkpoint /root/autodl-tmp/checkpoints/crm_lto/splitA/crm_best.pt \
  --task_indices 0,1,2,3,4 \
  --K 10 --n_rollouts 20 --seed 42 \
  --output_file logs/lto_splitA_indist_eval.json

python evaluate.py --benchmark object \
  --mode crm_obs_only \
  --checkpoint /root/autodl-tmp/checkpoints/crm_lto/splitB/crm_best.pt \
  --task_indices 5,6,7,8,9 \
  --K 10 --n_rollouts 20 --seed 42 \
  --output_file logs/lto_splitB_indist_eval.json
```

---

### 7. 预估时间和资源

| 阶段 | 预估样本数 | 预估时间 |
|------|-----------|---------|
| Precompute Split A (5 tasks × 50 demos) | ~36,500 | ~6.5 hours |
| Precompute Split B (5 tasks × 50 demos) | ~36,500 | ~6.5 hours |
| Train Split A (50 epochs) | - | ~15 min |
| Train Split B (50 epochs) | - | ~15 min |
| Eval Split A held-out (5 tasks × 20 rollouts) | - | ~20-30 min |
| Eval Split B held-out (5 tasks × 20 rollouts) | - | ~20-30 min |
| Eval in-dist (×2) | - | ~40-60 min |
| **总计** | | **~15 hours** |

**降速方案**: 用 `--max_demos_per_task 10` 可将 precompute 从 13h 降到 ~1h（但训练数据减少 5 倍），训练 ~10 min/split。

**GPU**: 1× RTX 4090 24GB，precompute 和 eval 各需要 ~8GB VRAM（SmolVLA），train 仅需 ~1GB。所有阶段可在同一 GPU 上串行运行。

---

### 8. 注意事项

1. **Task name 匹配陷阱**: HDF5 文件排序和 LIBERO benchmark API 的 task 顺序不同。代码修改中必须用 task name 字符串匹配，不能依赖数字 index。
2. **norm_stats**: 当前的 `norm_stats.pt` 是从 spatial-only 数据计算的。Leave-task-out 实验中，建议分别用各 split 的训练数据重新计算 norm stats，或直接用未归一化模式（如果已有不归一化的训练路径）。
3. **Precompute 可复用**: 如果先用 `--max_demos_per_task 50` 预计算全部 10 tasks 的 object cache 并保存 task_names，则两个 split 可以共享同一份 cache，只在 train 时过滤。这样 precompute 只跑一次 ~13h。

---
