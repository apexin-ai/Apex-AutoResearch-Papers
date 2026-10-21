Atlas Analysis Scripts (准备完成)

文件:
- src/atlas_analysis.py: 5模块 (A:特征排序, B:单调性+JT test, C:EDD计算, D:跨模型一致性热图, E:PCA)
- src/atlas_plots.py: 学术级可视化 (PDF+PNG)
- scripts/run_atlas_analysis.sh: pipeline 脚本

Dry-run 结果 (MVP Pythia 20k samples):
- Top features: var_surprisal > mean_surprisal > p90_ppl > p75_ppl > hapax_ratio
- Monotonicity: 16/19 features |Mono|=1.0, 大部分递减, rep_*gram 递增
- EDD=3: 所有相邻深度对可区分 (0v1:0.9996, 1v2:0.9245, 2v3:0.8051)
- PCA: PC1=85.4%, PC2=14.2%, 合计99.6%
- JT test: 所有特征 p<0.001

多模型分析 (Analysis D) 去掉 --single 即可启用。