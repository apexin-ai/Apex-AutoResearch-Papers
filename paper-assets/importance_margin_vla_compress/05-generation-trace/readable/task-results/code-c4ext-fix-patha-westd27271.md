# code c4ext fix pathA westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c4ext_fix_pathA_westd27271_20260519T182110_result.json`
- **Structured JSON:** [`b05552212a0ecaa230bf.json`](../../sessions/b0/b05552212a0ecaa230bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`submit_training_job` 工具不存在于当前 MCP 工具集中。按任务要求汇报：**该工具不可用**。

作为替代，我可以用 `tmux` session 启动训练（不是 nohup），这样进程有持久会话、可 reattach 查看输出。是否用 tmux 方式启动？

命令将是：
```bash
tmux new-session -d -s openvla_sc_m128 \
  'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
   cd /root/autodl-tmp/importance_margin_vla_compress && \
   export HF_HUB_OFFLINE=1 && \
   python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m128.yaml --seed 42 \
   2>&1 | tee logs/train_openvla_vtc_m128_seed42.log'
```

- GPU: cuda:0（默认）
- `HF_HUB_OFFLINE=1` 防联网
- 日志写入 `logs/train_openvla_vtc_m128_seed42.log`

---
