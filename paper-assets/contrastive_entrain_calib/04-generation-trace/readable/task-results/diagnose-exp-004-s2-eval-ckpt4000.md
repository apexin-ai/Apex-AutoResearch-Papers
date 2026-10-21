# diagnose exp 004 s2 eval ckpt4000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-004-s2-eval-ckpt4000_20260522T164528_result.json`
- **Structured JSON:** [`14227e10d55855b17bc4.json`](../../sessions/14/14227e10d55855b17bc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**两个实验都没有真正失败——它们都成功完成了。**

### exp-004-s2-eval-ckpt4000
日志显示 362/362 样本全部跑完，结果已写入：
- ToF=0.1160, NoF=0.9227, SYCONScore=0.2061
- 结果文件: `/root/contrastive_entrain_calib/results/exp004_s2_d027_eval/exp004-s2-ckpt4000_preset_eval.json`

### exp-004-s2-eval-ckpt3500
同样 362/362 完成，结果已写入：
- ToF=0.1326, NoF=0.8895, SYCONScore=0.2308
- 结果文件: `/root/autodl-tmp/results/exp004s2_act_eval/checkpoint-3500/exp004s2_act_ckpt3500_preset_eval.json`

### 之前的 ckpt2500 失败
这个是**真失败**——checkpoint 文件损坏：`SafetensorError: Error while deserializing header: incomplete metadata, file not fully covered`（路径是 `exp004_s2/checkpoint-2500`，不同于当前两个用的 `exp004s2_act_seed2`）。

### GPU 状态
GPU 0 空闲（2MiB），GPU 1/2/3 各有 python 进程在跑（其他任务）。

```json
{"root_cause":"eval_unified_preset.py 不输出 sentinel 文件也不写 W&B，监控系统检测进程退出后找不到成功标记，误判为失败。两个实验实际均已成功完成（362/362 samples）。","error_type":"infrastructure","fix_steps":["将 ckpt4000 和 ckpt3500 的状态手动更正为 completed","在 eval_unified_preset.py 结尾添加 sentinel 文件写入（如 touch output_dir/DONE），使监控系统能识别成功"],"can_auto_fix":true,"affects_ckpt3500":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "eval_unified_preset.py 不输出 sentinel 文件也不写 W&B，监控系统检测进程退出后找不到成功标记，误判为失败。两个实验实际均已成功完成（362/362 samples）。",
    "error_type": "infrastructure",
    "fix_steps": [
      "将 ckpt4000 和 ckpt3500 的状态手动更正为 completed",
      "在 eval_unified_preset.py 结尾添加 sentinel 文件写入（如 touch output_dir/DONE），使监控系统能识别成功"
    ],
    "can_auto_fix": true,
    "affects_ckpt3500": true
  }
}
```

</details>

---
