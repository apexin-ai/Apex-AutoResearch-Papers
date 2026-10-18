# ops cqa1 verify and audit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1_verify_and_audit_20260526T093041_result.json`
- **Structured JSON:** [`d89fed1e9a9819343f50.json`](../../sessions/d8/d89fed1e9a9819343f50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。以下是三部分汇总：

---

## Part 1: cqa1-33015 GPU 0+1 验证

**部署确认成功。** 两个实验均在运行：

| GPU | PID | 实验 | 启动时间 | CPU时间 |
|-----|-----|------|---------|---------|
| 0 | 212677 | π0.5 L2norm k=0.75 Long seed42 | 17:13 | 101 min |
| 1 | 213217 | π0.5 Attention k=0.75 Long seed42 | 17:14 | 98 min |

GPU 2 (PID 77661, L2norm k=0.5) 和 GPU 3 (PID 77832, Random k=0.5) 也正常运行，未动。

---

## Part 2: Goal seed43 Registry 注册

两个结果已注册为 DONE/success：

| exp_id | Mode | SR | Episodes |
|--------|------|----|----------|
| `eval_openvla_l2norm_k09_goal_seed43_v3` | L2norm k=0.9 | **75.2%** (376/500) | 500 |
| `eval_openvla_random_k09_goal_seed43` | Random k=0.9 | **80.4%** (402/500) | 500 |

注：还发现一个额外结果文件 `openvla_baseline_goal_seed43.json`（SR=77.6%），未在任务范围内但已存在于服务器。

---

## Part 3: 全 4 台服务器 nvidia-smi 审计

| 服务器 | GPU | 型号 | Memory Used | Util% | 进程/实验 | 状态 |
|--------|-----|------|-------------|-------|----------|------|
| **cqa1-33015** | 0 | RTX 4090 D | 10483/24564 MiB | 42% | π0.5 L2norm k=0.75 Long s42 | 正常 |
| | 1 | RTX 4090 D | 10647/24564 MiB | 43% | π0.5 Attn k=0.75 Long s42 | 正常 |
| | 2 | RTX 4090 D | 10017/24564 MiB | 11% | π0.5 L2norm k=0.5 Long s42 | 正常 |
| | 3 | RTX 4090 D | 10017/24564 MiB | 58% | π0.5 Random k=0.5 Long s42 | 正常 |
| **westd-38929** | 0 | RTX PRO 6000 BW | 15980/97887 MiB | 60% | OpenVLA Random k=0.85 Object s42 v2 | 正常 |
| | 1 | RTX PRO 6000 BW | 16358/97887 MiB | 76% | OpenVLA Random k=0.5 Long s42 v2 | 正常 |
| | 2 | RTX PRO 6000 BW | 15964/97887 MiB | 34% | OpenVLA Attn k=0.85 Goal s42 v3 | 正常 |
| | 3 | RTX PRO 6000 BW | 15980/97887 MiB | 54% | OpenVLA Attn k=0.85 Object s42 | 正常 |
| **westd-41074** | 0 | RTX PRO 6000 BW | 15748/97887 MiB | 7% | OpenVLA Random k=0.85 Long s42 v3 | ⚠️ 低util |
| | 1 | RTX PRO 6000 BW | 15980/97887 MiB | 56% | OpenVLA L2norm k=0.85 Object s42 | 正常 |
| | 2 | RTX PRO 6000 BW | 1/97887 MiB | 0% | — | ⚠️ 空闲 |
| | 3 | RTX PRO 6000 BW | 15980/97887 MiB | 34% | OpenVLA L2norm k=0.95 Object s42 | 正常 |
| **westd-27271** | 0 | RTX PRO 6000 BW | 1/97887 MiB | 0% | — (L2norm goal s43 已完成) | ⚠️ 空闲 |
| | 1 | RTX PRO 6000 BW | 15964/97887 MiB | 69% | OpenVLA Attn k=0.9 Goal s43 | 正常 |

### 异常标记

1. **westd-41074 GPU 2** — 完全空闲（0% util, 1 MiB），无任何进程
2. **westd-27271 GPU 0** — 完全空闲，L2norm Goal seed43 v3 已完成退出
3. **westd-41074 GPU 0** — 显存已占（15748 MiB）但 util 仅 7%，Random k=0.85 Long 可能接近完成或在 episode 间隙

总计：**14 GPU 中 11 个正常运行，2 个空闲可调度，1 个低利用率待观察。**

---
