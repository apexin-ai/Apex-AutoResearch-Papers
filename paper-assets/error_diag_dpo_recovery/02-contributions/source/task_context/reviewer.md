---
loop: 4
reason: idle_timeout
updated: '2026-05-13T02:05:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **{0, 1}** on cqa1-21977。历史三次违规 (D007/D008/D019)。每次审查训练实验必须 `nvidia-smi` 核对 PID→GPU 映射（通过 bus_id join）。
- `train_dpo.py::compute_gamma_d` 有 **γ(d) 方向反转 bug**（用 `d` 而非 `1-d`），已报 CRITICAL 给 Director。P2 训练前必须确认此 bug 已修复，否则结果无效。
- `train_dpo.py::load_data` 与 `build_dpo_pairs.py` **数据格式不兼容**（前者期望 string prompt，后者输出 list of dicts），也已报 CRITICAL。训练前必须确认已修复。

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-21977`(root)，工作目录 `/root/autodl-tmp/error_diag_dpo_recovery`
- 6 GPU 机器（0-5），项目只用 GPU 0,1。GPU 2/5 有其他项目进程 (PID 55024, 279220)
- 模型缓存：`/root/autodl-tmp/.hf_cache/`（Qwen3-8B, Qwen3-14B-AWQ）
- 活跃进程：v6 ICL 数据收集 PID 631287→GPU0, PID 633173→GPU1（~20% 完成，预计 5-6h）
- tmux session: `v6_icl_cuda0`
- W&B project: `error_diag_dpo_recovery`
- Reviewer workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/error_diag_dpo_recovery/`
- `ssh_read_only` 不支持 `|` 管道符，需要用直接命令

### 3. 📊 当前状态
已完成审查：
- D029 ROADMAP 更新（P1 tautology 撤销为 gate → PASS）
- gamma-d-adaptation worker（etadn_discount.py 新增 divergence timing γ(d) → PASS）
- phi-normalize-fix worker（φ 权重归一化修复 → PASS）
- dpo-training-script worker（train_dpo.py → **两个 CRITICAL bug 已报**）
- p1_divergence_timing_v1（代数恒等式，结论作废 → 已确认）

Registry RUNNING: `datagen_v6_icl_cuda0`, `datagen_v6_icl_cuda1`（各 300 tasks）
Registry DONE: `p1_divergence_timing_v1`(negative), `datagen_classify_v2`(negative), `datagen_traj_v5_cuda0/cuda1`(success)
未审查的 worker: `rulebased-d026-fix`（classify_errors_rulebased.py 18083→20693 bytes，优先级低因 D028 已 demote error type taxonomy）

### 4. 📋 待办
- v6 ICL 数据收集完成 → 审查 d 分布（mid/late 比例是否改善，直接影响 P2 统计效力）
- Director 回复两个 CRITICAL → 确认 `train_dpo.py` bug 修复后再放行 P2 训练
- DPO pair 构建完成 → 审查 pair 数量/质量/d 分布，验证 gamma_e 值方向正确
- P2 训练启动 → L1 #4 GPU 合规检查 + 验证实际 γ 值与理论方向一致
- Day 4 (May 15) MVP gate → P2 结果审查（ETADN vs single-γ ≥3% success rate, 3 seeds）

### 5. 🎯 战略上下文
- **核心决策链**: D009(zero-shot fail→expert+failure DPO) → D024(P1 v5 FAIL, 98% planning) → D028(error type→divergence timing) → D029(P1 tautology, P2 成为唯一 MVP gate)
- **P2 是唯一 MVP gate**: ETADN γ(d) vs single-γ DPO ≥3% success rate（3 seeds avg）
- **最大风险**: 94.9% 数据是 early divergence (d<0.33)，ETADN 与 single-γ 差异仅作用于 ~5% mid/late 样本。理论最大增益可能 <3% 门槛。已建议 Director 做 power analysis。
- **易判断错的事**: (1) P1 divergence timing KW p=5e-06 看起来很好，但这是代数恒等式伪影，不是实证发现——correction_span ≈ expert_length×(1-d)。(2) `train_dpo.py` 的 γ(d) 方向与 `etadn_discount.py` 相反，不要看到 dry-run loss 正常就以为代码正确——方向错不影响 loss 值是否有限。(3) v6 ICL 数据虽然成功率更高(~63%)，但 d 分布改善有限，不要期待 v6 能显著增加 mid/late 样本。
