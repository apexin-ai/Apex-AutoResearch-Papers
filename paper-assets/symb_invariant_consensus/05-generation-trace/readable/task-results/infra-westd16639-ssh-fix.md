# infra westd16639 ssh fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd16639-ssh-fix_20260518T153046_result.json`
- **Structured JSON:** [`7e97bc133b54dab1839f.json`](../../sessions/7e/7e97bc133b54dab1839f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. SSH key 直连
**已修复成功。** westd-25068 → westd-16639 无密码 SSH key 认证正常工作。

### 2. 模型下载状态

| 模型 | 大小 | safetensors 文件数 | 状态 |
|------|------|-------------------|------|
| Qwen2.5-14B-Instruct | 28G | 8 | **已完成** |
| Qwen3-14B | 28G | 8 | **已完成** |
| Mistral-7B-Instruct-v0.3 | 6.6G | 3 | **下载中** (3个 wget 进程仍在运行) |

Mistral 模型 3 个 safetensors 分片正在并行下载，当前 6.6G（完整约 ~15G），预计还需一段时间。

### 3. Python 环境
**全部缺失。** vllm、z3、transformers、torch 均未安装。需要搭建完整环境。

### 4. GPU 信息
**4 × NVIDIA RTX PRO 6000 Blackwell Server Edition**，每卡 ~96GB 显存，共 ~384GB。非常强大的配置。

### 5. 代码和数据
- **代码**: `/root/autodl-tmp/sica_project/` 已到位，包含 `symb_invariant_consensus/` 目录
- **数据**: 已到位，包含 `folio_full.json`、`proofwriter_full.json`、`case_study_3problems.json` 等

### 6. 磁盘
350G 总量，已用 62G，剩余 289G (18%)，空间充足。

---
