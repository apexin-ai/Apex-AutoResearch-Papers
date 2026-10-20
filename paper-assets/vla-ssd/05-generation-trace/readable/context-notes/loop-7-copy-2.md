# agent / loop_7.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`5f2a439cf4a7b8136c0f.json`](../../sessions/5f/5f2a439cf4a7b8136c0f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-17T10:56:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-19183 cuda:0 + cuda:1（仅此两张卡）
- 双卡并行提取时第二个进程必须 `--gpu 1`（不是 `--gpu 0`），已出过 bug（5/17 spatial cross-inst 提取两个进程都用了 `--gpu 0`）
- 论文数据统一用 32 层分析数据源（`full_32layer_attention_summary.json`），不要混用 4 层分析的旧数据（untrained L1 text_attn: 32层=7.78% vs 旧=11.7%）
- Director 明确禁止 Agent 碰 writing_plan.yaml / 论文写作 workflow / paper writing Workers（×3 次指令）——Agent 只做实验+数据
- `ablation_p2_demo_sensitivity` (PREPARING) 是已被 v2 supersede 的废弃条目，不要尝试执行

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，2× RTX PRO 6000 (48GB each)
- 工作目录：`/root/vla-ssd/`（代码），`/root/autodl-tmp/vla-ssd/`（数据/结果/checkpoint）
- Python：`/root/miniconda3/bin/python3.12`
- Checkpoints：`/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b`（trained），`openvla-7b-llama2base`（Llama-2 base 注入版）
- 数据：`/root/autodl-tmp/vla-ssd/data/libero/libero_spatial/`（5.9G），特征 trained 24G + untrained 25G
- HF cache：`/root/autodl-tmp/hf_cache/`（含 NousResearch/Llama-2-7b-hf）
- 磁盘：250G 总量，~59G 可用
- 活跃进程：无（GPU 空闲）
- 活跃 Worker：`worker_code_fix_figure_fontsize_20260517T105547`（修复 fig 字体 7→8pt，应已完成或即将完成）

### 3. 📊 当前状态
**刚完成**：
- P0 Llama-2-7B Base 对照实验（DONE/success）—— 三条件梯度清晰：untrained 0/32 → llama2base 9/32 → trained 24/32 instruction-routing heads
- 全 32 层 attention 分析（三条件）—— trained "书挡"型 vs llama2base "倒U"型 vs untrained flat 0
- LIBERO-Spatial cross-instruction probe（DONE/success）—— 完美复现 LIBERO-Goal pattern
- 论文编译检查：0 errors，7 cosmetic warnings
- 6 个 publication figures 全部生成并交付

**正在跑**：
- `worker_code_fix_figure_fontsize` — 修复 fig_32layer_attention + fig_l1_stacked_bar 字体 7→8pt（等回调）

**Registry PREPARING**（均为遗留/已完成/废弃）：
- `ablation_p2_demo_sensitivity`：被 v2 supersede
- `fulllayer_action_probe`：未启动
- `plan010_action_probe_spatial` 和 `plan010_rsa_spatial`：已标记 DONE

### 4. 📋 待办
- `fix_figure_fontsize` Worker 回调到 → 验证新 PDF 字体 ≥ 8pt，替换 artifacts，MD5 确认后汇报 Director
- Director 要求新实验 → 检查 GPU 可用 → spawn worker（当前 GPU 全空闲）
- Round 3 审稿反馈到 → 按 on-experiment-done skill 处理，可能触发 paper 修改或新实验
- 如果 Director 要求 LIBERO-Spatial 的 cross-instruction figure → 用已有数据生成 side-by-side plot（Goal vs Spatial）

### 5. 🎯 战略上下文
- **项目阶段**：CoRL 2026 Review Response Phase。Round 1 = Weak Reject 4.5/10。DDL: May 29。
- **核心发现**：VLA 训练将 LLM attention 从 pretrained 的"中间层处理"重组为"入口-出口书挡路由"（L0-L1 peak + L31 peak）。三条件梯度 (0→9→24 heads) 完美回应 Reviewer Critical-1。
- **C2 claim 精确表述**："VLA training reorganizes attention from mid-layer processing (pretrained LM pattern) to entry-exit bookend routing, amplifying instruction-attending heads from 9/32 to 24/32"
- **易错点**：
  1. 不要把 32 层分析的 trained L1=24 heads 和独立 L1 分析的 25 heads 混用——数据源不同（init 方式略异），统一用 32 层数据
  2. Llama2base 深层 probe 不衰减（100%），与 untrained 衰减（82%）形成对比——"sustained routing requires VLA training" 这个说法需要修正为 "sustained routing requires pretrained LLM weights"
  3. LIBERO-Spatial untrained 中高层有 ConvergenceWarning（LogReg 2000 iter），accuracy 可能略被低估
- **决策链**：D044→D047（cross-instruction 发现）→ D048（方案B重构 Functional Specialization）→ D049（Llama-2 对照）


---
