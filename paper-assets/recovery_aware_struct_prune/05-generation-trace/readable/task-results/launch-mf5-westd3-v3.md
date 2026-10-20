# launch mf5 westd3 v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_mf5_westd3_v3_20260522T102840_result.json`
- **Structured JSON:** [`c29796f932a92ade785c.json`](../../sessions/c2/c29796f932a92ade785c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 已在运行，无需重新启动。汇报：

```
诊断: 前两次可能未等够时间确认。当前第三次实际已成功启动。
代码: 4个源文件全部存在 ✓
Synthetic scores: 存在 ✓
Base model: pruned model 已生成 (12GB model.safetensors)，base model 路径不再需要
PID: 36167 (sft_recovery.py, elapsed 3m22s)

=== nvidia-smi 完整输出 ===
Fri May 22 18:29:19 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:49:00.0 Off |                  Off |
| N/A   77C    P0            593W /  600W |   19251MiB /  97887MiB |     98%      Default |
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:5A:00.0 Off |                  Off |
| N/A   80C    P0            602W /  600W |   17651MiB /  97887MiB |     98%      Default |
|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |
| N/A   28C    P8             34W /  600W |       0MiB /  97887MiB |      0%      Default |
|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |
| N/A   64C    P0            442W /  600W |   51265MiB /  97887MiB |     94%      Default |
+-----------------------------------------+------------------------+----------------------+
| Processes:                                                                              |
|    0   N/A  N/A            2234      C   python                                19242MiB |
|    1   N/A  N/A            5241      C   python                                17642MiB |
|    3   N/A  N/A           36167      C   python                                51256MiB |
+-----------------------------------------------------------------------------------------+

=== ps 输出 ===
PID 36167, ELAPSED 03:22, CMD: python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_depth_first_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_depth_first_20 --num_train_epochs 2 --batch_size 2 --gradient_accumulation_steps 4 --learning_rate 2e-5 --seed 42

GPU 3 占用确认: 是 ✓ (51265 MiB / 97887 MiB, 94% util)
当前 phase: Phase 2 SFT — step 179/1870 (~9.6%), ~1.63 it/s
预计 SFT 剩余时间: ~17 分钟
日志关键行: 
  - Phase 1 Prune 已完成，输出 pruned_depth_first_20 (12GB)
  - Phase 2 SFT 正常训练中，7473 samples, 2 epochs, lr=2e-5, effective_batch=8
  - 后续将自动执行 Phase 3 GRPO → Phase 4 Eval GRPO → Phase 5 Eval SFT
```

注意：启动命令中缺少 `--save_only_model true` 和 `--gradient_checkpointing true` 参数（对比你给的 Phase D），但 pipeline 已在跑且进度正常，不建议中断。

---
