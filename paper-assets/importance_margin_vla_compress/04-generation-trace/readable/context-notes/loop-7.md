# director / loop_7.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`93893ba34b10420e2a08.json`](../../sessions/93/93893ba34b10420e2a08.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-17T07:43:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cqa1-33015 cuda:0-3（4×RTX 4090）+ westd-27271 cuda:0-1（2×RTX 4090）
- westd 有 sim 环境（LIBERO eval），cqa1 没有——所有 closed-loop eval 必须在 westd 跑
- eval_success_rate_libero.py 刚修过 pruning bug（hook dimension guard），修复版在 westd 上。任何新 eval 必须用修复版，且确认 hook 打印 token 数量验证 pruning 生效
- batch64 训练（cqa1:1）已两次在 step 3550 静默 OOM 死亡，第三次已改 num_workers=1 + save_every=2000 + pin_memory=false，如果再死需进一步减配置
- `/root/autodl-tmp/` 是持久存储，服务器重启不丢数据；但进程会丢，训练需从 checkpoint 恢复
- cqa1 磁盘 /autodl-pub 96% 已满（350GB 剩余），写 checkpoint 前需确认空间

### 2. 🖥️ 基础设施快照
- **westd-27271**: connect.westd.seetacloud.com, root, 工作目录 /root/autodl-tmp/importance_margin_vla_compress
- **cqa1-33015**: connect.cqa1.seetacloud.com, root, 工作目录 /root/autodl-tmp/importance_margin_vla_compress
- 代码路径：/root/autodl-tmp/importance_margin_vla_compress/
- Checkpoints: /root/autodl-tmp/importance_margin_vla_compress/checkpoints/
- Eval results: /root/autodl-tmp/importance_margin_vla_compress/eval_results/
- 关键 checkpoint 名:
  - `libero_full_ft_100k/` — baseline Full FT seed=42 (SR=44.8%)
  - `libero_imm_twostage_fullft/` — IMM 100K (Stage2, SR=0% bypass)
  - `libero_imm_twostage_fullft_k07/` — k=0.7 variant
  - Stage1 checkpoint 从 `libero_imm_twostage_fullft/` 中 `stage: stage1_complete` 提取
- 活跃进程（重启后需确认 PID）：
  - westd:0 — eval_stage1only_object_v2_fixed（修复后真实 pruning eval）
  - westd:1 — eval_stage1only_spatial（用 buggy 代码，结果无效）
  - cqa1:1 — libero_fullft_batch64_v2（第三次尝试，已改配置）

### 3. 📊 当前状态
**刚做完**：修复 eval 脚本 pruning bug（hook dimension guard 导致 pruning 从未执行）。修复后重跑 Stage1-only eval，早期 3 task 结果 = 0/150 (0% SR)。之前 "lossless 44.8%" 完全是假阳性。

**RUNNING 实验**：
- `eval_stage1only_object_v2_fixed` (westd:0) — 修复后真实 pruning eval，3/10 tasks done (0%)，等完整结果
- `libero_fullft_batch64_v2` (cqa1:1) — batch=64 baseline，第三次重启，~step 150/100K
- `eval_stage1only_spatial` (westd:1) — 用 buggy 代码跑的，结果无效，需 kill

**FAILED（刚失败）**：
- `train_acis_stage1only_k07` (cqa1:2) — 进程异常死亡，可能磁盘/OOM
- `train_acis_stage1only_k03` (cqa1:3) — 同上，跑到 step 5000/10000 后死

**空闲 GPU**：cqa1:0, cqa1:2, cqa1:3

**等待中**：
- eval_stage1only_object_v2_fixed 完整 10-task 结果（~30min）
- 用户回复方向选择（A: k=0.9 / B: token merging / C: negative paper）
- Manager hypothesis-driven 指令已执行（registry 自检 + parent 链补全完成）

### 4. 📋 待办
- eval_stage1only_object_v2_fixed 完成 → 汇总 10-task 真实 pruning SR，汇报用户和 Director
- 用户选方向 A (k=0.9) → 快速在 westd 跑 k=0.9 Stage1-only eval（~10min，用已有 ACIS）
- 用户选方向 B (token merging) → 需要改 eval 脚本把 hard mask 换成 soft merge，然后重训 ACIS 或直接用已有 ACIS 的 importance score 做 merge 权重
- 用户选方向 C (negative paper) → 汇总所有实验数据给 Paper Agent
- batch64_v2 再次在 ~step 3550 死亡 → 进一步减配置（grad_accum 16→8 + batch 4→8 保持等效，或用 gradient checkpointing）
- cqa1:2/3 空闲 + 磁盘问题确认后 → 清理磁盘，重启 ACIS k=0.7/k=0.3 训练（为 compression curve 数据）
- seed1 训练已完成 → checkpoint rsync 到 westd 做 SR eval（但优先级低于方向决策）

### 5. 🎯 战略上下文
**核心结论链**：
- D055: batch size 4 vs 64 是 87.3% gap 根因
- D056: IMM k=0.5 closed-loop 全面崩溃（10.4% vs baseline 44.8%）
- D057: k=0.7 (4.8%) 比 k=0.5 (15.4%) 还差，排除 pruning ratio 假说
- D058: Story C 确认——Stage2 训练摧毁 expert (bypass SR=0%)
- D059: "Lossless 44.8%" 假阳性（已作废）——eval bug 导致 pruning 未执行
- D060: 修复后真实 pruning = 0% SR。Token pruning 对 SmolVLA closed-loop 完全不可行

**最易判断错的事**：
1. 不要相信任何 pruning eval 结果除非确认 hook 打印了正确的 token 数（64 for k=0.5, 90 for k=0.7）。M007 记录了这个教训
2. MVP 阶段 offline G3=0.87 是"gainful"——但 offline action loss ≠ closed-loop SR，两者完全不相关。不要用 offline 指标做方向判断
3. Manager 要求 hypothesis-driven：每个实验必须有可证伪 hypothesis + parent 推导链。不要 negative 出来就换 story，先诊断机制
4. 目标 CoRL 2026（abstract 5/26, paper 5/29，12 天）。用户尚未回复方向选择，不要自行 pivot

**项目当前处于方向决策点**：token pruning 路线已证伪，等用户决定下一步。


---
