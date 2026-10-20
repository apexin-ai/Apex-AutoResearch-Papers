## MVP 实验结论 (2026-05-17) ⚠️ NEGATIVE

### Round 1 (one-hot features): GIN 0.845 < RF 0.862 (-1.8pp)
- 原因: one-hot tool features 给 RF 提供 tool identity shortcut

### Round 2 (semantic MiniLM-L6 features): GIN 0.848 < RF 0.962 (-11.5pp)
- GIN+SupCon holdout AUROC: 0.8475±0.0431 (10-mode mean)
- RF semantic holdout AUROC: 0.9622±0.0176 (10-mode mean)
- **MVP Gate FAIL**: GIN 未超过 RF+5pp

### 根因: 图结构极度稀疏
- 61.5% 的图有 **0 条边** (string-matching 建边在短链上失效)
- 仅 6.1% 有 ≥2 条边
- GNN message passing 在无边图上退化为 MLP
- Graph size 是 label shortcut: 大图(≥4 nodes) 仅 1.8% 是攻击

### 教训
- STAC 攻击链 84.7% 为 2-3 步，天然不适合 graph learning (需要更长链)
- String-matching 建边太严格，实际 data-flow 无法通过文本匹配捕获
- RF + semantic embedding (mean/max pool) 是极强 baseline，graph structure 未提供额外价值
- 早期 dry-run 的高 AUROC (0.85) 是误导——那是 in-distribution，不反映 GIN vs RF 差距

---

## STAC Dataset 调研结果 (2026-05-17)

### 核心统计
- 483 attack traces, Public, CC BY-NC 4.0
- 链长: mean=2.62, 84.7% 为 2-3 步, 256 unique tools
- 10 种 failure mode 均匀分布 (42-55/类)
- SHADE-Arena 4 环境占 80.7%

---

## 关键决策 (2026-05-17)

### Benign 数据: MVP 只用合成 (不用 ToolBench)
- **原因**: ToolBench 工具集与 STAC 不同 → node feature shortcut
- **方案**: benign_generator.py 合成 600 条, 深度分布匹配 STAC

### Data leakage 修复
1. holdout test set 包含 15% benign
2. linear probe early stopping 不碰 test
3. holdout 评估用全量 encoder

---

## 服务器环境 (2026-05-17)

- 服务器: bjb2-32660 (`ssh -p 32660 root@connect.bjb2.seetacloud.com`)
- GPU: 2× RTX 5090 32GB (cuda:0, cuda:1)
- Python 3.12.3 / CUDA 13.0 / PyTorch 2.8.0+cu128 / PyG 2.7.0
- 项目路径: `/root/contrastive_graph_jailbreak_detect`

---

## 技术栈

- SupConLoss: HobbitLong/SupContrast, [bsz, 2, feat_dim] L2-normalized + labels
- GIN: 3-layer GINConv + BatchNorm + global_mean_pool + projection head
- Augmentation: dropout_edge + drop_feature + subgraph (手写)
- Semantic embedding: sentence-transformers/all-MiniLM-L6-v2 (384-dim)

---

## Benign 数据源

| Repo | 有 Benign | 数据量 | 备注 |
|------|:-:|:-:|:-:|
| ToolBench | YES | 126K | MVP 不用 (工具集不同) |
| SHADE-Arena | YES (少量) | 数百 | 后续可用 |
| AgentBench | 需生成 | - | 无预录 traces |
| Agent-SafetyBench | NO | - | 仅工具定义 |
