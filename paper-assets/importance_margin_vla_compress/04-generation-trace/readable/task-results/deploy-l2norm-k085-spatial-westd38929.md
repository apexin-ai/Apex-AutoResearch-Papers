# deploy l2norm k085 spatial westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_l2norm-k085-spatial-westd38929_20260522T010546_result.json`
- **Structured JSON:** [`b9a76ed1a16157abb262.json`](../../sessions/b9/b9a76ed1a16157abb262.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

新实验已加载完成，正在启动 eval。汇报如下：

## westd-38929
| GPU | 实验 | 状态 | 进度 | GPU占用 |
|-----|------|------|------|---------|
| GPU0 | L2norm k=0.85 Spatial s42 (n=500) | **已部署** PID=185483 | 模型加载完毕，pruning 217/256 tokens, 开始eval | 9700 MiB |
| GPU1 | random k=0.9 Spatial s42 (n=50) | alive PID=9135 | T8/10, ep30/50 (93%), 累计 215/400=**53.8%** | 10602 MiB |
| GPU2 | random k=0.925 Object s43 (n=50) | alive PID=68039 | T5/10 完成, 累计 98/300=**32.7%** | 10545 MiB |
| GPU3 | random k=0.85 Spatial s42 (n=50) | alive PID=48598 | T5/10 完成, 累计 161/300=**53.7%** | 10596 MiB |

## westd-41074
| GPU | 实验 | 状态 | 进度 | GPU占用 |
|-----|------|------|------|---------|
| GPU0 | L2norm k=0.85 Object s42 (n=50) | alive PID=818572 | T5/10, ep30/50 (100%), 累计 247/250=**98.8%** | 10529 MiB |
| GPU1 | L2norm k=0.95 Object s42 (n=50) | alive PID=818652 | T5/10, ep30/50 (100%), 累计 241/250=**96.4%** | 10545 MiB |
| GPU2 | (其他任务) | — | — | 28546 MiB |
| GPU3 | (其他任务) | — | — | 27526 MiB |

**注意**: westd-38929 GPU1/2/3 和 westd-41074 GPU0/1 的实验都是 n_episodes=50，新部署的 GPU0 是 n_episodes=500（按指令），运行时间会长很多。

---
