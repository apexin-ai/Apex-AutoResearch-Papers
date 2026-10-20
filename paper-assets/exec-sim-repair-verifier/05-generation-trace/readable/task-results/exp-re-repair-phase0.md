# exp re repair phase0

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_re-repair-phase0_20260516T084228_result.json`
- **Structured JSON:** [`2e38832fc987ec17959a.json`](../../sessions/2e/2e38832fc987ec17959a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 0 完成 — 结果报告

### 运行状态
Phase 0 成功完成：10 instances × 4 conditions × 3 samples = 120 次生成，总耗时 ~22 分钟。

### 核心结果

| Condition | Best-of-K Mean Sim | Δ vs Control |
|-----------|-------------------|-------------|
| **control** | **0.820** | — |
| cls-diag | 0.818 | -0.002 |
| oracle-diag | 0.809 | -0.011 |
| random-diag | 0.719 | **-0.101** |

### 发现

1. **Diagnostic 信息没有帮助**：control 最优，所有 diagnostic 条件持平或更差
2. **Random diagnostic 明确有害** (-10pp)：证实模型确实在读诊断信息，但随机信息会误导
3. **天花板效应**：5/10 实例已经接近完美修复（>0.93 相似度），无提升空间
4. **根因**：mutation patches 太简单（机械性反转），8B base model 不善于利用诊断指令

### 遇到的 Bug / 问题
- vLLM 0.18.1 不支持 Qwen3ForCausalLM → 改用 transformers generate
- 长 diagnostic prompt (356+ tests) 导致生成极慢 → 加了 max_show=15 截断
- 前次进程 GPU 内存未释放 → 需要 kill 子进程（非 bash wrapper）

### Phase 1 建议
1. 用 agent predictions（非 mutations）作为 incorrect patches — 结构性差异更大
2. 用 instruct 模型（Qwen3-8B-Instruct 或 API）
3. Docker 执行验证（真实 resolve rate）
4. 精简 diagnostic（只显示 failing tests）

详细报告：`artifacts/re_repair_phase0_results.md`

---
