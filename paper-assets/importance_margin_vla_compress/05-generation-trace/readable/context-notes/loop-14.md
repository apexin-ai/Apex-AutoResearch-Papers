# director / loop_14.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_14.md`
- **Structured JSON:** [`cd70ded83ddbc94f0d60.json`](../../sessions/cd/cd70ded83ddbc94f0d60.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-24T02:08:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- X-VLA 所有实验必须 `--domain_id 3`，domain_id=2 产出 0% Goal SR（M082 教训）
- X-VLA mode flag: `--mode l2_norm`（下划线）；OpenVLA: `--mode l2norm_prune`；π0.5: `--prune_mode l2norm`——三个不同，搞混浪费 GPU（M084/M089）
- π0.5 Random pruning 必须用 CPU RNG fix 代码（`torch.randperm(n).to(device)` 在 CPU 生成），pre-fix 数据跨硬件不可复现（D183）
- westd-41074 上 π0.5 实验必须设 `HF_HUB_OFFLINE=1`（不是 TRANSFORMERS_OFFLINE=1），否则 tokenizer 崩溃。GPU 3 有 cache，GPU 0/1/2 需先从 GPU 3 环境 rsync tokenizer cache
- JSON 文件名碰撞（M087）：X-VLA eval 输出 `xvla_prune_k{ratio}_libero_{suite}.json` 不含 mode，不同 pruning mode 会互相覆盖
- Agent 队列深度 > 3 时不要继续发消息，用 `replace_agent_queue` 合并（M088 教训）

### 2. 🖥️ 基础设施快照
- **westd-38929** (4×H100): X-VLA 服务器。代码 `/root/autodl-tmp/importance_margin_vla_compress`。正在跑 X-VLA Random k=0.85 × 3 suites (Object/Goal/Spatial, disruption peak RoPE 假说测试)
- **westd-27271** (2×GPU): OpenVLA 服务器。GPU 0 跑 OpenVLA 实验，GPU 1 部署中
- **westd-41074** (4×H100): π0.5 服务器。tokenizer cache 问题导致 GPU 0/1/2 频繁崩溃，GPU 3 正常。需要 rsync tokenizer fix
- **cqa1-33015** (4×GPU): π0.5 服务器（有网络）。GPU 0/1 跑 Object Random post-fix (k=0.9/k=0.95 完成), GPU 2/3 部分空闲
- HF cache: cqa1 在 `/root/autodl-tmp/.hf_cache`；其他服务器各异
- 无 W&B 集成——eval 脚本不写 W&B sentinel，CRON 经常误判为 failed（需手动 SSH 检查日志）

### 3. 📊 当前状态
**刚做完**：
- D194: Object k=0.95 post-fix=74.0%，fig_method_gap 解除暂停，gap 修正为 24.2pp (原 28.8pp)
- D193: Disruption peak 确认真实（非 seed artifact），Object k=0.85 跨 seed 3.6-9%，L2=99%
- X-VLA CV 矩阵 8/8 完成（dual-seed verified，所有 L2 anti-informative -8~-28pp）
- π0.5 attention 4 suite 完成：Goal/Spatial/Long ≈ Random (±3pp)，Object -30.4pp 灾难性
- Paper Agent 已完成 D190 (log-decay)、D191+D193 (disruption peak 强化)、π0.5 attention cross-suite 更新

**运行中**：
- westd-38929: X-VLA Random k=0.85 × Object/Goal/Spatial（RoPE 假说验证，初步 ~62-65% 无 death valley）
- cqa1: Object Random post-fix 部分完成（k=0.5=68.2%, k=0.7=74.0%, k=0.9=9.0%, k=0.95=74.0%）
- westd-41074 GPU 3: π0.5 Random k=0.85 Goal seed43（disruption peak 验证）
- Paper Agent: 处理 D194 fig_method_gap 恢复 + Object death valley 曲线

**等待中**：
- X-VLA k=0.85 × 3 suites 完成 → 确认 RoPE 假说
- westd-41074 tokenizer fix → 解放 3 GPU
- Paper Agent fig_method_gap regeneration

### 4. 📋 待办
- X-VLA k=0.85 Object/Goal/Spatial 完成 → 如果 ~62-65% 确认无 death valley，通知 Paper Agent 写 RoPE 假说段落；如果出现 death valley → 重新评估 disruption peak 解释
- westd-41074 tokenizer fix 完成 → 部署 π0.5 seed43 验证实验 + Spatial Random post-fix
- π0.5 Random k=0.85 Goal seed43 完成 → 与 seed42=52.4% 对比，确认 Goal disruption peak 跨 seed 一致性
- Paper Agent 完成 fig_method_gap → 确认 17× multiplier，检查 abstract/intro 是否一致
- 所有 post-fix + CV 数据到位 → re-submit formal review (`submit_paper_to_review`)
- May 26: Abstract submission deadline
- May 29: Paper submission deadline

### 5. 🎯 战略上下文
**核心叙事**: Architecture-dependent importance scoring — connector type (entangling BART / linear MLP / MLP) 决定哪种 scoring method (L2/Attention) 有效。3 模型 × 4 LIBERO suites 验证。

**决策链**: D183(CPU RNG fix) → D185(architecture-dependent framing) → D188(OpenVLA L2 fix) → D189(Object pre-fix invalidation) → D190(log-decay range) → D191(disruption peak discussion) → D192(seed artifact hypothesis) → D193(撤回 D192, confirmed real) → D194(fig_method_gap unblocked)

**最容易判断错的事**:
1. π0.5 Random 数据的 pre/post-fix 状态——不要假设任何 Random 数据是 post-fix，必须检查 registry 中 experiment 创建时间（May 23 前 = pre-fix）或名称含 v2/postfix
2. Disruption peak 不是 bug/artifact——D193 已确认是真实现象，不要再怀疑。Object k=0.85=3.6% 是真实的
3. Agent 队列管理——CRON 重复消息会快速堆积到 depth 17+，主动用 replace_agent_queue 清理
4. westd-41074 GPU 0/1/2 不能直接部署 π0.5——必须先 fix tokenizer cache
5. fig_method_gap 的 Spatial 值 76.4% 是正确的（post-fix = pre-fix），只有 Object 值变了（69.4% → 74.0%）


---
