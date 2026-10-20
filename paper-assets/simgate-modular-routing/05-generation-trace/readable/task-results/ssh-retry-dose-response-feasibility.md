# ssh retry dose response feasibility

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_retry-dose-response-feasibility_20260518T025841_result.json`
- **Structured JSON:** [`41497bbd83714e8ba590.json`](../../sessions/41/41497bbd83714e8ba590.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。以下是完整汇报。

---

## 可行性检查结果

| 检查项 | 状态 | 详情 |
|--------|------|------|
| **代码** | PASS | `src/reflexion_baseline.py` 支持 `--mode retry --max-trials N`，已有完整 `run_trial_loop` + `APIAgent` |
| **模型** | PASS | `/root/autodl-tmp/models/Qwen2.5-7B-Instruct/` 4 shard safetensors 齐全 |
| **GPU** | PASS | 4× RTX PRO 6000 96GB 全部空闲 (0MiB/0%) |
| **vLLM** | **需启动** | 无 vLLM 进程在跑，需先在 cuda:2 (port 8000) 启动 |
| **数据** | PASS | 既有 reflexion part1+part2 (11 tasks × 20 eps)，`reflexion_summary.json` 可用。N=3 retry baseline 已跑完 (DR=40.9%) |
| **Task 列表** | PASS | 10 个 death-prone tasks 确认（已排除 `find-non-living-thing`） |

## 脚本信息

- **路径**: `/root/autodl-tmp/simgate-modular-routing/run_retry_dose_response.py`
- **核心逻辑**: 复用 `src/reflexion_baseline.py` 的 `APIAgent` + `run_trial_loop`，retry 模式（无 reflection）
- **输出目录**: `results/retry_dose_response/retry_n{1,5,10}/` + 汇总 `dose_response_summary.json`

## 启动命令

```bash
# 1. 先启动 vLLM (cuda:2, port 8000)
VLLM_USE_FLASHINFER_SAMPLER=0 CUDA_VISIBLE_DEVICES=2 nohup python -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/models/Qwen2.5-7B-Instruct \
  --port 8000 --gpu-memory-utilization 0.9 --trust-remote-code \
  > logs/vllm-7b-dose.log 2>&1 &

# 2. 等 vLLM ready 后跑实验
cd /root/autodl-tmp/simgate-modular-routing
python run_retry_dose_response.py --n-values 1,5,10 --episodes-per-task 20
```

## 预估运行时间

- N=1: 200 eps × ~30s/ep ≈ 1.7h
- N=5: 200 eps × ~2.5min/ep (avg ~3 trials) ≈ 8h
- N=10: 200 eps × ~4min/ep (avg ~5 trials) ≈ 13h
- **总计约 20-25 小时**（可考虑双端口 vLLM 并行 N=1 和 N=5 缩短到 ~15h）

## 现有 retry 代码关键参数

- Task 列表: 11 tasks（含 `find-non-living-thing`），dose-response 脚本已排除为 10
- Episode 数: 20 per task（可调 `--episodes-per-task`）
- 模型加载: vLLM OpenAI-compatible API（`http://localhost:8000/v1`），model name = `Qwen2.5-7B-Instruct`
- Max steps per episode: 30
- Death threshold: score ≤ -100

---
