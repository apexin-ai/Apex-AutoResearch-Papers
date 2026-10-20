# ssh exp001 proprietary judges

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp001_proprietary_judges_20260522T041459_result.json`
- **Structured JSON:** [`4dea80176de52228ce33.json`](../../sessions/4d/4dea80176de52228ce33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。汇总报告如下：

---

## 汇总报告

### 1. 代理可用模型列表

| Judge | 代理 Model ID | JUDGE_MAP 名称 |
|-------|--------------|----------------|
| GPT-5.5 | `gpt-5.5` | `gpt-5.5-proxy` |
| Claude Opus 4.7 | `claude-opus-4-7` | `claude-opus-4.7-proxy` |
| Claude Sonnet 4.6 | `claude-sonnet-4` | `claude-sonnet-4.6-proxy` |
| DeepSeek-V4-Pro | `deepseek-v4-pro` | `deepseek-v4-pro-proxy` |
| Qwen3-235B | `qwen3-235b-a22b` | `qwen3-235b-proxy` |
| Gemini 2.5 Pro | `gemini-2.5-pro` | `gemini-2.5-pro-proxy` |

### 2. 模型测试结果

全部 ✅。GPT-5.5 不支持 temperature=0（已设为 None 跳过）。

### 3. 配置文件

```
exp001/config_gpt-5.5-proxy_arena.yaml
exp001/config_claude-opus-4.7-proxy_arena.yaml
exp001/config_claude-sonnet-4.6-proxy_arena.yaml
exp001/config_deepseek-v4-pro-proxy_arena.yaml
exp001/config_qwen3-235b-proxy_arena.yaml
exp001/config_gemini-2.5-pro-proxy_arena.yaml
```

每个 judge 写入独立输出目录 `results/&lt;judge-name>/`。

### 4. Tmux Session 状态

| Session | PID (python) | 状态 |
|---------|------|------|
| exp001-gpt55 | 195498 | 运行中 |
| exp001-opus47 | 195513 | 运行中 |
| exp001-sonnet46 | 195532 | 运行中 |
| exp001-deepseek | 195659 | 运行中 |
| exp001-qwen3 | 195679 | 运行中 |
| exp001-gemini | 195696 | 运行中 |

### 5. 各 Judge 已收集条数（启动约 2 分钟后）

| Judge | 已收集 | 速率 |
|-------|--------|------|
| gpt-5.5-proxy | 17 | ~0.1 items/s |
| qwen3-235b-proxy | 15 | ~0.1 items/s |
| gemini-2.5-pro-proxy | 12 | ~0.08 items/s |
| claude-sonnet-4.6-proxy | 5 | ~0.04 items/s |
| deepseek-v4-pro-proxy | 5 | ~0.04 items/s |
| claude-opus-4.7-proxy | 1 | ~0.01 items/s（延迟高） |

### 6. 问题与处理

- **GPT-5.5 不支持 temperature=0**：ProxyJudge 中该模型设 `temperature=None`（不传参数）
- **Claude 模型 ID 与预期不同**：代理使用 `claude-opus-4-7` / `claude-sonnet-4` 而非带日期的完整 ID
- **Opus 延迟大**：每次请求约 60-90s，但正在正常产出
- **并发写入安全**：采用 per-judge 独立输出目录避免冲突
- **代码改动**：在 `judge_interface.py` 末尾添加了 `ProxyJudge` 类 + 6 条 JUDGE_MAP 注册

每个 judge 需要收集 3000 条 pairwise judgment（500 prompts × 3 target models × 2 positions）。按当前速率，最快的 (gpt-5.5) 约 6-7 小时完成，最慢的 (opus) 可能需要更久。

---
