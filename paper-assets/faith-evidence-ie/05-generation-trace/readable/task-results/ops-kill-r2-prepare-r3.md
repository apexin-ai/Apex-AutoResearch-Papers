# ops kill r2 prepare r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-r2-prepare-r3_20260514T113128_result.json`
- **Structured JSON:** [`6b74ac98b604905da2d0.json`](../../sessions/6b/6b74ac98b604905da2d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。汇总如下：

---

## Part 1: r2 Kill 确认

- PID 39556 已 force kill（`kill_job` 返回 `force_killed: true`）
- tmux session `mvp2_grpo_ced_r2` 已清理
- GPU 状态：**4× 0%, 0 MiB — 全部释放**

## Part 2: KL 早停 Callback 已添加

代码 diff（`/root/autodl-tmp/freige/training/grpo_trainer.py`）：

| 行号 | 修改内容 |
|------|---------|
| 24 | import 加入 `TrainerCallback` |
| 30-39 | 新增 `KLDivergenceCallback` 类（on_log 检测 `kl > max_kl` 时触发 `should_training_stop`） |
| 376-377 | 新增 `--max_kl` CLI 参数，默认 100.0 |
| 492 | 创建 `callbacks = [KLDivergenceCallback(max_kl=args.max_kl)]` |
| 501 | `GRPOTrainer` 构造传入 `callbacks=callbacks` |

## Part 3: 单 GPU 运行方式

无 `PartialState`/`accelerate` 硬依赖。`local_rank` 仅从 `os.environ.get("LOCAL_RANK", 0)` 获取，单卡默认 0。

**单卡启动命令**：
```bash
CUDA_VISIBLE_DEVICES=0 python -m freige.training.grpo_trainer --stage 3 ...
```
无需 `accelerate launch`。

## Part 4: 后续实验就绪状态

| 实验 | 代码 | 数据 | 依赖 | 可启动? | 建议 GPU |
|------|------|------|------|---------|----------|
| mvp2_grpo_ced_r3 | ✅ `training/grpo_trainer.py` stage=3 | ✅ docred/ | ✅ SFT adapter + NLI model | ✅ | cuda:0 |
| mvp2_sft_eval | ✅ `eval/run_eval.py` | ✅ docred/dev.json | ✅ SFT adapter at `/root/autodl-tmp/sft_output` | ✅ | cuda:1 |
| mvp2_grpo_extract | ✅ `training/grpo_trainer.py` stage=1, ced_weight=0 | ✅ docred/ | ✅ SFT adapter | ✅ | cuda:2 |
| mvp2_grpo_flatnli | ✅ `training/grpo_trainer.py` stage=2 (auto flat_nli) | ✅ docred/ | ✅ SFT adapter + NLI model | ✅ | cuda:3 |

- NLI cache 独立目录不存在（`/root/autodl-tmp/nli_cache/` 无），但 `train_nli_cache.json` 在 docred 数据目录中
- SFT adapter 就绪：base=`Qwen3-4B`, r=64, alpha=128, LORA

## Part 5: 启动命令

所有命令需在 `cd /root/autodl-tmp` 下执行，先 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。

**mvp2_grpo_ced_r3**（单卡，num_iterations=1，KL 早停）：
```bash
CUDA_VISIBLE_DEVICES=0 python -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/grpo_ced_r3 \
  --stage 3 --num_iterations 1 --max_kl 100.0 \
  --num_generations 4 --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 --num_epochs 1 \
  --learning_rate 5e-5 --kl_coef 0.04 \
  --wandb_run_name mvp2_grpo_ced_r3
```

**mvp2_sft_eval**：
```bash
CUDA_VISIBLE_DEVICES=1 python -m freige.eval.run_eval \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --adapter_path /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/eval_results/sft \
  --batch_size 4 --max_new_tokens 1024 --split dev
```

**mvp2_grpo_extract**（stage 1，无 CED）：
```bash
CUDA_VISIBLE_DEVICES=2 python -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/grpo_extract \
  --stage 1 --ced_reward_weight 0.0 \
  --num_iterations 1 --max_kl 100.0 \
  --num_generations 4 --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 --num_epochs 1 \
  --learning_rate 5e-5 \
  --wandb_run_name mvp2_grpo_extract
```

**mvp2_grpo_flatnli**（stage 2，auto flat_nli mode）：
```bash
CUDA_VISIBLE_DEVICES=3 python -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/grpo_flatnli \
  --stage 2 --num_iterations 1 --max_kl 100.0 \
  --num_generations 4 --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 --num_epochs 1 \
  --learning_rate 5e-5 --kl_coef 0.04 \
  --wandb_run_name mvp2_grpo_flatnli
```

---
