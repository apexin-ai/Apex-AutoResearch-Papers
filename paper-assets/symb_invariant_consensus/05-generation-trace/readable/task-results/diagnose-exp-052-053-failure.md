# diagnose exp 052 053 failure

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-052-053-failure_20260518T233314_result.json`
- **Structured JSON:** [`a6c96ce159c21da0006b.json`](../../sessions/a6/a6c96ce159c21da0006b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根本原因：exp-052/053 的实验运行脚本从未被部署到服务器。**

具体证据：

| 检查项 | exp-033（成功） | exp-052/053（失败） |
|--------|----------------|-------------------|
| 运行脚本 | `scripts/run_exp033.sh` ✅ | **不存在** ❌ |
| tmux 会话 | `exp033` 活跃运行中 ✅ | **无** ❌ |
| 结果目录 | 有 log + 数据 ✅ | **空目录**（仅 mkdir） |
| vLLM 服务 | GPU1 port 8001 活跃 ✅ | GPU2/3 port 8002/8003 **已死** |

**失败时间线**（CST = UTC+8）：

1. **07:19 CST** — 部署系统在服务器上创建了 `results/exp052_*/` 和 `results/exp053_*/` 目录
2. **07:19-07:20 CST** — vLLM 服务在 GPU 2 (port 8002) 和 GPU 3 (port 8003) 成功启动，日志正常，响应了 health check (`GET /v1/models` → 200 OK)
3. **之后** — 没有实验 Python 脚本被启动（无 `run_exp052.sh`/`run_exp053.sh`，无 tmux session，无实验日志）
4. **~07:30 CST** — cron 连续 5 次探测不到 sentinel 文件和 W&B run，判定 "process dead"
5. vLLM 进程随后被回收，GPU 2/3 现在完全空闲（0MiB）

**不是环境问题**：
- 磁盘空间充足（overlay 43%, /dev/sda2 40%）
- conda 环境正常（exp-033 在同一环境中正常运行）
- GPU 硬件正常（4x RTX PRO 6000，GPU 0/1 正常跑着 vLLM）
- Mistral-7B 模型路径 `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3` 存在（vLLM 成功加载）

**问题出在部署侧**：部署流程只完成了"创建目录 + 启动 vLLM"这两步，但漏掉了"部署运行脚本 + 在 tmux 中启动实验"这一步。需要检查部署代码中 exp-052/053 的 launch 逻辑。

---
