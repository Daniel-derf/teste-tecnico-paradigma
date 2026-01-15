"""
Algoritmo para construir árvore binária com regras específicas:
- Raiz: maior valor do array
- Esquerda: valores à esquerda da raiz, ordem decrescente
- Direita: valores à direita da raiz, ordem decrescente
"""

class Node:
    """Representa um nó da árvore"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    """Árvore binária com regras customizadas"""
    def __init__(self, arr):
        self.root = self._build_tree(arr)
    
    def _build_tree(self, arr):
        """Constrói a árvore recursivamente seguindo as regras"""
        if not arr:
            return None
        
        max_value = max(arr)
        max_index = arr.index(max_value)
        
        root = Node(max_value)
        
        left_arr = arr[:max_index]
        right_arr = arr[max_index + 1:]
        
        root.left = self._build_tree(left_arr)
        root.right = self._build_tree(right_arr)
        
        return root
    
    def print_tree(self, node=None, prefix="", is_tail=True):
        """Imprime a árvore de forma visual"""
        if node is None:
            node = self.root
        
        if node is None:
            return
        
        print(prefix + ("└── " if is_tail else "├── ") + str(node.value))
        
        children = []
        if node.left:
            children.append((node.left, False))
        if node.right:
            children.append((node.right, True))
        
        for i, (child, is_last) in enumerate(children):
            extension = "    " if is_tail else "│   "
            self.print_tree(child, prefix + extension, is_last and i == len(children) - 1)
    
    def get_structure(self):
        """Retorna estrutura da árvore como dicionário"""
        def _to_dict(node):
            if node is None:
                return None
            return {
                'value': node.value,
                'left': _to_dict(node.left),
                'right': _to_dict(node.right)
            }
        return _to_dict(self.root)
    
    def inorder(self, node=None, first_call=True):
        """Percurso em ordem (esquerda, raiz, direita)"""
        if first_call:
            node = self.root
        
        if node is None:
            return []
        
        result = []
        result.extend(self.inorder(node.left, False))
        result.append(node.value)
        result.extend(self.inorder(node.right, False))
        return result
    
    def preorder(self, node=None, first_call=True):
        """Percurso pré-ordem (raiz, esquerda, direita)"""
        if first_call:
            node = self.root
        
        if node is None:
            return []
        
        result = []
        result.append(node.value)
        result.extend(self.preorder(node.left, False))
        result.extend(self.preorder(node.right, False))
        return result


def build_tree_from_array(arr):
    """
    Função principal para construir a árvore a partir de um array
    
    Args:
        arr: Lista de inteiros únicos
    
    Returns:
        Tree: Objeto árvore construído
    """
    if not arr:
        raise ValueError("Array não pode estar vazio")
    
    if len(arr) != len(set(arr)):
        raise ValueError("Array não pode conter duplicatas")
    
    return Tree(arr)
