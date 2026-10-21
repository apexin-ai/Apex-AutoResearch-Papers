# exp-012 候选模型调研

## 硬件约束
- 1× RTX PRO 6000 Blackwell, 98GB VRAM
- 当前部署: Qwen3-32B-FP8 (~35GB)
- vLLM 0.20.2

---

## 候选评估

| 模型 | 总参数 | FP8 VRAM (weights) | 单卡可行? | vLLM 支持 | Guided JSON | HuggingFace ID |
|------|--------|-------------------|-----------|-----------|-------------|----------------|
| LLaMA-3.3-70B-Instruct | 70B | ~70GB | ✅ (需独占) | ✅ 原生 | ✅ | `nvidia/Llama-3.3-70B-Instruct-FP8` |
| LLaMA-3.1-70B-Instruct | 70B | ~70GB | ✅ (需独占) | ✅ 原生 | ✅ | `nvidia/Llama-3.1-70B-Instruct-FP8` |
| Gemma-2-27B-IT | 27B | ~27GB | ✅ 可并行 | ✅ | ✅ | `google/gemma-2-27b-it` (FP8: `RedHatAI/gemma-2-27b-it-FP8-dynamic`) |
| Phi-4 | 14B | ~14GB | ✅ 可并行 | ✅ | ✅ | `microsoft/phi-4` |
| Mistral-Large-2 | 123B | ~130GB | ❌ 超出 | — | — | — |
| DeepSeek-V3-0324 | 671B MoE | ~690GB | ❌ 超出 | — | — | — |
| DeepSeek-V2-Lite | 15.7B MoE (2.4B active) | ~16GB | ✅ | ⚠️ 需验证 | ⚠️ 不确定 | `deepseek-ai/DeepSeek-V2-Lite-Chat` |

### 排除
- **Mistral-Large-2 (123B)**: FP8 ~130GB，单卡放不下
- **DeepSeek-V3**: 671B MoE，最少需要 8×H100
- **DeepSeek-V2-Lite**: MoE 架构在 vLLM guided decoding 下兼容性不确定，且仅 2.4B active params，NER 指令跟随能力存疑

---

## 推荐 Top-2

### 🥇 LLaMA-3.3-70B-Instruct-FP8

**理由**:
1. **不同 family**: Meta LLaMA vs Alibaba Qwen，论文说服力最强
2. **能力对等**: 70B FP8 与 Qwen3-32B 在 NER 任务上能力可比，不会引发 reviewer 对"模型太小不公平"的质疑
3. **vLLM 成熟**: Llama 架构是 vLLM 最早、最稳定支持的架构，guided decoding 零问题
4. **现成 FP8**: NVIDIA 官方量化版 `nvidia/Llama-3.3-70B-Instruct-FP8`，无需自行量化
5. **VRAM**: ~70GB weights + KV cache，98GB 单卡可跑（需停掉 Qwen3，设 `--max-model-len 8192 --gpu-memory-utilization 0.95`）

**风险**: 需要独占 GPU，不能与 Qwen3 同时运行。实验需串行。

### 🥈 Phi-4 (14B)

**理由**:
1. **不同 family**: Microsoft Phi vs Alibaba Qwen
2. **VRAM 极小**: FP16 ~28GB，FP8 ~14GB，可与 Qwen3-32B 并行运行
3. **vLLM 原生支持**: 有官方 recipe，guided decoding 正常
4. **效率**: 小模型推理快，实验周转时间短
5. **论文角度**: 如果 type confusability 在 14B 小模型上也成立，反而增强论证——说明现象不依赖模型规模

**风险**: 14B vs 32B 规模差距大。如果 Phi-4 在 NER 上整体表现差，难区分"因为模型弱"还是"因为 type confusability"。

---

## 部署方案

### LLaMA-3.3-70B-Instruct-FP8
```bash
# 停掉 Qwen3 后启动
python -m vllm.entrypoints.openai.api_server \
  --model nvidia/Llama-3.3-70B-Instruct-FP8 \
  --max-model-len 8192 \
  --gpu-memory-utilization 0.95 \
  --port 8001
```

### Phi-4
```bash
# 可与 Qwen3 并行，用不同端口
python -m vllm.entrypoints.openai.api_server \
  --model microsoft/phi-4 \
  --max-model-len 8192 \
  --port 8002
```

---

## 建议策略

优先跑 **LLaMA-3.3-70B** 作为论文主力第二模型（能力对等，说服力强）。如果时间允许，再补 **Phi-4** 作为第三模型（验证规模无关性）。三个模型 × 三个 family（Qwen/LLaMA/Phi）是很强的 multi-model evidence。
