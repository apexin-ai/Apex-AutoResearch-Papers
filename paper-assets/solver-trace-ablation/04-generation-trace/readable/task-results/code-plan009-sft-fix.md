# code plan009 sft fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan009-sft-fix_20260514T111706_result.json`
- **Structured JSON:** [`0a258ea9205d76face9b.json`](../../sessions/0a/0a258ea9205d76face9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修复均已正确应用。

## 修改 diff

**Fix 1 — device_map (line 160)**
```diff
-        device_map="auto",
+        device_map={"": 0},
```
`device_map={"": 0}` 将整个模型加载到 `CUDA_VISIBLE_DEVICES` 映射后的 `cuda:0`，不会跨卡。

**Fix 2 — GPU 隔离 guard (lines 131-134)**
```diff
         logger.info(f"Set CUDA_VISIBLE_DEVICES={args.gpu}")
+    elif "CUDA_VISIBLE_DEVICES" not in os.environ:
+        logger.error("CUDA_VISIBLE_DEVICES not set and --gpu not specified. "
+                     "Refusing to run without explicit GPU isolation (C002/C005).")
+        sys.exit(1)
```
如果既没传 `--gpu` 也没设环境变量，脚本直接拒绝启动。

## Dry-run 跳过

两张卡分别被 plan006 (81GB/97GB) 和 plan018-s43 (86GB/97GB) 占满，加载 Qwen3-4B (~8GB bf16) 会 OOM。不做 dry-run。

## 重新提交命令模板

```bash
export CUDA_VISIBLE_DEVICES=1 && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/solver-trace-ablation && \
nohup python3 scripts/train_sft.py \
  --model_path /root/autodl-tmp/models/Qwen3-4B \
  --data_path data/train_500_seed42.jsonl \
  --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r2 \
  --num_steps 500 \
  --seed 42 \
  --bf16 \
  --wandb_project solver-trace-ablation \
  --wandb_run plan009-sft-s42-r2 \
  > /root/autodl-tmp/outputs/plan009_sft_s42_r2/train.log 2>&1 &
```

等 cuda:1 上 plan018-s43 跑完后再提交。

---
