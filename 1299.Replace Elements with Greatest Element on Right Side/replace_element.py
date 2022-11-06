class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        for x in range(1, len(arr)):
            arr[x - 1] = max(arr[x: len(arr)])
        arr[len(arr) - 1] = -1
        return arr

#max(arr[1:2]) mostra o maximo do elemento 1 ate o 2 (nao é o indice do array)