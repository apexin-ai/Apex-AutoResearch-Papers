# DivEye Citation Audit: "Basani & Chen, ICLR 2026"

## 引用原文

`src/baselines.py` 第 4 行 docstring：

```
DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, ICLR 2026)
```

代码中 DivEye 用于 recursive generation depth estimation 的 baseline，提取 surprisal 多样性特征 + XGBoost 分类。

## 验证结果

**结论：NOT fake — 但 venue 标注有误。**

| 项目 | 引用中 | 实际 |
|------|--------|------|
| 作者 | Basani & Chen | ✅ Advik Raj Basani (BITS Goa) & Pin-Yu Chen (IBM Research) |
| 方法 | DivEye | ✅ 真实存在，GitHub: [IBM/diveye](https://github.com/IBM/diveye) |
| 论文 | — | "Diversity Boosts AI-Generated Text Detection" (arXiv: 2509.18880) |
| Venue | ICLR 2026 | ❌ **实际发表于 TMLR '26**（Transactions on Machine Learning Research） |
| Workshop | — | 另有 ICML DIG-BUG '25 workshop 版本 |

### 判断依据

1. GitHub 官方仓库 `IBM/diveye` 标注 `[TMLR '26]`
2. OpenReview 有两个 submission ID：`DNgsOhGZBI`（TMLR）和 `QuDDXJ47nq`（疑似 ICLR 投稿）
3. 可能曾投稿 ICLR 2026 但最终发表于 TMLR

### DivEye 与本项目的关系

DivEye 原始任务是 AI-generated text detection（二分类：人写 vs 机器写）。本项目是 recursive generation depth estimation（多分类：生成深度 0/1/2/3）。两者共享 surprisal diversity 特征空间，DivEye 作为 baseline 合理。

## 修正建议

将 `src/baselines.py` 中引用修正为：

```
DivEyeBaseline — Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)
```

完整引用：
> Advik Raj Basani and Pin-Yu Chen. "Diversity Boosts AI-Generated Text Detection." *Transactions on Machine Learning Research (TMLR)*, 2026. arXiv: 2509.18880.

## 参考链接

- arXiv: https://arxiv.org/abs/2509.18880
- GitHub: https://github.com/IBM/diveye
- OpenReview (TMLR): https://openreview.net/forum?id=DNgsOhGZBI
- HuggingFace Demo: https://huggingface.co/spaces/pinyuchen/Diveye_AI_text_detector
