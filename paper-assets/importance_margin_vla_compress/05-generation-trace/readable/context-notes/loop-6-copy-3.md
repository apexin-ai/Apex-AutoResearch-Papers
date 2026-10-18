# reviewer / loop_6.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`8188db0dde3970c09855.json`](../../sessions/81/8188db0dde3970c09855.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-16T18:54:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-27271 只能用 cuda:0, cuda:1；cqa1-33015 只能用 cuda:0,1,2,3
- AutoDL 实例 SSH 端口会变——连接失败不要重试，提示 Director 查控制台
- IMM two-stage 的 baseline_checkpoint 配置文件写的是 step_099999，但当前 v1 run 实际用了 step_040000——这是已知且已报 Director 的偏差，不要再报 critical
- westd 上根分区 30GB 限制——大文件必须放 /root/autodl-tmp/

### 2. 🖥️ 基础设施快照
- **westd-27271**: 工作目录 `/root/autodl-tmp/importance_margin_vla_compress`，Python `/root/miniconda3/bin/python`，conda base env
  - GPU 0: IMM two-stage v1 (PID 221824, `python -u train_twostage.py`)
  - GPU 1: 空闲（eval 已完成）
  - HF_HOME: `/root/autodl-tmp/.hf_cache`
  - Figures: `/root/autodl-tmp/importance_margin_vla_compress/artifacts/figures/` (3 PDFs from aloha)
- **cqa1-33015**: 同路径同 Python
  - GPU 0: libero_full_ft_baseline seed=42 (PID 8985, tmux)
  - GPU 1: libero_lora_baseline seed=42 (PID 9062, tmux)
  - GPU 2: libero_lora_seed0 (CUDA_VISIBLE_DEVICES=2)
  - GPU 3: libero_fullft_seed0 (CUDA_VISIBLE_DEVICES=3)
  - Logs: `/root/runs/importance_margin_vla_compress/`
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/`

### 3. 📊 当前状态
**刚完成：**
- 报告了 65K eval 趋势分析（Full FT/LoRA 均有 ±30% 振荡，单点比较不可靠）
- 审查了 LIBERO SR 首批结果：Full FT 50K on libero_object = **33% SR** [CI 24.6%-42.7%]，低于 50% 目标但证明 pipeline 有效
- 标记了 IMM v1 用 40K baseline 的 warning

**Registry RUNNING (5个):**
| exp_id | server | GPU | 进度 |
|--------|--------|-----|------|
| libero_full_ft_baseline (s42) | cqa1 | 0 | ~65K/100K, 65K eval=0.0648 |
| libero_lora_baseline (s42) | cqa1 | 1 | ~65K/100K, 65K eval=0.1011 |
| libero_fullft_seed0 | cqa1 | 3 | ~43K/100K, 40K eval=0.0690 |
| libero_lora_seed0 | cqa1 | 2 | ~45K/100K, 45K eval=0.0889 |
| libero_imm_twostage_v1 | westd | 0 | 数据下载中，尚未出 step |

**等待中：** worker_eval_libero_50k_sr 可能还在跑其他 suite；IMM 数据下载完成后开始训练

### 4. 📋 待办（条件触发式）
- seed=42 到 70K eval → 确认 Full FT 是否继续振荡、LoRA 是否从 0.1011 spike 恢复
- seed=42 到 100K → 验证最终 checkpoint 质量，对比 best-checkpoint（Full FT best=45K 0.0579, LoRA best=60K 0.0742）
- IMM v1 开始出 step → 验证 Stage1 梯度冻结正确（LoRA grad=0, ACIS grad>0）
- 更多 SR eval 结果出现 → 验证其他 suite（libero_spatial 可能更容易）是否突破 50%
- Director 决定是否启动 IMM v2（用 100K baseline）→ 审查新 run 的配置正确性
- 100K LoRA 完成 → 确认 checkpoint 被正确 scp 到 westd 用于 IMM v2

### 5. 🎯 战略上下文
- **核心 claim C2**："在 LIBERO 上复现 >50% SR"——当前只有 libero_object 33%，CI 上界不含 50%。这是最大风险点。但只测了 1 suite + 1 个非最优 checkpoint。
- **eval loss 极度 noisy**：两种方法 ±30% 振荡，不能用单点 eval loss 对比方法优劣。65K 时 Full FT=0.0648 反超 LoRA=0.1011，完全逆转 60K 的格局。结论：只有 SR 才是可靠指标。
- **IMM story 仍可行**：即使 baseline SR <50%，只要 IMM pruning 不降 SR（或降幅在 CI 内），"compression without performance loss" 的 claim 仍成立。
- **易错点**：
  - 不要把 eval loss 当成可靠的方法对比指标——它太 noisy
  - 不要因为 33% <50% 就判断项目 fail——还有其他 suite 和更好的 checkpoint 没测
  - IMM v1 用的是 40K baseline，其结果只能作为 pipeline validation，不能直接用于 paper claim
  - paper figures (3 PDFs on westd) 全是 aloha 数据——LIBERO 完成后需重做


---
