//canConstruct(abcdef, [ab,adc,cd,def,abdcd]) = 'abc' + 'def -> true
//Recursive
// const canConstruct = (target, wordBank) => {
//     if (target == '') return true;
//     for  (let word of wordBank){
//         if (target.indexOf(word) == 0){
//             const suffix = target.slice(word.length);
//             if (canConstruct(suffix, wordBank) == true) return true;
//         }
//     }
//     return false;
// };

// console.log(canConstruct('abcdef', ['ab', 'ab', 'cd', 'def', 'abcd']));
//time : o(n^m*m) (slice operation o(m)) 
//space: o(m*m) (suffix (slice))

// const canConstruct = (target, wordBank, memo = {'':true}) => {
//     if (target in memo) return memo[target];
//     for  (let word of wordBank){
//         if (target.indexOf(word) == 0){
//             const suffix = target.slice(word.length);
//             if (canConstruct(suffix, wordBank, memo) == true){
//                 memo[target] = true;
//                 return true;
//             }
//         }
//     }
//     memo[target] = false;
//     return false;
// };

// console.log(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']));
//time: o(n*m*m) space: o(m*m)

//Iterative
// const canConstruct = (target, wordBank) => {
//     const table = Array(target.length + 1).fill(false);
//     table[0] = true;
//     for (let i = 0; i <= target.length; i++) {
//         if (table[i] == true){
//             for (let word of wordBank){
//                 if (target.slice(i, i + word.length) == word){
//                     table[i + word.length] = true;
//                 }
//             }
//         }
//     }
//     return table[target.length];
// };

// console.log(canConstruct('abcdef', ['ab', 'abc', 'cd', 'de', 'abcd']));
//time: o(m*n*m) o(m):slicing operation space:o(m)