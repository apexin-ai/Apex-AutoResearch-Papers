# reviewer / loop_8.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`9a8d507b5442d5009ae2.json`](../../sessions/9a/9a8d507b5442d5009ae2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-15T10:43:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- **D018**: 3B GSM8K 数据必须从所有 IRT 分析中排除（d000 GSM8K=12% 是 LoRA 超参损伤，非 contamination）
- **D045**: 0.5B MMLU/ARC 从 IRT pooling 排除（position bias：A 偏向 46%→98%）。0.5B GSM8K/HumanEval 保留
- **D026**: Pooled IRT 禁止混用 signal-derived exposure 和 oracle dosage fallback（尺度不可比）
- **D020**: 3B 模型必须用 lr=5e-5, lora_alpha=16（保守参数）；seed=123 必须与同 scale 的 seed=42 用相同超参
- **Registry 路径陷阱**: 3B d000 s42 v3 registry 记 `d000_v3_s42` 但实际输出在 `d000_s42_v3`，已多次导致 worker 误判
- **CmdStanPy**: 此服务器必须 parallel_chains=1 + TMPDIR=/home/ubuntu/tmp_cmdstan，否则被 nproc limit kill

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-21977`，6× RTX 4090D (24GB each)
- 代码根目录：`/root/contamcal-irt-calibration`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- HF cache：`/root/autodl-tmp/.hf_cache`
- Eval 结果：`/root/autodl-tmp/exp001/eval_results/`
- SFT checkpoints：`/root/autodl-tmp/exp001/checkpoints/`
- IRT 结果：`/root/autodl-tmp/exp006/`
- Extreme gamma sweep：`/root/contamcal-irt-calibration/exp004_sim_sweep/results_extreme_gamma/`（2/80 完成，~20h 剩余）
- 截至 handoff 时活跃进程：
  - GPU 0: SFT 训练（d025 v3 或 d005 v4，~14-15GB）
  - GPU 3: SFT 训练（~16GB, 89% util）
  - GPU 4: PID 530975，1.5B base pretrained eval（exp_008_base_pretrained_15B_eval，registry 仍 PREPARING 未更新 RUNNING）
  - GPU 5: 刚释放（1.5B d000 s123 eval 完成 10:41 UTC）
  - GPU 1: 空闲
  - GPU 2: 低占用（~3.6GB, 44%，可能是 Stan chains）

### 3. 📊 当前状态
刚完成一系列 eval 完成审查：
- **exp_001_eval_05B_d000_s123_aligned**: DONE, MMLU=42.2%, GSM8K=34.1%, ARC=49.7% ✅
- **exp_001_eval_15B_d000_s123_aligned**: DONE, MMLU=58.5%, GSM8K=65.4%, ARC=75.8% ✅
- **joint_fit.py 2PL bug 修复**: 4 处修改全部审查通过 ✅
- **2PL vs 4PL ablation**: 2PL 更 efficient（CI 窄 47%、MAE 低 4.3x），但 draws 数不同是混淆因素（已 warning）
- **GSM8K cross-seed variance**: 14.78pp 差距确认为 v1/v2 版本混淆，非纯 seed 方差 ✅

Registry 系统性问题未解：多个 worker 完成但不更新 RUNNING→DONE（exp_008_base_pretrained_15B_eval 仍 PREPARING）。

### 4. 📋 待办
- exp_008_base_pretrained_15B_eval（GPU 4, PID 530975）完成 → 验证 metrics，核查 registry 是否更新
- exp_001_eval_15B_d000_s123_aligned analysis worker 到来 → 审查 metrics 录入（已独立验证数据）
- GPU 0/3 SFT 训练完成 → 审查：确认超参合规（D020）、CUDA_VISIBLE_DEVICES 显式设置（C004）
- extreme gamma sweep 进展（2/80）→ 每隔一段时间抽查 results_extreme_gamma/ 新增文件数
- 新 IRT pooled fit 提交（加入 s123 数据后 N 扩展）→ 审查：D026 信号同源性、D045 排除规则、D018 3B GSM8K 排除
- 论文章节审查请求到来 → 按 Section 5 模板审，先查 red-section skill 合规

### 5. 🎯 战略上下文
- **核心结论链**: MVP simulation PASS (D003/D004) → empirical coverage collapse 确认 model misspecification → gamma 检测有效但 score correction 仅限 accuracy-sensitive benchmarks → 2PL 比 4PL 在小 N 下更 efficient
- **ARC gamma 负方向**: 4 条独立证据，已定性为 discriminative validity case study（不再尝试翻转）
- **当前瓶颈**: N_models 不足（当前 N=8 pooled），gamma CI 含零。seed=123 系列正在扩展 N→~30
- **最易判断错的事**: (1) 不要把不同训练版本（v1 aggressive vs v2 conservative params）的 3B 结果直接对比——path 命名混乱；(2) 不要因为 0.5B MMLU/ARC 数字变化就断言 contamination effect——那是 position bias；(3) registry 显示的状态经常滞后，永远 ssh 独立验证
- **GPU 空闲浪费**: 连续两个 worker 因结果已存在而跳过 GPU 1 提交，已提醒 Director 但 GPU 1 可能仍空闲——优先关注


---
