//how many ways to construct a target
//Recursive
// const countConstruct = (target, wordBank, memo = {'':1}) => {
//     if (target in memo) return memo[target];
//     let totalCount = 0;
//     for (let word of wordBank) {
//         if (target.indexOf(word) == 0){
//             const numWaysForRest = countConstruct(target.slice(word.length), wordBank, memo);
//             totalCount += numWaysForRest;
//         }
//     }
//     memo[target]= totalCount;
//     return memo[target];
// };

// console.log(countConstruct('abcdef', ['ab', 'ab', 'cd', 'def', 'abcd']));
//time: o(n*m*m) space: o(m*m)

//Iterative
// const countConstruct = (target, wordBank) => {
//     const table = Array(target.length + 1).fill(0);
//     table[0] = 1;
//     for (let i = 0; i <= target.length; i++){
//         if (table[i] != 0){
//             for (word of wordBank){
//                 if (target.slice(i, i + word.length) == word){
//                     table[i + word.length] += table[i]; 
//                 }
//             }
//         }
//     } 
//     return table[target.length];
// };

// console.log(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']));
//time: o(m*n*m) space:o(m) 