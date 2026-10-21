"""
BN Stats Recalculation Experiment (MF2)
For each conv layer in R50: swap weights Muon->AdamW, recalculate BN running stats
using 10k train samples, then evaluate val accuracy.
"""
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torchvision.models import resnet50
import numpy as np
from scipy import stats
import json
import copy
import argparse

def get_cifar100_loaders(data_dir, batch_size=50):
    transform_train = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.5071, 0.4867, 0.4408), (0.2675, 0.2565, 0.2761)),
    ])
    transform_val = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5071, 0.4867, 0.4408), (0.2675, 0.2565, 0.2761)),
    ])
    train_set = torchvision.datasets.CIFAR100(root=data_dir, train=True, download=True, transform=transform_train)
    val_set = torchvision.datasets.CIFAR100(root=data_dir, train=False, download=True, transform=transform_val)
    train_subset = torch.utils.data.Subset(train_set, range(10000))
    train_loader = torch.utils.data.DataLoader(train_subset, batch_size=batch_size, shuffle=False, num_workers=4)
    val_loader = torch.utils.data.DataLoader(val_set, batch_size=100, shuffle=False, num_workers=4)
    return train_loader, val_loader

@torch.no_grad()
def evaluate(model, val_loader, device):
    model.eval()
    correct = 0
    total = 0
    for images, labels in val_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = outputs.max(1)
        correct += predicted.eq(labels).sum().item()
        total += labels.size(0)
    return 100.0 * correct / total

def recalc_bn_stats(model, train_loader, device):
    """Forward pass train subset to recalculate BN running stats."""
    model.train()
    with torch.no_grad():
        for images, _ in train_loader:
            images = images.to(device)
            model(images)
    model.eval()

def get_conv_layers(model):
    """Get all conv layer names (weight-swappable layers)."""
    layers = []
    for name, module in model.named_modules():
        if isinstance(module, (nn.Conv2d, nn.Linear)):
            layers.append(name)
    return layers

def get_module_by_name(model, name):
    parts = name.split('.')
    module = model
    for part in parts:
        module = getattr(module, part)
    return module

def compute_stable_rank(weight):
    """Stable rank = ||W||_F^2 / ||W||_2^2"""
    w = weight.float().view(weight.size(0), -1)
    fro_sq = torch.sum(w ** 2).item()
    spectral_sq = torch.linalg.norm(w, ord=2).item() ** 2
    return fro_sq / spectral_sq if spectral_sq > 0 else 0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--muon-ckpt', required=True)
    parser.add_argument('--adamw-ckpt', required=True)
    parser.add_argument('--data-dir', default='/root/spectral_optim_vision_geometry/data/')
    parser.add_argument('--gpu', type=int, default=0)
    parser.add_argument('--output', default='bn_stats_recalc_results.json')
    args = parser.parse_args()

    device = torch.device(f'cuda:{args.gpu}')
    
    train_loader, val_loader = get_cifar100_loaders(args.data_dir)
    
    muon_state = torch.load(args.muon_ckpt, map_location='cpu', weights_only=False)
    adamw_state = torch.load(args.adamw_ckpt, map_location='cpu', weights_only=False)
    
    if 'model_state_dict' in muon_state:
        muon_state = muon_state['model_state_dict']
    elif 'state_dict' in muon_state:
        muon_state = muon_state['state_dict']
    if 'model_state_dict' in adamw_state:
        adamw_state = adamw_state['model_state_dict']
    elif 'state_dict' in adamw_state:
        adamw_state = adamw_state['state_dict']
    
    model = resnet50(num_classes=100).to(device)
    model.load_state_dict(muon_state)
    baseline_acc = evaluate(model, val_loader, device)
    print(f"Muon baseline accuracy: {baseline_acc:.2f}%")
    
    conv_layers = get_conv_layers(model)
    print(f"Found {len(conv_layers)} layers to test")
    
    results = []
    
    for i, layer_name in enumerate(conv_layers):
        model.load_state_dict(muon_state)
        
        module = get_module_by_name(model, layer_name)
        weight_key = f"{layer_name}.weight"
        bias_key = f"{layer_name}.bias"
        
        if weight_key not in adamw_state:
            print(f"  [{i+1}/{len(conv_layers)}] {layer_name}: not in AdamW checkpoint, skipping")
            continue
        
        sr_muon = compute_stable_rank(module.weight.data)
        sr_adamw = compute_stable_rank(adamw_state[weight_key])
        sr_divergence = (sr_muon - sr_adamw) / sr_adamw if sr_adamw > 0 else 0
        
        module.weight.data = adamw_state[weight_key].to(device)
        if bias_key in adamw_state and module.bias is not None:
            module.bias.data = adamw_state[bias_key].to(device)
        
        recalc_bn_stats(model, train_loader, device)
        
        corrected_acc = evaluate(model, val_loader, device)
        acc_change = corrected_acc - baseline_acc
        
        print(f"  [{i+1}/{len(conv_layers)}] {layer_name}: SR_div={sr_divergence:.4f}, "
              f"corrected_acc={corrected_acc:.2f}%, delta={acc_change:+.2f}%")
        
        results.append({
            'layer_name': layer_name,
            'stable_rank_muon': sr_muon,
            'stable_rank_adamw': sr_adamw,
            'stable_rank_divergence': sr_divergence,
            'corrected_acc': corrected_acc,
            'acc_change': acc_change,
        })
    
    acc_changes = [r['acc_change'] for r in results]
    sr_divs = [r['stable_rank_divergence'] for r in results]
    
    beneficial_count = sum(1 for a in acc_changes if a >= 0)
    beneficial_ratio = beneficial_count / len(acc_changes)
    
    spearman_rho, spearman_p = stats.spearmanr(sr_divs, acc_changes)
    
    summary = {
        'baseline_acc': baseline_acc,
        'n_layers': len(results),
        'corrected_beneficial_ratio': beneficial_ratio,
        'corrected_spearman_rho': spearman_rho,
        'corrected_spearman_p': spearman_p,
        'original_spearman_rho': 0.45,
        'per_layer': results,
    }
    
    with open(args.output, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\n=== SUMMARY ===")
    print(f"Baseline accuracy: {baseline_acc:.2f}%")
    print(f"Layers tested: {len(results)}")
    print(f"Corrected beneficial ratio: {beneficial_ratio:.3f} ({beneficial_count}/{len(results)})")
    print(f"Corrected Spearman rho: {spearman_rho:.4f} (p={spearman_p:.4f})")
    print(f"Original Spearman rho: 0.45")
    print(f"Results saved to {args.output}")

if __name__ == '__main__':
    main()
