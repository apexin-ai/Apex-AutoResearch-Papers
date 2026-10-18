# infra fix data proxy

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-data-proxy_20260513T195022_result.json`
- **Structured JSON:** [`78350dcd0102a1950f21.json`](../../sessions/78/78350dcd0102a1950f21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

| 项目 | 状态 |
|------|------|
| **tmux 清理** | 已清理 mvp_001 / sanity_001，无残留 GPU 进程 |
| **C4 calibration 数据** | 策略 A 失败（代理 ProxyError），使用**策略 B**（WikiText-103 替代），100 samples / 66KB |
| **WikiText-2 eval 数据** | 已缓存到 HF_HOME，离线加载验证通过 |
| **profiler.py 修改** | 新增 `--calibration_data` 参数；`_load_calibration_data()` 优先从本地 JSON 加载，fallback 到 HF streaming |
| **run_mvp.py 修改** | 新增 `--calibration_data` 参数，透传给 DistortionProfiler |
| **eval_ppl.py** | 无需修改代码，tmux 中设 `HF_HOME=/root/autodl-tmp/.hf_cache` 即可离线加载 |
| **语法验证** | profiler.py / run_mvp.py / eval_ppl.py 全部通过 |

**使用方式**：启动实验时传入 `--calibration_data /root/ratekv/c4_calibration.json`，tmux session 需设置环境变量：
```bash
export HF_HOME=/root/autodl-tmp/.hf_cache
```

**无剩余 blocker。**

---
