# infra seed bug fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_seed-bug-fix_20260517T000425_result.json`
- **Structured JSON:** [`42cdee774ded6267246a.json`](../../sessions/42/42cdee774ded6267246a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 结果汇报

### 1. PID 628482 (008d_civo_trigger_s2)
已成功 kill，ps 确认进程不存在。

### 2. 诊断结果：seed bug 根因

**不是 `args_type` 解析问题** — 测试确认 `args_type(0)("1")` 正确返回 `int(1)`。

**真正的 code bug 在 `tools.py:332` + `dreamer.py:142`：**

- `tools.sample_episodes(episodes, length, seed=0)` 创建独立的 `np.random.RandomState(0)` 硬编码 seed=0
- `make_dataset(episodes, config)` 调用时**没有传递 `config.seed`**
- 结果：replay buffer 采样的随机序列**完全不受 `--seed` 影响**，永远是 seed=0

**加剧因素**：s2 的日志显示 `Logdir logdir/exp_008d_civo_trigger_s1`（使用了 s1 的 logdir + checkpoint），两个 run 共享相同模型权重 + 相同采样序列 → bit-for-bit identical。

### 3. 修复内容
- `dreamer.py:142`：`tools.sample_episodes(episodes, config.batch_length)` → `tools.sample_episodes(episodes, config.batch_length, seed=config.seed)`
- `dreamer.py:222`：添加 `print(f"[SEED CHECK] config.seed = {config.seed}", flush=True)`

### 4. 验证结果
```
[SEED CHECK] config.seed = 3
```
传入 `--seed 3`，输出正确。

### 5. cuda:1 (PID 629444) 状态
正常运行中（exp_019a_v2_pickcube_baseline），未受影响。

---
