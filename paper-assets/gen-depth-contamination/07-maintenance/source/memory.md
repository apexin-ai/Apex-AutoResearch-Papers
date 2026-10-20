# Memory — gen-depth-contamination

## 审计结果 (2026-05-25)

全文数字审计完成：~549 个数字，29 个问题（6 高、8 中、15 低）。核心表格（tab_filtering_main、tab_alpha_sweep、tab_crossscorer、tab_pairwise_significance）零误差。问题集中在 figure 脚本硬编码值（scorer 不一致）和少数 text 段落。已汇报 Director，等待修复策略确认。

### 关键问题速查
- Fig 2/3a Pythia: self-scored 0.6539 应改为 Qwen cross-scored 0.6074
- Fig 3b caption: 完全不匹配图内容
- experiments_c1.tex:56 "> 0.99 at ≤1.5B": 不准确
- discussion.tex:27 JSD 0.077: 归属 arXiv 但实为 LLaMA-8B C4
- OBD 38.6% vs per-depth 38.0%: 不一致
- method.tex:72 MAE 0.984: registry 找不到

## 模型版本验证记录

- Qwen2.5-1.5B-Instruct: 用作 cross-scorer（2026-05 验证）
- GPT-5.5 / Claude: exp_011 LLM depth estimation baseline

## 实验设计约束

- batch_size=32 因 RTX PRO 6000 Blackwell 98GB 足够，但 self-BLEU 计算是 CPU bottleneck（占 OBD 53% 时间）
- AutoDL 上 FineWeb/C4 streaming 均不可用（proxy 超时），只能用已有本地数据
- exp_014 v1 数据（5K CC docs）可用于独立指标分析

## 决策记录

- D112: exp_014 独立指标结果定位为 rebuttal 补充证据，采用 "weak but directional" framing
- runtime_benchmark conclusion=negative: OBD 44.3ms/doc（最慢），rebuttal framing "trades 2-3× latency for unique depth discrimination"
