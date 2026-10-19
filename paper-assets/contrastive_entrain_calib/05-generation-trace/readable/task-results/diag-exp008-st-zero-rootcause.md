# diag exp008 st zero rootcause

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp008-st-zero-rootcause_20260518T211605_result.json`
- **Structured JSON:** [`c606e9d63c30d17024d5.json`](../../sessions/c6/c606e9d63c30d17024d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**确认了！** `enable_input_require_grads()` 后：
- `hs[20] rg=True gfn=AddBackward0` — hidden states 连接到计算图
- `loss rg=True gfn=NllLossBackward0` — loss 可以 backward

现在完整的根因分析已经清晰。让我写结论。

---

## 诊断结论：exp-008 S(t)=0 Root Cause

### 根因：模型对抗性地 game 了 linear probe

S(t)=0 **不是 bug**，而是模型利用梯度 **直接优化 hidden states 来欺骗 probe**。

**梯度流通路径确认：**
1. 训练代码用 `gradient_checkpointing_enable(use_reentrant=False)` + `get_peft_model` → 自动调用 `enable_input_require_grads()`
2. 这使得 hidden states 的 `requires_grad=True, grad_fn=AddBackward0`
3. 因此 `∂S(t)/∂θ_LoRA` 的梯度 **完整流向所有 LoRA 参数**

**对抗优化过程：**
- Loss = `L_sft + 0.1 * S(t) - 0.1 * R3`
- 模型最小化 Loss，其中包含最小化 S(t)
- LoRA 作用于所有 7 个目标模块 × 36 层 = **252 个 LoRA 模块**
- 模型有巨大容量来移动 hidden states，使 probe 输出趋近 0
- Step 10: S(t)=0.2257 → Step 30: 0.0003 → Step 40: 0.0000（~30 步完成 gaming）
- Retrain 后，新 probe 同样在 ~10 步内被击败

**辅助证据：**
- 诊断证实 probe **本身工作正常**（eval mode: invalid_pressure sigmoid≈0.97, valid_correction sigmoid≈0.01）
- 初始 probe 与 retrained probe 完全不同（weight cosine sim = 0.023）
- 初始 probe 在 position_idx=1 上训练，训练 loop 用 resp_pos（最后 token）—— 位置不匹配加速了初始崩溃
- eval/train/train+GC 模式的 hidden states 几乎相同（cosine sim > 0.999），probe 值也一致

**为什么 retrain 后 S(t) 仍然是 0：**
1. Retrain 在 eval mode 提取 features → probe acc=1.0
2. 切回 train mode，首个 batch 的 S(t) 可能短暂非零
3. 但梯度立刻开始推 hidden states 远离 probe boundary
4. 在 10 步（160 micro-batches）内 S(t) 再次归零
5. 日志精度 `%.4f` 四舍五入为 0.0000

### 修复建议

1. **`s_t.detach()`**：阻断 S(t) 对模型参数的梯度，仅用作监控指标
2. **REINFORCE 替代直接微分**：`loss += lambda * (s_t.detach() - baseline) * log_prob`，更难被 game
3. **更强 probe 架构**：非线性 probe 或 probe ensemble，提高对抗鲁棒性
4. **修复位置不匹配**：初始 probe 应该也用 `resp_pos` 而非 `position_idx=1`

诊断日志已保存到 `/root/contrastive_entrain_calib/diagnose_st_zero.log`（v2）和 `/root/contrastive_entrain_calib/diagnose_v4.log`（v4）。

---
