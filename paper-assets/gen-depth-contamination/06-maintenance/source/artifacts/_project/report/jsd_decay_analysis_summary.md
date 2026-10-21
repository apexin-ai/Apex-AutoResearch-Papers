JSD Decay Analysis: 11 model x domain + 1 retrain-chain

产出文件（cqa1-22115）:
- artifacts/jsd_decay_curves.pdf / .png — cross-model x cross-domain JSD decay 图
- artifacts/jsd_decay_analysis.json — 完整定量分析
- artifacts/scripts/jsd_decay_analysis.py — 可复现脚本

核心发现:

1. 两种截然不同的衰减模式:
| 模式 | Cliff ratio (0v1/1v2) | lambda (decay rate) | 代表实验 |
|------|----------------------|---------------------|---------|
| Sharp cliff | 10-50x | 2.9-6.3 | C4 全部, Wiki 全部, OLMo arXiv |
| Gradual decay | 1.6-3.0x | 0.7-1.2 | Llama/Qwen/Pythia on arXiv |

2. OLMo 是极端 outlier:
- arXiv cliff 47x, Wiki cliff 50x — 几乎所有信息在第一步就坍塌
- 1→2 之后 JSD 立即平坦化 (~0.003-0.007)

3. arXiv domain 的独特性（排除 OLMo outlier）:
- Cliff ratio 仅 1.6-3.0x（C4 为 6-15x），信息丢失更渐进
- 收敛 floor 更高 (~0.007-0.009 vs C4 的 ~0.003-0.004)
- 与 arXiv K*=3 一致——结构化文本的代际退化更慢

4. Retrain-chain 根本性不同:
- Cliff ratio 仅 1.31x, lambda=0.285
- JSD 从 0.17 缓慢降到 0.064，没有 cliff

5. 衰减速度并非 universal:
- C4: lambda ≈ 2.9 (consistent across 4 models)
- Wikipedia: lambda ≈ 4.2
- arXiv (non-OLMo): lambda ≈ 1.0 (3x slower than C4)