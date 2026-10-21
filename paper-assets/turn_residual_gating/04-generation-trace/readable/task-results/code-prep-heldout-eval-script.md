# code prep heldout eval script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_heldout_eval_script_20260519T135925_result.json`
- **Structured JSON:** [`d2f5a67b0f05c06c32a2.json`](../../sessions/d2/d2f5a67b0f05c06c32a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

**脚本已准备完成：** `/root/turn_residual_gating/scripts/run_4way_eval_heldout.sh`

**变更内容：**
- 数据路径：`ultrachat_eval_sample.json` → `ultrachat_eval_heldout.json`
- 输出目录：`runs/4way_eval` → `runs/phase2_4way_eval_heldout`
- 其余 8 路 eval 配置（4 模型 × 2 GAR 变体）不变

**验证结果：**
- held-out 数据文件存在（452KB，50 样本）
- 全部 5 个 checkpoint 路径有效（TG v7 lora + gate_params.pt、UG lora + gate_params.pt、LoRA-only lora）
- 脚本已有执行权限

**运行命令：**
```bash
cd /root/turn_residual_gating && bash scripts/run_4way_eval_heldout.sh
```

**预期运行时间：** 8 轮 eval，每轮需加载模型 + 跑 50 样本推理。单轮约 3-5 分钟，总计约 25-40 分钟（含模型加载开销）。

---
