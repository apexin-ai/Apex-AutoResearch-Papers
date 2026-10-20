## 缓解方法诊断分析结果（125M seed=42）

### 分析 1: 近重复度（Contriever embeddings）
Gen 1→7 近重复率：ε=0.95 下 1.4%→2.3%，ε=0.85 下 3.0%→5.5%
结论：ADR/SemDeDup 去重空间极小

### 分析 2: Gen-0 PPL 分布
Gen 4/7 mean=1.4, P99=2.1，分布极度压缩
结论：RPF 过滤信号极弱

### 分析 3: RGDS 选中 vs 拒绝
Gen 4: selected mean PPL=1.30 vs rejected=1.50, d=-1.11
Gen 7: selected mean PPL=1.20 vs rejected=1.30, d=-0.94
结论：RGDS 系统性选择低 PPL（更模板化）样本，加速 collapse