# ssh prompt sensitivity exit check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prompt-sensitivity-exit-check_20260517T072405_result.json`
- **Structured JSON:** [`0d697dd30860edade493.json`](../../sessions/0d/0d697dd30860edade493.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：成功完成

- **EXIT_CODE=0**，tmux session 已退出，results.json 已生成 (4529 bytes, 273 lines)
- 唯一的 warning 是 CUDA 版本兼容性提示（SM 12.x requires CUDA >= 12.9），不影响结果
- 全部 4 variants × 2 count levels = **8 组结果完整**，每组 10 batches

### 结果汇总

| Variant | Count | Mean Acc | BCS r | BCS p | 显著? |
|---------|-------|----------|-------|-------|-------|
| v2 | 8 | 0.7688 | -0.3326 | 0.348 | No |
| v2 | 32 | 0.5643 | **-0.6477** | **0.043** | **Yes** |
| instruction_rewrite | 8 | 0.8469 | -0.2228 | 0.536 | No |
| instruction_rewrite | 32 | 0.6617 | -0.4693 | 0.171 | No |
| cot | 8 | 0.7490 | 0.2543 | 0.478 | No |
| cot | 32 | 0.6169 | -0.5661 | 0.088 | No (marginal) |
| minimal | 8 | 0.8521 | -0.1703 | 0.638 | No |
| minimal | 32 | 0.6146 | **-0.7710** | **0.009** | **Yes** |

### Cross-variant pooled correlation

| Variant | r | p | Direction |
|---------|------|------|-----------|
| v2 | -0.1464 | 0.538 | negative |
| instruction_rewrite | -0.0700 | 0.769 | negative |
| cot | 0.1929 | 0.415 | positive |
| minimal | -0.0442 | 0.853 | negative |

### 关键发现

1. count=32 时 BCS-accuracy 负相关更强且更稳定（v2 和 minimal 达到 p<0.05）
2. count=8 时相关性弱且不显著，符合预期（schema 少时 BCS 区分度低）
3. `minimal` prompt 在 count=32 下负相关最强 (r=-0.77, p=0.009)
4. Pooled 后相关性被稀释，所有 variant 都不显著——说明 count 是重要的调节变量
5. `cot` 是唯一在 count=8 下显示正相关趋势的 variant（r=0.25），但不显著

---
