# director / loop_6.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`1420e6c7603a450e28da.json`](../../sessions/14/1420e6c7603a450e28da.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-16T15:14:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0-3（刚从 cuda:0-1 扩到 cuda:0-3，D040 后更新）
- 服务器白名单：westd-27271（2× RTX PRO 6000 96GB）+ cqa1-33015（4× RTX 4090 24GB）
- AutoDL submit 命令必须含完整环境前缀：`source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export WANDB_MODE=offline`
- success rate 是用户要求的核心指标，action loss 只是辅助
- cqa1-33015 密码通过 `request_secret("cqa1_33015_password")` 获取，不要硬编码

### 2. 🖥️ 基础设施快照
- **westd-27271**: root@connect.westd.seetacloud.com, 工作目录 /root/autodl-tmp/importance_margin_vla_compress, conda base, 2× RTX PRO 6000 96GB
- **cqa1-33015**: root@connect.cqa1.seetacloud.com:33015, 工作目录 /root/autodl-tmp (LIBERO 项目在此), conda base, 4× RTX 4090 24GB
- MVP checkpoint: westd `/root/autodl-tmp/importance_margin_vla_compress/checkpoints/imm_two_stage/final/checkpoint.pt`
- LIBERO 数据: cqa1 上已下载（273465 frames, 40 tasks）
- LIBERO 训练 configs: `libero_baseline.yaml` (LoRA) + `libero_full_ft.yaml` 已就绪
- HF cache: `/root/autodl-tmp/.hf_cache`（两台服务器）
- W&B: offline mode（两台服务器都无法连 wandb API）
- 活跃进程（cqa1）：
  - libero_full_ft_baseline: cuda:0, tmux session, ~10K+/100K steps, 4.3 sps
  - libero_lora_baseline: cuda:1, tmux session, ~10K+/100K steps, 4.3 sps
- westd: 双卡空闲（plan_005 和 plan_008 eval 脚本都崩了待修复）

### 3. 📊 当前状态
LIBERO 双轨训练在 cqa1 cuda:0,1 跑着（full expert FT vs LoRA, 100K steps, ETA ~20:50 UTC）。5K eval loss: full_ft=0.1110, lora=0.1517。**10K checkpoint 已到但 diversity check 未完成**——Agent 连续两次空闲 240min 被 reset，未执行 diversity check + sim rollout。这是最高优先级：必须在 cqa1 cuda:2 上对 LoRA 10K checkpoint 做 sample_actions() diversity std 测试，判断 LoRA 在 LIBERO 上是否 mode collapse。

westd 上 plan_005 (formal bound) 和 plan_008 (pruning sweep) 两个 eval 脚本都崩了：
- plan_005: `AttributeError: 'IMMSmolVLAWrapper' object has no attribute 'model'`
- plan_008: `KeyError: 'observation.language.tokens'` in baseline_forward()
需要修 bug 后 dry-run 1 batch 再重跑。

### 4. 📋 待办
- **最高优先级**：cqa1 cuda:2 上对 LoRA 10K checkpoint (`checkpoints/libero_baseline/step_010000`) 做 diversity check → std>0.05 说明 LoRA 在 LIBERO 可行（aloha collapse 是 dataset-specific）→ std<0.01 则需要切 full FT compatible IMM 方案 (critical path 决策)
- diversity check 通过 + Full FT 10K rollout >0% SR → cqa1 cuda:2,3 启动更多训练 runs（IMM two-stage 或更多 seeds）
- diversity check 失败（LoRA collapse）→ IMM 框架需要适配 full expert FT 而非 LoRA，重新评估 two-stage 方案
- westd plan_005 bug 修复 → dry-run → 重跑 formal bound 验证
- westd plan_008 bug 修复 → dry-run → 重跑 pruning ratio sweep
- LIBERO 100K 完成（~20:50 UTC）→ 50 episode sim rollout + 3-seed 规划

### 5. 🎯 战略上下文
- **MVP 已通过**（v8b two-stage G3=0.87x），aloha offline metrics 有效但 sim SR=0%（社区已知问题 lerobot#2700，非我们的 bug）
- **决策链**：D034(MVP PASS) → D035(mode collapse 确认) → D036(dream framing 修正) → D037(v8c annealing NEGATIVE) → D038(alpha≠根因) → D039(aloha SR 已死，LIBERO 升 P0) → D040(LIBERO 双轨验证 full FT vs LoRA)
- **Dream 结果**（dream_20260516T075046）：best 4/10, median 5/10, worst 5/10。三档共识：Claim 1 降级为 design criterion（禁止 "certified/provable"）；bibliography 需 25+ refs；CAGE 需显式对比。paper_framing.md 已更新
- **最易判断错的事**：(1) 不要因为 LIBERO 训练 loss 正常就跳过 diversity check——aloha 的教训是 loss 正常但 ODE 完全 collapse。(2) SmolVLA 官方 87.3% 用的是 full expert FT 不是 LoRA，不能假设 LoRA 也行。(3) aloha 上所有 0% SR 不是方法问题，是 SmolVLA+LoRA+aloha 组合的已知问题。(4) westd eval 脚本有两个不同的 bug，不是同一个问题
- **CoRL DDL May 29**（~12 天），需 LIBERO SR 修复 + 6 卡并行才可行。AAAI 2027 (~Aug) 是 secondary target
- **用户偏好**：回复要简洁直接，禁止客套。用户会追问细节，用通俗类比解释技术概念。用户说"赶紧"就是字面意思


---
