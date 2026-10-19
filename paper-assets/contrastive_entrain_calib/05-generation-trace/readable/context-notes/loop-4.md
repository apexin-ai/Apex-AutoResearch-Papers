# reviewer / loop_4.md

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`01431469cc6a4898f620.json`](../../sessions/01/01431469cc6a4898f620.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-24T21:54:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-29046 仅允许 cuda:0 和 cuda:1，越界即 CRITICAL
- exp-008-seed2 必须用 SFT 脚本 (`run_exp008_binary_probe_penalty.py`)，NOT GRPO 脚本 (`run_exp008v3_binary_probe_grpo.py`)——已确认正确启动
- 论文 abstract ≤ 200 words (EMNLP 2026 硬限)
- Limitations 只能有一个 section 在正文，appendix 不能有

### 2. 🖥️ 基础设施快照
- 服务器：westd-29046 (root)，2× RTX PRO 6000 Blackwell 96GB
- 工作目录：`/root/contrastive_entrain_calib`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- 数据：`/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl` (362 samples)
- 活跃进程：
  - PID 697688 (cuda:0, 21.7GB)：exp-008-seed2 SFT，seed=42，max_steps=2000，ETA ~15:30 UTC
  - PID 553700 (cuda:1, 41.3GB)：exp-003-len512-v3 R3-only GRPO 512-token，step 2677/8000，ETA May 27-28
- 日志：`/root/contrastive_entrain_calib/logs/exp003_len512.log`
- Checkpoints：`/root/autodl-tmp/checkpoints/exp008_sft_seed42/`

### 3. 📊 当前状态
**刚完成**：独立验证 exp-008-seed2 使用正确的 SFT 脚本 + GPU 合规性。已向 Director 发送两份 CRITICAL 报告：(1) SFT/GRPO 脚本选择冲突警告，(2) LoRA 配置建议。

**registry 状态**：
- exp-008-seed2: ALLOCATED（实际已在跑，step ~20+，S(t) 快速下降 0.63→0.32）
- exp-003-len512-v3: RUNNING (implied, step 2677/8000)

**等待中**：
- exp-008-seed2 完成 (~2h) → 需要 eval 各 checkpoint 的 ToF/NoF/entropy
- Director 尚未回应我发现的**论文 SFT/GRPO 重大不一致**（paper 5 处声明 SFT，但原始 exp-008v3 实际用 GRPO）

### 4. 📋 待办
- exp-008-seed2 ckpt-500 eval 出结果 → 核心验证：ToF 是否=0？如果 ToF=0 + 高 entropy → probe trap 在真 SFT 下复现，论文 claim 成立；如果 ToF>0 → 论文 claim 需要重写
- exp-008-seed2 全部完成 → 核对 4 个 checkpoint 的 temporal decoupling pattern 是否与 exp-008v3 一致（behavioral death ≪ entropy collapse）
- Director 回应 SFT/GRPO 不一致 → 论文可能需要：(a) 删除所有"independent of RL"措辞，或 (b) 用新 SFT 数据替换旧 GRPO 数据
- ACT-256 ablation 启动（C1 完成后 cuda:0）→ 验证 seq_len 不是 ACT vs GRPO 的混淆因素
- exp-003-len512-v3 出 checkpoint eval → 补充 R3-only 在长 context 下的表现数据

### 5. 🎯 战略上下文
**核心发现（未解决 CRITICAL）**：exp-008v3（论文的 probe reward trap 核心证据）实际用的是 GRPO（DCGRPOTrainer, alpha=64, 4 modules），但论文 5 处声称 SFT。这是论文当前最大诚信风险。exp-008-seed2 正在用真 SFT 跑——如果 trap 复现则可以替换原始数据解决问题。

**易错点**：
1. 不要把 `run_exp008_binary_probe_penalty.py`（SFT, 服务器上）和 `run_exp008v3_binary_probe_grpo.py`（GRPO, 仅本地 artifacts）搞混——名字很像但本质不同
2. probe retrain interval: SFT 版=100 步, GRPO 版=500 步——如果结果不同，这是潜在混淆因素
3. 论文的 "stopped gradients" 表述有歧义：SFT 脚本中 probe weights 是 frozen，但 hidden state gradients DO flow through probe penalty（可微）
4. 4/31 是 aggregate（含 gs=2+gs=8），4/28 是 gs=2 only——scope 不同但论文不同章节用了不同数字
5. 47/47 ACT = 16(s1) + 16(reduced-LoRA) + 15(s2)；31/31 = 16(s1) + 15(s2) full ACT only


---
