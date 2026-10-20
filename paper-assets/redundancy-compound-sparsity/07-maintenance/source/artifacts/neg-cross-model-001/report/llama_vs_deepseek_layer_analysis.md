# Llama vs DeepSeek Per-Layer Analysis

## Key Findings

### 1. Llama per-layer r 极其均匀
32 层 r 范围 0.393–0.485，标准差极小。每一层的 anchor_sim 都与 surprisal 强相关。

### 2. DeepSeek 有 11 个弱/负相关层
r < 0.05 的层集中在 L0-3 和 L13-20，直接拖垮全局 r（0.147）。最强层 L4 r=0.287 仍远低于 Llama 最低值。

### 3. Layer Group 对比

| Group | Llama r | DeepSeek r | Gap |
|-------|---------|------------|-----|
| Early | 0.450 | 0.128 | +0.322 |
| Mid | 0.434 | 0.072 | **+0.361** |
| Late | 0.472 | 0.130 | +0.342 |

Mid layers gap 最大，DeepSeek L13-17 几乎全是 r≈0 死区。

### 4. Δpert 方向性完全不同
- Llama late layers (L20-31): Δpert 平均 **+14.3%**，信号最强
- DeepSeek mid+late layers: Δpert **−3.3% 到 −3.6%**，cross-axis 反转

### 5. 架构解读
GQA 多 KV head → anchor_sim 在每层都是可靠冗余度信号。
MLA 低秩压缩 KV → early/mid layers 对应关系被破坏。

## 产出文件（服务器端）
- /home/sonny/redundancy-compound-sparsity/results/neg_cross_model/analysis/llama_per_layer_r.pdf
- /home/sonny/redundancy-compound-sparsity/results/neg_cross_model/analysis/llama_per_layer_dpert.pdf
- /home/sonny/redundancy-compound-sparsity/results/neg_cross_model/analysis/llama_vs_deepseek_r_comparison.pdf
- /home/sonny/redundancy-compound-sparsity/results/neg_cross_model/analysis/llama_vs_deepseek_dpert_comparison.pdf
- /home/sonny/redundancy-compound-sparsity/results/neg_cross_model/analysis/llama_vs_deepseek_summary.md