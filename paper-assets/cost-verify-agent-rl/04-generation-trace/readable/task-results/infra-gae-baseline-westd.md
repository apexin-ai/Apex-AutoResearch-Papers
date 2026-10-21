# infra gae baseline westd

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gae-baseline-westd_20260517T134928_result.json`
- **Structured JSON:** [`4d5bf91302a19427da13.json`](../../sessions/4d/4d5bf91302a19427da13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功提交并运行。

---

## 总结

**环境验证结果：**
- 服务器：westd-47453，Ubuntu 22.04
- GPU：4× NVIDIA RTX PRO 6000 Blackwell 96GB（使用 cuda:0, cuda:1）
- Python 3.12.3, PyTorch 2.10.0+cu128, CUDA 12.8
- verl 0.6.1, TRL 1.1.0

**同步操作：**
- 从 bjb1-17606 同步 checkpoint (3.3G) ✅
- 从 bjb1-17606 同步 ALFWorld 数据 (2.2G) ✅
- 修复 ragen/verl 包路径指向 ✅
- 从 bjb1-17606 拷贝 PyTorch 补丁（select_algorithm.py duplicate template fix）✅
- 配置 wandb API key ✅

**GAE → REINFORCE++ 降级原因：**
- TRL 1.1.0 已移除 `AutoModelForCausalLMWithValueHead`，GAE 所需的 critic head 无法加载
- 按 plan_003b 备选方案切换到 `reinforce_plus_plus_baseline`（不需要 critic）

**实验状态：**
- exp_id: `gae_baseline_seed1`
- tmux session: `gae_baseline_seed1`
- PID: 40267
- wandb run: `dt79qyd9`
- val_before_train (step 0) 已完成：success=6.25%, action_valid=77.96%
- 正在进入 step 1 training rollout

---
