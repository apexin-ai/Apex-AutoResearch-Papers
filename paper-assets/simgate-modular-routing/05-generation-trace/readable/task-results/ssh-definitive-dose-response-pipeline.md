# ssh definitive dose response pipeline

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_definitive-dose-response-pipeline_20260518T183352_result.json`
- **Structured JSON:** [`5565e97e24d79ad23db4.json`](../../sessions/55/5565e97e24d79ad23db4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Step 4 完成。Step 5 汇报：

## Reflexion Dose-Response (final_dr, 分母=200)
| N | Episodes | Deaths | final_dr | Wilson 95% CI |
|---|----------|--------|----------|---------------|
| 1 | 200 | 95 | 47.5% | [40.69%, 54.40%] |
| 2 | 200 | 80 | 40.0% | [33.46%, 46.92%] |
| 3 | 200 | 68 | 34.0% | [27.79%, 40.81%] |
| 4 | 200 | 73 | 36.5% | [30.14%, 43.37%] |
| 5 | 200 | 70 | 35.0% | [28.73%, 41.84%] |

## Retry Dose-Response (final_dr, 分母=200)
| N | Episodes | Deaths | final_dr | Wilson 95% CI |
|---|----------|--------|----------|---------------|
| 1 | 200 | 96 | 48.0% | [41.18%, 54.90%] |
| 2 | 200 | 94 | 47.0% | [40.20%, 53.91%] |
| 3 | 200 | 87 | 43.5% | [36.82%, 50.43%] |
| 4 | 200 | 86 | 43.0% | [36.33%, 49.93%] |
| 5 | 200 | 87 | 43.5% | [36.82%, 50.43%] |

## Baselines
- 72B: 34.5%
- Deterministic: 16.3%

## Figure
- PDF 远程路径: `westd-18266:/root/autodl-tmp/simgate-modular-routing/analysis/dose_response_figure.pdf`
- 本地路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dose_response_figure.pdf`
- 文件大小: 16,097 bytes
- 已注册到 manifest.yaml

---
