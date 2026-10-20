# code fix and relaunch

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-and-relaunch_20260519T222907_result.json`
- **Structured JSON:** [`577fa71d4fc5f17117ec.json`](../../sessions/57/577fa71d4fc5f17117ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**PASS.** Dry-run 3 步全部成功。

### 结果总结

**崩溃原因**: `--adapter_tmp_dir` 不是合法参数（脚本中不存在），去掉即可。

**FinetuneAffordConfig 全部参数**:
| 参数 | 类型 | 默认值 |
|------|------|--------|
| `vla_path` | str | `openvla/openvla-7b` |
| `data_root_dir` | Path | `datasets/rlds` |
| `dataset_name` | str | `libero_spatial_no_noops` |
| `run_root_dir` | Path | `runs` |
| `shuffle_buffer_size` | int | 100000 |
| `use_l1_regression` | bool | True |
| `use_diffusion` | bool | False |
| `num_diffusion_steps_train` | int | 50 |
| `use_film` | bool | False |
| `num_images_in_input` | int | 1 |
| `use_proprio` | bool | False |
| `batch_size` | int | 2 |
| `learning_rate` | float | 5e-4 |
| `lr_warmup_steps` | int | 0 |
| `num_steps_before_decay` | int | 100000 |
| `grad_accumulation_steps` | int | 1 |
| `max_steps` | int | 200000 |
| `save_freq` | int | 10000 |
| `save_latest_checkpoint_only` | bool | False |
| `resume` | bool | False |
| `resume_step` | Optional[int] | None |
| `image_aug` | bool | True |
| `use_lora` | bool | True |
| `lora_rank` | int | 32 |
| `lora_dropout` | float | 0.0 |
| `wandb_entity` | str | `disabled` |
| `wandb_project` | str | `afford-invar` |
| `run_id_note` | Optional[str] | None |
| `run_id_override` | Optional[str] | None |
| `wandb_log_freq` | int | 10 |
| `paraphrases_path` | str | `/root/afford_invar/data/paraphrases.json` |
| `num_paraphrases` | int | 3 |
| `alpha` | float | 0.1 |
| `lambda_H` | float | 0.01 |
| `layer_idx` | int | 18 |
| `afford_mid_dim` | int | 256 |
| `afford_output_size` | int | 128 |

**paraphrase hit rate 监控**:
- `build_paraphrase_inputs` 新增 hit/total 计数返回
- 每步 console 输出含 `para_hit=100%`
- 同步记入 metrics dict 和 recent_metrics smoothing

**Dry-run 输出**:
```
[Step 0] L_act=0.4121  L_con=0.398475  H_ent=-8.4587  L_tot=0.4520  para_hit=100%
[Step 1] L_act=4.5625  L_con=0.577287  H_ent=-8.3969  L_tot=4.6202  para_hit=100%
[Step 2] L_act=4.1875  L_con=1.295869  H_ent=-6.4455  L_tot=4.3171  para_hit=100%
[Step 3] L_act=2.2812  L_con=0.196240  H_ent=-5.4234  L_tot=2.3009  para_hit=100%
```

**正确的全训练启动命令**（可直接复制）:
```bash
CUDA_VISIBLE_DEVICES=0 WANDB_MODE=disabled torchrun --nproc_per_node=1 --master_port=29501 \
  vla-scripts/finetune_afford.py \
  --vla_path /root/autodl-tmp/openvla-7b \
  --data_root_dir /root/autodl-tmp/modified_libero_rlds \
  --dataset_name libero_goal_no_noops \
  --run_root_dir /root/afford_invar/runs \
  --lora_rank 32 --batch_size 2 --learning_rate 5e-4 \
  --max_steps 200000 --save_freq 10000 \
  --paraphrases_path /root/afford_invar/data/paraphrases.json \
  --layer_idx 18 --alpha 0.1 --lambda_H 0.01 --num_paraphrases 3
```

**判定: PASS** — 无 unrecognized arguments、loss 正常、hit rate 100%、无 NaN/OOM。

---
