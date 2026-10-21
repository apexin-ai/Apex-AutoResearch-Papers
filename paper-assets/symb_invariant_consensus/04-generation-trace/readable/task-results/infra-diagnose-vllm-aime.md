# infra diagnose vllm aime

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_diagnose-vllm-aime_20260515T154618_result.json`
- **Structured JSON:** [`96af8500bcaabdd347c8.json`](../../sessions/96/96af8500bcaabdd347c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是报告：

---

## AIME v2 实验诊断报告

### 进程状态
| 组件 | 状态 | PID |
|------|------|-----|
| tmux bash shell | **alive** (sleeping) | 121139 |
| timeout wrapper | **alive** (sleeping) | 121143 |
| `python -u run_full_mvp.py` | **alive** (sleeping) | 121144 |
| vLLM EngineCore | **alive** (GPU 100%) | 102970 |

### GPU 状态
- **GPU**: NVIDIA RTX PRO 6000 Black, 89149MiB / 97887MiB
- **利用率**: 100%，温度 65°C，功耗 411W/600W
- **正常**，无硬件问题

### vLLM 状态
- `/health` → **200 OK**
- `/v1/models` → 正常返回（QwQ-32B, max_model_len=16384）
- 测试推理请求 → **<1s 返回**，引擎功能正常
- **当前 running requests: 12**, waiting: 0

### 卡死原因
日志明确显示：**第 5 题（aime2024_II_05，凸六边形几何题）的 12 条 trace 生成请求持续超时**。

时间线：
- `22:01` — 第 4 题完成，开始第 5 题
- `22:11` — 第一次请求超时（~10min client timeout）
- 之后每 ~10 分钟重试一次，全部超时
- `23:41` — 最近一次重试，仍然超时
- **已卡死 ~1h 47min**

根因：12 条并发 trace（k=12, max_tokens=10240）在单 GPU 上竞争资源，每条 trace 的吞吐极低。客户端 ~600s 超时后重试，但旧请求可能仍在 vLLM 中 running，形成恶性循环——vLLM metrics 显示恰好 12 个 running requests。

### 已完成结果摘要
4/30 题完成，总耗时 2226.9s（~37min）：

| 题号 | ID | SICA | SC | GT | 耗时 |
|------|----|------|----|----|------|
| 1 | aime2024_II_01 | 73 ✓ | 73 ✓ | 73 | 470s |
| 2 | aime2024_II_02 | ✗ (Z3异常) | ✗ | 236 | 624s |
| 3 | aime2024_II_03 | 45 ✓ | 45 ✓ | 45 | 631s |
| 4 | aime2024_II_04 | 33 ✓ | 33 ✓ | 33 | 502s |

准确率：SICA 3/4 = 75%, SC 3/4 = 75%

### 建议
**需要 kill 实验 + 重启。** 当前状态无法自行恢复——每次重试都会超时。两个选择：

1. **Kill 实验进程（121143），保留 vLLM**：vLLM 本身是好的（test request 秒回），只需 kill 掉 running 中的 stuck requests。然后增大 client timeout 或减小并发 k 值后重启实验。
2. **Kill 实验 + 重启 vLLM**：更彻底，清除 vLLM 中的残留请求状态。

推荐方案 1，因为 vLLM 引擎没有故障。kill 后可以考虑降低 `--k` 为 8 或增大 HTTP timeout 来避免同类问题。

---
