# Memory — spectral_collapse_ews

## 跨架构验证完成总结 (2026-05-25)

### GPT-2-medium 跨架构核心发现
- **初始谱极度集中**: GPT-2-medium eff_rank=23 vs Pythia=417（差 18 倍），导致 collapse 幅度远大于 Pythia（SLV -55.1% vs -11.6%），decompression transient 也更剧烈（SLV +34.1% vs +4.3%）
- **r_crit ∈ (0.25, 0.3] 架构无关**: GPT-2-medium 与 Pythia 在相同 r 值下产生相同 trajectory type
- **3-gen pilot 局限**: raw SLV 在 r=0.25 和 r=0.3 都有 Gen 2 transient dip（-1.85% vs -1.18%），EMA-smoothed 均单调递增。3 代不足以区分 Type II/III，论文用保守措辞 "consistent with Pythia phase boundary"
- **论文 §4.6 + Table 5 已集成全部 4 条件**: r=0 (Type I, 9-gen), r=0.25 (---, 3-gen), r=0.3 (III, 3-gen), r=1.0 (Ctrl, 3-gen)

### 审稿状态 (Round 2)
- 25/27 issues resolved
- R1-N2 (r=0.5 缺 seed): best-effort per D036, 2-seed 已在论文
- R1-W1 (r_crit coarseness): rebuttal 处理, continuous crossover 论证
- R2-C2 (跨架构): ✅ 已解决, §4.6 + Table 5

## GPT-2-medium 跨架构写作措辞 (2026-05-24)

**Director 决策**：3-gen pilot 无法区分 Type II 和 Type III。论文中对 GPT-2-medium r=0.25 使用保守措辞："consistent with the Pythia phase boundary; the 3-generation window does not resolve the Type II/III distinction at r=0.25"。原因：EMA-smoothed SLV 在 3 代内对 r=0.25 和 r=0.3 均单调递增，raw SLV dip 不足以在短窗口内做出 Type II 判定。

## 竞品实验参考
（见 literature_map.yaml）

## 决策记录

### 3-seed 均值方案 (2026-05-21)
Director 确认所有 Table 使用 seed 42+43+44 三种子均值。Table 1 (r=0) 全列已更新。Table 3 r=0 行同步。HeSw 数据由 Reviewer 独立审计验证。

### Table 3 r=0.50 数据源统一 (2026-05-21)
r=0.50 行全部统一为 fixed_mix_seed42 (exp_004) 数据源，不再混用 adaptive_k10_seed42。

### Phase III 衰退率 (2026-05-21)
3-seed 重新计算: 1.78±0.22 %/gen (原 2-seed: 1.67±0.18)。

### HellaSwag 文件命名问题 (2026-05-21)
lm_eval 新版本输出 `results_TIMESTAMP.json` 而非 `results.json`。Worker 收集脚本需用 glob 匹配。

### 磁盘管理教训 (2026-05-21)
rtx6000-diagprobe 数据盘 (/root/autodl-tmp) 可用空间需要监控。exp_014 因磁盘满在 Gen 6 崩溃。清理 7 个旧 checkpoint 目录释放 ~102GB 后恢复。提交实验前必须检查磁盘。

### D-4 高方差 (2026-05-21)
r=0 Gen 10 D-4 三种子: seed42=0.4259, seed43=0.394, seed44=0.1515。s.d.=0.15，CV 远高于 SLV (CV~1.3%)。这是论文 §4.5 的讨论点。

### Seed 42 原始数据参考值 (2026-05-21)
从 pipeline results 文件提取的 seed42 per-gen 数据：
- Gen 0: eff_rank=417.55, SLV=2366.68, PPL=9.55, HeSw=.413, D-4=.7414
- Gen 2: eff_rank=496.44, SLV=2469.93, PPL=13.58, HeSw=.376, D-4=.4103
- Gen 5: eff_rank=479.21, SLV=2370.17, PPL=24.59, HeSw=.344, D-4=.3377
- Gen 7: eff_rank=464.20, SLV=2304.19, PPL=38.89, HeSw=.319, D-4=.3481
- Gen 10: eff_rank=442.46, SLV=2178.95, PPL=76.78, HeSw=.301, D-4=.4259

## ε-clipping 验证 (2026-05-24)
完整验证结果在 `artifacts/epsilon_clipping_verification.json`。结论：ε-clipping 从未生效。Worst case (GPT-2-medium Gen 10, r=0, eff_rank=97.02): min(σ)=1.60×10⁻², 比 ε=10⁻¹⁰ 大 8 个数量级。W2 彻底消解。

## 环境信息

### rtx6000-diagprobe
- conda 环境: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 项目路径: `/root/spectral_collapse_ews`
- checkpoint 盘: `/root/autodl-tmp/spectral_collapse_ews/`
- GPU: 2x RTX PRO 6000 Blackwell Server Edition (98GB each)

### 模型版本
- Pythia-410M: EleutherAI/pythia-410m-deduped (已缓存在服务器)
- Pythia-1B: EleutherAI/pythia-1b-deduped (已缓存)
- GPT-2-medium: gpt2-medium (355M, 已缓存)
- lm_eval: 需要注意 results 文件命名格式变化
