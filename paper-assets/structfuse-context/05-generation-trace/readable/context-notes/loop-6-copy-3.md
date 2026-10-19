# reviewer / loop_6.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`776e68e4a0faeb0f7c16.json`](../../sessions/77/776e68e4a0faeb0f7c16.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-14T07:58:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 bjb1-42106 仅两张卡：cuda:0 归 m2_full_qwen，cuda:1 归 m2_full_starcoder。不可交叉使用。
- 两个训练脚本已被 D026 修改为 `--num-epochs 2`（s43+）。**不要改回 3**——s42 保留 3 epochs 是刻意的（提供 overfitting curve），其余 runs 必须 2 epochs。
- M1 reextract v2 是 CPU-only 后台任务，不占 GPU，但磁盘写入 all.jsonl（追加模式）——不要清理 `/root/autodl-tmp/structfuse/full_m1_data/` 目录。
- 项目 constraints.yaml 为空（无显式 gpu_ids 白名单），但历史有两次 GPU 越界事故（D005 cuda:5、D012 cuda:0），严查 CUDA_VISIBLE_DEVICES。

### 2. 🖥️ 基础设施快照
- **服务器**: bjb1-42106（root），2× NVIDIA RTX PRO 6000 Blackwell 96GB
- **工作目录**: `/root/structfuse`（代码）、`/root/autodl-tmp/structfuse/`（数据/checkpoint/artifacts）
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **模型**: Qwen `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B`；StarCoder 从 HF cache
- **数据**: Qwen 训练数据 `/root/autodl-tmp/structfuse/full_m2_training_data/`；StarCoder `/root/autodl-tmp/structfuse/full_m2_starcoder_data/`
- **训练日志**: Qwen `/root/runs/m2_full_qwen/{strategy}_s{seed}.log`；StarCoder `/root/runs/m2_full_starcoder/`
- **WandB**: 离线模式，日志在 `/root/autodl-tmp/structfuse/wandb_logs/`
- **活跃进程**: m2_full_qwen (tmux, cuda:0, PID 73544)；m2_full_starcoder (tmux, cuda:1, PID 74122)；m1_reextract_v2（4 CPU workers，后台）
- **Artifacts**: `/root/autodl-tmp/structfuse/artifacts/`（neg_difficulty 可视化 22 文件、stats JSON）

### 3. 📊 当前状态
**刚完成的审查**（全部 PASS，无 critical/warning）：
- neg_difficulty_visualization：22 个可视化 artifact，数据与 registry 一致
- experiment_plan 知识更新：plan_002/013 关联 full M2 registry IDs
- eval@2000 urgent check：Qwen 过拟合确认（best step 1000）
- D026 epoch 缩减：双脚本改为 2 epochs，registry 记录完整
- StarCoder eval@1500：过拟合确认（val_loss +6.4%），registry 已更新

**RUNNING 实验**：
- `m2_full_qwen`: random_s42 epoch 3 中（step ~3000+/4242），即将完成，s43 将以 2 epochs 启动
- `m2_full_starcoder`: random_s42 epoch 2 中（step ~2000/4242），eval@1500 已确认过拟合
- `m1_reextract_v2`: ~15/82 repo groups 完成，预计还需 ~10-13h

### 4. 📋 待办（条件触发式）
- Qwen random_s42 完成（~1-2h） → 验证 s43 自动启动 + 确认 `--num-epochs 2` 生效（检查日志首行参数）
- StarCoder eval@2000 出来 → 交叉验证日志 vs registry，确认过拟合模式与 Qwen 一致
- 任何 seed 完成 → 检查 best checkpoint 保存正确（`best_by_val_loss` + `best_by_recall_at_1` 两个目录都在）
- M2 全部 18 runs 完成 → 审查统计检验方案（D019/D020 的 bootstrap CI + paired t-test），验证 go/no-go 判定
- m1_reextract_v2 完成 → 验证新增 structural data 数量，核对 Claim 3 scalability 数字更新
- Director 转发 framing 提案 → 立即 Read `negative-framing-review.skill.md`，四维度审

### 5. 🎯 战略上下文
**核心决策链**: D024 是转折点——旧 Claim 2（"embedding harms"）已证伪（BM25 proxy 被错误标记为 embedding）。新叙事线：embedding universally helps → dataflow conditionally helps → mechanistic explanation via representation saturation（D021 neg_difficulty 分析支撑）。

**D018/D019/D020 锁定了 go/no-go 阈值**：full M2 结果出来前不修改。Go 需要 dataflow > random CI > 0（双 encoder）；Conditional Go 允许单 encoder 显著。阈值偏保守（n=3, df=2, Type II error 高）。

**最容易判断错的事**：
1. **不要因为 pilot 差异 <2pp 就预判 No-Go**——pilot 只有 1 seed + 24 repos，full M2 是 3 seeds + 131 repos，统计功效完全不同
2. **StarCoder dataflow "negative" 结论（pilot）不代表方法失败**——D021 已解释为 encoder capacity 差异（StarCoder pretrained separability 已足够高），这是 mechanistic insight 不是 failure
3. **plan_014 (temperature ablation) 已缩减为 6 runs（D025）**，不是原来的 9 runs
4. **m1_reextract_v2 定位是 camera-ready/后续投稿**，不在当前投稿关键路径上——不要因为它还没完就拦 M2 结论


---
