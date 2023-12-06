//grid traveller
//Recursive
//  const gridTraveller = (m,n) => {
//     if (m == 1 && n == 1) return 1;
//     if (m == 0 || n == 0) return 0;
//     return gridTraveller(m-1,n) + gridTraveller(m, n-1);
//  };

//  console.log(gridTraveller(2,3));
//time comp o(2^(n+m)) space o(n + m)


//  const gridTraveller = (m,n, memo = {}) => {
//     const key = m + ',' + n;
//     if (key in memo) return memo[key];
//     if (m == 1 && n == 1) return 1;
//     if (m == 0 || n == 0) return 0;
//     memo[key] = gridTraveller(m-1,n, memo) + gridTraveller(m, n-1, memo);
//     return memo[key];
//  };

//  console.log(gridTraveller(18,18));

// const gridTraveller = (m,n, memo = {'1,1':1}) => {
//     const key = m + ',' + n;
//     const key2 = n + ',' + m;
//     if (key in memo) return memo[key];
//     if (key2 in memo) return memo[key2];
//     if (m == 0 || n == 0) return 0;
//     memo[key] = gridTraveller(m-1,n, memo) + gridTraveller(m, n-1, memo);
//     return memo[key];
//  };

//  console.log(gridTraveller(3,2));

//Iterative
// const gridTraveller = (m,n) => {
//     const table = Array(m + 1).fill().map(() => Array(n + 1).fill(0));
//     table[1][1] = 1;
//     for (let i = 0; i <= m; i++){
//         for (let j = 0; j <= n; j++){
//             const current = table[i][j];
//             if (j + 1 <= n) table[i][j + 1] += current;
//             if (i + 1 <= m) table[i + 1][j] += current;
//         }
//     }
//     return table[m][n];
// };

// console.log(gridTraveller(18,18));
//time: o(m*n) space:(m*n)
