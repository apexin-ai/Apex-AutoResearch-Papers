# Memory

## 关键决策与经验

[2026-05-15] 5-seed 主实验 (full dose) 最终结果: TaxEI=Random=58.3%=137/235 (均值完全一致), Vanilla=67.3±4.7%。taxonomy 标签零收益，这是论文的核心 negative result。

[2026-05-15] Forward pass v2 (trajectory-level): v1 的 monotonic dose-response gap 是 turn-level aggregation bug 的产物，已作废。v2 发现 Random 2.1× deeper memorization。

[2026-05-15] Extended statistics: bootstrap TaxEI-Vanilla significant (CI [+3.4,+15.8]), 但 frequentist marginal (p=0.073), power 仅 45.2%。需 n=9 seeds 达 80% power。

[2026-05-15] D033 Forward pass v2 (trajectory-level): v1 monotonic dose-response gap 作废，不能引用 v1 数据。

[2026-05-15] Eval 并行上限 2 个: 8B 模型 eval 需 ~18GB，4 并行必 OOM。同一时间 eval ≤ 2。**更新 [2026-05-16]**: RTX 5090 32GB 上实测每个 eval ~16.8GB，可在 4 张卡上各跑一个 eval（每卡独占）。但绝不能两个 eval 共享同一张 GPU。

[2026-05-15] 10% Dose-Response 5-seed 完整结果:
- TaxEI 10%: s42=61.7%, s0=70.2%, s123=55.3%, s1=51.1%, s7=68.1% → 均值 61.3±8.1%
- Random 10%: s42=68.1%, s0=66.0%, s123=55.3%, s1=68.1%, s7=61.7% → 均值 63.8±5.4%
- Vanilla baseline: 67.3±4.7%
- 所有 pairwise 不显著 (p>0.19)，TaxEI vs Random d=0.27，需 109 seeds 达 80% power

[2026-05-16] **25% Dose-Response 5-seed 完整结果 — 出现显著差异！**
- TaxEI 25%: s42=48.9%, s0=46.8%, s123=46.8%, s1=63.8%, s7=57.4% → 均值 52.7±7.6%
- Random 25%: s42=55.3%, s0=61.7%, s123=51.1%, s1=72.3%, s7=59.6% → 均值 60.0±8.0%
- **Vanilla vs TaxEI 25%: p=0.004, d=2.63 (极大效应量, power=0.989)**
- **Vanilla vs Random 25%: p=0.039, d=1.36 (power=0.629)**
- **TaxEI 25% vs Random 25%: p=0.029, d=-1.49**
- TaxEI dose-response 斜率 0.58 pp/% 是 Random 的 2 倍 (0.29)
- Page's trend: TaxEI p=0.004, Random p=0.044

[2026-05-16] **D036 Framing 决策：维持 negative result framing。** 25% TaxEI vs Random p=0.029 未过 Bonferroni 校正 (α=0.017 for 3 comparisons)，不能 claim 为显著。Dose-dependent taxonomy penalty 作为 secondary finding。

[2026-05-16] **50% Dose-Response 5-seed 完整结果（D037 校正 Vanilla 值）**:
- TaxEI 50%: s42=51.1%, s0=70.2%, s123=46.8%, s1=63.8%, s7=55.3% → 均值 57.4±9.5%
- Random 50%: s42=57.4%, s0=46.8%, s123=70.2%, s1=70.2%, s7=46.8% → 均值 58.3±11.7%
- Vanilla (D037 corrected): s42=61.7%, s0=68.1%, s123=66.0%, s1=66.0%, s7=74.5% → 均值 67.3±4.7%
- Vanilla vs TaxEI 50%: p=0.0864, d=1.31 — 未过 Bonferroni
- Vanilla vs Random 50%: p=0.2453, d=1.01 — 不显著
- TaxEI ≈ Random at 50%: p=0.9203 — 几乎无差异
- Bootstrap Vanilla vs TaxEI: p=0.0104, CI=[2.16, 17.48]
- Random dose-response 单调递减显著 (Spearman rho=-0.9, p=0.037)
- s0/s123 值完全对调 (permutation p=0.13，不算罕见)

[2026-05-16] **D040: WebShop 降级为 Discussion section。** P1 (step_order_swap) 无法适配 WebShop（action space 高度线性），taxonomy 从 4 缩到 3，跨环境对比不对等。论文 Discussion 增加 ALFWorld vs WebShop 结构性差异分析。Claim 8 从实验 claim 改为 Discussion 观察。

[2026-05-16] **Failure Analysis 5-seed 平衡数据**: TaxEI loop_repetition 34.8% (Vanilla 15.6%, Random 12.8%)。TaxEI 是 Vanilla 的 2.2×、Random 的 2.7×。Loop 占 TaxEI 全部失败的 79%。数据来自 recovery eval trajectories（clean eval 不存 trajectory）。

[2026-05-16] Recovery-paired datagen 完成: 711/760 variants 成功，输出 data/recovery_paired/recovery_paired.jsonl (20.8MB)。Operator 分布: C1=182, C4=175, P1=170, P2=184。

[2026-05-16] **Recovery-paired SFT 数据设计**: recovery_paired.jsonl 是嵌套结构 (error_prefix + recovery_continuation)，需转换为扁平 messages 格式。用 recovery_only 模式提取 5,408 条 recovery continuation steps。TaxEI-RP = TaxEI 9,029 + recovery 5,408 = **14,437 samples**。Dry-run 成功 (5 steps, loss 4.019→2.424)，峰值显存 35.5 GiB。

[2026-05-16] **TaxEI-RP Recovery Eval 5-seed 定论（D043 + s7 补全）**:
- s42: 38.3% (18/47) | C1=50%, C4=27.3%, P1=50%, P2=25%
- s0: 46.8% (22/47)
- s1: 48.9% (23/47) | C1=41.7%, C4=36.4%, P1=75%, P2=41.7%
- s123: 57.4% (27/47) | C1=58.3%, C4=45.5%, P1=66.7%, P2=58.3%
- s7: 59.6% (28/47)
- **Mean: 50.2±8.6%** — 低于 TaxEI baseline (58.3%) 和 Vanilla (67.3%)
- Detection rate 全 0%
- **结论: Recovery-paired training 适得其反，模型学到了错误模式而非恢复能力 (Claim 7 定论)**

[2026-05-16] **Qwen Recovery Eval 完成 15/15 ✓**:
- Vanilla: 61.7/68.1/66.0/66.0/74.5 → Mean 67.3±4.7% (5/5 ✅)
- TaxEI: 59.6/46.8/61.7/61.7/57.4 → Mean 57.4±6.4% (5/5 ✅)
- Random: 63.8/55.3/66.0/51.1/53.2 → Mean 57.9±6.0% (5/5 ✅)
- **Recovery eval 再次确认 TaxEI ≈ Random（57.4% vs 57.9%，差 0.5pp）**
- Recovery rate ≈ clean eval success rate（D041 结论：模型靠"resilience"通过 injected scenarios，不是靠检测和恢复）

[2026-05-16] **LLaMA-3.1-8B 跨模型验证 3-seed 完整结果（D045/D047）**:
- **Clean SR**:
  - Vanilla (4,358): s42=72.3%, s0=72.3%, s123=72.3% → Mean 72.3±0.0%
  - TaxEI (9,029): s42=76.6%, s0=76.6%, s123=61.7% → Mean 71.6±8.6%
  - Random (9,029): s42=76.6%, s0=74.5%, s123=76.6% → Mean 75.9±1.2%
- **Recovery Rate (injected, eval seed=42 统一)**:
  - Vanilla: s42=74.5%, s0=74.5%, s123=68.1% → Mean 72.4±3.7%
  - TaxEI: s42=74.5%, s0=74.5%, s123=61.7% → Mean 70.2±7.4%
  - Random: s42=76.6%, s0=74.5%, s123=76.6% → Mean 75.9±1.2%
- **Eval seed confound 已排除**: s123 原用 eval seed=123 (RR: V=70.2%, T=59.6%, R=78.7%)，统一 eval seed=42 后 (RR: V=68.1%, T=61.7%, R=76.6%)，TaxEI 仍为唯一异常。差距从 19.1pp 缩至 14.9pp 但仍显著。
- **跨模型统计检验**: Levene TaxEI vs Random p=0.027（方差显著不同）; Bootstrap 均值差 CI [-0.142, 0.014] 跨零; Fisher 检测率 p=0.047 OR=2.6
- **⚠️ 训练数据量混淆（critical confound）**: Vanilla=4,358 samples, TaxEI/Random=9,029。
- **⚠️ detection_rate 指标为假阳性**：LLaMA 的 21-36% detection 全部由导航短语 "go back to X" 中的 "back" 触发关键词匹配，非真实错误检测。不可引用此指标。

[2026-05-16] **Eval 脚本架构（P0 关键发现）**:
- `eval/injected_eval.py`: **永远注入错误**，没有 `--no_inject` 参数。输出 `recovery_rate` + `detection_rate` + `by_operator` 分解。`--model_variant` 仅作标签。
- `eval/recovery.py`: 有 `--inject` / `--no_inject` 开关，默认 `inject=False`（即 clean eval）。输出 `success_rate` + `by_task_type` 分解。
- **之前所有用 `injected_eval.py` 的 LLaMA 结果均为 injected recovery rate，不是 clean success rate。**
- Clean eval 命令: `python3 eval/recovery.py --model_path <ckpt> --base_model <base> --num_episodes 47 --task_list eval/eval_tasks_47.json --output eval_results/<name>_clean.json`（不加 `--inject`）

[2026-05-16] 50% 训练 OOM 教训: batch_size=8 + max_length=4096 对 50% 数据集 OOM。修复: bs=4, gradient_accumulation_steps=2。swift sft --model 必须用本地完整路径。

[2026-05-15] submit_training_job 必须用 bash -c "..." 包裹含 source/conda 的命令。

[2026-05-15] Registry 状态机不能跳步。转 RUNNING 必须带 spec。

[2026-05-15] [失败模式] autodl-5090 项目路径为 /root/autodl-tmp/tax_error_inject_agent。

[2026-05-16] **Worker 假完成反复发生**: Worker 启动后台进程后报 done，导致无人收集结果。vanilla-s123 injected eval 经历 5 次假完成才成功。关键教训：(1) Worker 必须轮询到进程结束并验证文件存在 (2) 不要信任 Worker 回调中的"已启动"报告 (3) 每个 eval 独占一张 GPU，禁止共享。

[2026-05-16] **Cron EXIT_CODE=129 是 tmux SIGHUP 误报**: submit_training_job 的 tmux wrapper 在训练正常退出后收到 SIGHUP（tmux session 清理），导致退出码被覆盖为 129。训练本身退出码为 0。应检查 checkpoint 完整性而非依赖退出码。
