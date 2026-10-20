# Repo-Level Eval 基础设施就绪性报告

**检查时间**: 2026-05-12 13:25 (home) / 2026-05-13 04:25 (seetacloud)

---

## 1. home-1x5090 (sonny@home) — Repo-Level CLS

### 训练状态
- **进程**: PID 2840848, GPU 0 (RTX 5090), 19GB VRAM, 97% util
- **命令**: `python3 train_repo_verifier.py --output_dir checkpoints_repo_cls_home/ --no_wandb`
- **进度**: step ~1606/6633 (24%), ~7s/step, 已跑 ~3h08m
- **预估剩余**: ~10h

### Eval 就绪状态

| 项目 | 状态 | 说明 |
|------|------|------|
| Eval 脚本 | ✅ | `eval_repo_level.py` — 统一 CLS/CWM eval，支持 `--mode cls/cwm` |
| Val 数据 | ✅ | `data/swebench_full/swebench_val.jsonl` (9,335 samples) |
| Test 数据 | ✅ | `data/swebench_full/swebench_test.jsonl` (9,784 samples) |
| 基础模型 | ✅ | `~/.cache/huggingface/hub/models--Qwen--Qwen3-4B` |
| torch | ✅ | 可导入 |
| peft | ✅ | 可导入 |
| sklearn | ✅ | 可导入 |
| datasets | ✅ | 可导入 |
| 磁盘 | ✅ | 351GB 可用 |
| **Checkpoints** | ❌ **严重** | `checkpoints_repo_cls_home/` **完全为空** |

### ❌ 严重问题：Checkpoint 未保存

训练配置 `save_strategy="steps"`, `save_steps=200`, `save_total_limit=3`。当前 step 1606，应有 checkpoint-1200/1400/1600。但：
- 目录完全为空（无文件、无子目录）
- 日志中 0 条 "Saving" 记录
- 日志中 0 条 "eval_loss" 记录（eval_strategy="steps", eval_steps=200 也未触发）
- 日志大小仅 99KB（只有 progress bar 输出）

**Trainer 的 eval 和 save 回调均未执行。** 训练正常推进但无持久化。若不修复，训练完成后仅靠末尾 `trainer.save_model(best_dir)` 保存最终模型（前提是 `load_best_model_at_end=True` 不会因缺少 eval metric 而报错）。

**建议**：立即排查 Trainer callback 为何未触发。

### Eval 启动命令模板（假设 checkpoint 可用后）

```bash
cd /home/sonny/exec-sim-repair-verifier

# Val set eval
python3 eval_repo_level.py \
  --mode cls \
  --checkpoint_dir checkpoints_repo_cls_home/best \
  --model_name Qwen/Qwen3-4B \
  --output eval_repo_cls_val.json \
  --save_predictions \
  --device cuda:0

# Test set eval
python3 eval_repo_level.py \
  --mode cls \
  --checkpoint_dir checkpoints_repo_cls_home/best \
  --model_name Qwen/Qwen3-4B \
  --output eval_repo_cls_test.json \
  --save_predictions \
  --device cuda:0
```

---

## 2. seetacloud-westd-4x5090 (root@seetacloud) — Repo-Level CWM v6

### 训练状态
- **进程**: PID 84887, GPU 2 (4x RTX 5090), 22GB VRAM, 96% util
- **命令**: `python3 train_repo_cwm.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v6/ --no_wandb`
- **进度**: step ~175/6633 (2.6%), ~8.5s/step, 已跑 ~1h
- **预估剩余**: ~15h
- **备注**: step 150 处已成功执行 eval（9335 samples, 12m33s） — eval 回调正常

### Eval 就绪状态

| 项目 | 状态 | 说明 |
|------|------|------|
| CWM Eval 脚本 | ✅ | `eval_repo_cwm.py` — CWM 专用 |
| CLS Eval 脚本 | ✅ | `eval_repo_verifier.py` — CLS 专用 |
| 统一 Eval 脚本 | ❌ | `eval_repo_level.py` 不存在（仅在 home） |
| Val 数据 | ✅ | `data/swebench_full/swebench_val.jsonl` (9,335 samples) |
| Test 数据 | ✅ | `data/swebench_full/swebench_test.jsonl` (9,784 samples) |
| 基础模型 | ✅ | `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B` |
| peft | ✅ | 可导入（conda base） |
| sklearn | ✅ | 可导入 |
| Checkpoints | ⏳ | 空（符合预期 — save_steps=500, 当前 step 175） |

### 注意事项

1. **model_name 默认值需覆盖**：`eval_repo_cwm.py` 默认 `--model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B`，实际在 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B`
2. **eval 默认 device=cuda:3**：训练在 GPU 2，eval 可用 GPU 0/1/3
3. **train_repo_cwm.py 只在 seetacloud 上存在**（home 无此文件）

### Eval 启动命令模板

```bash
cd /home/sonny/exec-sim-repair-verifier
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# CWM v6 eval
python3 eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_v6/best \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
  --output eval_repo_cwm_v6_results.json \
  --device cuda:3

# CLS eval（需将 home 的 checkpoint 传过来或在 home 上跑）
python3 eval_repo_verifier.py \
  --checkpoint_dir <CLS_CHECKPOINT_PATH> \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
  --output eval_repo_cls_results.json \
  --save_predictions \
  --device cuda:3
```

---

## 3. 缺失项清单

| # | 优先级 | 项目 | 说明 |
|---|--------|------|------|
| 1 | P0 | home CLS checkpoint 未保存 | Trainer eval/save 回调未触发，1606 步无持久化 |
| 2 | P1 | seetacloud 缺 `eval_repo_level.py` | 非阻塞，用 `eval_repo_cwm.py` 替代 |
| 3 | P1 | eval 脚本读哪个 split 需确认 | 需读 eval 脚本 main() 确认默认读 test 还是 val |
| 4 | P2 | seetacloud eval 默认 model_name 错误 | 启动时显式传 `--model_name` 即可 |

---

## 4. Checkpoint 当前状态

| 服务器 | 目录 | 内容 |
|--------|------|------|
| home | `checkpoints_repo_cls_home/` | **空** ❌（异常） |
| seetacloud | `/root/autodl-tmp/checkpoints_repo_cwm_v6/` | **空**（预期内，首存在 step 500） |

### 训练时间线预估

| 服务器 | 总步数 | 当前步 | 速度 | 预估完成时间 |
|--------|--------|--------|------|-------------|
| home | 6633 | ~1606 | ~7s/step | ~2026-05-12 23:30 |
| seetacloud | 6633 | ~175 | ~8.5s/step | ~2026-05-13 18:30 |

### Eval 所需数据汇总

| 文件 | home | seetacloud | 行数 |
|------|------|-----------|------|
| swebench_train.jsonl | ✅ | ✅ | 70,748 |
| swebench_val.jsonl | ✅ | ✅ | 9,335 |
| swebench_test.jsonl | ✅ | ✅ | 9,784 |
