# code mvp k3 framework

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-k3-framework_20260512T101924_result.json`
- **Structured JSON:** [`578fffaa655f604f398a.json`](../../sessions/57/578fffaa655f604f398a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个文件已创建，导入验证通过。

文件清单：

| 文件 | 功能 |
|------|------|
| `config.py` | MVP 配置（K=3, CSS 阈值, CIRCUS B=10） |
| `circuit_discovery.py` | 三种方法统一接口 + edge name 归一化 |
| `circus.py` | config-bagging + core/contingent/noise 分层 |
| `css.py` | 跨方法二值共识计算 + 阈值筛选 |
| `cross_tabulate.py` | 2×2 交叉表 + off-diagonal % 计算 |
| `evaluation.py` | 电路 faithfulness 评估（CPR/CMD） |
| `run_mvp.py` | 完整 pipeline（8 步 + gate 判定） |

核心设计点：
- 所有方法统一输出 `Dict[str, float]`，edge name 归一化到 TransformerLens 格式
- CSS 逻辑完整可运行（compute_css / threshold_css / binarize_scores）
- CIRCUS config-bagging 用 percentile-based 阈值，B=10 bin
- 交叉表数据结构用 `CrossTable` dataclass，off-diagonal % 是属性直接读取
- 需要 GPU 验证的库调用（EAP-IG/ACDC/Edge Pruning/evaluation ablation）标记了 TODO

---
