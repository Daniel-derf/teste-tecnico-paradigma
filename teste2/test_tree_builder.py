"""
Testes unitários para o algoritmo de construção de árvore
"""
import pytest
from tree_builder import build_tree_from_array, Tree, Node


class TestTreeBuilder:
    """Testes para a construção da árvore"""
    
    def test_cenario_1(self):
        """Testa o cenário 1 fornecido no desafio"""
        arr = [3, 2, 1, 6, 0, 5]
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 6
        
        assert tree.root.left.value == 3
        assert tree.root.left.left is None
        assert tree.root.left.right.value == 2
        assert tree.root.left.right.right.value == 1
        
        assert tree.root.right.value == 5
        assert tree.root.right.left.value == 0
        assert tree.root.right.right is None
        
        assert tree.preorder() == [6, 3, 2, 1, 5, 0]
        assert tree.inorder() == [3, 2, 1, 6, 0, 5]
    
    def test_cenario_2(self):
        """Testa o cenário 2 fornecido no desafio"""
        arr = [7, 5, 13, 9, 1, 6, 4]
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 13
        
        assert tree.root.left.value == 7
        assert tree.root.left.right.value == 5
        
        assert tree.root.right.value == 9
        assert tree.root.right.right.value == 6
        assert tree.root.right.right.left.value == 1
        assert tree.root.right.right.right.value == 4
        
        assert tree.preorder() == [13, 7, 5, 9, 6, 1, 4]
        assert tree.inorder() == [7, 5, 13, 9, 1, 6, 4]
    
    def test_array_com_um_elemento(self):
        """Testa array com apenas um elemento"""
        arr = [42]
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 42
        assert tree.root.left is None
        assert tree.root.right is None
        assert tree.preorder() == [42]
        assert tree.inorder() == [42]
    
    def test_array_com_dois_elementos(self):
        """Testa array com dois elementos"""
        arr = [5, 10]
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 10
        assert tree.root.left.value == 5
        assert tree.root.right is None
        assert tree.preorder() == [10, 5]
        assert tree.inorder() == [5, 10]
    
    def test_maior_elemento_no_inicio(self):
        """Testa quando o maior elemento está no início"""
        arr = [100, 50, 25, 75]
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 100
        assert tree.root.left is None
        assert tree.root.right.value == 75
        assert tree.preorder() == [100, 75, 50, 25]
    
    def test_maior_elemento_no_fim(self):
        """Testa quando o maior elemento está no final"""
        arr = [25, 50, 75, 100]
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 100
        assert tree.root.left.value == 75
        assert tree.root.right is None
        assert tree.preorder() == [100, 75, 50, 25]
    
    def test_maior_elemento_no_meio(self):
        """Testa quando o maior elemento está no meio"""
        arr = [30, 20, 100, 40, 50]
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 100
        assert tree.root.left.value == 30
        assert tree.root.left.right.value == 20
        assert tree.root.right.value == 50
        assert tree.root.right.left.value == 40
    
    def test_valores_negativos(self):
        """Testa array com valores negativos"""
        arr = [-5, -1, 3, -10, 0]
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 3
        assert tree.root.left.value == -1
        assert tree.root.left.left.value == -5
        assert tree.root.right.value == 0
        assert tree.root.right.left.value == -10
    
    def test_array_ordenado_crescente(self):
        """Testa array já ordenado crescente"""
        arr = [1, 2, 3, 4, 5]
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 5
        assert tree.root.right is None
        assert tree.preorder() == [5, 4, 3, 2, 1]
    
    def test_array_ordenado_decrescente(self):
        """Testa array ordenado decrescente"""
        arr = [5, 4, 3, 2, 1]
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 5
        assert tree.root.left is None
        assert tree.preorder() == [5, 4, 3, 2, 1]
    
    def test_array_intercalado(self):
        """Testa array com valores intercalados"""
        arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 10
        assert tree.inorder() == arr  
    
    def test_array_com_zero(self):
        """Testa array que contém zero"""
        arr = [5, 0, 10, -5, 3]
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 10
        assert 0 in tree.inorder()
    
    def test_array_grande(self):
        """Testa array com muitos elementos"""
        arr = list(range(1, 21))  
        tree = build_tree_from_array(arr)
        
        assert tree.root.value == 20
        assert tree.inorder() == arr
        assert len(tree.preorder()) == 20


class TestTreeValidation:
    """Testes de validação de entrada"""
    
    def test_array_vazio_levanta_erro(self):
        """Testa que array vazio levanta ValueError"""
        with pytest.raises(ValueError, match="Array não pode estar vazio"):
            build_tree_from_array([])
    
    def test_array_com_duplicatas_levanta_erro(self):
        """Testa que array com duplicatas levanta ValueError"""
        arr = [1, 2, 3, 2, 4]
        with pytest.raises(ValueError, match="Array não pode conter duplicatas"):
            build_tree_from_array(arr)
    
    def test_array_todas_duplicatas(self):
        """Testa array com todos elementos iguais"""
        arr = [5, 5, 5, 5]
        with pytest.raises(ValueError, match="Array não pode conter duplicatas"):
            build_tree_from_array(arr)


class TestTreeStructure:
    """Testes da estrutura interna da árvore"""
    
    def test_node_criacao(self):
        """Testa criação de um nó"""
        node = Node(42)
        assert node.value == 42
        assert node.left is None
        assert node.right is None
    
    def test_tree_get_structure(self):
        """Testa a representação em dicionário da árvore"""
        arr = [1, 3, 2]
        tree = build_tree_from_array(arr)
        
        structure = tree.get_structure()
        assert structure['value'] == 3
        assert structure['left']['value'] == 1
        assert structure['right']['value'] == 2
    
    def test_percurso_inorder_retorna_array_original(self):
        """Testa que in-ordem sempre retorna o array original"""
        test_arrays = [
            [3, 2, 1, 6, 0, 5],
            [7, 5, 13, 9, 1, 6, 4],
            [1, 2, 3, 4, 5],
            [10, 5, 15, 3, 7, 12, 20]
        ]
        
        for arr in test_arrays:
            tree = build_tree_from_array(arr)
            assert tree.inorder() == arr, f"Falhou para array: {arr}"
    
    def test_raiz_sempre_maior_valor(self):
        """Testa que a raiz é sempre o maior valor"""
        test_arrays = [
            [3, 2, 1, 6, 0, 5],
            [7, 5, 13, 9, 1, 6, 4],
            [-10, -5, -20, -1],
            [100],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ]
        
        for arr in test_arrays:
            tree = build_tree_from_array(arr)
            assert tree.root.value == max(arr), f"Falhou para array: {arr}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
