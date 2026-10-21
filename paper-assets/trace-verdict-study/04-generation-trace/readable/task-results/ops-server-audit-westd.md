# ops server audit westd

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-audit-westd_20260523T195153_result.json`
- **Structured JSON:** [`d6b2b6976febb4f3a4dc.json`](../../sessions/d6/d6b2b6976febb4f3a4dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11235 审计结果

### 分类建议：**B** — 暂不跑实验，后续需要保留

---

### GPU 状态
| GPU | 型号 | 显存占用 | GPU-Util | 进程 |
|-----|------|----------|----------|------|
| 0 | RTX PRO 6000 Blackwell | 49175MiB / 97887MiB | 0% | **无** |
| 1 | RTX PRO 6000 Blackwell | 0MiB / 97887MiB | 0% | 无 |

**异常**: GPU 0 占用 ~48GB 显存但无进程，疑似僵尸显存泄漏，重启实例可释放。

### 进程
- 无训练/eval 进程
- 5 个轻量 `http.server`（论文/图表预览用）
- 标准系统服务（supervisord, jupyter, tensorboard, sshd）

### 磁盘占用

| 分区 | 容量 | 已用 | 可用 | 占比 |
|------|------|------|------|------|
| 根分区 / | 30G | 21G | 9.8G | 68% |
| 数据盘 /root/autodl-tmp | 250G | 203G | 48G | **82%** |

**数据盘明细**：

| 目录 | 大小 | 说明 |
|------|------|------|
| trace-verdict-study-checkpoints/ | **102G** | 大量实验 checkpoint（~90个子目录） |
| models/ | **53G** | 通用模型（非本项目专属） |
| div_cal_verify/ | **34G** | 非本项目目录，待确认归属 |
| trace-verdict-study-models/ | 15G | Qwen2.5-Coder-1.5B + 7B |
| trace-verdict-study-data/ | 903M | 训练数据 |
| .hf_cache/ | 65M | — |

项目代码目录 `/root/trace-verdict-study/` 仅 509M，内含 1 个 >100MB 文件（deepseek adapter 153MB）。

### 理由

1. **无活跃实验** — 无 GPU 进程，无训练/eval 进程，CodeLlama gradient masking 实验已结束
2. **论文提交在即** — ARR DDL 5/25，2-3 个月后 rebuttal 可能需要补实验，checkpoint 和模型暂需保留
3. **磁盘偏满** — 数据盘 82%，102G checkpoint 是主要占用；`div_cal_verify/`（34G）如非本项目可优先清理
4. **GPU 0 显存泄漏** — 建议找机会重启实例释放 48GB 僵尸显存

---
