# Wang et al. 7B Model Search Results

## 结论
**没有** 7B 模型。Wang et al. (arXiv 2507.06457) 仅训练了 340M 和 1.3B 两个规模的模型，未训练或发布任何 7B 模型。

## HuggingFace 搜索结果
- **Collection 地址**: https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e
- **340M 模型**: ~31 个（6 种 linear attention × 5 种 hybrid ratio + baselines），训练 20B tokens
- **1.3B 模型**: ~31 个（同上配置），训练 100B tokens
- **7B 模型**: 无
- 搜索 "GatedDeltaNet 7B" 仅找到 allenai/Olmo-Hybrid-7B（Allen AI 的模型，非 Wang et al.）和 Idiap 的 1.4B 模型

## 论文中的相关描述
- 论文明确说实验仅限 340M 和 1.3B 两个规模
- Conclusion/Limitations 原文: "Our analysis is confined to models up to 1.3B parameters, a 2,048-token context window, and block-wise mixing ratios."
- 论文提到 10B+ 规模的验证是 open question: "Whether the observed trade-offs persist at the 10B+ scale, with 128k token contexts...remains open."
- 这意味着 Wang et al. 的结论在 7B 规模上尚未被验证，我们的 7B 实验可以填补这个 gap

## 服务器现有文件 (westb-48145)
- `/root/autodl-tmp/models_7b/` 目录存在，但仅包含 **Qwen2.5-7B-Instruct**（基座模型）
- 无任何 Wang et al. 的 hybrid linear attention 7B 模型
- 相关下载日志: `/root/autodl-tmp/download_7b.log`, `/root/autodl-tmp/download_7b_ms.log`

## 其他相关 7B hybrid 模型（非 Wang et al.）
- **allenai/Olmo-Hybrid-7B**: 75% 层使用 GatedDeltaNet heads，Allen AI 训练
- **Nvidia Nemotron-Flash-3B**: 包含 gated_deltanet.py，但仅 3B 规模
