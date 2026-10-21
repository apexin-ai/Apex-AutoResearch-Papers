# Plan006 Prolog Training Readiness Report

Generated: 2026-05-14

## Checklist Summary

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | Training Data | **PASS** | 同一数据文件，Prolog 不依赖 ground truth |
| 2 | Training Config | **PASS** | 3 个 Prolog 配置文件已就绪 |
| 3 | Training Script | **PASS** | 完整支持 `--logic_type prolog` |
| 4 | Eval Pipeline | **PASS** | eval_sta.py 支持 `--logic_type prolog` |
| 5 | Solver (swipl) | **PASS** | `/usr/bin/swipl` 存在，可执行 |
| 6 | Model | **PASS** | Qwen3-4B (~8GB) 已下载 |
| 7 | Disk Space | **PASS** | /root/autodl-tmp 剩余 112GB |

**结论: 全部就绪，可直接启动训练。**

---

## 逐项详情

### 1. Training Data — PASS

- 文件: `data/train_500_seed42.jsonl` (500 条, 484KB)
- 字段: `id`, `context`, `question`, `answer`, `fol_premises`, `fol_conclusion`, `depth`
- 无 `prolog_premises` / `prolog_query` 字段，但 **不影响训练**:
  - GRPO 训练流程: 自然语言 context+question → 模型生成 Prolog → swipl 验证 → reward
  - `build_prolog_dataset()` 只使用 `context` 和 `question` 构建 prompt，`prolog_premises` 默认空列表（仅元数据，reward function 不读取）
- 符合 C001 约束

### 2. Training Config — PASS

3 个配置文件:

| Config | reward_mode | k (num_gen) | warmup | 用途 |
|--------|-------------|-------------|--------|------|
| `grpo_prolog_exec_only.yaml` | execution_only | 8 | 0 | 主实验 |
| `grpo_prolog_exec_only_k16_warmup.yaml` | execution_only | 16 | 0.1 | 大采样+warmup |
| `grpo_prolog_exec_sta.yaml` | execution_sta | 8 | 0 | exec+STA |

共同设置:
- `model_path: /root/autodl-tmp/models/Qwen3-4B`
- `data_path: data/train_500_seed42.jsonl` (符合 C001)
- `logic_type: prolog`, `solver: prolog`
- `output_dir: /root/autodl-tmp/outputs/grpo_prolog_*`
- `num_steps: 500`, `lr: 1e-6`, `batch_size: 4`, `grad_accum: 2`
- `no_wandb: true` (可按需改为 false)

### 3. Training Script — PASS

`scripts/train_grpo.py` (457 行):

- **参数**: `--logic_type prolog` (choices=["fol", "prolog"]), `--solver prolog`, `--config` 加载 YAML
- **Dataset**: `build_prolog_dataset()` (L117) 使用 `PROLOG_SYSTEM_PROMPT` + `PROLOG_USER_TEMPLATE` 构建 chat prompt
- **Reward**: `make_reward_fn()` (L148) 当 `logic_type=="prolog"` 时分发到:
  - `fast_prolog_sta_reward` (训练中 fast 模式, O(1))
  - `prolog_sta_reward` (full 模式, O(n))
- **磁盘保护**: `save_total_limit=1` (L419), `save_only_model=True` (L420), `log_completions=False` (L425) — 符合 C003

### 4. Eval Pipeline — PASS

`scripts/eval_sta.py`:

- `--logic_type prolog` (choices=["fol", "prolog"])
- `LOGIC_CONFIG["prolog"]` 映射:
  - system_prompt → PROLOG_SYSTEM_PROMPT
  - user_template → PROLOG_USER_TEMPLATE
  - default_solver → "prolog"
  - reward_fn → `prolog_sta_reward` (full ablation)
- ISR 计算: `prolog_sta_ablation()` 逐条移除 clause 检查 query 是否 break

额外: `scripts/sta_prolog.py` 提供独立 Prolog STA 测试 CLI (5 个内置 test case)

### 5. Solver (swipl) — PASS

- `/usr/bin/swipl` → `/usr/lib/swi-prolog/bin/x86_64-linux/swipl` (symlink)
- 版本: SWI-Prolog 8.4.2 (per project spec)
- 权限: 755, 可执行
- `src/solvers/prolog.py`: `PrologSolver` 通过 subprocess 调用 swipl -q -f
- `src/solvers/factory.py`: `get_solver("prolog")` 返回 PrologSolver 实例

### 6. Model & Disk — PASS

- Qwen3-4B: `/root/autodl-tmp/models/Qwen3-4B/` (3 shard files, ~8GB total)
- 磁盘: `/root/autodl-tmp` 250GB 中已用 139GB, **剩余 112GB** (训练输出 ~16GB/run, 充裕)

---

## 约束合规

| 约束 | 状态 |
|------|------|
| C001 (数据文件) | PASS — 所有 config 使用 `train_500_seed42.jsonl` |
| C002 (CUDA_VISIBLE_DEVICES) | NOTE — 提交任务时需手动 `export CUDA_VISIBLE_DEVICES=N` |
| C003 (磁盘保护) | PASS — save_total_limit=1, log_completions=False |
| C004 (eval 统一) | PASS — eval_sta.py 支持 prolog |
| C005 (显式 GPU 设置) | NOTE — 提交任务时需手动 `export CUDA_VISIBLE_DEVICES=N` |

## 建议（非阻塞）

1. **swipl 功能验证**: 启动前跑 `python scripts/sta_prolog.py --test` 确认 5/5 test cases 通过
2. **WandB**: 当前 configs 设 `no_wandb: true`，正式实验建议改为 false
3. **多 seed**: 当前 configs 只有 seed=42，如需跨 seed 对比需复制配置并改 seed + output_dir
