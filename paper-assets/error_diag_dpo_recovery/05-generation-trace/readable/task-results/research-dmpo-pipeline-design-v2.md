# research dmpo pipeline design v2

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_dmpo-pipeline-design-v2_20260512T104112_result.json`
- **Structured JSON:** [`b013ad2d4386c08a9293.json`](../../sessions/b0/b013ad2d4386c08a9293.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计文档已完成并注册（`art_20260512_c89733`）。

核心设计要点：

1. **DMPO Loss**：在 trl v1.4.0 的 `_compute_loss` 中，将 `per_token_logps.sum(dim=1)` 替换为 φ-weighted 聚合。φ(t,T,γ) = γ^t·(1-γ^(T-t))/(1-γ^T) 通过 `turn_ids` 张量映射到每个 token。

2. **ETADN γ_e 注入**：DataCollator 从样本 `error_type` 查表得 γ_e（action=0.85, verify=0.92, plan=0.97），构建 per-sample gamma 向量传入 loss 计算。

3. **三模式 ablation**：`mode` flag 切换 dpo（无加权）/ dmpo（全局 γ）/ etadn（per-sample γ_e），同一代码框架覆盖全部实验。

4. **QLoRA ref model**：`precompute_ref_log_probs=True`，训练前缓存 ref logps，训练时不加载 ref model，省 VRAM。

5. **VRAM**：单卡 ~15-17 GB，24 GB 4090D 可运行。两卡各跑独立 run，6 个实验分 3 轮完成。

---
