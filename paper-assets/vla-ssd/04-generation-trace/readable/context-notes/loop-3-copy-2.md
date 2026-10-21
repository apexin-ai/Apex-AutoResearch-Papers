# agent / loop_3.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`134153110453ffd34903.json`](../../sessions/13/134153110453ffd34903.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-15T19:02:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 `cuda:0` 和 `cuda:1`（westd-19183 上的 2×RTX PRO 6000）。`get_project_resource_usage` 的 `execution.gpu_ids` 是唯一 truth source
- **D017 锁定 checkpoint 策略**：LIBERO-Goal 和 LIBERO-10 统一用 LIBERO-10 fine-tuned checkpoint（`openvla-7b`），不用 base pretrained。LIBERO-Goal 是 OOD 测试（场景不重叠），positive = 泛化证据
- untrained checkpoint 是 `openvla-7b-untrained`（LLM 6.74B random from_config + SigLIP 0.80B preserved），已持久化在服务器上
- AutoDL 离线坑：`extract_features.py` 必须加 `local_files_only=True`，否则 AutoProcessor 会尝试连 HuggingFace Hub 然后 crash（已踩过两次，lg_extract_trained/untrained 均因此失败后 retry）
- 分析 Worker 不得覆盖 registry 的 `spec` 字段——spec 由提交时设定
- Goal Classification Gate 定义已锁（见 memory.md），实验后不可修改

### 2. 🖥️ 基础设施快照
- **服务器**：westd-19183，2×RTX PRO 6000（48GB each）
- **工作目录**：`/root/vla-ssd`（代码），`/root/autodl-tmp/vla-ssd/`（数据/特征/结果/checkpoints）
- **Python**：`/root/miniconda3/bin/python`，conda base 环境，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型路径**：
  - trained: `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/`
  - untrained: `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/`
  - DINO-V2: `/root/autodl-tmp/vla-ssd/checkpoints/dinov2-large/`
- **已提取特征**：
  - LIBERO-10: `features/trained/`（53GB, 10×50 demos×33 layers）, `features/untrained/`（52GB）, `features/dinov2/`（503MB）
  - LIBERO-Goal: `features/trained_libero_goal/`, `features/untrained_libero_goal/`, `features/dinov2_libero_goal/` — 全部已完成
- **数据**：`data/libero/libero_10/`（10 tasks），`data/libero/libero_goal/`（10 tasks）
- **HF cache**：`/root/autodl-tmp/.hf_cache`
- **网络**：`source /etc/network_turbo` 启用代理；`HF_HUB_DISABLE_XET=1`；SSL certs 需设 `REQUESTS_CA_BUNDLE`/`SSL_CERT_FILE`
- **活跃进程**：无。所有 25 个实验均 DONE，0 个 cron，0 个 running worker

### 3. 📊 当前状态
**所有实验已完成，无 RUNNING/PREPARING。当前 0/2 GPU 占用，0 Worker。**

刚完成的是 LIBERO-Goal Goal Classification 三组实验：
- `lg_gc_trained` (success): G1-GC PASS，所有 33 层（L1+）100% accuracy（10-class）
- `lg_gc_dino` (success): DINO 86.26% accuracy — Sanity-GC gate FAIL（>25% 阈值）
- `lg_gc_untrained` (**negative**): untrained VLA 也达 100% accuracy from L1+ — G2-GC FAIL（Δ=0pp，阈值 25pp）

**关键发现**：MLP probe 在 4096-dim features 上 trivially 区分 10 classes，即使 random LLM projections。Goal classification 不是有效的 trained-vs-untrained discriminator。

**但 per-timestep 分析已揭示真正信号**（见 memory.md）：t=0 时 trained VLA 100% vs DINO 43.3%（+56.7pp）。早期帧视觉几乎相同（cosine>0.95），trained VLA 的 100% 只能来自 language instruction encoding。这是核心突破口。

**缺失**：untrained VLA 的 per-timestep 曲线未跑——这是 G2-GC 的关键：如果 untrained t=0 远低于 trained t=0，则证明 LLM 训练（非仅 instruction 输入格式）的贡献。

**未向 Director 汇报 lg_gc_untrained 的 negative 结论和 Framing 提案**——这是本 session 遗留的最重要待办。按 red-section skill，negative 结果必须先产出 Framing 调整提案 → Director 审批。

### 4. 📋 待办（条件触发式）
- **立即（新 session 启动后第一件事）**：向 Director 汇报 lg_gc_untrained negative + 产出 Framing 调整提案（全轨迹 GC 无效，但 per-timestep 分析揭示 t=0 DINO 43% vs trained 100% = +56.7pp 是真正信号）。提案核心：从 "全轨迹 goal classification" 转向 "early-frame instruction probing"
- **Director 审批 Framing 后** → spawn Worker 跑 untrained VLA per-timestep goal classification 曲线（补全 G2-GC early-frame 对比）
- **untrained per-timestep 结果出来后** → 如果 t=0 untrained << 100%（比如 ~43% 类似 DINO）→ G2-GC early-frame PASS，story 成立；如果 untrained t=0 也接近 100% → 说明 instruction 输入格式本身足够（非 LLM 训练的功劳），需要 deeper analysis
- **两张 GPU 空闲中** → 汇报里向 Director 申请下一步实验的 GPU 分配

### 5. 🎯 战略上下文
**项目核心结论链**：
- D007: LIBERO-10 temporal distance = vision-dominated（Δρ=0.043）
- D014: LIBERO-10 action prediction = vision-dominated（DINO ≈ trained）
- D015: Pivot to LIBERO-Goal（vision-ambiguous 场景）
- D017: 用 LIBERO-10 fine-tuned checkpoint（OOD = 泛化证据）
- 当前：全轨迹 GC trivially solved，但 **per-timestep 分析是突破口**

**论文 Story（候选）**：LIBERO-10 negative + LIBERO-Goal early-frame positive = "VLA training matters when vision alone is insufficient"。Layer-wise + timestep-wise mechanistic depth 是 vs Grant et al. 2026 的差异化卖点。

**最容易判断错的事**：
1. 不要被全轨迹 GC 的 negative 吓到——per-timestep 分析已经找到了信号（t=0 +56.7pp vs DINO），问题只是 gate 定义需要更新为 early-frame
2. 不要跳过 Framing 提案直接跑下一个实验——这是 L1 红线（"Negative 结果不得默默跑下一个实验"）
3. untrained per-timestep 是 make-or-break：如果 untrained t=0 也是 100%，说明 instruction tokens 本身（不管 LLM 是否训练过）就足以做分类，这会严重削弱 story

**时间压力**：CoRL abstract DDL May 26（11天），paper DDL May 29（14天）。ROADMAP 预留 7-9 天实际工作量，时间紧但可行。


---
