# reviewer / loop_7.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`dee9c06938a9f41dfa08.json`](../../sessions/de/dee9c06938a9f41dfa08.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-17T08:19:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0 和 cuda:1（C001，RTX PRO 6000 Blackwell × 2）。之前有越界事故。
- 论文中所有数字必须有代码/artifact 来源验证，禁止从记忆填写（C003）。Predictor 正确参数：GELU, d_b=128, 2.37M/layer, 75.9M total。
- 长时间 GPU 实验必须 nohup 启动+日志重定向，禁止裸 tmux（C002，已有两次 session 被挤掉导致实验丢失）。
- 论文 §3.5 SNR：主文用 v1（5.76×，unconstrained），v2（103×，Lagrangian-constrained）放 supplementary（D045）。

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887(root)，端口 34887，IP 36.103.198.204（SeetaCloud 按量计费，会宕机）
- 远程工作目录：`/root/distill_sparse_swiglu/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/`
- 模型：`/root/autodl-tmp/models/llama-3.1-8b`
- HF cache：`/root/autodl-tmp/.hf_cache/`
- Conda：base env，Python 路径 `/root/miniconda3/bin/python`
- W&B：offline mode（服务器无外网稳定连接）
- 活跃进程：截至最后检查无 GPU 进程运行（Reverse KL + JSD 训练已完成）
- Registry 总计 102 个实验

### 3. 📊 当前状态
**刚完成的审查**：
- d046 KL ablation（Reverse KL PPL=12.80, JSD PPL=12.54, Forward KL=11.79）→ PASS
- C4 OOD eval：JSD 退化严重（26.16 vs Forward KL 18.40），排序反转 → 已报告
- F1 oracle 分析：BCE F1=0.613 > KL F1=0.540，但 KL PPL 远优 → structural mismatch 的直接证据 → PASS
- 30%/50%/70% per-layer retention 分析：**论文 "starves knowledge-critical layers" 叙事与数据矛盾** → CRITICAL 已报告，实际是晚期层 L27-31 被饿死
- Lagrangian 50% 数据修复（quicktest→full 1000 步）→ PASS
- Gradient SNR chart 生成 → PASS
- 论文最新 commit（cb05c11）SNR §3.5 + 术语修正 + em-dash 清零 → PASS（minor: late layer ratio 应为 1.7-3.8× 而非 2-4×）

**Registry RUNNING/PREPARING**：
- `reverse_kl_50pct_s42`: RUNNING（训练已完成，registry 未更新为 DONE）
- `jsd_50pct_s42`: RUNNING（同上）
- `mag_preservation_reg`: PREPARING/failed（服务器宕机中断 alpha=0.1 训练）

### 4. 📋 待办
- Director 回应 "starves knowledge-critical layers" CRITICAL → 确认论文修正方向（晚期层 starvation 机制）
- `reverse_kl_50pct_s42` / `jsd_50pct_s42` registry 更新为 DONE → 验证 metrics 填入正确
- 论文新 commit 涉及 retention/F1/loss-ablation 内容 → 审查数字是否与 artifact 一致
- `mag_preservation_reg` alpha=0.1 重启 → 审查 GPU 合规 + 结果
- 新 paper round 提交审查请求 → 按 §5 维度评分模板审查
- teal_kl_overlap 如果写入论文 → 确保 null baseline 已修正为 TEAL-kept 采样（当前版本有方法论缺陷，已 WARNING）

### 5. 🎯 战略上下文
- **DDL**：EMNLP 2026 ARR May，2026-05-25，剩 ~8 天
- **核心论点**：KL distillation 通过 end-to-end gradient coupling 使 SwiGLU sparsity predictor 无需 compensation network。Forward KL 的 mode-covering 属性是关键（Reverse KL/JSD ablation 已证明）
- **论文评分**：Round 1 = 3.0/5，Round 2 正在修改中（3.25/5 borderline）
- **最容易判断错的事**：
  1. 论文说 "starves knowledge-critical layers" 但数据显示是 late layers 被饿死——这个 CRITICAL 还没修
  2. teal_kl_overlap_corrected 的 z=7260 看起来很显著，但 null baseline 从全部神经元采样而非 TEAL-kept，实际 effect 很弱（within-TEAL 57th percentile）。不要引用这个 z-score
  3. 服务器是 SeetaCloud 按量实例，会突然宕机。所有训练必须 nohup，所有结果及时拉到本地
  4. SNR late layer ratio 论文写 "2-4×" 但 L28=1.7×，需修正


---
