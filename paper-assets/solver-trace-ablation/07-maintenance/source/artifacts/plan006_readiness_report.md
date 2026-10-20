# Plan006 Prolog GRPO Readiness Report

**Date**: 2026-05-14 (updated)  
**Status**: ✅ READY — 代码/数据/eval 全部就绪，待 GPU 空闲即可启动

## 检查结果

### 1. Prolog 数据
- **不需要单独的 Prolog 数据文件**。训练数据仍使用 `data/train_500_seed42.jsonl`（500 条，C001 compliant）
- `build_prolog_dataset()` 使用相同 JSONL 但切换 prompt 为 Prolog 格式（`PROLOG_SYSTEM_PROMPT`），让模型将 NL 形式化为 Prolog 而非 FOL
- 实验设计正确：相同 NL 输入，不同形式化目标

### 2. 训练代码
- `train_grpo.py` **完全支持** Prolog：
  - `--logic_type prolog` + `--solver prolog` CLI 参数已实现
  - `build_prolog_dataset()` 使用 `PROLOG_SYSTEM_PROMPT` / `PROLOG_USER_TEMPLATE`
  - `make_reward_fn()` 在 `logic_type == "prolog"` 时自动切换到 `prolog_sta_reward` / `fast_prolog_sta_reward`
- Reward 代码：`src/sta/prolog_reward.py` 完整实现（parse、ablation、ISR 计算）
- Solver 代码：`src/solvers/prolog.py` 完整实现（`PrologSolver` via swipl subprocess）

### 3. SWI-Prolog 集成
- `swipl` 位置：`/usr/bin/swipl`，版本 8.4.2 ✅
- 简单证明测试：PASSED ✅
- `sta_prolog.py` 测试套件：**5/5 PASSED** ✅

### 4. Config
三份 Prolog 配置均已就位：

**grpo_prolog_exec_only.yaml**（plan006-prolog-exec-s42）：
- `data_path: data/train_500_seed42.jsonl`（C001 ✅）
- `logic_type: prolog`, `solver: prolog`, `reward_mode: execution_only`
- `exec_weight: 1.0`, `sta_weight: 0.0`
- `num_steps: 500`, `batch=4`, `grad_accum=2`, `k=8`, `lr=1e-6`
- `save_total_limit=1` hardcoded in GRPOConfig（C003 ✅）

**grpo_prolog_exec_sta.yaml**（plan006-prolog-sta-s42）：
- 同上但 `reward_mode: execution_sta`, `exec_weight: 0.5`, `sta_weight: 0.5`

**grpo_prolog_exec_only_k16_warmup.yaml**（备选变体）：
- `num_generations: 16`, `warmup_ratio: 0.1`，其余同 exec_only

### 4.5 eval_sta.py Prolog 支持
- `eval_sta.py` 已支持 `--logic_type prolog`（LOGIC_CONFIG 注册了 prolog_sta_reward + swipl solver + Prolog prompt）
- C004 compliant：跨 run ISR 对比可统一使用 eval_sta.py ✅

### 5. Dry-run
- `python scripts/train_grpo.py --help` 正常运行 ✅
- 非阻塞警告：vLLM 版本兼容性提示、kernels 包缺失（CPU gemm only，不影响训练）

### 6. 资源
- 磁盘：`/root/autodl-tmp/` 112GB 可用（较之前下降，仍足够）✅
- 模型：`/root/autodl-tmp/models/Qwen3-4B` 已就位（另有 Qwen3-4B-ms 备份）

## 启动命令模板

3 seeds (42/43/44)，每次占 1 张 GPU：

```bash
# Seed 42 (GPU N)
export CUDA_VISIBLE_DEVICES=N
cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
nohup python scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_only.yaml \
  --seed 42 \
  --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42 \
  --wandb_run plan006_prolog_exec_s42 \
  --no_wandb \
  > /root/autodl-tmp/outputs/plan006_prolog_exec_s42.log 2>&1 &

# Seed 43 (GPU M)
export CUDA_VISIBLE_DEVICES=M
nohup python scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_only.yaml \
  --seed 43 \
  --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 \
  --wandb_run plan006_prolog_exec_s43 \
  --no_wandb \
  > /root/autodl-tmp/outputs/plan006_prolog_exec_s43.log 2>&1 &

# Seed 44 (GPU M2)
export CUDA_VISIBLE_DEVICES=M2
nohup python scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_only.yaml \
  --seed 44 \
  --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44 \
  --wandb_run plan006_prolog_exec_s44 \
  --no_wandb \
  > /root/autodl-tmp/outputs/plan006_prolog_exec_s44.log 2>&1 &
```

CLI `--seed` / `--output_dir` 会覆盖 YAML 中的默认值，无需为每个 seed 创建单独 config。

## 注意事项
- 启动前替换 N/M/M2 为实际空闲 GPU 编号（C002: 必须 export，不能 inline）
- 如需 wandb 追踪，去掉 `--no_wandb` 并确保 `--wandb_project solver-trace-ablation`
- 每 seed 训练 500 steps（configs 中 num_steps=500），单卡预计 10-15 小时
- `prolog_premises`/`prolog_query` 字段在数据中不存在，`build_prolog_dataset()` fallback 为空值——不影响训练（reward 从模型输出中解析 Prolog 代码）
