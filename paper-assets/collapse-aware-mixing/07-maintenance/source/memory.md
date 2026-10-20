# Memory — collapse-aware-mixing

## 核心假设挑战

### Pivot B 验证结果：generated eff_rank 不比 n-gram 更早 (2026-05-13)
Generated eff_rank 在 G0→G2 暴跌（63.89→3.87→1.06），holdout eff_rank 完全稳定（~111.5）。信号存在但**不比 n-gram entropy 更早**：n-gram 在 G1 step 152 检测，generated eff_rank 在 G1 final 才检测。compare verdict = PIVOT_B_LOSES。**核心洞察从"更好的指标"转向"正确的观测面"**：问题不是用什么指标，而是在哪里测（generation space vs holdout space）。所有 holdout-side 指标（eff_rank、PPL、token entropy）对 collapse 失灵，所有 generation-side 指标（n-gram entropy、coverage、generated eff_rank）都能检测。

### P0 脚本 pivot 依赖 (2026-05-13)
Pivot 确认前，只有不依赖 eff_rank 度量方式的 baseline 脚本（w=0/0.1/0.3/0.5/0.7/1.0）可以启动。PI 相关脚本（pi_sweep_p0, seed_validation）必须等 narrative 方向确认后更新 controlled_pipeline.py 的控制信号（可能改为 generation-side n-gram entropy），再启动。

### 所有 holdout 指标均对 collapse 失灵 (2026-05-13)
v7 G1 dry-run 确认：不仅 eff_rank（+0.2%），PPL（+1.1%）、token_entropy_mean、spectral_entropy **全部未检测到 collapse**。而 4 个 generation-side 指标（unigram/bigram/trigram entropy, vocab coverage）在 G1 step 152 同时触发（unigram -43.5%）。**问题不是"eff_rank vs PPL"，而是"generation-side vs ALL holdout-side metrics"。**

## 竞争格局

### SIGMA 已占据"谱分析检测 collapse"位置 (2026-05-12)
SIGMA (2026-01) 已将 Gram 矩阵谱分析用于 LLM model collapse 检测。**不能 claim "首次将谱分析用于 collapse 检测"。** 但 SIGMA 无控制机制、未验证 leading indicator。我们的 novelty = SIGMA 谱监控 + ERBP 理论动机 + EntroPIC PI 控制范式，首次组合成：谱有效秩 → PI 控制器 → 动态 real/synthetic 比例调节。推荐 framing：从 "spectral metrics detect collapse" → **"from passive monitoring to active closed-loop control"**。

### 文献扫描 novelty 确认 (2026-05-14)
**Negative result 有 novelty**：无人报告过 holdout spectral eff_rank 在 model collapse 期间上升。Schaeffer 2025 (arxiv:2503.03150) position paper 指出 collapse 定义混乱，间接支持单一 spectral metric 可能失效。Homogeneity Trap (Liu 2026, arxiv:2601.02080) 提供 spectral metrics 可反直觉行为的另一证据。

**Plan A novelty 完好**："collapse detection + control theory + real/synthetic data mixing" 三者交叉区域空白。最近竞争者 TiKMiX/AC-ODM/DoGraph 全部是 domain-level/loss-driven dynamic mixing，无人做 collapse-aware mixing。

**时间窗口警告**：dynamic data mixing 领域 2025H2-2026H1 论文密集，从 "dynamic mixing" 到 "collapse-aware mixing" 跨步不大。**建议 3 个月内产出核心结果。**

**控制信号建议**：若 Plan A 继续，控制信号应从 eff_rank 切换到 n-gram entropy / unique token ratio / vocab coverage decay（text-level metrics 更直接反映 tail distribution 消失）。

详见 artifact: literature_scan_20260514.md（含 9 篇新论文及 novelty 评估）。

## 经验教训

### compare_eff_rank_vs_ngram.py 阈值不对称 (2026-05-13)
脚本中 generated_eff_rank 检测阈值 rel=0.5%（abs=3.0），n-gram 指标阈值 rel=10%（abs=0.5），相差 20 倍。verdict 不可直接引用——需要用统一阈值（如 rel=5% 或 2σ noise floor）重新判定。否则审稿人会攻击"leading indicator 只是更低的 detection threshold"。

### v7 G1 synth gen 只产出 13.8M/20M tokens (2026-05-13)
collapsed 模型生成更短序列（early EOS），G1 synth gen 实际产出 13.8M tokens（目标 20M, 差 31%）。G2 训练数据量因此比预期少。**不影响 collapse 检测有效性判断**，但论文中报告 tokens_per_generation 时需注明实际产出 vs 目标。另外 padding_side=right 的 confound 可能人为加速 collapse（quantitative magnitudes may be inflated），但 holdout failure 结论不受影响。

### 合成数据生成是迭代训练实验的主要瓶颈 (2026-05-13)
Pythia-1b 在单 RTX PRO 6000 上生成速度 ~76s/batch，瓶颈在单 batch 生成速度而非 token 总量。90M tokens 需 ~28h/代，20M tokens 仍需 ~6h/代。3 代迭代实验：v5(90M)=58h, v7(20M)=30h+。**Post-MVP 必须优化 synth gen**：增大 generation batch size / fp16 generation / 多 GPU 并行。timeout 要覆盖完整 pipeline 时间（至少 48h for 20M×3 代）。

### Decoder-only 模型生成必须用 left-padding (2026-05-13)
v5 每个 batch 报 "right-padding was detected" 警告。对 decoder-only 模型做 `model.generate()` 时必须设置 `tokenizer.padding_side = 'left'`，否则 padding tokens 在序列右侧会影响 autoregressive 生成质量。合成数据质量直接影响下游 collapse 检测的可靠性。

### padding_side 修复残留：eval 阶段未覆盖 (2026-05-13)
D007 修复了 generate.py 中合成数据生成的 padding_side='left'，但 pilot_pipeline.py 评估阶段（metric 计算中的 token 生成）仍加载默认 padding_side='right' 的 tokenizer。**v7 中 68 次 right-padding 警告仍出现。** 影响范围：n-gram entropy、coverage 指标可能有偏（基于生成 tokens 计算）；eff_rank 和 ppl 基于 holdout 数据计算，**不受影响**。v7 不中断，**v7 结束后必须修复 pilot_pipeline.py 评估代码路径的 padding_side**。

### 实验运行期间禁止修改依赖代码 (2026-05-12)
Reviewer 指出：v5 pipeline 运行期间 Worker 修改了 metrics.py 和 pilot_pipeline.py。虽然当前 run 不受影响（进程已加载旧模块），但**今后实验进程运行期间不修改服务器上该实验依赖的代码文件**。新功能等 run 完成后再部署。

### Pythia-1b + wikitext-103 + lr=1e-5 导致发散 (2026-05-12)
mvp_pilot_v4 在 G0 训练 760 步后 loss 维持 106-116（正常应为 2-4），PPL 溢出到 inf。独立诊断确认 ratio=1.00（非 transformers 报告 artifact，是真实发散）。grad_norm 43-113 无 NaN/Inf，训练速度稳定 2.08s/step，说明梯度计算正常但 loss landscape 不对。**lr=1e-5 对 Pythia-1b fine-tune wikitext-103 可能过大，下次考虑 2e-6 或更低。**

### tmux + conda 环境激活 (2026-05-12)
submit_training_job 通过 tmux 执行命令，tmux 默认用 sh 而非 bash。bash -c 命令**必须**包含 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，否则 python3 找不到。mvp_pilot 因此崩溃。

### AutoDL network_turbo 必须在 tmux 命令中显式激活 (2026-05-12)
submit_training_job 的命令在 tmux 新 session 中执行，不继承 Worker SSH session 的环境变量。因此 `source /etc/network_turbo` 必须写在 bash -c 命令里，否则 HuggingFace 不可达（`Errno 101: Network is unreachable`）。同时需设置：
- `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`
- `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`
- `HF_HUB_DISABLE_XET=1`
- `HF_HOME=/root/autodl-tmp/.hf_cache`

mvp_pilot_v2 因此崩溃（tokenizer vocab_file 未缓存 → AttributeError）。

### HF 数据集下载锁阻塞 (2026-05-12)
dry-run/测试后必须清理遗留 Python 进程，否则 HF dataset builder lock 会阻塞后续正式实验。PID 2371（测试用 `load_dataset('openwebtext')`）持锁 3.5+ 小时阻塞 mvp_pilot_v3。修复方法：`kill <PID>` + 清理 `.lock` 和 `.incomplete` 文件。**提交正式实验前先 `ps aux | grep python` 检查遗留进程。**

### flash_attention_2 → sdpa 回退 (2026-05-12)
cqa1-38874 上 flash-attn 编译失败（A6000 架构），train.py 已改用 sdpa（`attn_implementation="sdpa"`）。

### AutoDL 磁盘限制 (2026-05-12)
根分区 ~30GB，模型/数据/输出必须写 `/root/autodl-tmp/`。HF_HOME 也应指向数据盘。

### pkill -f 自杀问题 (2026-05-12)
在 `bash -c "...pkill -f pilot_pipeline..."` 中执行 `pkill -f pilot_pipeline` 会匹配 bash 进程本身导致自杀（EXIT_CODE=129=128+SIGHUP）。解决方案：不在 submit_training_job 命令中包含 pkill，改用 kill_job 单独杀进程。

### env_init.sh 简化启动 (2026-05-12)
将所有环境变量设置集中到 `/root/collapse-aware-mixing/env_init.sh`，launch script 只需 `source env_init.sh` 即可。减少命令长度和出错机会。

### v5 tokens_per_generation 90M vs ROADMAP 100M (2026-05-12)
launch_pilot_v5.sh 传了 `--tokens-per-generation 90000000`，而 ROADMAP 写 100M。PilotConfig 默认值是 100M 但 parse_args 默认 90M。每代少 10M tokens、少 1 个 checkpoint（9+1 而非 10+1）。**不影响 MVP GO/NO-GO 判定**（Director 确认），但后续正式实验需统一为 100M。

### r_target bug 根因：experiment_plan.yaml 传播 (2026-05-13)
r_target=50.0 反复出现在 3 个文件中（main_experiment.py、run_seed_validation.sh、controller.py default）。Reviewer 全局扫描发现**根源是 experiment_plan.yaml 的 controller_defaults.r_target: 50.0**——Agent 写新代码时从此处复用。Pythia-1B 实际 eff_rank ≈ 677，50.0 差一个数量级。已修复：experiment_plan.yaml r_target 改为 0（auto-infer），sweep 范围改为相对百分比。**教训：规划文件中的默认值会被 Agent 当作 ground truth 复用，必须与代码语义一致。**

### SVD vs Gram Matrix 命名不一致 (2026-05-13)
代码用 SVD(E) 的奇异值 σ_i 计算 eff_rank（L1-normalize σ_i → entropy → exp），但 paper_framing.md 写"spectral effective rank of the embedding Gram matrix"（应为 Gram 特征值 λ_i = σ_i²）。L1-normalize(σ_i) ≠ L1-normalize(σ_i²)，两种定义的 eff_rank 不同。**论文描述需与代码一致**——建议改论文为"singular value effective rank"或改代码用 σ²。只要 pipeline 内一致即可，不影响实验有效性。

## 代码决策

### PI Controller 设计 (2026-05-12)
- 公式: `w_t = w_{t-1} - Kp*(r_t - r_{t-1}) - Ki*(r_t - r_target)`
- rank 下降 → w 增大（更多真实数据）；rank 恢复 → w 减小
- clamp 到 [w_min, w_max]，默认 [0.1, 0.9]
- 默认参数: Kp=0.01, Ki=0.005, r_target=50.0, w_init=0.5

### AutoDL submit 命令模板 (2026-05-12)
```
bash -c "source /etc/network_turbo 2>/dev/null; export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt; export HF_HUB_DISABLE_XET=1; export HF_HOME=/root/autodl-tmp/.hf_cache; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/collapse-aware-mixing && python3 <script> <args> 2>&1 | tee /tmp/<log>.log"
```

### logit KL divergence 待部署 (2026-05-12)
审计 Worker 已在服务器上补充了 `compute_logit_kl_divergence()`（metrics.py）和 pilot_pipeline.py 的 prev_model_dir 参数。但因 v5 运行中被修改，属违规操作。代码已在服务器上，v5 完成后的下一轮 run 自动生效。

### analyze_g0.py holdout 修复 (2026-05-12)
默认 `--holdout-path` 从硬编码本地路径改为 `None`，`holdout_path is None` 时自动用 `load_dataset("wikitext", "wikitext-103-raw-v1", split="test")` 从 HF Hub 加载。传路径时仍走原逻辑，向后兼容。

### analyze_g0.py 运行命令 (2026-05-12)
兼容性已验证通过。v5 完成后运行：
```
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python /root/collapse-aware-mixing/analyze_g0.py \
    --checkpoint-dir /root/autodl-tmp/output/G0/training \
    --output-dir /root/autodl-tmp/output/g0_analysis \
    --model-name EleutherAI/pythia-1b
```

## 服务器环境

### cqa1-38874
- 1× RTX PRO 6000 96GB
- Python 3.12, PyTorch 2.10.0, transformers 4.57.6
- conda base 环境: `/root/miniconda3/`
- 项目代码: `/root/collapse-aware-mixing/`
- 输出目录: `/root/autodl-tmp/output/`（v5）, `/root/autodl-tmp/output_v7/`（v7）, `/root/autodl-tmp/output_seed0/`（seed0 r2）
