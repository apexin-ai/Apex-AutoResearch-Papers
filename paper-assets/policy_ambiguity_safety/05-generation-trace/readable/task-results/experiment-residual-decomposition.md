# experiment residual decomposition

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_residual_decomposition_20260522T221812_result.json`
- **Structured JSON:** [`d6f50d1812565c23482e.json`](../../sessions/d6/d6f50d1812565c23482e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态总结：**

两个脚本已完成，逻辑验证通过：

1. **`residual_decomposition/run_replication.py`** — 分层采样 50 clauses → 运行 1000 episodes（50×2 conditions×2 models×5 reps）→ 自动 judge
   - 支持 `--resume`（按 clause_id|condition|model|rep 去重）
   - 保存 `manifest.json` 记录采样配置
   - 错误处理：API 失败不会中断整个 batch

2. **`residual_decomposition/analyze_variance.py`** — 读取 judgments → ICC(1) 方差分解 → 输出 `results.json`
   - Overall ICC + per-condition + per-ambiguity-type 分解
   - Cell consistency 统计（unanimous vs mixed cells）
   - 映射回原始 60.8% 残差的比例

**阻塞项：** OpenRouter API 余额不足（402 Insufficient balance）。充值后运行：

```bash
cd artifacts
source .venv/bin/activate
python3 residual_decomposition/run_replication.py
# 完成后分析：
python3 residual_decomposition/analyze_variance.py
```

---
