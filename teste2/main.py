"""
Teste dos cenários fornecidos para construção da árvore
"""
from tree_builder import build_tree_from_array


def main():
    print("=" * 60)
    print("CENÁRIO 1")
    print("=" * 60)
    arr1 = [3, 2, 1, 6, 0, 5]
    print(f"Array de entrada: {arr1}")
    
    tree1 = build_tree_from_array(arr1)
    print(f"\nRaiz: {tree1.root.value}")
    print(f"Galhos da esquerda: {arr1[:arr1.index(6)]}")
    print(f"Galhos da direita: {arr1[arr1.index(6)+1:]}")
    print("\nÁrvore construída:")
    tree1.print_tree()
    
    print("\n" + "=" * 60)
    print("CENÁRIO 2")
    print("=" * 60)
    arr2 = [7, 5, 13, 9, 1, 6, 4]
    print(f"Array de entrada: {arr2}")
    
    tree2 = build_tree_from_array(arr2)
    print(f"\nRaiz: {tree2.root.value}")
    print(f"Galhos da esquerda: {arr2[:arr2.index(13)]}")
    print(f"Galhos da direita: {arr2[arr2.index(13)+1:]}")
    print("\nÁrvore construída:")
    tree2.print_tree()
    
    print("\n" + "=" * 60)
    print("PERCURSOS")
    print("=" * 60)
    print(f"\nCenário 1 - Pré-ordem: {tree1.preorder()}")
    print(f"Cenário 1 - In-ordem: {tree1.inorder()}")
    
    print(f"\nCenário 2 - Pré-ordem: {tree2.preorder()}")
    print(f"Cenário 2 - In-ordem: {tree2.inorder()}")


if __name__ == "__main__":
    main()
