# ssh fix ratelimiter and restart judges

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_ratelimiter_and_restart_judges_20260522T071918_result.json`
- **Structured JSON:** [`edb4787e5e3ddcc34eae.json`](../../sessions/ed/edb4787e5e3ddcc34eae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成。汇总：

---

### 1. RateLimiter 修复 ✓

**修改前**（L34-39）— sleep 在锁内，8 workers 串行化：
```python
def wait(self):
    with self._lock:
        elapsed = time.time() - self.last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)  # 锁内 sleep！
        self.last_call = time.time()
```

**修改后** — 锁内只计算+预占时间槽，sleep 在锁外：
```python
def wait(self):
    with self._lock:
        now = time.time()
        elapsed = now - self.last_call
        sleep_time = max(0, self.min_interval - elapsed)
        self.last_call = now + sleep_time  # 预占
    if sleep_time > 0:
        time.sleep(sleep_time)  # 锁外 sleep
```

### 2. RPM 配置更新 ✓

3 个 local judge config 全部 `rpm: 100` → `rpm: 999`（本地 vLLM 推理无需限流）。

### 3. Response 生成进度 — 未完成

| 模型 | 已生成 | 目标 | 进度 |
|------|--------|------|------|
| llama-3.3-70b | 71 | 500 | 14% |
| qwen2.5-72b | 46 | 500 | 9% |
| mistral-large-2 | 23 | 500 | 5% |

生成脚本在 `gen-vllm` tmux session 中运行（`generate_vllm_online.py --all --workers 32`，启动于 15:10）。日志显示速度约 0.04-0.10 items/s per model，**预计还需 75-200 分钟**（约 1.5-3.5 小时）。

### 4. Judge 收集 — 暂不重启

Response 远未完成，不启动 judge 收集。等 3 个模型都到 500 后再用 `--workers 8` 启动，届时 RateLimiter 修复 + RPM 999 已就绪，8 workers 将真正并行。

---
