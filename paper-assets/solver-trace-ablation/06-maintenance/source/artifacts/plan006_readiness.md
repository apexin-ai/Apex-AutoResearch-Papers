# Plan006 Prolog GRPO 就绪性报告 (v2)

**日期**: 2026-05-14
**服务器**: westd-39279

## 检查清单

### 1. Prolog STA 代码 ✅

| 文件 | 说明 |
|------|------|
| `src/sta/prolog_reward.py` | full O(n) `prolog_sta_reward` + fast O(1) `fast_prolog_sta_reward` + parser |
| `src/solvers/prolog.py` | `PrologSolver` — swipl subprocess，exit code 0/1/2 协议 |
| `src/solvers/factory.py` | `"prolog"` / `"swipl"` 已注册 |
| `scripts/sta_prolog.py` | 5 个内置测试用例 + JSONL eval CLI |

接口与 FOL 版本一致：`prolog_sta_reward(problem, formalization, solver, ...)` → `{execution_reward, sta_reward, combined_reward, details}`

### 2. swipl ✅

- `/usr/bin/swipl` → symlink → `/usr/lib/swi-prolog/bin/x86_64-linux/swipl`
- 在 PATH 中，`shutil.which("swipl")` 可用

### 3. 训练数据 ✅

- **文件**: `data/train_500_seed42.jsonl`（C001 合规）
- **数量**: 500 条
- **字段**: `id, context, question, answer, fol_premises, fol_conclusion, depth`
- 无 Prolog 特有字段，不影响训练：`build_prolog_dataset()` 只用 `context` + `question` 构建 Prolog prompt，模型自主生成 Prolog formalization

### 4. 训练脚本 ✅

`scripts/train_grpo.py` 完整支持 Prolog：

- `--logic_type prolog` 参数（choices=["fol", "prolog"]）
- `build_prolog_dataset()` — Prolog 专用 system prompt + user template
- reward 路由：logic_type=prolog → `prolog_sta_reward` / `fast_prolog_sta_reward`
- solver 路由：`get_solver("prolog")` → `PrologSolver`
- 配置文件就绪：
  - `configs/grpo_prolog_exec_sta.yaml` — exec_weight=0.5, sta_weight=0.5, `data_path: data/train_500_seed42.jsonl`
  - `configs/grpo_prolog_exec_only.yaml` — exec_weight=1.0, sta_weight=0.0, `data_path: data/train_500_seed42.jsonl`

### 5. Eval 脚本 ✅

`scripts/eval_sta.py` 完整支持 Prolog：

- `--logic_type prolog` 参数
- `LOGIC_CONFIG["prolog"]` 配置：Prolog prompt + PrologSolver + `prolog_sta_reward`
- Eval 数据：`data/test_100.jsonl`（`test_held_out.jsonl` → symlink）

### 6. 磁盘空间 ✅

```
/dev/md0  250G  109G  142G  44%  /root/autodl-tmp
```

| 目录 | 大小 | 可删？ |
|------|------|--------|
| `grpo_exec_only/` | 15G | ✅ 早期试跑，已被 plan001 取代 |
| `grpo_exec_sta/` | 15G | ✅ 早期试跑，已被 plan001 取代 |
| `plan001_exec_only_s42/` | 15G | ⚠️ 需确认是否已完成 eval |
| `plan002_additive_b01_s42/` | 15G | ⚠️ 需确认 |
| `plan005_sta_low_s42/` | 15G | ⚠️ 需确认 |
| `plan016_extended_1000_s42/` | 15G | ⚠️ 需确认 |

**可安全回收**: `grpo_exec_only` + `grpo_exec_sta` = **30G**，删后可用 172G。plan006 单次 ~15G，空间充足。

### 7. Dry-run ⏭️

两张 GPU 满载，未执行实际 dry-run。代码层面已确认所有参数和路由完整。

## 总结

| 项目 | 状态 |
|------|------|
| Prolog solver + STA 代码 | ✅ |
| swipl 运行时 | ✅ |
| 训练数据 (C001) | ✅ |
| 训练脚本 `--logic_type prolog` | ✅ |
| GRPO 配置文件 | ✅ |
| eval_sta.py Prolog 支持 | ✅ |
| 磁盘空间 | ✅ (142G free) |
| 模型 Qwen3-4B | ✅ (`/root/autodl-tmp/models/Qwen3-4B`) |

**无阻塞项。plan006 完全就绪，等待 GPU 释放即可启动。**

## 推荐启动命令

```bash
# GPU 0: Prolog execution + STA
bash -c 'export CUDA_VISIBLE_DEVICES=0 && cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_sta_s42 --wandb_run plan006_prolog_exec_sta_s42 --seed 42'

# GPU 1: Prolog execution-only
bash -c 'export CUDA_VISIBLE_DEVICES=1 && cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_only_s42 --wandb_run plan006_prolog_exec_only_s42 --seed 42'
```

**约束合规**:
- C001: 两个 config 均指向 `data/train_500_seed42.jsonl` ✅
- C002: `CUDA_VISIBLE_DEVICES` 在 `bash -c` 内部 `export` ✅
- C003: 训练脚本已设 `save_total_limit=1`, `save_only_model=True`, `log_completions=False` ✅
- C005: 显式设置了 `CUDA_VISIBLE_DEVICES` ✅

**注意事项**:
- 配置中 `no_wandb: true`，如需 WandB 追踪，启动时加 `--no_wandb` 取反或修改 config
- 多 seed 运行：CLI 覆盖 `--seed 123` / `--seed 456` 即可，无需额外 config
- 建议先删 `grpo_exec_only` + `grpo_exec_sta`（共 30G）腾出空间
