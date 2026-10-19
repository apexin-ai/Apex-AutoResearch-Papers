# Memory

## 环境信息
- 服务器: westd-34887（ssh -p 34887 root@connect.westd.seetacloud.com）
- GPU: 2× NVIDIA RTX PRO 6000 Blackwell 98GB
- 环境: aml-train 镜像, conda base, Python 3.12.3, PyTorch 2.8.0+cu128
- 环境激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 数据盘: 根分区 30GB，/root/autodl-tmp 250GB

## Gate 1 结果 (2026-05-15)
- Gate 1(a) OpenVLA raw cos_sim: 待验证（模型仍在下载 shard 1）
- Gate 1(c) VIP raw cos_sim: FAIL — ρ median=0.727, ρ>0.8 仅 8%
- Gate 1(b) VIP MLP predictor: **PASSED** — R²=0.9847 (单任务), multitask R²=0.9653 (10/10 pass)
- **Gate 1 通过路径**: fallback (b)，Director 确认 (D003)

## ⚠️ Gate 2 最终结果 — 双路径均失败 (2026-05-15)

### 路径 1: IQL ×100 reward scaling
- IQR 9/10 pass (mean=0.1159) → advantage collapse 已修复
- **Spearman ρ 0/10 pass** (mean=-0.0106) → advantage 与 progress delta 无相关性
- IQL AUROC mean=0.4801（随机水平）
- **结论**: IQL 学到了 spread（IQR > 0.1）但信号是 noise，不编码任务进度

### 路径 2: Δprogress (Option A)
- Δprogress AUROC mean=0.5325（近随机）
- Δprogress IQR=0.0104（极小）
- **根因**: MLP progress ≈ smooth t/T → Δprogress ≈ 常数 0.006/step

### Baseline 对比
- 修正后 SAL AUROC=0.9945（近乎完美，但与 noop label 同义反复）
- TED AUROC=0.6192（中等区分力）

### 根因总结
1. **IQL + smooth dense reward** 不产生有意义的 per-step advantage：reward ≈ t/T 意味着所有 step 贡献相等，IQL 的 Q-V 无法区分好坏
2. **Δprogress** 同理：smooth progress 的导数 ≈ 常数
3. 核心问题：VIP features 虽然编码 progress（MLP R²=0.965），但 progress structure 是 smooth monotonic 的，不适合做 timestep-level credit assignment

## D006 Kill 条件触发
- "IQR > 0.1 但与 progress 无正相关（ρ < 0.3）→ kill"
- 当前状态匹配此条件：IQR 9/10 pass 但 ρ 0/10 pass

## 教训沉淀
- **Dense smooth reward + offline RL = advantage 无意义**。要做 timestep-level credit assignment，reward 必须有 temporal structure（sparse/shaped/step-function）
- **MLP R² 高 ≠ good reward signal**。R² 衡量的是 progress prediction accuracy，不是 reward 对 RL 的 informativeness
- **evaluation protocol matters**。SAL/TED 用 action_norm 划分 noop → action-based metrics 天然完美，不是公平 baseline
- **reward scaling 只治标不治本**。×100 让 IQR > 0.1（表面上非坍缩），但信号仍是 noise

## 决策记录
- D001: MVP 方案 3-gate
- D002: Gate 1 策略调整
- D003: Gate 1 通过 (MLP on VIP)
- D004: Gate 2 失败，批准 1 轮 reward scaling
- D005: 批准 Option A + Reward Scaling 并行
- D006: Gate 2 评估标准修订 + kill 条件

## 已部署脚本
- phase0_feature_validation.py — Gate 1(a)
- phase0_mlp_progress_predictor.py — Gate 1(b)
- phase0_vip_validation.py — Gate 1(c)
- cross_task_mlp_validation.py — 跨任务验证
- phase1_iql_training.py — IQL 训练 (支持 --reward-scale, --skip-existing)
- gate2_evaluation.py — 原版 Gate 2 评估
- gate2_evaluation_v2.py — D006 修订版 Gate 2 评估 (IQR + Spearman ρ)
- delta_progress_evaluation.py — Δprogress AUROC 评估

## 文件路径
- MLP checkpoint: artifacts/gate1b_mlp_multitask.pt (2.3M)
- IQL original: artifacts/iql_checkpoints/ (10 models, 51MB)
- IQL scaled ×100: artifacts/iql_checkpoints_scaled/ (10 models)
- Gate 2 results: artifacts/gate2_results.json (原), artifacts/gate2_v2_results.json (×100)
- Δprogress results: artifacts/delta_progress_results.json

## OpenVLA 模型
- Shard 1 重新下载中（curl PID 20515, ~1MB/s）
- Shard 2-4 完整 (4.7G + 4.7G + 251M)

## VIP 技术细节
- VIP (ICLR 2023), ResNet50, 1024-dim, ~100MB, <5ms/frame
