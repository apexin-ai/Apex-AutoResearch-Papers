# director / loop_4.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`c20ce8b9e20132b5e4b2.json`](../../sessions/c2/c20ce8b9e20132b5e4b2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-15T14:32:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0/1/2/3（rtx5090-4x 服务器，4×RTX 5090 32GB）
- DREEAM baseline 刚因 GPU 错配出过 CRITICAL（registry 写 cuda:2 实际跑 cuda:0），submit 后必须用 /proc/PID/environ 验证 CUDA_VISIBLE_DEVICES 与 registry 一致
- plan_011 GRPO G=8 实验用了 bf16 + kl_coef=0.01（非原始 QLoRA 4-bit + kl_coef=0），三变量混淆——不能直接归因单一变量
- AutoDL 环境必须 `source /etc/network_turbo` + 设 `HF_HUB_DISABLE_XET=1` + SSL 证书变量

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (connect.bjb2.seetacloud.com) + bjb2-12179，工作目录 /root/autodl-tmp/freige
- 根分区小，大文件全放 /root/autodl-tmp/
- 模型：SFT base = /root/autodl-tmp/qwen3_4b_sft_lora_merged；GRPO G=8 输出 = /root/autodl-tmp/grpo_ced_g8_bf16/
- DREEAM 代码：/root/autodl-tmp/DREEAM/
- 活跃进程（截至 handoff）：
  - DREEAM teacher (PID 213006, cuda:2, 30 epochs ~1.8h)
  - CED reranker (PID 178055, cuda:0)
  - maxtok1536_r2 eval (cuda:1)
  - flat-NLI scoring (cuda:3)

### 3. 📊 当前状态
**刚处理完**：
- plan_011 GRPO G=8 训练完成（100 steps, EXIT_CODE=0），reward 趋势积极（f1_reward 0.56-1.85 未崩塌，CED reward 上升），**但 registry 仍为 RUNNING，且 dev set eval 尚未执行**——这是最高优先级待办
- DREEAM baseline (plan_004) GPU 迁移：从 cuda:0 kill 后用 cuda:2 重启成功，CRITICAL 已解决。Registry status 仍为 QUEUED 应改 RUNNING
- 取消了队列中过时的"GRPO G=8 配置匹配"指令（训练已完成，先 eval 再说）

**Agent 队列**：刚 RESET_BOTH 前深度 7+，有多个 worker:done 待处理（plan_001 monitor、plan_008 topk3 random、gpu-status-fix、dreeam-global-fix-rerun）

### 4. 📋 待办
- **plan_011 registry 更新为 DONE + dev set eval** → 这是当前最紧急的。eval 结果决定 Claim 3 方向：rel_f1 保持 → GRPO failure 可能是 QLoRA/G=4 的锅而非 GRPO 本质问题；rel_f1 崩 → 加强 Claim 3（GRPO 对 IE 任务确实有 catastrophic forgetting）
- DREEAM teacher 训练完成（~1.8h 后）→ 跑 DREEAM dev eval 获得 Evi-F1 baseline 数字
- CED reranker (plan_005) 完成 → 收集 reranker eval 结果
- plan_008 topk3 random 数据已就绪（8037 samples）→ 启动 RSFT 训练对比 CED-scored topk3
- plan_001 flat-NLI scoring 完成 → 启动 flat-NLI RSFT 训练（C2 ablation 核心）
- Reviewer 建议：如 topk3 vs random 差异显著，追加 doc-balanced random baseline 消除 per-doc 分布混淆

### 5. 🎯 战略上下文
- **项目核心**：Faith & Evidence in IE——用 CED (Contrastive Evidence Distillation) 做 document-level RE 的 evidence-aware 训练，对比 RSFT vs GRPO
- **四个 Core Claims**：C1=CED+RSFT 提升 evidence 质量；C2=CED scoring 优于 flat-NLI；C3=GRPO 对 IE 有 catastrophic forgetting（negative result）；C4=EDCR 作为新评估指标
- **MVP 已通过**，处于 Research 阶段 + 审稿同步进行中（Review Director 在 C 群独立审稿）
- **关键决策链**：D031/D033 确认 GRPO 全线失败 → plan_011 G=8 是验证"failure 是否因 G=4 太小" → 如果 G=8 eval 也 fail 则 C3 更强，如果改善则需修改论文结论
- **易错点**：plan_011 三变量混淆（bf16/kl_coef/G）——eval 结果无论好坏都不能归因给单一变量，需要后续 ablation 拆分
- **GPU 利用率**：4 张卡当前全部在用，Reviewer 会盯 GPU 空转，DREEAM 完成后立即安排下一个实验上 cuda:2


---
