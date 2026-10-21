# analysis ced kl001 r4 health

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ced-kl001-r4-health_20260514T153711_result.json`
- **Structured JSON:** [`8f96adff9d7796ade678.json`](../../sessions/8f/8f96adff9d7796ade678.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验刚启动约 5 分钟，目前只到 step 2/100，还没有指标输出。

**状态汇总**:

| 检查项 | 结果 |
|--------|------|
| 进程 | 存活，PID 68084，运行 4m56s |
| GPU | cuda:0 占用 13632MiB / 32607MiB，48% util |
| 进度 | **2/100 steps** |
| step_time | ~112s/step（符合 num_generations=8 预期） |
| 指标 | **尚无输出**（太早，metrics 通常在几步后才打印） |

**判断**: 启动正常，模型加载成功，NLI reward model 就绪，训练已开始跑。但 step 2 还没有 KL / grad_norm / reward 等指标可看。

预计再跑 5-10 分钟（~step 5-7）后会有首批指标。需要我稍后再查一次吗？

---
