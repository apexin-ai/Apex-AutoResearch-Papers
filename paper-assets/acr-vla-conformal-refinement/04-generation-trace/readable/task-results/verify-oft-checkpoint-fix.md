# verify oft checkpoint fix

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_oft-checkpoint-fix_20260522T121952_result.json`
- **Structured JSON:** [`d414e19c03124dcd2fac.json`](../../sessions/d4/d414e19c03124dcd2fac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境初始化超时了（30s 限制）。当前 eval 进度约 54%（270/500 episodes），全部失败。

汇总诊断结果：

**确认正确的部分：**
- Checkpoint 来源：`moojink/openvla-7b-oft-finetuned-libero-object` ✓
- 模型权重已包含 merged LoRA ✓  
- action_head、proprio_projector 文件存在 ✓
- 代码逻辑：官方 OFT repo，参数默认值正确 ✓
- config.json/modeling_prismatic.py 的修改不影响 L1 regression 路径 ✓

**问题：**
- 270+ episodes，0% 成功率（论文报告 ~96%）
- 当前参数 `num_trials=50, seed=7`（任务要求 `20, 42`）

**未排除的可能原因：**
- MuJoCo 3.8.1 与 LIBERO 的兼容性问题
- 环境渲染出的图像与训练时不同
- 模型下载不完整/权重损坏

建议：Kill 当前 eval，用 **HF Hub 路径直接加载**（跳过本地文件），重新跑 eval。是否执行？

---
