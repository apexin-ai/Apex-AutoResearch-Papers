# research supcon gnn reference

**contrastive graph jailbreak detect** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_supcon-gnn-reference_20260517T052927_result.json`
- **Structured JSON:** [`0d11df15769200fc439f.json`](../../sessions/0d/0d11df15769200fc439f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成，结果已写入 `memory.md`。核心发现：

- **SupConLoss**: 直接用 HobbitLong/SupContrast 的实现，输入 `[bsz, 2, feat_dim]` L2-normalized features + labels
- **GIN Encoder**: 3 层 GINConv (内含 2-layer MLP) + BatchNorm + global_add_pool，标准 PyG 写法
- **Graph Augmentation**: PyG 原生 `dropout_edge` + 手写 `drop_feature` + `subgraph` 即可覆盖三种增强，无需额外依赖
- **最近前驱**: LCGNN (DASFAA 2021) 是图分类 SupCon 最直接参考；PyGCL 库提供模块化框架但增加依赖

---
