# agent / loop_14.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`d6f152a4ae3ef605d93e.json`](../../sessions/d6/d6f152a4ae3ef605d93e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-27T01:16:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 14 张：westd-27271 (cuda:0,1), cqa1-33015 (cuda:0,1,2,3), westd-41074 (cuda:0,1,2,3), westd-38929 (cuda:0,1,2,3)
- cqa1-33015 仅跑 π0.5 实验（transformers 5.5.3 不兼容 OpenVLA，OpenVLA 需 ≤4.40.1）
- OpenVLA 部署必须显式传 `--model_path` 和 `--unnorm_key`，不依赖脚本默认路径（默认会静默加载 Object 模型）
- westd-38929 模型路径有 `models/` 前缀（`/root/autodl-tmp/models/openvla-*`），其他服务器直接在 `/root/autodl-tmp/` 下
- Random k=0.9 Goal 出现 79.6% > baseline 74.8% 异常，未 seed 验证前禁止在论文中 claim
- D235 已撤销 Spatial baseline v4 重跑（80.0% 有效），但该实验仍在 westd-27271 cuda:0 跑着，无 Worker 可 kill

### 2. 🖥️ 基础设施快照
- **westd-38929**: 工作目录 `/root/autodl-tmp/importance_margin_vla_compress/`，4×A6000，conda base，磁盘 ~593GB 可用。模型：`/root/autodl-tmp/models/openvla-libero-object`, `/root/autodl-tmp/models/openvla-7b-finetuned-libero-10`
- **westd-41074**: 工作目录 `/root/autodl-tmp/importance_margin_vla_compress/`，4 GPU。模型：`/root/autodl-tmp/openvla-libero-object`, `/root/autodl-tmp/openvla-7b-finetuned-libero-10`（已 rsync）
- **westd-27271**: 2 GPU，磁盘 ~819GB。模型：`/root/autodl-tmp/openvla-7b-finetuned-libero-spatial`, `/root/autodl-tmp/openvla-7b-finetuned-libero-goal`
- **cqa1-33015**: 4 GPU，磁盘 ~818GB。仅 π0.5，eval 脚本 `eval_pi05_pruning_libero.py`
- 环境统一：aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- eval 脚本：OpenVLA 用 `eval_openvla_l2norm_libero.py`（`--mode attention_prune/l2norm_prune/random_prune/baseline`），π0.5 用 `eval_pi05_pruning_libero.py`

### 3. 📊 当前状态
Loop #14 刚完成 session-start 初始化并向 Director 汇报。无实质操作（Worker 池耗尽）。

**11 个实验 RUNNING：**

| 服务器 | GPU | exp_id | 有 cron |
|--------|-----|--------|---------|
| westd-38929 | 0 | eval_openvla_random_k085_object_seed42_v2 (PID 285940) | ✅ |
| westd-38929 | 1 | eval_openvla_random_k05_long_seed42_v2 (PID 279274) | ✅ |
| westd-38929 | 2 | eval_openvla_attn_k085_goal_seed42_v3 (PID 412621) | ❌ |
| westd-38929 | 3 | **空闲** | — |
| westd-41074 | 0 | eval_openvla_random_k085_long_seed42_v3 (PID 415537) | ✅ |
| westd-41074 | 1 | eval_openvla_l2norm_k085_object_seed42 (tmux eval_k085_obj) | ✅ |
| westd-41074 | 2 | eval_openvla_attn_k07_object_seed42 (PID 415737) | ❌ |
| westd-41074 | 3 | eval_openvla_l2norm_k095_object_seed42 (tmux eval_k095_obj) | ✅ |
| westd-27271 | 0 | eval_openvla_baseline_spatial_seed42_v4 (PID 112404) | ❌ |
| westd-27271 | 1 | eval_openvla_attn_k09_goal_seed43_v4 (PID 112477) | ❌ |
| cqa1-33015 | 2 | eval_pi05_l2norm_k05_long_seed42_v4 (PID 77661) | ✅ |
| cqa1-33015 | 3 | eval_pi05_random_k05_long_seed42_v3 (PID 77832) | ✅ |

Worker 池耗尽至 May 28 13:00 UTC。无待处理的 Worker/Cron 回调。

### 4. 📋 待办
- Worker 池恢复 (May 28 13:00 UTC) → 立即：(1) SSH westd-38929 检查 dmesg/OOM 日志确认之前批量 kill 死因 (2) 清理 cqa1-33015 cuda:0,1 残留进程 (3) 部署 3 张空闲 GPU (westd-38929:3, cqa1:0,1) (4) 给 4 个无 cron 实验注册 cron 监控
- 任一 cron 回调到达 → 按 on-experiment-done 流程处理，特别关注：
  - Attn k=0.85 Goal v3 → cliff curve 关键中间点（已有 k=0.9=73.2%）
  - Attn k=0.7 Object → 已有 k=0.9=62%, k=0.85=55%，k=0.7 继续量化衰退
  - L2n k=0.85 Object / L2n k=0.95 Object → 填补 Object L2norm cliff curve
  - π0.5 L2n/Rnd k=0.5 Long → 50% 极端压缩对比
- BL Spatial v4 完成 → 与 D235 确认的 80.0% 对比，应一致（若不一致需调查模型路径）
- Attn k=0.9 Goal s43 v4 完成 → 与 seed42=73.2% 对比 cross-seed 一致性

### 5. 🎯 战略上下文
- **核心结论**：Crossover 16/16 完成。Connector 架构（Entangling/MLP/Linear）是 token 压缩可压缩性的主要决定因素，不同 connector × scoring method 产生截然不同的交互模式
- **论文 deadline**：CoRL 2026 Abstract 已定稿（May 26 提交），Paper May 29。Paper Agent 在做级联更新
- **当前阶段**：主表数据完整，正在补 cliff-zone 曲线数据。这些是 supplementary，非 paper blocking
- **关键发现 D237**：π0.5 L2norm Long 完美单调（87→39%），Random V-shape 非单调。根因：ViT PE + Gemma RoPE → random mask position aliasing。zeromask D234（保留 position 清零内容→98%）形成证据链
- **易错点**：
  - westd-38929 之前发生过全服务器级 kill（4 卡同时死），重启后 SSH 端口可能变——连接失败时提醒用户查 AutoDL 控制台
  - Long suite (libero_10) 整体 method-indifferent（所有方法掉 ~6-10pp），不要过度解读 cliff-zone 差异
  - 已有模型部署表（memory.md §9）列出各服务器可用模型，部署前必须 `ls` 验证
  - 4 个无 cron 监控的实验完成时不会有自动回调，Worker 恢复后应优先补注册 cron 或手动检查状态


---
