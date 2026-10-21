"""Patch eval_openvla_l2norm_libero.py to add attention-based pruning."""
import math

filepath = '/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py'
with open(filepath, 'r') as f:
    content = f.read()

# 1. Add "attention_prune" to mode choices
content = content.replace(
    'choices=["baseline", "random_prune", "l2norm_prune"]',
    'choices=["baseline", "random_prune", "l2norm_prune", "attention_prune"]'
)

# 2. Add math import if not present
if 'import math' not in content.split('\n')[1]:  # check it's not already in the multi-import line
    content = content.replace(
        'import argparse, io, json, math, os, sys, time',
        'import argparse, io, json, math, os, sys, time'
    )

# 3. Add AttentionPruningHook class after L2NormPruningHook
ATTN_HOOK_CLASS = '''

class AttentionPruningHook:
    """Keep top-k vision tokens ranked by attention importance.

    Runs a 2-layer probe through the LLM backbone using only the vision
    token embeddings (self-attention). Tokens that receive more total
    attention from other vision tokens are considered more important.
    """
    def __init__(self, k_ratio, vla):
        self.k_ratio = k_ratio
        self.vla = vla
        self.logged = False

    def __call__(self, module, input, output):
        import torch.nn.functional as F

        B, N, D = output.shape
        keep = max(1, int(N * self.k_ratio))
        if keep >= N:
            return output

        lm = self.vla.language_model.model
        position_ids = torch.arange(N, device=output.device).unsqueeze(0).expand(B, -1)

        hidden = output
        all_attn = []

        with torch.no_grad():
            for layer_idx in range(min(2, len(lm.layers))):
                layer = lm.layers[layer_idx]
                normed = layer.input_layernorm(hidden)

                head_dim = layer.self_attn.head_dim
                n_q_heads = layer.self_attn.num_heads
                n_kv_heads = layer.self_attn.num_key_value_heads

                q = layer.self_attn.q_proj(normed)
                k = layer.self_attn.k_proj(normed)
                v = layer.self_attn.v_proj(normed)

                q = q.view(B, N, n_q_heads, head_dim).transpose(1, 2)
                k = k.view(B, N, n_kv_heads, head_dim).transpose(1, 2)
                v = v.view(B, N, n_kv_heads, head_dim).transpose(1, 2)

                cos, sin = layer.self_attn.rotary_emb(v, position_ids)
                from transformers.models.llama.modeling_llama import rotate_half
                q_embed = (q * cos) + (rotate_half(q) * sin)
                k_embed = (k * cos) + (rotate_half(k) * sin)

                if n_kv_heads != n_q_heads:
                    n_rep = n_q_heads // n_kv_heads
                    k_embed = k_embed.repeat_interleave(n_rep, dim=1)
                    v = v.repeat_interleave(n_rep, dim=1)

                attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)
                attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)
                all_attn.append(attn_weights)

                attn_out = torch.matmul(attn_weights.to(v.dtype), v)
                attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)
                attn_out = layer.self_attn.o_proj(attn_out)
                hidden = hidden + attn_out

                normed2 = layer.post_attention_layernorm(hidden)
                mlp_out = layer.mlp(normed2)
                hidden = hidden + mlp_out

        avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)  # [B, N, N]
        importance = avg_attn.sum(dim=1)  # [B, N]

        _, indices = torch.topk(importance, keep, dim=-1)
        indices = indices.sort(dim=-1).values
        pruned = torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))

        if not self.logged:
            print(f"[Attn Pruning] {N} -> {keep} vision tokens (k={self.k_ratio}), "
                  f"importance range=[{importance.min():.4f}, {importance.max():.4f}]",
                  flush=True)
            self.logged = True

        return pruned

'''

# Insert after L2NormPruningHook class
content = content.replace(
    '\ndef count_vision_tokens',
    ATTN_HOOK_CLASS + '\ndef count_vision_tokens'
)

# 4. Add attention_prune hook registration in main()
content = content.replace(
    '''    elif args.mode == "l2norm_prune":
        hook_handle = vla.projector.register_forward_hook(L2NormPruningHook(args.k_ratio))
        print(f"[*] L2 norm pruning: k={args.k_ratio}", flush=True)''',
    '''    elif args.mode == "l2norm_prune":
        hook_handle = vla.projector.register_forward_hook(L2NormPruningHook(args.k_ratio))
        print(f"[*] L2 norm pruning: k={args.k_ratio}", flush=True)
    elif args.mode == "attention_prune":
        hook_handle = vla.projector.register_forward_hook(AttentionPruningHook(args.k_ratio, vla))
        print(f"[*] Attention pruning: k={args.k_ratio}", flush=True)'''
)

# 5. Update result filename to handle attention_prune
content = content.replace(
    '''        elif args.mode == "random_prune":
            k_str = str(args.k_ratio).replace(".", "")
            out_path = f"{out_dir}/openvla_random_prune_k{k_str}_{suite_short}_seed{args.seed}.json"
        else:
            k_str = str(args.k_ratio).replace(".", "")
            out_path = f"{out_dir}/openvla_l2norm_prune_k{k_str}_{suite_short}_seed{args.seed}.json"''',
    '''        elif args.mode == "random_prune":
            k_str = str(args.k_ratio).replace(".", "")
            out_path = f"{out_dir}/openvla_random_prune_k{k_str}_{suite_short}_seed{args.seed}.json"
        elif args.mode == "attention_prune":
            k_str = str(args.k_ratio).replace(".", "")
            out_path = f"{out_dir}/openvla_attention_prune_k{k_str}_{suite_short}_seed{args.seed}.json"
        else:
            k_str = str(args.k_ratio).replace(".", "")
            out_path = f"{out_dir}/openvla_l2norm_prune_k{k_str}_{suite_short}_seed{args.seed}.json"'''
)

# 6. Update k_ratio inclusion in results dict
content = content.replace(
    '"k_ratio": args.k_ratio if args.mode in ("random_prune", "l2norm_prune") else None',
    '"k_ratio": args.k_ratio if args.mode in ("random_prune", "l2norm_prune", "attention_prune") else None'
)

with open(filepath, 'w') as f:
    f.write(content)

print("OK: patched eval_openvla_l2norm_libero.py")
