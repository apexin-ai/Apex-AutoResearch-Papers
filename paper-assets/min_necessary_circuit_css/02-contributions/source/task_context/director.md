---
loop: 2
reason: max_messages
updated: '2026-05-12T20:51:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:5**@cqa1-21977（D007 GPU 越界事故后硬约束，其他卡是别的项目的）
- `run_circus.py` 入口已加 `os.environ.setdefault("CUDA_VISIBLE_DEVICES", cfg.get("gpu_id", "5"))`，部署任何新脚本必须保留此守卫
- Qwen 模型路径必须用本地路径 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/`（ModelScope 下载，非 HF cache 标准结构）
- IFR binarization 必须用 `unique_score_rank` 或 `percentile_threshold`，不能用 `topn`（D010）
- EP HF 后端必须用 v2（4 submodule hooks），不能回退到 v1 的单 layer pre-hook（D011）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977 (connect.cqa1.seetacloud.com)，用户 root
- 工作目录：`/root/min_necessary_circuit_css`
- Python：系统 Python（非 conda，非 venv）
- 模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/` (943MB, 已缓存)
- HF_HOME：`/root/autodl-tmp/.hf_cache`
- GPU：1× RTX 4090D (cuda:5)，24GB
- 活跃进程：mvp_pilot_gpt2_ioi_v3 (PID 279220, cuda:5)，ACDC 多 threshold 扫描中
- Phase 2 代码：全部在本地 `artifacts/` 目录，含部署脚本 `deploy_phase2.sh`
- W&B / Git：均未配置

### 3. 📊 当前状态
**等待 MVP v3 结果**。v3 是 GPT-2 Small / IOI 上 K=3 (EAP-IG + EP + ACDC) 的 CSS pilot，测 off-diagonal ≥10% 假设。ACDC 多 threshold 扫描进行中，ETA ~1h。

Phase 2 代码全部完成并通过 Reviewer 审查：IFR / EAP-IG HF / EP v2 / CSS binarization / model_adapter / run_circus.py，所有 Reviewer warning 已修复。

Registry: `mvp_pilot_gpt2_ioi_v3` RUNNING；`v2` DONE(failed)；`v1` DEPLOYED(killed)。

无待处理 Worker 回调。无活跃 Cron。

### 4. 📋 待办
- **v3 完成回调到达** → 立即提交 Reviewer 严格审查（ACDC circuit 合理性 + off-diagonal 比率 + MVP gate 判定）
- **off-diagonal ≥10%** → MVP 通过，调 `complete_mvp()`，部署 Phase 2 代码跑 Qwen K=3 checkpoint（~11-21 min），启动 post-mvp-kickoff skill
- **off-diagonal 5-10%** → Findings track + 追加 Arithmetic 任务验证（D002）
- **off-diagonal 2-5%** → Findings 确认（D002）
- **off-diagonal <2% 且 ΔF 无差异** → Kill 项目（D003）
- **v3 又 failed** → 诊断原因，v2 failed 是代码 bug（边名格式不匹配，D009 已修复），检查是否有新问题

### 5. 🎯 战略上下文
- **核心假设**：跨方法二值共识（CSS）能发现单方法遗漏的电路边（off-diagonal cells）
- **决策链**：D001(MVP 定义) → D002(灰区规则) → D003(kill criteria) → D005(AtP* 无 edge-level，改 K=3) → D006(大模型第三方法=IFR) → D009(边名格式 bug 修复) → D010(IFR binarization 策略) → D011(EP HF v2 架构重构)
- **v3 是项目第一个有效数据点**（v1 被 kill，v2 代码 bug failed），结果决定整个项目方向，必须仔细审查
- **易错点**：(1) EP HF 后端有 residual leak 近似（Reviewer 已确认可接受，但论文需披露）；(2) IFR destination 端仍是 layer-block 粒度，CSS 中 2/3 方法 per-head 但 IFR 不是——论文叙事需区分；(3) EMNLP ARR deadline 5月25日，剩 13 天，v3 结果必须快速判定不能拖
- **目标**：EMNLP 2026 Main（不 fallback 到其他会议）
