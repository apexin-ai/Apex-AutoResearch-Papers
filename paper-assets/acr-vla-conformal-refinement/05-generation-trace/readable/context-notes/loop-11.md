# director / loop_11.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`45f311ad126ace6e5098.json`](../../sessions/45/45f311ad126ace6e5098.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-05-17T22:05:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- K=1 和 K=10 结果**禁止交叉比较**。K=10 数据仅作 supplementary evidence（D049 用户硬要求）。**但用户尚未回复 D051 framing 选择**——我已发消息请用户确认是否将 K=10 升为 primary（Option A）或走纯 analysis paper（Option B）。在用户回复前不要锁定 framing。
- CRM 设计禁止直接照搬已有论文的命名模块（如 FiLM）。标准方法可用但组合和动机必须原创。
- LIBERO 并发上限：每台服务器最多 4 个 LIBERO 评估进程（M005）
- 4 台服务器均为本项目分配：bjb2-40593, bjb1-18228, bjb1-32546, bjb2-28827
- CoRL 2026 唯一投稿目标（abstract DDL ~May 26, full paper DDL ~Jun 2），禁止 fallback

### 2. 🖥️ 基础设施快照
- **bjb2-28827** (connect.bjb2.seetacloud.com): 6×4090, /root/acr-vla-conformal-refinement/src/。SmolVLA + CRM 主机。K=1 multi-scale checkpoint: /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt
- **bjb1-32546** (connect.bjb1.seetacloud.com): 6×4090, SmolVLA eval 环境。Multi-scale checkpoint 复制为 crm_k1_best_multiscale.pt
- **bjb1-18228** (connect.bjb1.seetacloud.com): 4×4090, OpenVLA eval 主机。OpenVLA 官方 repo: /root/autodl-tmp/openvla, 独立 conda env: /root/autodl-tmp/conda_envs/openvla (transformers 4.40.1)。模型: /root/autodl-tmp/models/openvla-libero-object/。HF_ENDPOINT=https://hf-mirror.com 必须设。
- **bjb2-40593** (connect.bjb2.seetacloud.com): 1×4090（不是 6 张！之前 ROADMAP 写错已修正）
- Python: 各服务器 /root/miniconda3/bin/python。bjb2-28827 无 wandb，训练必须 --no_wandb

### 3. 📊 当前状态
**刚完成**：
- D051 已 log：Scenario B 确认。K=1 multi-scale 3-seed mean=10.33% ≈ VLA-only 10.8%，无净增益。
- OpenVLA eval pipeline 修通：根因是 transformers 5.8 DynamicCache bug，用官方 repo + transformers 4.40.1 解决。干跑 spatial 80%（论文报 84.7%）。
- Latency profiling 完成：CRM 0.3ms, CGS 6.2ms, ACR overhead 0.34%, VLA K=1:193ms K=5:965ms K=10:1914ms K=20:3858ms
- 已向用户发出 D051 framing 选择请求（Option A vs B），**等待回复**

**RUNNING（约 14 个）**：
- `eval-openvla-object-vla-only-seed42-v2`: bjb1-18228 cuda:1, ~50% 完成, 初步 alphabet_soup 90%, cream_cheese ~100%。预计 ~4h 完成
- `eval-obs-only-object-norm02-k5-seed42`: bjb1-18228 cuda:0, K=5 sweep, ~32%, ~33h 剩余
- `eval-obs-only-object-norm02-k20-seed42`: bjb1-18228 cuda:2, K=20 sweep, 极慢 ~46h 剩余
- `eval-random-selection-object-seed42`: bjb2-40593 cuda:0, ~35%, 初步 cream_cheese=10%, salad_dressing=10%（远低于 CRM-guided 22%）
- 多个 magnitude sweep 补 seed 实验分布在 bjb2-28827 和 bjb1-32546
- `eval-perdof-object-norm02-seed43-r3`: bjb1-32546 cuda:4, 刚部署

### 4. 📋 待办（条件触发式）
- 用户回复 D051 framing 选择 → 更新 paper_framing.md + ROADMAP，启动 Paper Agent
- OpenVLA eval 完成 → 收集 SR，如果 ~80-90% 则 baseline 有效。然后评估 Claim 3 验证路径：OpenVLA SR 远高于 SmolVLA (88% vs 11%)，直接套 CRM 可能 overcorrect——需要在 OpenVLA feature space 重训 CRM，验证 conditioning-magnitude pattern 是否复现
- Random selection baseline 完成 → 收集 SR，如果显著低于 obs_only K=10 (17.5%)，则证明 CRM scoring 有价值（不是随便选就行）
- K=5 eval 完成 → 与 K=10 对比画 K-value tradeoff curve。K=20 如果出了是 bonus，不必等
- Magnitude sweep 补 seed 完成 → 更新 Figure 2 数据，确保每个 norm 点 ≥3 seeds
- GPU 释放 → 按优先级部署：OpenVLA + CRM (plan_802) > magnitude 补 seed > 额外 OpenVLA seeds

### 5. 🎯 战略上下文
- **决策链**: D049（用户确认 K=1+OpenVLA 方向）→ D050（K=1 fallback=VLA-only）→ D051（Scenario B 确认，K=1 multi-scale 也无增益）
- **核心矛盾**: D049 说 K=10 作 supplementary，但 D051 确认 K=1 negative。K=10 是唯一正结果 (p=0.0074)。已请用户决定是否将 K=10 升为 primary。
- **已锁定硬证据**: K=10 obs_only 6v6 Fisher p=0.0074 (17.5% vs 12.3%); magnitude sweep obs_only 稳定 15-17.5%, perdof collapse 14→0%; latency 0.34% overhead; K=1 redistribution pattern (complex tasks +23pp, simple tasks -20pp, net zero)
- **OpenVLA 注意**: VLA-only baseline 预计 ~88%，远高于 SmolVLA 11%。CRM 对强 VLA 可能 overcorrect。Claim 3 的验证路径不是简单套用 SmolVLA CRM，而是看 conditioning-magnitude interaction pattern 是否在 OpenVLA feature space 上复现。
- **易错点**: (1) 不要混淆 fallback model（单层 960D）和 multi-scale model（4层融合）的结果——两者都 negative 但原因不同; (2) OpenVLA eval 必须用官方 repo 代码 + 独立 conda env，不能用我们的 openvla_eval.py（transformers 5.8 bug）; (3) GPU 低利用率 18-22% 是 LIBERO simulation CPU-bound 正常模式，不是问题; (4) bjb2-40593 只有 1 张 4090，不是 6 张


---
