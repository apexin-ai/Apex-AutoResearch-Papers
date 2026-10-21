# D008 Eval Command Templates

准备日期: 2026-05-13
目的: 训练完成后零延迟启动 eval

---

## CLS v5 Eval (home-1x5090)

checkpoint 路径模板: `/root/autodl-tmp/checkpoints_repo_cls_v5/checkpoint-{BEST}`
注: best checkpoint 需从 `trainer_state.json` 读取

### argparse 参数一览

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--checkpoint_dir` | (必填) | LoRA checkpoint 目录 |
| `--model_name` | `Qwen/Qwen3-4B` | base model 名称/路径 |
| `--data_dir` | `data/swebench_full` | 测试数据目录 (含 swebench_test.jsonl) |
| `--output` | `eval_repo_cls.json` | 汇总指标 JSON 输出 |
| `--pred_output` | `eval_repo_cls_predictions.jsonl` | 逐条预测 JSONL 输出 |
| `--batch_size` | `16` | 推理 batch size |
| `--max_seq_length` | `2048` | 输入最大 token 长度 |
| `--device` | `cuda:0` | 推理设备 |
| `--dry_run` | (flag) | 仅测试数据加载，不做推理 |

注: `max_new_tokens=8` 硬编码在 `run_inference` 中 (L144)，CLS 只输出 pass/fail 标签。

```bash
# CLS v5 eval (home-1x5090)
cd /home/sonny/exec-sim-repair-verifier
python3 eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_v5/checkpoint-{BEST} \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --output /root/autodl-tmp/eval_results/cls_v5/eval_repo_cls.json \
  --pred_output /root/autodl-tmp/eval_results/cls_v5/eval_repo_cls_predictions.jsonl \
  --batch_size 16 \
  --max_seq_length 2048 \
  --device cuda:0
```

运行前:
```bash
mkdir -p /root/autodl-tmp/eval_results/cls_v5
```

---

## CWM v11 Eval (seetacloud-westd-4x5090)

checkpoint 路径模板: `/root/autodl-tmp/checkpoints_repo_cwm_v11/checkpoint-{BEST}`

### argparse 参数一览

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--checkpoint_dir` | (必填) | LoRA checkpoint 目录 |
| `--model_name` | `Qwen/Qwen3-4B` | base model 名称/路径 |
| `--data_dir` | `data/swebench_full` | 测试数据目录 (含 swebench_test.jsonl) |
| `--output` | `eval_repo_cwm.json` | 汇总指标 JSON 输出 |
| `--pred_output` | `eval_repo_cwm_predictions.jsonl` | 逐条预测 JSONL 输出 |
| `--batch_size` | `8` | 推理 batch size |
| `--max_seq_length` | `2048` | 输入最大 token 长度 |
| `--max_new_tokens` | `1024` | 生成最大 token 数 (CWM 生成执行轨迹) |
| `--device` | `cuda:0` | 推理设备 |
| `--dry_run` | (flag) | 仅测试数据加载，不做推理 |
| `--max_samples` | `None` | 限制测试样本数量 |
| `--output_dir` | `None` | 输出目录 (默认脚本所在目录) |

### 三组 max_new_tokens 消融

```bash
# 环境变量 (westd 离线模式)
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1

mkdir -p /root/autodl-tmp/eval_results/cwm_v11_tok1024
mkdir -p /root/autodl-tmp/eval_results/cwm_v11_tok512
mkdir -p /root/autodl-tmp/eval_results/cwm_v11_tok256
```

```bash
# CWM v11 eval — max_new_tokens=1024 (primary)
cd /home/sonny/exec-sim-repair-verifier
python3 eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_v11/checkpoint-{BEST} \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --output_dir /root/autodl-tmp/eval_results/cwm_v11_tok1024 \
  --output eval_repo_cwm.json \
  --pred_output eval_repo_cwm_predictions.jsonl \
  --batch_size 8 \
  --max_seq_length 2048 \
  --max_new_tokens 1024 \
  --device cuda:0
```

```bash
# CWM v11 eval — max_new_tokens=512 (ablation)
cd /home/sonny/exec-sim-repair-verifier
python3 eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_v11/checkpoint-{BEST} \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --output_dir /root/autodl-tmp/eval_results/cwm_v11_tok512 \
  --output eval_repo_cwm.json \
  --pred_output eval_repo_cwm_predictions.jsonl \
  --batch_size 8 \
  --max_seq_length 2048 \
  --max_new_tokens 512 \
  --device cuda:0
```

```bash
# CWM v11 eval — max_new_tokens=256 (ablation)
cd /home/sonny/exec-sim-repair-verifier
python3 eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_v11/checkpoint-{BEST} \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --output_dir /root/autodl-tmp/eval_results/cwm_v11_tok256 \
  --output eval_repo_cwm.json \
  --pred_output eval_repo_cwm_predictions.jsonl \
  --batch_size 8 \
  --max_seq_length 2048 \
  --max_new_tokens 256 \
  --device cuda:0
```

注: westd 上用系统 python3（不激活 conda）。

---

## Paired Bootstrap (D008 Go/No-Go)

### argparse 参数一览

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--cls_preds` | (必填) | CLS predictions JSONL |
| `--cwm_preds` | (必填) | CWM predictions JSONL |
| `--n_bootstrap` | `10000` | bootstrap 重采样次数 |
| `--seed` | `42` | 随机种子 |
| `--tost_margin` | `2.0` | TOST 等价性检验 margin (pp) |
| `--output` | `paired_bootstrap_repo_results.json` | 输出 JSON |
| `--dry_run` | (flag) | 仅加载预测并显示统计，跳过 bootstrap |

### CLS v5 vs CWM v11 (primary, tok1024)

```bash
cd /home/sonny/exec-sim-repair-verifier
python3 paired_bootstrap_repo.py \
  --cls_preds /root/autodl-tmp/eval_results/cls_v5/eval_repo_cls_predictions.jsonl \
  --cwm_preds /root/autodl-tmp/eval_results/cwm_v11_tok1024/eval_repo_cwm_predictions.jsonl \
  --n_bootstrap 10000 \
  --seed 42 \
  --tost_margin 2.0 \
  --output /root/autodl-tmp/eval_results/d008_paired_bootstrap_cls_v5_vs_cwm_v11_tok1024.json
```

### CLS v5 vs CWM v11 (ablation, tok512)

```bash
python3 paired_bootstrap_repo.py \
  --cls_preds /root/autodl-tmp/eval_results/cls_v5/eval_repo_cls_predictions.jsonl \
  --cwm_preds /root/autodl-tmp/eval_results/cwm_v11_tok512/eval_repo_cwm_predictions.jsonl \
  --output /root/autodl-tmp/eval_results/d008_paired_bootstrap_cls_v5_vs_cwm_v11_tok512.json
```

### CLS v5 vs CWM v11 (ablation, tok256)

```bash
python3 paired_bootstrap_repo.py \
  --cls_preds /root/autodl-tmp/eval_results/cls_v5/eval_repo_cls_predictions.jsonl \
  --cwm_preds /root/autodl-tmp/eval_results/cwm_v11_tok256/eval_repo_cwm_predictions.jsonl \
  --output /root/autodl-tmp/eval_results/d008_paired_bootstrap_cls_v5_vs_cwm_v11_tok256.json
```

---

## 执行顺序

1. 训练完成 → 从 `trainer_state.json` 读取 best checkpoint step，替换 `{BEST}`
2. CLS eval (home-1x5090) + CWM eval tok1024 (westd) 可并行
3. CWM tok512 和 tok256 消融串行（同一 GPU）
4. CLS predictions 需从 home 传到 westd（或反之），再跑 paired bootstrap
5. 解读 paired bootstrap 结果 → D008 Go/No-Go 决策
