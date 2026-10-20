# train openhands fewshot probe

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_openhands-fewshot-probe_20260514T135633_result.json`
- **Structured JSON:** [`da86b59cb5409746bcde.json`](../../sessions/da/da86b59cb5409746bcde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**已提交。**

- **PID**: 56595
- **tmux session**: `openhands-fewshot-probe`
- **GPU**: cuda:1
- **日志**: `~/runs/agent_progress_probe/openhands-fewshot-probe.log`

**预期运行时间**：~10-15 分钟。主要开销在加载 2.9GB embeddings.pt 到内存（~30s），之后 4 个 few-shot 比例各训练最多 10 epochs（early stopping patience=3），GRU 模型很小所以训练很快。

**实验设计**：
- 固定 OH 数据 70/15/15 instance-level split
- Zero-shot baseline + 4 个 few-shot 比例（5%/10%/20%/50% 的训练 instances）
- 从 SWE-agent checkpoint 初始化，lr=1e-4，pos_weight 处理 6.6% stagnation 不平衡
- 输出到 `fewshot_results/fewshot_results.json`

---
