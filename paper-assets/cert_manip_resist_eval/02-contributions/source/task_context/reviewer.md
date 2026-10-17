---
loop: 3
reason: max_wall_time
updated: '2026-05-25T06:02:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- FP16 baseline 只能用 `CUDA_VISIBLE_DEVICES=0`（项目 gpu_ids 白名单）
- Monte Carlo PID 18494 纯 CPU，不占 GPU，不要误 kill
- 论文 fractional logit 数字已审计修正：V2 实际为 9/12→9/12→9/12（flat），论文原写 9→11→12 需修正，**不要用旧数字**
- Adaptive R²（论文 0.275 / registry 0.256）无审计链，结果文件不存在，引用前必须重跑

### 2. 🖥️ 基础设施快照
- 服务器：`seetacloud-rtx6000`，GPU: 1× NVIDIA RTX PRO 6000 Blackwell (98GB)
- 代码根目录：`/root/cert_manip_resist_eval`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- HF cache：`/root/autodl-tmp/.hf_cache`，ModelScope cache：`/root/autodl-tmp/modelscope_cache`
- 结果目录：`/root/cert_manip_resist_eval/artifacts/results/plan001/`
- 活跃进程：
  - PID 18494 — Monte Carlo size calibration，CPU 多核满载 8h+，无输出（正常，结束时写 `monte_carlo_size_calibration.json`）
  - PID 50564 — FP16 baseline V3（bugfix 后），tmux `r1w2-fp16-baseline`，正在下载 Qwen 14B FP16 权重（HF 速度慢 ~1MB/s），日志 `/tmp/fp16_baseline_v3.log`

### 3. 📊 当前状态
刚完成一批 R5 response 实验的审查：
- **Quant dummy regression** → K_eff survives（6/6/4），但 predictor shift 不 survive（6→6→4 非递增）。VIF 极高（K=7 达 1086）。已报 WARNING。
- **β_std trajectory** → K_eff β_std 0.35→0.44→0.40 稳定，η_max 0.27→0.08 下降。来源是 DBEI 数据（B=999 Webb），sig counts 与主分析不同，已提醒不要混用。
- **Bayesian posterior entropy** → concentration ratio 仅降 2.3pp（0.890→0.867），不足以解释 0/12 neutralization。Worker JSON 过度解读为 "diversity collapse"，已打回。
- **API-only power** → β_std ratio ~1.6×（效应更强），非显著纯属 power 不足。K=7 仅 36 panels，power=0。
- **Fractional logit V2 audit** → **CRITICAL**：K=5 实际 9/12（非论文 11/12），K=7 实际 9/12（非论文 12/12）。论文 §4.2、Intro contribution 1 需修正。
- **FP16 baseline V3** → bug 已修（`gold = chr(65 + s["answer"])`），AWQ Qwen14B MMLU=0.710 ARC=0.840。FP16 下载中。
- **PaperBanana Fig 1** → 两次失败（CLI 兼容性 + 文件未落盘），纯工具问题。
- **Abstract/Intro rewrite** → PASS with warnings（fractional logit 数字 + adaptive R²）

Registry: `r1w2-fp16-baseline` RUNNING，其余全 DONE。

### 4. 📋 待办
- Monte Carlo PID 18494 产出 `monte_carlo_size_calibration.json` → 审查 rejection rate 是否 ~5%（nominal size），over-reject 条件数
- FP16 baseline V3 完成 → 核实 AWQ vs FP16 delta（期望 <2pp），检查所有模型是否评测成功
- Director 处理 fractional logit CRITICAL 后 → 验证论文修正（§4.2 L125, Intro contribution 1, Limitations）是否改为 9/9/9
- Quant dummy regression 写入论文 → 审查是否同时报告 "K_eff survives" 和 "predictor shift attenuates"（不能只报好消息）
- Adaptive R² 重跑后 → 核实结果文件并更新论文数字

### 5. 🎯 战略上下文
- 项目核心：K_eff（MI-based diversity metric）与 panel manipulation resistance 的 descriptive association。Predictor shift（K=3 co-determination → K≥5 K_eff dominance）是论文主叙事。
- **最易判断错的事**：多种推断方法（OLS/WCB/crossed RE/fractional logit/DBEI）给出不同 significance counts，不要混用。主分析用 WCB B=9999 Rademacher（K=3: 4/12, K=5: 7/12, K=7: 8/12）。DBEI 用 B=999 Webb（counts 不同）。Fractional logit V2 是 9/9/9（flat）。
- **Quant dummy 是双刃剑**：K_eff survives 是好消息（不纯是量化代理），但 predictor shift 不 survive（6→6→4）。如果论文只报前者不报后者，审稿人会攻击 cherry-picking。
- **Bayesian 0/12 机制未解**：concentration 假说效果量太小（2.3pp），需要承认 "mechanism unclear"。Worker V2 新增了 K_eff variance compression 解释（CV 0.157→0.131），但未独立验证。
- **Copula GoF appendix L396 仍有数据混合问题**（jittered MMLU 102/105 + non-jittered ARC 105/105），之前报过 WARNING，可能未修。
