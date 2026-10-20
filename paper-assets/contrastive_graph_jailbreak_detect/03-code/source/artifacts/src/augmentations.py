import torch
from torch_geometric.data import Data


def dropout_edge(data: Data, p: float = 0.2) -> Data:
    edge_index = data.edge_index
    num_edges = edge_index.size(1)
    mask = torch.rand(num_edges) >= p
    new_edge_index = edge_index[:, mask]

    new_data = Data(x=data.x.clone(), edge_index=new_edge_index, batch=data.batch)
    if hasattr(data, 'y'):
        new_data.y = data.y
    return new_data


def drop_feature(data: Data, p: float = 0.2) -> Data:
    x = data.x.clone()
    feat_dim = x.size(1)
    mask = torch.rand(feat_dim) >= p
    x[:, ~mask] = 0.0

    new_data = Data(x=x, edge_index=data.edge_index.clone(), batch=data.batch)
    if hasattr(data, 'y'):
        new_data.y = data.y
    return new_data


def subgraph(data: Data, ratio: float = 0.8) -> Data:
    num_nodes = data.x.size(0)
    num_keep = max(1, int(num_nodes * ratio))

    perm = torch.randperm(num_nodes)[:num_keep]
    perm, _ = perm.sort()

    # Build node mapping
    node_map = torch.full((num_nodes,), -1, dtype=torch.long)
    node_map[perm] = torch.arange(num_keep)

    # Filter edges
    edge_index = data.edge_index
    mask = node_map[edge_index[0]] >= 0
    mask &= node_map[edge_index[1]] >= 0
    new_edge_index = node_map[edge_index[:, mask]]

    new_x = data.x[perm]

    # Remap batch
    new_batch = data.batch[perm] if data.batch is not None else None

    new_data = Data(x=new_x, edge_index=new_edge_index, batch=new_batch)
    if hasattr(data, 'y'):
        new_data.y = data.y
    return new_data


_AUG_FNS = {
    "dropout_edge": dropout_edge,
    "drop_feature": drop_feature,
    "subgraph": subgraph,
}


def augment_graph(data: Data, aug_type: str = "dropout_edge", **kwargs) -> Data:
    fn = _AUG_FNS[aug_type]
    return fn(data, **kwargs)


def dual_augment(data: Data, aug1: str = "dropout_edge", aug2: str = "drop_feature") -> tuple[Data, Data]:
    view1 = augment_graph(data, aug1)
    view2 = augment_graph(data, aug2)
    return view1, view2
