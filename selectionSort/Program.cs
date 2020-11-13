using System;
using System.Collections.Generic;

namespace selectionSort
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int> {156, 141, 35, 94, 88, 61, 111};
            System.Console.WriteLine("Before: " + string.Join(",", numbers));
            System.Console.WriteLine("After: " + string.Join(",", selectionSort(numbers)));
        }

        private static int[] selectionSort(List<int> arr){
            var newArr = new int[arr.Count];

            for (int i = 0; i < newArr.Length; i++)
            {
                var smallest = findSmallest(arr);
                newArr[i] = arr[smallest];
                arr.RemoveAt(smallest);
            }

            return newArr;
        }

        private static int findSmallest(List<int> arr){
            int smallest = arr[0];
            int smallest_index = 0;

            for (int i = 0; i < arr.Count; i++)
            {
                if (arr[i] < smallest){
                    smallest = arr[i];
                    smallest_index = i;
                }
            }

            return smallest_index;
        }
    }
}
