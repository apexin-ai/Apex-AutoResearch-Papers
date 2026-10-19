# code mvp 001 setup and run

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_001_setup_and_run_20260520T141803_result.json`
- **Structured JSON:** [`3e41104580a2771694e9.json`](../../sessions/3e/3e41104580a2771694e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已启动，正在执行 Step 1 (Extract activations)。

**部署完成，总结：**

| 项目 | 状态 |
|------|------|
| 服务器 | westd-13176, 4× RTX PRO 6000 Blackwell 96GB, CUDA 13.0 |
| Python 环境 | conda base, Python 3.12.3, torch 2.8.0+cu128 |
| 依赖安装 | transformers 5.8.1, datasets 4.8.5, scikit-learn 1.8.0, pandas 3.0.3 |
| 代码部署 | 4 个 .py + run_mvp.sh → /root/xling_calib_direction/ |
| 实验提交 | mvp_001, GPU 0, tmux session `mvp_001`, PID 3301 |
| 日志 | ~/runs/xling_calib_direction/mvp_001.log |
| Registry | RUNNING, spec 已写入 |

实验预计运行 2-3 小时（主要是 activation 提取阶段需要逐条推理 ~14K × 6 语言）。

---
