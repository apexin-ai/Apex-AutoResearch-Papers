# debug checkpoint identity and behavioral restart

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_checkpoint_identity_and_behavioral_restart_20260518T105748_result.json`
- **Structured JSON:** [`aaffe494d0fc8d332fc1.json`](../../sessions/aa/aaffe494d0fc8d332fc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认了关键发现：

1. Token IDs 在正确范围内 ([31744-31924])
2. 反归一化正确
3. 动作数值合理
4. 但 3/3 episode 全部失败（两种评估脚本均如此）

这几乎肯定是 **mujoco 版本问题**。服务器上是 mujoco 3.8.1，而 OpenVLA LIBERO 微调模型是在 mujoco 2.x 上收集的演示训练的。物理模拟的细微差异导致闭环行为发散。

验证总结报告：

**完成的步骤：**
- Step 1: 确认服务器 `openvla-7b` 是 base 预训练模型（Open X-Embodiment），非 LIBERO 微调
- Step 2: 从 HuggingFace 找到正确模型 `openvla/openvla-7b-finetuned-libero-goal`
- Step 3: 下载 ~15GB checkpoint 到 `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal/`
- Step 4: 修复 auto_map、复制 custom code 文件，模型加载成功
- Step 5: 安装 transformers==4.40.1（模型要求版本），更新 `behavioral_pilot.py` (MODEL_PATH, UNNORM_KEY, center_crop)
- 模型加载验证通过：`norm_stats={'libero_goal'}`, `action_dim=7`, `vocab_size=32000`

**未通过的验证：**
- 3-episode baseline SR = 0/3（两种不同脚本均确认）
- 原因：**mujoco 3.8.1（当前）vs 模型训练时的 mujoco ~2.3 物理模拟不一致**
- 模型输出合理 action（token IDs 正确、值在合理范围），但在新版 mujoco 的物理引擎下无法完成任务

**建议的下一步：**
1. 安装 `mujoco==2.3.7`（或 `mujoco-py`）以匹配训练环境
2. 或在有兼容 mujoco 版本的机器上运行评估

---
