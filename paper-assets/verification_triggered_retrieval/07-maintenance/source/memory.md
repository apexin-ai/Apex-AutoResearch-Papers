# Memory — verification_triggered_retrieval

## MVP 实验教训 (2026-05-17)

### 核心发现：query form 对检索质量无正向影响，大 corpus 上甚至负向
- **mvp_001**（小 corpus ~2000 passages）：两种 query 无显著差异（-0.74pp, p=0.106），因 entity matching 主导，overlap ~90%+
- **mvp_002**（Wikipedia 21M passages, BM25）：overlap 降至 53%（两种 query 确实检索到不同文档），但 verification queries **显著更差**（-3.28pp, p=0.005, d=-0.141）
- 原假设"断言形式 query 更匹配 Wikipedia 声明性结构"被彻底证伪——方向相反，且在排除 corpus 大小混淆因素后效应更强
- **根因分析**：Wikipedia passages 是百科风格叙述，BM25 对疑问词（What/Who/How）的处理反而有利于匹配段落中的关键实体词；而 verification query 的 "Evidence supporting or contradicting that..." 前缀引入了噪声词，稀释了实体匹配信号

### Kill criteria 触发
按 D001 预设标准：overlap↓ but entailment diff ≤ 0 → KILL

### 实验设计注意事项
- Qwen3-8B 用 transformers 逐条推理（非 vllm batch）200 条耗时 ~94 min
- vllm 与 torch 2.8 ABI 不兼容
- Pyserini 预建 Wikipedia index 下载不稳定，最终用 Tevatron/wikipedia-nq-corpus (21M passages) 本地建 BM25 index (19GB)

### 环境信息
- westd-46807: RTX PRO 6000 Blackwell 95GB, CUDA 12.8, miniconda3
- MuSiQue dev 200 条已准备: /root/autodl-tmp/data/musique_dev_200.json
- Wikipedia BM25 index: /root/autodl-tmp/indexes/ (19GB)
