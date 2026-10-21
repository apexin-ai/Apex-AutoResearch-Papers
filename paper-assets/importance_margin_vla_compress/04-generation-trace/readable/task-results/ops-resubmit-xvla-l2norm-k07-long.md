# ops resubmit xvla l2norm k07 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resubmit_xvla_l2norm_k07_long_20260523T080300_result.json`
- **Structured JSON:** [`81f23cb62e46cb09149d.json`](../../sessions/81/81f23cb62e46cb09149d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功提交并运行。

**诊断结果：** v1 失败根因是命令中 `cd /root/autodl-tmp/X-VLA` 路径不存在（实际代码在 `/root/autodl-tmp/importance_margin_vla_compress/`），加上 tmux 内未激活 conda 导致 `python` 找不到。

**v2 修复：**
- 工作目录改为 `/root/autodl-tmp/importance_margin_vla_compress/`
- 添加 conda 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 日志 tee 到 `logs/eval_xvla_l2norm_k07_long_seed42_v2.log`

**当前状态：**
- 服务器：westd-38929 GPU0（RTX PRO 6000 96GB），已占用 ~5GB，进程 PID 822357
- tmux session：`eval_xvla_l2norm_k07_long_v2`
- Registry：RUNNING，hypothesis/parent 已设置
- 模型加载中，日志正常输出

---
