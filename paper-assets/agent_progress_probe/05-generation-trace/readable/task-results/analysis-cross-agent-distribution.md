# analysis cross agent distribution

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-agent-distribution_20260514T123954_result.json`
- **Structured JSON:** [`bb34f259913c1710ad52.json`](../../sessions/bb/bb34f259913c1710ad52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**1. `command_repetition` 是迁移失败的首要原因**
- OpenHands 上 firing rate 92.23%（vs SWE-agent 65.59%），且在 OpenHands **progress 窗口**中 71% 的时间投了 stagnation 票——巨量误报
- 原因：OpenHands 大量使用 `cd + grep/find/python` 重复 bash 模式进行正常探索，而 SWE-agent 有专用命令（open/search_dir）不触发重复检测

**2. `file_diff_delta` 是唯一可靠的跨 agent 信号**
- OH progress 窗口：87% 投 progress，0.2% 投 stagnation
- OH stagnation 窗口：31% 投 stagnation，0.02% 投 progress
- 这解释了单 LF oracle (macro-F1=0.9582) 碾压 probe

**3. Embedding 域偏移极其严重**
- 域分类器准确率 **99.82%**，Proxy A-distance=1.993（接近理论最大值 2.0）
- 两个 agent 的 embedding 空间几乎完全可分

**4. 行为模式根本不同**
- SWE-agent: 24.5 AI steps/traj，31.6% edit 命令
- OpenHands: 64.0 AI steps/traj，30.2% python 执行 + 25.5% 文件读取
- Action type 完全不重叠

**5. OpenHands 解决率 48.1% vs SWE-agent 16.3%**，意味着更多轨迹包含真实进展阶段，但 cmd_repetition 将其错误标为 stagnation

报告和 JSON 已保存到 `artifacts/` 目录。

---
