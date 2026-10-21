# Repo-Level Eval 预检报告

**日期**: 2026-05-16  
**服务器**: seetacloud-westd-4x5090

---

## 检查结果汇总

| # | 检查项 | 状态 | 备注 |
|---|--------|------|------|
| 1 | eval_repo_verifier.py 存在 | ✅ PASS | 12960B, 可读 |
| 2 | eval_repo_cwm.py 存在 | ✅ PASS | 18764B, 可读 |
| 3 | eval_repo_cls.py 存在 | ✅ PASS | wrapper 脚本使用此文件 |
| 4 | 测试数据 swebench_test.jsonl | ✅ PASS | 9784 行，符合预期 |
| 5 | CLS checkpoint 目录 | ⚠️ PARTIAL | 仅 checkpoint-2211 (epoch 1/3, step 2211/6633) |
| 6 | CWM checkpoint 目录 | ❌ FAIL | 目录为空，无任何 checkpoint |
| 7 | 依赖包 (torch, transformers, peft, sklearn, numpy, datasets, tqdm) | ✅ PASS | 全部已安装 |
| 8 | 磁盘空间 /root/autodl-tmp/ | ✅ PASS | 71GB 可用 |
| 9 | GPU 占用 | ⚠️ INFO | GPU0: 19/31GB, GPU1: 19/31GB (训练进行中) |

---

## 问题与风险

### 1. CWM checkpoint 目录为空
`/root/autodl-tmp/checkpoints_deepseek_cwm_repo/` 无任何文件。可能原因：
- 训练刚启动，尚未达到首个 save_steps
- 训练配置 save_steps 较大

**建议**: 等待 CWM 训练产出首个 checkpoint 后再 eval。

### 2. CLS trainer_state 异常
- `eval_loss: NaN` (epoch 1.0 处)
- `best_model_checkpoint: null`
- 训练仍在进行 (max_steps=6633, 当前 2211, epoch 1/3)

**建议**: eval 时直接用最终 checkpoint（训练结束后目录里最大步数的 checkpoint），不依赖 best_model_checkpoint。

### 3. 默认 model_name 指向 Qwen
`eval_repo_verifier.py` 默认 `--model_name=/root/.cache/huggingface/hub/Qwen/Qwen3-4B`。DeepSeek 训练需覆盖为:
```
/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct
```

---

## Eval 命令模板

### 方式一：使用 wrapper 脚本（推荐，自动检测 model）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /home/sonny/exec-sim-repair-verifier

# CLS eval (训练完成后，cuda:0 空闲时)
./run_repo_eval.sh 0 /root/autodl-tmp/checkpoints_deepseek_cls_repo cls

# CWM eval (训练完成后，cuda:1 空闲时)
./run_repo_eval.sh 1 /root/autodl-tmp/checkpoints_deepseek_cwm_repo cwm
```

### 方式二：直接调用 eval 脚本

#### CLS Eval (eval_repo_verifier.py)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /home/sonny/exec-sim-repair-verifier

CUDA_VISIBLE_DEVICES=0 python3 eval_repo_verifier.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo/checkpoint-2211 \
  --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
  --split test \
  --max_seq_length 8192 \
  --device cuda:0 \
  --output /root/autodl-tmp/eval_results/deepseek_cls_repo_test/eval_repo_cls_results.json \
  --save_predictions
```

#### CWM Eval (eval_repo_cwm.py)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /home/sonny/exec-sim-repair-verifier

CUDA_VISIBLE_DEVICES=1 python3 eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/<CHECKPOINT_NAME> \
  --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
  --split test \
  --max_seq_length 8192 \
  --max_new_tokens 1024 \
  --device cuda:0 \
  --batch_size 8 \
  --output_dir /root/autodl-tmp/eval_results/deepseek_cwm_repo_test \
  --output /root/autodl-tmp/eval_results/deepseek_cwm_repo_test/eval_repo_cwm.json \
  --pred_output /root/autodl-tmp/eval_results/deepseek_cwm_repo_test/eval_repo_cwm_predictions.jsonl
```

> ⚠️ `<CHECKPOINT_NAME>` 待 CWM 训练产出 checkpoint 后替换。

---

## Checkpoint 目录结构

### CLS (`/root/autodl-tmp/checkpoints_deepseek_cls_repo/`)
```
checkpoint-2211/
  ├── adapter_config.json     (base_model: deepseek-coder-6.7b-instruct)
  ├── adapter_model.safetensors
  ├── tokenizer.json, tokenizer_config.json, special_tokens_map.json
  ├── trainer_state.json
  ├── training_args.bin
  ├── optimizer.pt, scheduler.pt, rng_state.pth
  └── chat_template.jinja, README.md
```

### CWM (`/root/autodl-tmp/checkpoints_deepseek_cwm_repo/`)
```
(空)
```

---

## 训练进度

| 任务 | GPU | 当前步数 | 总步数 | Epoch | 最新 loss |
|------|-----|---------|--------|-------|----------|
| CLS (deepseek-cls-repo) | cuda:0 | 2211 | 6633 | 1.0/3.0 | 0.0146 |
| CWM (deepseek-cwm-repo) | cuda:1 | ? | ? | ? | ? |

---

## 结论

CLS eval 流程就绪，等训练完成即可执行。CWM 需等首个 checkpoint 落盘。无依赖阻塞问题。
