"""Patch eval_smolvla_pruning_official.py to add attention-based pruning."""
import math

filepath = '/root/autodl-tmp/importance_margin_vla_compress/eval_smolvla_pruning_official.py'
with open(filepath, 'r') as f:
    content = f.read()

# 1. Add "attention_prune" to mode choices
content = content.replace(
    'choices=["baseline", "l2norm_prune", "random_prune"]',
    'choices=["baseline", "l2norm_prune", "random_prune", "attention_prune"]'
)

# 2. Add register_attention_prune_hook function after register_random_prune_hook
ATTN_HOOK_FN = '''

def register_attention_prune_hook(connector, policy, k_ratio, method="true_removal"):
    """Attention-based pruning: 2-layer self-attention probe among vision tokens."""
    import math
    call_count = [0]

    def hook_fn(module, input, output):
        import torch.nn.functional as F

        tokens = output[0] if isinstance(output, tuple) else output
        if tokens.dim() != 3:
            return output
        B, N, D = tokens.shape
        k = max(1, int(N * k_ratio))
        if k >= N:
            return output

        vlm = policy.model.vlm_with_expert.vlm.model
        lm = vlm.text_model
        position_ids = torch.arange(N, device=tokens.device).unsqueeze(0).expand(B, -1)

        hidden = tokens
        all_attn = []

        with torch.no_grad():
            for layer_idx in range(min(2, len(lm.layers))):
                layer = lm.layers[layer_idx]
                normed = layer.input_layernorm(hidden)

                head_dim = layer.self_attn.head_dim
                q = layer.self_attn.q_proj(normed)
                k_proj = layer.self_attn.k_proj(normed)
                v = layer.self_attn.v_proj(normed)

                n_q_heads = q.shape[-1] // head_dim
                n_kv_heads = k_proj.shape[-1] // head_dim

                q = q.view(B, N, n_q_heads, head_dim).transpose(1, 2)
                k_proj = k_proj.view(B, N, n_kv_heads, head_dim).transpose(1, 2)
                v = v.view(B, N, n_kv_heads, head_dim).transpose(1, 2)

                cos, sin = lm.rotary_emb(v, position_ids)
                from transformers.models.llama.modeling_llama import rotate_half
                q_embed = (q * cos) + (rotate_half(q) * sin)
                k_embed = (k_proj * cos) + (rotate_half(k_proj) * sin)

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

        _, topk_idx = torch.topk(importance, k, dim=-1)
        topk_idx_sorted = topk_idx.sort(dim=-1).values

        if call_count[0] < 2:
            log.info("Attention hook: N=%d, k=%d (keep %.1f%%), method=%s, "
                     "importance_range=[%.4f, %.4f]",
                     N, k, k_ratio * 100, method,
                     importance.min().item(), importance.max().item())
        call_count[0] += 1

        if method == "true_removal":
            pruned = torch.gather(tokens, 1, topk_idx_sorted.unsqueeze(-1).expand(-1, -1, D))
        else:
            mask = torch.zeros(B, N, dtype=torch.bool, device=tokens.device)
            mask.scatter_(1, topk_idx_sorted, True)
            pruned = tokens.clone()
            pruned[~mask] = 0

        if isinstance(output, tuple):
            return (pruned,) + output[1:]
        return pruned

    return connector.register_forward_hook(hook_fn)

'''

# Insert after register_random_prune_hook function
# Find the end of register_random_prune_hook by locating its return statement
content = content.replace(
    '    return connector.register_forward_hook(hook_fn)\n\n\ndef find_connector',
    '    return connector.register_forward_hook(hook_fn)\n' + ATTN_HOOK_FN + '\ndef find_connector',
    1  # only replace first occurrence (the random_prune one is second)
)

# If the above didn't work (because there are two such return statements), try a different approach
if 'register_attention_prune_hook' not in content:
    # Find the second occurrence of the return statement (end of random_prune hook)
    idx1 = content.find('    return connector.register_forward_hook(hook_fn)')
    if idx1 >= 0:
        idx2 = content.find('    return connector.register_forward_hook(hook_fn)', idx1 + 1)
        if idx2 >= 0:
            insert_pos = content.find('\n', idx2) + 1
            content = content[:insert_pos] + ATTN_HOOK_FN + content[insert_pos:]

# 3. Add attention_prune handling in the eval loop
content = content.replace(
    '''                    elif args.mode == "random_prune":
                        hook = register_random_prune_hook(connector, args.k_ratio, args.pruning_method)
                        action_chunk = predict_actions(policy, batch)
                        hook.remove()''',
    '''                    elif args.mode == "random_prune":
                        hook = register_random_prune_hook(connector, args.k_ratio, args.pruning_method)
                        action_chunk = predict_actions(policy, batch)
                        hook.remove()
                    elif args.mode == "attention_prune":
                        hook = register_attention_prune_hook(connector, policy, args.k_ratio, args.pruning_method)
                        action_chunk = predict_actions(policy, batch)
                        hook.remove()'''
)

# 4. Update result summary to handle attention_prune
content = content.replace(
    '    if args.mode != "baseline":',
    '    if args.mode not in ("baseline",):'
)

# 5. Update pruning_method in summary
content = content.replace(
    '"pruning_method": args.pruning_method if args.mode != "baseline" else "none"',
    '"pruning_method": args.pruning_method if args.mode != "baseline" else "none"'
)

# 6. Update k_ratio in summary
content = content.replace(
    '"k_ratio": args.k_ratio if args.mode != "baseline" else None',
    '"k_ratio": args.k_ratio if args.mode != "baseline" else None'
)

with open(filepath, 'w') as f:
    f.write(content)

print("OK: patched eval_smolvla_pruning_official.py")
