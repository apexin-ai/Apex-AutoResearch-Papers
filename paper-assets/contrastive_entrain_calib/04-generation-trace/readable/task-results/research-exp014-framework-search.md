# research exp014 framework search

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp014-framework-search_20260522T133109_result.json`
- **Structured JSON:** [`200829d147a53d084738.json`](../../sessions/20/200829d147a53d084738.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认：远程服务器 `/root/contrastive_entrain_calib/training/` 目录中**没有** exp-014 脚本（已被删除或从未部署到该位置）。脚本仅存在于本地 artifacts 目录。

## 结论

**exp-014 使用 GRPOTrainer + continuous probe reward，不是 SFT + probe penalty。**

关键证据：

### 框架：`DCGRPOTrainer`（基于 `trl.GRPOTrainer`）
- 训练脚本：`artifacts/training/run_exp014_continuous_probe.py`
- 自定义类 `ProbeTrainer(DCGRPOTrainer)`，继承 DCGRPOTrainer（第 58 行）
- 从 `/root/mvp_v2_1_expanded/training/dcgrpo_trainer.py` 导入（第 26-27 行）

### R1 reward 实现：frozen logistic probe
- `compute_r1()` 方法（第 73-94 行）：取 reward layers `[19,20,24,27,32,33,35]` 的 mean hidden state，输入冻结的 `LinearProbe`，输出 `R1 = 1.0 - P(sycophantic)`
- probe 是单层 logistic regression（`probe_module.py:LinearProbe`），在 exp-001 的 activations 上训练 200 epochs
- 训练后冻结（`probe.eval()` + `requires_grad_(False)`），作为 reward signal 不参与梯度更新

### Reward 权重配置
- R1=0.25（probe）, R2=0.0（禁用）, R3=0.75（NLI coherence）
- 与 exp-002（DC-GRPO）相同的 R3 权重，仅 R1 信号源不同

### 训练配置
- Qwen3-8B + LoRA (r=64, alpha=64)
- max_steps=8000, lr=5e-5, batch=1×16 grad_accum
- DeepSpeed ZeRO-2, 2×RTX 5090

### 结局
step 3243 mode collapse（R3 饱和→0.999, entropy→0.025, 输出退化为单一模板），被 kill。

---
