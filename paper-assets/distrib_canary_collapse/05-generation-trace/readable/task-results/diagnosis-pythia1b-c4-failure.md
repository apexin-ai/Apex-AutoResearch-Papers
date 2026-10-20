# diagnosis pythia1b c4 failure

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_pythia1b_c4_failure_20260517T123326_result.json`
- **Structured JSON:** [`35ba2879a72734451b17.json`](../../sessions/35/35ba2879a72734451b17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

**失败根因**：下载 Pythia-1B 模型时网络连接中断。

EXIT_CODE 内容：
```
1
('Connection broken: IncompleteRead(145523872 bytes read, 1945177656 more expected)', IncompleteRead(...))
```

即下载了 ~138MB 后断开，还有 ~1.85GB 未完成。这是 HuggingFace Hub 下载 `EleutherAI/pythia-1b` 权重文件时的网络超时/断连错误。

**已完成进度**：零。实验目录下只有 `config.json` 和 `EXIT_CODE`，没有任何 generation 数据产出。模型下载失败在第一步就中止了。

**C4 数据状态**：`data/c4_5k/` 完整存在（14MB，train/eval/prompts 三个 split 齐全），数据不是问题。

**修复建议**：
1. 先手动确认 HF 模型缓存中是否有部分下载残留：`ls ~/.cache/huggingface/hub/models--EleutherAI--pythia-1b/`
2. 直接重跑即可，无需改代码。如果服务器到 HF Hub 的连接不稳定，可以：
   - 设置 `HF_HUB_DOWNLOAD_TIMEOUT=600` 环境变量增加超时
   - 或用 `huggingface-cli download EleutherAI/pythia-1b --resume-download` 预先下载模型到缓存，然后再启动实验

---
