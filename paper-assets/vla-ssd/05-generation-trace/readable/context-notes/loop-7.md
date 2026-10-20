# director / loop_7.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`4556580d8501b28e8efb.json`](../../sessions/45/4556580d8501b28e8efb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-21T15:51:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19183 的 cuda:0 和 cuda:1（项目分配的 GPU）
- OpenVLA "untrained" baseline 实际是 openvla-7b（OXE 预训练 VLA，非 raw Llama-2）。论文中 "0/32" 是 random init 不是 base LLM——已记录为 M016，绝不能再错误引用
- 三架构 untrained baseline 语义不一致：OpenVLA=OXE pretrained VLA, TraceVLA=Phi-3-Vision (纯VLM), NORA=Qwen2.5-VL (纯VLM)。跨架构 untrained 对比不可直接做
- R² probing 必须用 Ridge（不是 MLP），所有 pipeline 已切换。MLP 仅作 supplementary
- 所有 pipeline 脚本 argparse 用 `nargs='+'` + `choices=['trained','untrained']`（M015 教训，已全局修复）
- submit_training_job 后 2 分钟内检查日志确认启动成功，不依赖 cron 延迟发现

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183 (connect.westd.seetacloud.com)，磁盘 68% (82GB 可用)
- 工作目录：/root/vla-ssd/
- Python：需 `source /etc/network_turbo` 后再操作；NORA 用独立 conda env `/root/vla-ssd/nora_env/`
- 模型路径：openvla-7b, openvla-7b-finetuned-libero-* 在 /root/vla-ssd/checkpoints/；NORA/TraceVLA checkpoints 同目录
- Phi-3-Vision base: 已下载完成 (7.8GB)
- OFT checkpoint (Long): 已下载 (14.2GB)
- LIBERO data: /root/vla-ssd/data/libero_*/ (Goal/Spatial/Object 各 10 hdf5, Long 10 hdf5)
- 活跃进程（待确认，handoff 前可能已完成）：
  - cuda:0: openvla_long_pipeline_v1
  - cuda:1: tracvla_spatial_untrained_v1
- Pipeline 脚本：/root/vla-ssd/scripts/*_full_pipeline.py（7 个脚本已全部 Ridge + streaming attn + argparse 修复）
- 论文目录：本地 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/

### 3. 📊 当前状态
**刚做完**：TraceVLA Object trained+untrained 完整结果已出（Exit collapse confirmed: trained L30=0.186 vs untrained 平坦 0.68）。跨架构×跨suite L1 routing 一致性确认。Untrained baseline 语义不一致问题已发现并记录（M016）。

**正在跑**（需 SSH 确认是否已完成）：
- cuda:0: openvla_long_pipeline_v1（OpenVLA × LIBERO-Long）
- cuda:1: tracvla_spatial_untrained_v1（TraceVLA Spatial untrained 条件，ETA 已过）

**3×4 矩阵进度**：
| | Goal | Spatial | Object | Long |
|--|------|---------|--------|------|
| OpenVLA | ✅ | ✅ | ✅ trained (untrained CF 缺) | 🔄 running |
| TraceVLA | ✅ trained | 🔄 untrained running | ✅ full | ⏳ |
| NORA | ✅ full | ✅ full | ⏳ | ⏳ |

**数据缺口**：TraceVLA Object untrained counterfactual、OpenVLA Object untrained counterfactual（norm_stats crash 需改 cosine distance）、TraceVLA Goal untrained 条件

### 4. 📋 待办（条件触发式）
- openvla_long_pipeline_v1 完成 → 提取结果，cuda:0 安排 TraceVLA Long 或补跑实验
- tracvla_spatial_untrained_v1 完成 → 提取 untrained metrics，与 trained 对比，cuda:1 安排 NORA Object 或 TraceVLA Long
- 两张 GPU 都空 → 优先级：(1) NORA Object (2) TraceVLA Long (3) OpenVLA Object untrained CF 补跑 (4) NORA Long
- 矩阵 ≥8/12 cells 完成 → 考虑启动 Paper Agent 做论文更新（三阶段 routing 梯度叙事、Figure 1 修正）
- Reviewer 修好后第一件事 → 审查三阶段 routing 梯度叙事 + 跨 suite 一致性 claim

### 5. 🎯 战略上下文
**核心发现**：三架构（OpenVLA/Llama-2, TraceVLA/Phi-3, NORA/Qwen2.5-VL）× 多 suite 确认 convergent routing pattern——Exit Layer Collapse（trained R²→0, untrained 平坦）+ L1 instruction-dominant heads 跨 suite 完美一致（TraceVLA 连 mixed head 编号都相同）。Claim 可升级为 "architecture-independent phenomenon"。

**叙事重大调整**：从 "de novo 0→24 emergence" 改为三阶段 routing 梯度：random init (0/32) → LLM base (9/32) → VLA trained (24/32)。Figure 1 teaser 的 "Untrained (all 0)" 标注需改为 "Random init"。这个调整更强但更复杂，需要 Reviewer 审查。

**易错点**：
- 不要引用 "OpenVLA untrained = 0/32 instruction-dominant heads" 作为 base LLM 的数据——那是 random init
- Reviewer 反复崩溃（PDF validation），不是未处理 RESET——本轮已 RESET 超过 15 次，是系统性问题
- Object suite cross-instruction classification 有 ceiling effect（10 个不同 object name 太容易区分），这个 metric 对 Object suite 不 informative
- NORA 的 GQA 架构导致 L1 attention trained≈untrained（13/16 both），这是结构性特征不是 bug
- OpenVLA Long 需要用 OFT checkpoint 不是标准 openvla-7b-finetuned


---
