"""Full bit-width PPL profiler for quant-only MCKP.
Profiles each KV head at {2, 4, 8, 16}-bit quantization.
"""

import json
import math
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer
from eval_ppl import patch_attention, restore_attention


class FullBitwidthProfiler:
    def __init__(self, model_path, calibration_data, device='cuda:0',
                 num_samples=16, seq_len=512):
        self.device = device
        self.seq_len = seq_len
        self.num_samples = num_samples

        print(f"Loading model {model_path}...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path, torch_dtype=torch.bfloat16, attn_implementation="eager"
        )
        self.model = self.model.to(device)
        self.model.eval()

        config = self.model.config
        self.num_layers = config.num_hidden_layers
        self.num_kv_heads = config.num_key_value_heads

        self.input_ids = self._load_calibration_data(calibration_data)
        total_heads = self.num_layers * self.num_kv_heads
        print(f"Config: {self.num_layers} layers, {self.num_kv_heads} KV heads/layer, "
              f"{total_heads} heads total")
        print(f"Calibration: {self.input_ids.shape[0]} seqs x {self.input_ids.shape[1]} tokens")

        self._baseline_ppl = None

    def _load_calibration_data(self, path):
        with open(path) as f:
            samples = json.load(f)
        all_ids = []
        for s in samples:
            tokens = self.tokenizer.encode(s["text"], add_special_tokens=False)
            if len(tokens) >= self.seq_len:
                all_ids.append(tokens[:self.seq_len])
            if len(all_ids) >= self.num_samples:
                break
        if not all_ids:
            raise RuntimeError(f"No calibration seqs with >= {self.seq_len} tokens")
        return torch.tensor(all_ids, dtype=torch.long, device=self.device)

    def _compute_ppl(self):
        with torch.no_grad():
            outputs = self.model(
                self.input_ids, use_cache=False,
                cache_position=torch.arange(self.seq_len, device=self.device)
            )
        shift_logits = outputs.logits[:, :-1].contiguous()
        shift_labels = self.input_ids[:, 1:].contiguous()
        loss = F.cross_entropy(
            shift_logits.float().view(-1, shift_logits.shape[-1]),
            shift_labels.view(-1),
            reduction="sum"
        )
        total_tokens = shift_labels.numel()
        return math.exp(loss.item() / total_tokens)

    def compute_baseline_ppl(self):
        if self._baseline_ppl is None:
            print("Computing baseline PPL...")
            self._baseline_ppl = self._compute_ppl()
            print(f"Baseline PPL: {self._baseline_ppl:.4f}")
        return self._baseline_ppl

    def profile_single_head(self, layer, head, bits):
        _ = self.compute_baseline_ppl()
        if bits >= 16:
            return 0.0
        allocations = {f"{layer},{head}": ["quant", bits]}
        orig_fwds = patch_attention(self.model, allocations)
        ppl = self._compute_ppl()
        restore_attention(self.model, orig_fwds)
        return ppl - self._baseline_ppl

    def profile_all(self, bit_widths=(2, 4, 8)):
        _ = self.compute_baseline_ppl()
        total_heads = self.num_layers * self.num_kv_heads
        total_evals = total_heads * len(bit_widths)
        done = 0

        profiles = {}
        for l in range(self.num_layers):
            profiles[str(l)] = {}
            for h in range(self.num_kv_heads):
                head_profile = {"quantization": {}}
                for bits in bit_widths:
                    delta = self.profile_single_head(l, h, bits)
                    head_profile["quantization"][str(bits)] = delta
                    done += 1
                    print(f"[{done}/{total_evals}] L{l}H{h} @{bits}bit: delta={delta:.6f}")
                profiles[str(l)][str(h)] = head_profile

        return profiles
