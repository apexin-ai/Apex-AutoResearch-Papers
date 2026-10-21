# infra recover and verify

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_recover_and_verify_20260516T211021_result.json`
- **Structured JSON:** [`a3eecbed696748a26a7b.json`](../../sessions/a3/a3eecbed696748a26a7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果已获取。汇总如下：

---

## Step 1: exp-015 FPR 分析 — 已完成 ✓

脚本因网络不通卡住，已 kill 并用离线模式重跑成功。结果：

| Method | Safe FPR | Pre-CP FPR | Precision | Coverage | Lead Time | Step Acc |
|--------|----------|-----------|-----------|----------|-----------|----------|
| text_static | 0.502 | 0.356 | 0.448 | 60.5% | +4.3 | 0.661 |
| text_temporal W=15 | 0.385 | 0.272 | 0.487 | 65.1% | +11.5 | 0.678 |
| HS_static LR L14 | 0.390 | 0.162 | 0.622 | 60.5% | +3.0 | 0.768 |
| HS_temporal LR W=15 | 0.392 | 0.160 | 0.583 | 65.1% | +4.9 | 0.726 |
| GRU multi-7L h=256 | 0.616 | 0.280 | 0.573 | 93.0% | +8.4 | 0.779 |

**关键发现**：text_temporal 的高 lead time (+11.5) 确实伴随高 FPR（Safe FPR=0.385, Pre-CP FPR=0.272）。HS 方法 Pre-CP FPR 仅 ~0.16，精度更高但 lead time 短。GRU 覆盖率最高(93%)但 Safe FPR 也最高(0.616)。

---

## Step 2: exp-014 BOCPD — 已完成 ✓

`bocpd_results.json` 存在（52KB），包含多条 trace 的完整结果。样例模式：
- BOCPD (lambda_10) 通常能检测到 changepoint，但 lead_time 普遍为负（检测晚于 commitment point）
- CUSUM 比 BOCPD 更晚检测到（或完全检测不到），尤其高阈值配置
- 两种方法在 trace 间表现差异大

---

## Step 3: 32B 下载验证 — 完成 ✓

| Model | Safetensors >1G | 预期 | config.json | 状态 |
|-------|----------------|------|-------------|------|
| DeepSeek-R1-Distill-Qwen-32B | 8 | 8 | ✓ | **完整** |
| QwQ-32B | 14 | 14 | ✓ | **完整** |

磁盘：
- deepseek-ai: 77G
- Qwen: 62G
- .hf_cache 总计: 139G
- /root/autodl-tmp: 142G used / 109G free (57%)

有一个 `._____temp` 空目录残留，无 `.incomplete` 文件。**两个 32B 模型下载完整，无中断。**

---

## Step 4: GPU 状态

| GPU | Memory Used | Memory Free |
|-----|------------|-------------|
| 0 | 3 MiB | 97250 MiB |
| 1 | 3 MiB | 97250 MiB |

无计算进程运行。两块 GPU 完全空闲（~97GB free each）。

---

## 网络状况

- huggingface.co: **不可达**
- hf-mirror.com: **可达**

后续需要网络访问 HF 的任务应设置 `HF_ENDPOINT=https://hf-mirror.com`，或使用离线模式。

---
