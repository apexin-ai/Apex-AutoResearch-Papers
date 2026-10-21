# fix detach ln v2 s2 resume from 30k

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_detach_ln_v2_s2_resume_from_30k_20260528T020400_result.json`
- **Structured JSON:** [`acbdd89d06dbfd31b824.json`](../../sessions/ac/acbdd89d06dbfd31b824.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动并运行中。但有两个需要注意的问题。

**汇报：**

**30000_chkpt 完整性：** 部分缺失。存在 action_head/occ_head/proprio_projector .pt 文件和 lora_adapter/adapter_model.safetensors，但 **缺少** model.safetensors (4 shards + index.json) 和 config.json。训练仍然成功启动了。

**进程状态：**
- PID: 45380，GPU 0
- VRAM: 62194MiB / 97887MiB
- GPU 利用率: 94%
- 速度: ~1.1 it/s

**日志输出：** 训练正在推进（step 61+），但进度条显示 total=35005 步，而非预期的 20005 步。35005 = 50005 - 15000，说明 finetune.py 的 max_steps 可能是相对于原始起始 checkpoint（15000_chkpt）计算的，而非相对于 resume_step(30000)。如果是这样，实际训练会跑到 step 15000+35005=50005，结果正确，只是 progress bar 的含义不同。

**潜在风险：** 30000_chkpt 缺少 model.safetensors 和 config.json。如果 save_training_checkpoint 仍需从 --vla_path 加载完整 base model 做 LoRA merge，首次 save（~step 5000 relative）可能会再次崩溃。建议关注 step 35000（即相对 step ~5000）附近的日志。

---
