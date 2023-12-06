//fibanocci
//recursive
// const fib = (n) => {
//     if (n <= 2) return 1;
//     return fib(n - 1) + fib(n-2);
// };

// console.log(fib(6))
//time complexity o(2^n) (binary tree)
//space complexity o(n) (height of tree)

//Dynanmic
//memorization (store duplicates)
// js objects, keys will be args n in fib(n), value will be fib(n)
// const fib = (n, memo = {1:1,2:1}) => {
//     if (n in memo) return memo[n];
//     memo[n] = fib(n - 1, memo) + fib(n-2, memo);
//     return memo[n];
// };
// console.log(fib(8));
//time,space complexity o(n)

//Iterative
// const fib = (n) => {
//     const table = Array(n+1).fill(0);
//     table[1] = 1;
//      for (let i = 0; i <= n; i++){
//         table[i + 1] += table[i];
//         table[i + 2] += table[i];
//      }
//      return table[n];
// };

// console.log(fib(8))
// time: o(n) space:o(n)

 
