# diagnose eval math500 sft cka only 20 westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_cka_only_20_westb_20260522T202951_result.json`
- **Structured JSON:** [`ac885dad1210c61455c4.json`](../../sessions/ac/ac885dad1210c61455c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因：GPU 0 硬件挂起（GPU hang）**

证据：
- 进程 234500 已死亡，无 Traceback、无 OOM、无 kernel kill 记录
- GPU 0 当前状态异常：**0 MiB 显存占用 + 100% utilization + 无任何进程**——这是 GPU hang 的典型表现（Xid fatal error 后 GPU 卡在计算循环中）
- 日志在 255/500 处突然中止，无错误输出
- 无系统重启、磁盘空间充足（33GB 剩余）

GPU 0 需要 reset 才能恢复正常。

```json
{"root_cause":"GPU 0 hung state (0 MiB memory, 100% utilization, no process) — silent CUDA fatal error killed process at 255/500 without traceback","error_type":"infrastructure","fix_steps":["nvidia-smi --gpu-reset -i 0","验证 GPU 0 恢复正常: nvidia-smi (应显示 0% util, 0 MiB)","重新提交实验"],"can_auto_fix":true,"resubmit_command":"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 nohup python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_cka_only_20_westb.json --seed 42 --dtype bfloat16 --max_new_tokens 2048 > /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_cka_only_20_westb.log 2>&1 &"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "GPU 0 hung state (0 MiB memory, 100% utilization, no process) — silent CUDA fatal error killed process at 255/500 without traceback",
    "error_type": "infrastructure",
    "fix_steps": [
      "nvidia-smi --gpu-reset -i 0",
      "验证 GPU 0 恢复正常: nvidia-smi (应显示 0% util, 0 MiB)",
      "重新提交实验"
    ],
    "can_auto_fix": true,
    "resubmit_command": "cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 nohup python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_cka_only_20_westb.json --seed 42 --dtype bfloat16 --max_new_tokens 2048 > /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_cka_only_20_westb.log 2>&1 &"
  }
}
```

</details>

---
