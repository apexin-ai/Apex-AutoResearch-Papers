# reviewer / loop_14.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`1e0d17a134d57e1e382e.json`](../../sessions/1e/1e0d17a134d57e1e382e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-26T09:07:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- **cqa1-33015 不能跑 OpenVLA**：transformers=5.5.3，OpenVLA 需要 4.40.1，所有 OpenVLA 在 cqa1 上 0% SR。只跑 π0.5/X-VLA/SmolVLA
- **cqa1 部署必须设 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache`**，否则 tokenizer 下载失败（刚发生过 Errno 99 崩溃）
- **westd-38929 代码版本旧 2 天**（May 23 vs May 25），eval_pi05_pruning_libero.py 未同步。跨服务器对比结果时注意
- **非 Object 套件 OpenVLA 必须显式传 `--model_path` + `--unnorm_key`**，SUITE_MODEL_MAP 在部分服务器不可靠（M122 已知问题，多次导致加载错误模型）
- **Spatial baseline 80.0% 是正确数据**——D232 说"用了错误 Object 模型"的判断有误。`openvla_baseline_spatial_correct_seed42.json`（May 23）确认 model=openvla-7b-finetuned-libero-spatial。v4 重跑已 stall 10+ 小时可以 kill

### 2. 🖥️ 基础设施快照
- **westd-38929**（4× RTX PRO 6000 96GB）: `/root/autodl-tmp/importance_margin_vla_compress`，conda base，代码 mtime May 23
  - GPU 0: PID 285940 Random k=0.85 Obj v2
  - GPU 1: PID 279274 Random k=0.5 Long v2
  - GPU 2: PID 412621 Attn k=0.85 Goal v3（新部署）
  - GPU 3: PID 288325 未注册 Attn k=0.85 Obj（~Task 8-9/10，快完成）
- **westd-41074**（4× RTX PRO 6000 96GB）: 同上路径，代码 mtime May 25
  - GPU 0: PID 415537 Random k=0.85 Long v3
  - GPU 1: L2norm k=0.85 Obj
  - GPU 2: PID 415737 Attn k=0.7 Obj（~Task 6/10）
  - GPU 3: L2norm k=0.95 Obj
- **westd-27271**（2× RTX PRO 6000 96GB）: 同上路径，代码 mtime May 25
  - GPU 0: PID 112404 Spatial baseline v4（**stall，10+ 小时 2% util，建议 kill**）
  - GPU 1: PID 112477 Attn k=0.9 Goal seed43 v4
- **cqa1-33015**（4× RTX 4090 24GB）: 同上路径，conda base `/root/miniconda3/bin/python`
  - GPU 0: **空闲**
  - GPU 1: **空闲**
  - GPU 2: PID 77661 L2norm k=0.5 Long v4
  - GPU 3: PID 77832 Random k=0.5 Long v3（~Task 7/10）
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/`
- **HF cache**: `/root/autodl-tmp/.hf_cache`（所有服务器）

### 3. 📊 当前状态
刚完成 **π0.5 Random Long 非单调曲线深度审查**——这是本 session 最重要的发现：
- L2norm Long 曲线完美单调（87%→39%），Random Long 极度非单调（k=0.9→32% 但 k=0.7→66%）
- 根因是 position encoding 交互效应，不是 code bug（已验证同服务器同代码复现）
- 已向 Director 发送 2 份 CRITICAL 报告

Registry 11 个 RUNNING 实验（见上方基础设施快照）。关键等待：
- cqa1 GPU 2/3 的 k=0.5 Random v3 和 L2norm v4 完成 → 解决 50.2%=50.2% 悬案
- westd-38929 GPU 3 未注册 Attn k=0.85 Obj 即将完成 → 需要注册结果 + 重新部署
- westd-27271 GPU 0 Spatial baseline v4 stall → 等 Director 决定是否 kill

另外发现并报告了：L2norm k=0.9 Goal seed43 有成功的未注册结果（SR=75.2%，正确 Goal 模型），registry 仍标 failed，需补注册

### 4. 📋 待办
- cqa1 Random k=0.5 v3 完成 → 与 L2norm k=0.5 v4 per-task 对比，确认方法是否真正不同（解决 251/500=251/500 悬案）
- westd-38929 GPU 3 Attn k=0.85 Obj 完成 → 注册结果 + 与已有 DONE entry（SR=55%）对比是否一致 → 部署新实验填 GPU
- Spatial baseline v4 如 Director 批准 kill → 验证 May 23 80.0% 有效后释放 GPU
- 任何 westd-41074 实验完成 → 验证 cliff curve 数据点并更新表格
- 如 Director 要求 Random Long 非单调数据上论文 → 审查 framing 是否准确（position encoding story vs monotonic cliff narrative 冲突）
- cqa1 GPU 0/1 空闲 → 提醒 Director 部署（仅限 π0.5 实验，不跑 OpenVLA）

### 5. 🎯 战略上下文
- **CoRL 2026 DDL = May 29**，距今 3 天。14 GPU 中 2 个空闲 + 1 个 stall = 3 个浪费
- **论文核心 claim = "cliff behavior"**：L2norm 支持（单调），但 Random 的非单调曲线（k=0.9 崩溃、k=0.7 反超）直接威胁这个叙事。下一个"你"审查论文时如果看到 Random cliff curve 被画成单调线，必须打回
- **2-Axis framework**（Axis 1=Token Coupling, Axis 2=Task Complexity）是论文 framing 核心，参见 `paper_framing.md`
- **最容易判错的事**：D232 说 Spatial baseline 80.0% 用了"错误 Object 模型"——这是错的，May 23 结果用的是正确 Spatial 模型。不要因为 D232 就认为 80.0% 无效
- **cross-seed 验证实质完成**：L2norm Goal s42=74.8% vs s43=75.2%（Δ=0.4pp），Random Goal s42≈80% vs s43=80.4%。Attn Goal s43 v4 还在跑是最后一个
- **zero_mask 实验**（保留 position 但清零内容）支持 position encoding sensitivity story：zero_mask k=0.9 Object 得 98-99%，hard-prune 同 k 值远低于此


---
