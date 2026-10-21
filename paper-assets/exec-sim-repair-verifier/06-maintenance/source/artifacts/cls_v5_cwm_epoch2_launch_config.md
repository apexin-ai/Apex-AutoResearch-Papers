# CLS v5 Retrain & CWM s42 Epoch 2 Eval — Launch Config

Generated: 2026-05-17

## 磁盘状态

```
/dev/md0  250G  185G  66G  74%  /root/autodl-tmp
```

66G 可用，足够。

---

## Command 1: CLS v5 Retrain (GPU 0)

```bash
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 \
/root/miniconda3/bin/python train_unified.py \
    --data_dir data/ \
    --task cls \
    --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
    --output_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/ \
    --run_name deepseek-cls-repo-v5 \
    --seed 42 \
    --max_seq_length 2048 \
    --batch_size 2 \
    --grad_accumulation 16 \
    --lr 2e-4 \
    --epochs 3 \
    --no_wandb
```

### 参数确认（复刻 v4）

| 参数 | 值 | 来源 |
|------|-----|------|
| model | deepseek-coder-6.7b-instruct | adapter_config.json |
| data | data/swebench_full/swebench_train.jsonl (70748 samples) | 自动检测 |
| val | data/swebench_full/swebench_val.jsonl (9335 samples) | 自动检测 |
| batch_size | 2 | training_args.bin |
| grad_accumulation | 16 | training_args.bin |
| lr | 2e-4 | training_args.bin |
| epochs | 3 | training_args.bin |
| warmup_ratio | 0.1 | training_args.bin |
| seed | 42 | training_args.bin |
| max_seq_length | 2048 | script default, FLOPS analysis confirms avg ~1011 tok/sample |
| lora_rank | 16 | adapter_config.json |
| lora_alpha | 32 | adapter_config.json |
| lora_dropout | 0.05 | adapter_config.json |
| target_modules | q_proj, k_proj, v_proj, o_proj | adapter_config.json |
| save_strategy | epoch | current script |
| eval_strategy | epoch | current script |

预计 steps: 6633 (2211/epoch), ~7.5s/step on 5090, 约 13.8 小时完成。

---

## Command 2: CWM s42 Epoch 2 Eval (GPU 2)

```bash
cd /home/sonny/exec-sim-repair-verifier && \
mkdir -p /root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_epoch2/ && \
CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 \
/root/miniconda3/bin/python eval_repo_cwm.py \
    --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-8844 \
    --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
    --split test \
    --max_seq_length 8192 \
    --max_new_tokens 512 \
    --batch_size 1 \
    --device cuda:0 \
    --output_dir /root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_epoch2/ \
    2>&1 | tee /root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_epoch2/eval.log
```

### 参数确认

| 参数 | 值 | 说明 |
|------|-----|------|
| checkpoint | checkpoint-8844 | epoch 2 (确认自 trainer_state.json: step=8844, epoch=2.0) |
| test data | swebench_test.jsonl (9784 samples) | eval_repo_cwm.py 默认 data_dir |
| max_seq_length | 8192 | 与 run_deepseek_repo_eval.sh 一致 |
| max_new_tokens | 512 | 与 run_deepseek_repo_eval.sh 一致 |

预计耗时：9784 samples / ~6.5 samples/sec ≈ 25 min（参考 CWM eval_runtime ~1424s for 9335 samples）。

---

## 注意事项

1. **Tokenizer BatchEncoding 陷阱已修复**: `train_unified.py` 的 `_extract_ids()` 函数正确处理 `apply_chat_template(tokenize=True)` 返回 BatchEncoding 的情况，通过 `hasattr(result, "input_ids")` 提取。

2. **CLS v4 只跑了 2 epochs**: trainer_state 显示 v4 在 step 4422 (epoch 2) 停止，max_steps=6633 (3 epochs)。v5 retrain 会跑完整 3 epochs。

3. **CWM s42 epoch 2 eval 目的**: 判断 CWM repo 在 epoch 3 (ckpt-13266) 的退化是过拟合还是 formulation-inherent。如果 epoch 2 表现优于 epoch 3，则确认过拟合。

4. **wandb**: CLS v5 用了 `--no_wandb` 以避免依赖。如需 wandb 记录，去掉此 flag（wandb project 默认 `exec-sim-repair-verifier`）。

5. **CUDA_VISIBLE_DEVICES 与 --device**: eval 脚本里写 `--device cuda:0`，但 `CUDA_VISIBLE_DEVICES=2` 使物理 GPU 2 映射为 cuda:0。

6. **output_dir 无冲突**: `/root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/` 和 eval output 目录均不存在。
